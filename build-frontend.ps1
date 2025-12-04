# Script para compilar o frontend e copiar para o backend

Write-Host "🔨 Compilando o frontend Vue..." -ForegroundColor Cyan

# Navegar para a pasta frontend
Set-Location -Path "$PSScriptRoot\frontend"

# Instalar dependências (se necessário)
if (-not (Test-Path "node_modules")) {
    Write-Host "📦 Instalando dependências do frontend..." -ForegroundColor Yellow
    npm install
}

# Compilar o projeto
Write-Host "⚙️ Executando build..." -ForegroundColor Yellow
npm run build

# Verificar se o build foi bem-sucedido
if (Test-Path "dist") {
    Write-Host "✅ Build concluído com sucesso!" -ForegroundColor Green
    
    # Remover dist antiga do backend (se existir)
    $backendDist = "$PSScriptRoot\backend\dist"
    if (Test-Path $backendDist) {
        Write-Host "🗑️ Removendo build antigo do backend..." -ForegroundColor Yellow
        Remove-Item -Path $backendDist -Recurse -Force
    }
    
    # Copiar nova dist para o backend
    Write-Host "📂 Copiando build para o backend..." -ForegroundColor Yellow
    Copy-Item -Path "dist" -Destination $backendDist -Recurse
    
    Write-Host "🎉 Processo concluído! O frontend foi compilado e copiado para o backend." -ForegroundColor Green
    Write-Host "📍 Localização: backend\dist" -ForegroundColor Cyan
} else {
    Write-Host "❌ Erro: Build falhou!" -ForegroundColor Red
    exit 1
}

# Voltar para a pasta raiz
Set-Location -Path $PSScriptRoot
