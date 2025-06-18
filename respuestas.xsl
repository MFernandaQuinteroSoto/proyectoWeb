<?xml version="1.0" encoding="UTF-8"?>
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
        