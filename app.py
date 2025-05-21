from flask import Flask, render_template, request, jsonify
from tsp import simulated_annealing, evalua_ruta
import random

app = Flask(__name__)

coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.67775, -103.34625),
    'Monterrey': (25.69161, -100.32183),
    'QuintanaRoo': (21.16311, -86.80231),
    'Michohacan': (19.7014, -101.20829),
    'Aguascalientes': (21.87641, -102.26438),
    'CDMX': (19.43271, -99.13318),
    'QRO': (20.59719, -100.38667)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calcular', methods=['POST'])
def calcular_ruta():
    data = request.get_json()
    T_MIN = float(data.get('temperatura_minima', 0.01))
    V_enfriamiento = int(data.get('velocidad_enfriamiento', 100))

    ruta = list(coord.keys())
    random.shuffle(ruta)
    mejor_ruta = simulated_annealing(ruta, coord, T_MIN, V_enfriamiento)
    distancia_total = round(evalua_ruta(mejor_ruta, coord), 2)

    return jsonify({'ruta': mejor_ruta, 'distancia': distancia_total})

if __name__ == '__main__':
    app.run(debug=True)
