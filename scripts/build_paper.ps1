$ErrorActionPreference = "Continue"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$PaperDir = Join-Path $Root "paper"
$DownloadsPdf = "C:\Users\wangz\Downloads\21.pdf"
$StatusPath = Join-Path $PaperDir "build_status.json"

$Status = [ordered]@{
  stage = "start"
  downloads_pdf = $DownloadsPdf
  steps = @()
  copied_to_downloads = $false
  removed_intermediate_pdf = $false
}

function Add-Step {
  param(
    [string]$Name,
    [int]$ExitCode,
    [string]$OutputPath
  )
  $script:Status.steps += [ordered]@{
    name = $Name
    exit_code = $ExitCode
    output = $OutputPath
  }
}

function Run-Native {
  param(
    [string]$Name,
    [string]$Exe,
    [string[]]$ArgsList
  )
  $OutPath = Join-Path $PaperDir ($Name + ".out.txt")
  try {
    & $Exe @ArgsList *> $OutPath
    $Code = $LASTEXITCODE
    if ($null -eq $Code) { $Code = 0 }
    Add-Step -Name $Name -ExitCode $Code -OutputPath $OutPath
  } catch {
    $_.Exception.Message | Out-File -FilePath $OutPath -Encoding utf8
    Add-Step -Name $Name -ExitCode 999 -OutputPath $OutPath
  }
}

try {
  Push-Location $PaperDir
  Run-Native -Name "pdflatex1" -Exe "pdflatex" -ArgsList @("-interaction=nonstopmode", "-halt-on-error", "main.tex")
  Run-Native -Name "bibtex" -Exe "bibtex" -ArgsList @("main")
  Run-Native -Name "pdflatex2" -Exe "pdflatex" -ArgsList @("-interaction=nonstopmode", "-halt-on-error", "main.tex")
  Run-Native -Name "pdflatex3" -Exe "pdflatex" -ArgsList @("-interaction=nonstopmode", "-halt-on-error", "main.tex")
  Pop-Location
} catch {
  $Status.stage = "build_exception"
  $Status.error = $_.Exception.Message
  try { Pop-Location } catch {}
}

$MainPdf = Join-Path $PaperDir "main.pdf"
if (Test-Path -LiteralPath $MainPdf) {
  try {
    $DownloadsDir = Split-Path -Parent $DownloadsPdf
    if (-not (Test-Path -LiteralPath $DownloadsDir)) {
      New-Item -ItemType Directory -Path $DownloadsDir -Force | Out-Null
    }
    Copy-Item -LiteralPath $MainPdf -Destination $DownloadsPdf -Force
    $Status.copied_to_downloads = Test-Path -LiteralPath $DownloadsPdf
    Remove-Item -LiteralPath $MainPdf -Force
    $Status.removed_intermediate_pdf = -not (Test-Path -LiteralPath $MainPdf)
    $Status.stage = "done"
  } catch {
    $Status.stage = "copy_failed"
    $Status.error = $_.Exception.Message
  }
} else {
  $Status.stage = "pdf_missing"
}

$Status | ConvertTo-Json -Depth 6 | Out-File -FilePath $StatusPath -Encoding utf8
exit 0
