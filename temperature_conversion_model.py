import numpy as np
import tensorflow as tf

class TemperatureConversionModel:
    def __init__(self):
        # Definir el modelo
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(units=1, input_shape=[1])
        ])
        self.model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

    def train(self, celsius, fahrenheit, epochs=500):
        # Entrenar el modelo
        self.model.fit(celsius, fahrenheit, epochs=epochs, verbose=0)
        print("Modelo entrenado.")

    def predict_celsius_to_fahrenheit(self, celsius_value):
        # Asegurarse de que el valor de entrada esté en el formato correcto (NumPy array)
        celsius_value = np.array([celsius_value])
        result = self.model.predict(celsius_value)
        print(f"{celsius_value[0]} grados Celsius son {result[0][0]} grados Fahrenheit.")
        return result[0][0]