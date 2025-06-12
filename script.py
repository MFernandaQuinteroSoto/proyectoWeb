from flask import Flask, render_template, request,jsonify
#import pandas as pd

#libreria para llamar archivos externos
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

#procedimiento para cargar el formulario en una ventana html de medio tamaño en la principal. 
@app.route('/cargar_contenido', methods=["POST"])
def cargar_contenido():
    if request.method=="POST":
        return render_template('preguntas.html')

#procedimiento para capturar los datos del formulario
@app.route('/procesar_formulario', methods=["POST"])
def procesar_formulario():
    if request.method=="POST":
        #dato1 = request.form["pregunta1"]
        #datos_formulario = request.form
        # Crear un diccionario
        #formulario_dict = {key: datos_formulario[key] for key in datos_formulario}
        # Convertir a lista de tuplas si es necesario
        #formulario_list = list(formulario_dict.items())

        # Obtener los datos enviados desde el frontend
        datos = request.get_json()  # Recibe el JSON enviado por AJAX

        # Procesar los datos (ejemplo simple)
        pregunta1 = datos.get('pregunta1', '')
        pregunta2 = datos.get('pregunta2', '')

        # Crear una respuesta JSON
        respuesta = {
            'status': 'success',
            'recibido': {
                'pregunta1': pregunta1,
                'pregunta2': pregunta2
            },
            'mensaje': f"Datos recibidos correctamente"
        }
        return jsonify(respuesta)  # Devolver la respuesta como JSON

        #return render_template('Index.html', formulario_list=formulario_list)
    else:
        return render_template('Index.html', mensaje=None)


if __name__ == '__main__':
    #con debug=true Flask muestra el paso a paso de la ejecución por si salen errores
    app.run(debug=False, port=5001)