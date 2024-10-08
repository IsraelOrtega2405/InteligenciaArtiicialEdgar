import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada (Celsius) y salida (Fahrenheit)
celcius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)  # Temperaturas en Celsius
fahrenheit = np.array([40, 24, 32, 45, 59, 72, 100], dtype=float)  # Temperaturas en Fahrenheit

# Definición del modelo
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

print("Comenzando entrenamiento...")
# Entrenamiento del modelo
historial = modelo.fit(celcius, fahrenheit, epochs=1000, verbose=False)
print("Modelo Entrenado!")

# Visualización del historial de entrenamiento
plt.xlabel("# Época")
plt.ylabel("Error")
plt.plot(historial.history["loss"])
plt.show()

print("Hagamos una predicción!")
# Predicción para 100 grados Celsius
resultado = modelo.predict([100.0])
print("El resultado es " + str(resultado) + " Fahrenheit")