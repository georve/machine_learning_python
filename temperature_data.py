import pandas as pd

class TemperatureData:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)
    
    def get_celsius_and_fahrenheit(self):
        celsius = self.data['Celsius'].values
        fahrenheit = self.data['Fahrenheit'].values
        return celsius, fahrenheit