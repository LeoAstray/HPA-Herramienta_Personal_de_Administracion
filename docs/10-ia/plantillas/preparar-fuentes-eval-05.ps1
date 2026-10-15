# Preparacion humana de fuentes. No ejecuta agentes ni configura permisos.
# ASCII en este script para PowerShell 5.1; las fuentes se leen y escriben en UTF-8.
[CmdletBinding()]
param([Parameter(Mandatory = $true)][string]$LabRoot)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$projectRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..\..'))
$lab = (Resolve-Path -LiteralPath $LabRoot).ProviderPath.TrimEnd('\', '/')
if ((Split-Path -Leaf $lab) -ne 'HPA-EVAL-05' -or
    (Split-Path -Leaf (Split-Path -Parent $lab)) -ne 'Tests') {
    throw 'LabRoot debe ser una carpeta Tests/HPA-EVAL-05 ya creada.'
}
if ($lab.StartsWith($projectRoot + '\', [StringComparison]::OrdinalIgnoreCase) -or
    $projectRoot.StartsWith($lab + '\', [StringComparison]::OrdinalIgnoreCase)) {
    throw 'El laboratorio debe estar separado del repositorio HPA.'
}

function Assert-PlainLabPath([string]$Path) {
    $current = [IO.Path]::GetFullPath($Path)
    while ($true) {
        if (Test-Path -LiteralPath $current) {
            $item = Get-Item -LiteralPath $current -Force
            if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
                throw 'Una ruta de destino contiene un enlace o punto de reanalisis. Revisala manualmente.'
            }
        }
        if ($current -eq $lab) { break }
        if (-not $current.StartsWith($lab + '\', [StringComparison]::OrdinalIgnoreCase)) {
            throw 'Destino fuera de la raiz del laboratorio.'
        }
        $current = Split-Path -Parent $current
    }
}

function Get-Sha256([byte[]]$Bytes) {
    $hasher = [Security.Cryptography.SHA256]::Create()
    try { return ([BitConverter]::ToString($hasher.ComputeHash($Bytes))).Replace('-', '') }
    finally { $hasher.Dispose() }
}

function Get-SectionKey([string]$Heading) {
    return [regex]::Replace($Heading.Normalize([Text.NormalizationForm]::FormD), '\p{Mn}', '')
}

function Select-Sections([string]$Text, [string[]]$Sections) {
    if (-not $Sections) { return $Text.TrimEnd() }
    $parts = [regex]::Split($Text, '(?m)(?=^## )')
    $selected = @($parts[0].TrimEnd())
    foreach ($section in $Sections) {
        $found = @($parts | Where-Object {
            $heading = ($_ -split "`n", 2)[0].TrimEnd("`r")
            (Get-SectionKey $heading) -eq ('## ' + $section)
        })
        if ($found.Count -ne 1) { throw "Seccion ausente o ambigua: $section" }
        $selected += $found[0].TrimEnd()
    }
    return $selected -join "`n`n"
}

function Write-NewFile([string]$Path, [byte[]]$Bytes) {
    Assert-PlainLabPath $Path
    [IO.Directory]::CreateDirectory((Split-Path -Parent $Path)) | Out-Null
    Assert-PlainLabPath $Path
    $stream = [IO.File]::Open($Path, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write)
    try { $stream.Write($Bytes, 0, $Bytes.Length) }
    finally { $stream.Dispose() }
}

$docsRoot = Join-Path $lab 'agente\docs'
$evaluatorRoot = Join-Path $lab 'evaluador'
$manifestPath = Join-Path $evaluatorRoot 'manifiesto-fuentes.json'
foreach ($directory in @($docsRoot, $evaluatorRoot)) {
    if (-not (Test-Path -LiteralPath $directory -PathType Container)) {
        throw 'Falta agente/docs o evaluador. Completa la estructura antes de copiar fuentes.'
    }
    Assert-PlainLabPath $directory
}
if (@(Get-ChildItem -LiteralPath $docsRoot -Force).Count -gt 0 -or
    (Test-Path -LiteralPath $manifestPath)) {
    throw 'Las fuentes o el manifiesto ya tienen contenido. No se sustituye ni elimina nada.'
}

# Lista cerrada. Los nombres de seccion se comparan sin tildes.
$sources = @(
    @{ Path = 'docs/README.md'; Sections = @('Proposito de esta documentacion', 'Como leerla') }
    @{ Path = 'docs/00-gobierno/estado-proyecto.md'; Sections = @('Estado actual', 'Objetivo del producto', 'Decisiones confirmadas', 'Pendiente de decision', 'Convencion de estado') }
    @{ Path = 'docs/01-proyecto/vision-y-alcance.md'; Sections = $null }
    @{ Path = 'docs/13-adrs/indice.md'; Sections = $null }
    @{ Path = 'docs/07-seguridad/README.md'; Sections = @('Documentos y archivos') }
    @{ Path = 'docs/10-ia/contexto-agentes.md'; Sections = $null }
    @{ Path = 'docs/10-ia/contrato-de-agentes.md'; Sections = $null }
    @{ Path = 'docs/10-ia/agentes-desarrollo.md'; Sections = @('Equipo y responsabilidad', 'Contratos por rol', 'Flujo minimo por cambio', 'Reglas de concurrencia', 'Reparto de pruebas', 'Entrada y salida de cada tarea', 'Portabilidad') }
    @{ Path = 'docs/general-docs/fuentes/adrs/ADR-001/ADR-001_ASANA_DESARROLLO_VS_PRODUCTO.md'; Sections = $null }
    @{ Path = 'docs/general-docs/fuentes/adrs/ADR-002/ADR-002_ARQUITECTURA_MULTICLIENTE_MOVIL_VOZ.md'; Sections = $null }
    @{ Path = 'docs/13-adrs/ADR-003-priorizacion-descubrimiento-ia-agentes.md'; Sections = $null }
    @{ Path = 'docs/13-adrs/ADR-004-contratos-agentes-desarrollo.md'; Sections = @('Contexto', 'Opciones y decision') }
    @{ Path = 'docs/13-adrs/ADR-005-modelo-core.md'; Sections = $null }
)
$allowed = @{}
foreach ($source in $sources) {
    $allowed[[IO.Path]::GetFullPath((Join-Path $projectRoot $source.Path))] = $true
}
$revision = & git --no-optional-locks -C $projectRoot rev-parse HEAD
if ($LASTEXITCODE -ne 0) { throw 'No se pudo identificar la revision base de HPA.' }
$utf8 = New-Object Text.UTF8Encoding($false, $true)
$prepared = @()
$entries = @()

# Toda la seleccion se valida en memoria antes de escribir el primer archivo.
foreach ($source in $sources) {
    $origin = [IO.Path]::GetFullPath((Join-Path $projectRoot $source.Path))
    $originalBytes = [IO.File]::ReadAllBytes($origin)
    $originalText = $utf8.GetString($originalBytes).TrimStart([char]0xFEFF).Replace("`r`n", "`n")
    $body = Select-Sections $originalText $source.Sections
    if ($body -match '(?i)\bEVAL-\d{2}\b|\bP(?:0[1-9]|1[0-3])\b') {
        throw "La seleccion contiene referencias a casos o resultados. Revisar: $($source.Path)"
    }
    $omittedLinks = New-Object 'System.Collections.Generic.List[string]'
    $body = [regex]::Replace($body, '\[([^\]\r\n]+)\]\(([^)\r\n]+)\)', [Text.RegularExpressions.MatchEvaluator]{
        param($match)
        $target = $match.Groups[2].Value
        if ($target.StartsWith('#') -or $target -match '^[a-zA-Z][a-zA-Z0-9+.-]*:') {
            return $match.Value
        }
        $targetFile = [Uri]::UnescapeDataString(($target -split '#', 2)[0])
        $targetPath = [IO.Path]::GetFullPath((Join-Path (Split-Path -Parent $origin) $targetFile))
        if ($allowed.ContainsKey($targetPath)) { return $match.Value }
        $omittedLinks.Add($target)
        return $match.Groups[1].Value + ' (referencia no incluida)'
    })
    $kind = if ($source.Sections) { 'extracto' } else { 'completa' }
    $note = '> Copia de laboratorio (' + $kind + ') de `' + $source.Path + '`. Uso limitado al encargo; las referencias no incluidas no autorizan consultar HPA ni otras fuentes.'
    $copyBytes = $utf8.GetBytes($note + "`n`n" + $body.TrimEnd() + "`n")
    $relativeDestination = 'agente/' + $source.Path
    $prepared += [pscustomobject]@{ Path = (Join-Path $lab $relativeDestination); Bytes = $copyBytes }
    $entries += [ordered]@{
        origen_relativo = $source.Path
        destino_relativo = $relativeDestination
        tipo = $kind
        secciones = @($source.Sections | Where-Object { $null -ne $_ })
        sha256_origen = Get-Sha256 $originalBytes
        sha256_copia = Get-Sha256 $copyBytes
        referencias_omitidas = @($omittedLinks.ToArray())
    }
}
$manifest = [ordered]@{
    version = 'EVAL-05-FUENTES-R1'
    fecha_utc = [DateTime]::UtcNow.ToString('o')
    origen_local = $projectRoot
    raiz_local = $lab
    revision_base = $revision.Trim()
    identificacion = 'Se lee la copia de trabajo, incluidos cambios locales. El hash de origen identifica su contenido; revision_base no afirma igualdad con HEAD.'
    generador_sha256 = (Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash
    adaptaciones = @('Marca de copia de laboratorio', 'Seleccion explicita de secciones cuando se indica', 'UTF-8 sin BOM y saltos LF', 'Enlaces locales a fuentes no incluidas convertidos a texto y registrados')
    limites = 'Preparacion de fuentes; no acredita permisos, exclusion tecnica del evaluador, cobertura de canales ni ejecucion de casos.'
    fuentes = @($entries)
}
$manifestBytes = $utf8.GetBytes(($manifest | ConvertTo-Json -Depth 8) + "`n")
foreach ($file in $prepared) { Write-NewFile $file.Path $file.Bytes }
Write-NewFile $manifestPath $manifestBytes
Write-Output ('Fuentes preparadas: ' + $prepared.Count + '. Manifiesto: evaluador/manifiesto-fuentes.json')
