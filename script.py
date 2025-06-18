from flask import Flask, render_template, request,jsonify
import xml.etree.ElementTree as ET
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

        # Crear XML
        root = ET.Element("datos")
        for key, value in datos.items():
            pregunta = ET.SubElement(root, key)
            pregunta.text = value
        
        # Instrucción para XSL
        xsl_pi = '<?xml-stylesheet type="text/xsl" href="respuestas.xsl"?>\n'
        tree_str = ET.tostring(root, encoding="unicode")

        # Guardar XML
        with open("respuestas.xml", "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write(xsl_pi)
            f.write(tree_str)

        # Guardar XSL
        xsl_content = """<?xml version="1.0" encoding="UTF-8"?>
        <xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

            <xsl:template match="/respuestas">
                <html>
                <body>
                    <h2>Respuestas del Usuario</h2>
                    <table border="1" cellpadding="5">
                        <tr><th>Pregunta</th><th>Respuesta</th></tr>
                        <tr><td>Comida ideal</td><td><xsl:value-of select="pregunta1"/></td></tr>
                        <tr><td>Color favorito</td><td><xsl:value-of select="pregunta2"/></td></tr>
                        <tr><td>Actividad</td><td><xsl:value-of select="pregunta3"/></td></tr>
                        <tr><td>Bebida</td><td><xsl:value-of select="pregunta4"/></td></tr>
                        <tr><td>Destino de viaje</td><td><xsl:value-of select="pregunta5"/></td></tr>
                        <tr><td>Música</td><td><xsl:value-of select="pregunta6"/></td></tr>
                        <tr><td>Defecto</td><td><xsl:value-of select="pregunta7"/></td></tr>
                        <tr><td>Película</td><td><xsl:value-of select="pregunta8"/></td></tr>
                        <tr><td>Temporada favorita</td><td><xsl:value-of select="pregunta9"/></td></tr>
                        <tr><td>Cualidad principal</td><td><xsl:value-of select="pregunta10"/></td></tr>
                    </table>
                </body>
                </html>
            </xsl:template>
        </xsl:stylesheet>
        """
        with open("respuestas.xsl", "w", encoding="utf-8") as f:
            f.write(xsl_content)

        return jsonify(respuesta)  # Devolver la respuesta como JSON

        #return render_template('Index.html', formulario_list=formulario_list)
    else:
        return render_template('Index.html', mensaje=None)


if __name__ == '__main__':
    #con debug=true Flask muestra el paso a paso de la ejecución por si salen errores
    app.run(debug=False, port=5001)