# 🏆 Ranking Game - Flask

## 📋 Descripción
Aplicación Flask que muestra un ranking interactivo de jugadores con diferentes opciones de filtrado y personalización de colores.

## 🚀 Cómo ejecutar

### Opción 1: Con PowerShell (Recomendado)
```powershell
# Ejecuta el script run.ps1 directamente
.\run.ps1
```

### Opción 2: Desde la carpeta del proyecto
```powershell
# 1. Navega a la carpeta del proyecto
cd "c:\Users\4C Programacion 2026\Desktop\python\python\flask\fundamentos\08_ranking_game"

# 2. Ejecuta con el entorno virtual
&'c:\Users\4C Programacion 2026\Desktop\python\.venv\Scripts\python.exe' app.py
```

### Opción 3: Copiar este comando en Terminal
```powershell
cd 'c:\Users\4C Programacion 2026\Desktop\python\python\flask\fundamentos\08_ranking_game' ; &'c:\Users\4C Programacion 2026\Desktop\python\.venv\Scripts\python.exe' app.py
```

## 🔗 Rutas disponibles

Una vez que la aplicación esté ejecutándose, abre tu navegador en:

| Ruta | Descripción |
|------|-------------|
| **http://localhost:5000/** | Página principal (ranking completo) |
| **http://localhost:5000/ranking** | Ranking de todos los jugadores |
| **http://localhost:5000/ranking/3** | Solo los 3 primeros jugadores |
| **http://localhost:5000/ranking/5/lightblue** | Top 5 con fondo azul claro |
| **http://localhost:5000/ranking/2/pink** | Top 2 con fondo rosa |

## 📁 Estructura de carpetas
```
08_ranking_game/
├── app.py              # Aplicación Flask principal
├── run.ps1             # Script para ejecutar rápidamente
├── README.md           # Este archivo
└── template/
    ├── index.html      # Plantilla principal
    └── ranking.html    # Plantilla alternativa
```

## ⚙️ Requisitos
- Python 3.x
- Flask instalado (se instala automáticamente con el entorno virtual)

Si necesitas instalar Flask manualmente:
```powershell
pip install flask
```

## 📝 Notas
- ✅ La aplicación corre en **debug=True**, se reinicia automáticamente al hacer cambios
- ✅ El servidor escucha en **http://127.0.0.1:5000** por defecto
- ✅ Todos los estilos están optimizados y responsive
- ✅ Muestra badges especiales con colores para los 3 primeros puestos
- ✅ El primer lugar tiene una corona 👑 de líder
