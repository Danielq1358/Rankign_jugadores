#!/usr/bin/env powershell
# =====================================================
# Script para ejecutar la aplicación Ranking Game
# =====================================================

Write-Host "🎮 Iniciando Ranking Game..." -ForegroundColor Green
Write-Host ""

# Navegar a la carpeta del proyecto
cd 'c:\Users\4C Programacion 2026\Desktop\python\python\flask\fundamentos\08_ranking_game'

# Ejecutar la aplicación con el entorno virtual
Write-Host "✅ Ejecutando app.py..." -ForegroundColor Cyan
Write-Host ""

&'c:\Users\4C Programacion 2026\Desktop\python\.venv\Scripts\python.exe' app.py

# Nota: Mantener la ventana abierta si hay un error
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ Error al ejecutar la aplicación" -ForegroundColor Red
    Read-Host "Presiona Enter para cerrar"
}
