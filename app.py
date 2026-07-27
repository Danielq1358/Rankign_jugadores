from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

# Datos de jugadores ordenados de mayor a menor puntaje
jugadores = [
   {"nombre": "CyberWarrior", "puntaje": 9100},
   {"nombre": "ShadowNinja", "puntaje": 8200},
   {"nombre": "PixelMaster", "puntaje": 7500},
   {"nombre": "AlexGamer", "puntaje": 5000},
   {"nombre": "UltraNoob", "puntaje": 3000}
]

# Ruta raíz - acceso directo
@app.route('/')
def inicio():
    return render_template('index.html', lista_jugadores=jugadores, color="#f4f4f4")

# Ruta para mostrar el ranking completo de jugadores
@app.route('/ranking')
def mostrar_ranking():
    return render_template('index.html', lista_jugadores=jugadores, color="#f4f4f4")

# Ruta para mostrar un número limitado de jugadores (ej: /ranking/3)
@app.route('/ranking/<int:cantidad>')
def ranking_limitado(cantidad):
    jugadores_filtrados = jugadores[:cantidad]
    return render_template('index.html', lista_jugadores=jugadores_filtrados, color="#f4f4f4")

# Ruta para personalizar el color del ranking cambiando el fondo (ej: /ranking/3/lightblue)
@app.route('/ranking/<int:cantidad>/<color_elegido>')
def ranking_color(cantidad, color_elegido):
    jugadores_filtrados = jugadores[:cantidad]
    return render_template('index.html', lista_jugadores=jugadores_filtrados, color=color_elegido)

if __name__ == "__main__":
   app.run(debug=True)