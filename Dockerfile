# Imagen base con Python 3.12
FROM python:3.12-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Cloud Run usa la variable PORT
ENV PORT=8080
EXPOSE 8080

# Ejecutar la aplicación
CMD ["gunicorn", "-b", ":8080", "app:app"]
