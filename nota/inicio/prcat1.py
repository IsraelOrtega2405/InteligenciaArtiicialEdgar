# Definición de letras en forma de asteriscos
letras = {
    'I': [
        " ***** ",
        "   *   ",
        "   *   ",
        "   *   ",
        " ***** ",
    ],
    'S': [
        " ***** ",
        "*     *",
        "      *",
        " *    *",
        " ***** ",
    ],
    'R': [
        " ***** ",
        "*    * ",
        " ***** ",
        "*    * ",
        "*     *",
    ],
    'A': [
        "   *   ",
        "  * *  ",
        " ***** ",
        "*     *",
        "*     *",
    ],
}

nombre = "ISRA"

# Imprimir el nombre en asteriscos
for i in range(5):  # Cada letra tiene 5 líneas
    for letra in nombre:
        if letra in letras:
            print(letras[letra][i], end="  ")  # Imprime cada línea de la letra
    print()  # Salto de línea al final de cada fila
