import random,os

import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, jsonify

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)

boletos_vendidos = set()
precio_boleto = 150.000
@app.route('/')
def index():
    return render_template('index.html', boletos_vendidos=boletos_vendidos, precio_boleto = precio_boleto)

@app.route('/show_data')
def showData():
    upload_df = pd.read_csv('static/datos_rifa - 0.csv', encoding='unicode_escape')
    updload_df_html = upload_df.to_html()

    return render_template('csv_data.html' , data_var = updload_df_html)

@app.route('/search_avalaible' , methods=['POST'])
def number_search():
    try:
        upload_df = pd.read_csv('static/datos_rifa - 0.csv', encoding='unicode_escape')
        data = upload_df.to_dict()
        number = int(request.json['numero'])

        for boleta in data['disponible']:
            if boleta == number:
                if data['disponible'][boleta] == "SI":
                    msj = "La boleta esta disponible"
                else:
                    msj = "La boleta NO esta disponible"

        return jsonify({'mensaje': msj})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/vender_boleto', methods=['POST'])
def vender_boleto():
    if len(boletos_vendidos) < 100:
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        abono = request.form['abono']

        # Validar que se ingresen todos los campos
        if not nombre or not apellido or not telefono or not direccion or not abono:
            return "Todos los campos son obligatorios. Por favor, completa el formulario."


        return redirect(url_for('index'))
    else:
        return "¡Todos los boletos han sido vendidos!"

if __name__ == '__main__':
    app.run(debug=True)
