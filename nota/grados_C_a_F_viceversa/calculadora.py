import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 1. Preparación de los Datos
# Definimos nuestros datos de entrada (gramos de café) y sus correspondientes salidas (mililitros de agua).
cafe_gramos = np.array([5, 10, 15, 20, 25, 30], dtype=float)  # Gramos de café
agua_ml = np.array([100, 200, 300, 400, 500, 600], dtype=float)  # Mililitros de agua

# 2. Visualización de los Datos
# Graficamos los datos de entrada y salida para ver la relación.

plt.scatter(cafe_gramos, agua_ml, color='blue')
plt.title('Relación entre Gramos de Café y Mililitros de Agua')
plt.xlabel('Gramos de Café')
plt.ylabel('Mililitros de Agua')
plt.grid()
plt.show()

# 3. Construcción del Modelo
# Creamos una red neuronal secuencial con una capa densa.
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1], activation='linear')  # Capa densa con 1 neurona
])

# 4. Compilación del Modelo
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),  # Tasa de aprendizaje de 0.1
    loss='mean_squared_error'  # Función de pérdida: error cuadrático medio
)

# 5. Entrenamiento del Modelo
print("Entrenando el modelo...")
historial = modelo.fit(cafe_gramos, agua_ml, epochs=500, verbose=0)  # Entrenamos durante 500 épocas sin salida detallada

# 6. Evaluación del Modelo
# Graficamos la pérdida durante el entrenamiento.
plt.plot(historial.history['loss'])
plt.title('Pérdida durante el Entrenamiento')
plt.xlabel('Épocas')
plt.ylabel('Pérdida')
plt.grid()
plt.show()

# 7. Pregunta al Usuario
# Preguntamos al usuario si desea preparar café.
respuesta = input("¿Deseas preparar café? (sí/no): ").strip().lower()

# 8. Lógica de Preparación de Café
if respuesta == 'sí' or respuesta == 'si':
    # Solicitar al usuario la cantidad de café en gramos.
    cafe_nuevo = float(input("Introduce la cantidad de café en gramos: "))  # Entrada del usuario

    # Usamos el modelo entrenado para hacer una predicción.
    prediccion = modelo.predict([cafe_nuevo])  # Predicción de la red neuronal

    # 9. Mostrar el Resultado
    print(f"{cafe_nuevo} gramos de café requieren aproximadamente {prediccion[0][0]:.2f} mililitros de agua.")
else:
    print("Está bien, quizás otra vez.")

# 10. Guardar el Modelo (Opcional)
# Guardamos el modelo entrenado para su uso futuro.
modelo.save('modelo_cafe_a_agua.h5')
print("Modelo guardado como 'modelo_cafe_a_agua.h5'.")
