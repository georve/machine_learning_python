# Conversión de Temperatura con TensorFlow

Este proyecto utiliza TensorFlow para construir un modelo de red neuronal simple que convierte temperaturas entre Celsius y Fahrenheit. El modelo se entrena utilizando un archivo CSV que contiene pares de temperaturas en ambas escalas.

## Estructura del Proyecto

El proyecto está dividido en tres archivos principales:

1. **`temperature_data.py`**: Contiene la clase `TemperatureData` para manejar la lectura y extracción de datos del archivo CSV.
2. **`temperature_conversion_model.py`**: Define la clase `TemperatureConversionModel` que construye, entrena y realiza predicciones utilizando un modelo de red neuronal.
3. **`main.py`**: El archivo principal que ejecuta el programa. Guarda los datos de temperatura en un archivo CSV, entrena el modelo, y realiza predicciones.

## Instalación

Para ejecutar el proyecto, necesitarás tener Python instalado, así como las bibliotecas necesarias. Puedes instalar las dependencias utilizando `pip`. Asegúrate de tener un entorno virtual o conda activado para evitar conflictos con otras bibliotecas.

1. Clona el repositorio (si es necesario):

    ```bash
    git clone https://github.com/georve/machine_learning_python
    cd machine_learning_python
    ```

2. Instala las dependencias necesarias:

    ```bash
    pip install pandas tensorflow numpy
    ```

## Ejecución

Para ejecutar el proyecto, simplemente corre el archivo `main.py`. Esto generará el archivo CSV, entrenará el modelo y mostrará algunas predicciones.

```bash
python main.py
