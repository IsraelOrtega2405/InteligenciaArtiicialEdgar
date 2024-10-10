import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada (Celsius y Fahrenheit)
celcius = np.array([-40, -10, 0, 8, 15, 22, 38, 100, 150, 200], dtype=float)  # Valores Celsius
fahrenheit = np.array([40, 24, 32, 45, 59, 72, 100, 212, 302, 392], dtype=float)  # Valores Fahrenheit

# Definición del modelo
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

print("Comenzando entrenamiento...")
historial = modelo.fit(celcius, fahrenheit, epochs=1000, verbose=False)
print("Modelo Entrenado!")

# Graficar la pérdida del entrenamiento
plt.xlabel("# Época")
plt.ylabel("Error")
plt.plot(historial.history["loss"])
plt.show()

print("¡Hagamos una predicción!")
resultado = modelo.predict([100.0])
print("El resultado es " + str(resultado[0][0]) + " Fahrenheit")
