import pandas as pd
import tensorflow as tf
from temperature_data import TemperatureData
from temperature_conversion_model import TemperatureConversionModel
class Main:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.data_handler = TemperatureData(csv_path)
        self.model = TemperatureConversionModel()

    def run(self):
        # Obtener datos
        celsius, fahrenheit = self.data_handler.get_celsius_and_fahrenheit()

        # Entrenar el modelo
        self.model.train(celsius, fahrenheit)

        # Realizar predicciones
        self.model.predict_celsius_to_fahrenheit(100)
        self.model.predict_celsius_to_fahrenheit(20)



# Ejecutar el programa principal
if __name__ == "__main__":
    main = Main('celsius_a_fahrenheit.csv')
    main.run()
