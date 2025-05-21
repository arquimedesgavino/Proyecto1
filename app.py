# app.py
import streamlit as st

# Título de la página
st.set_page_config(page_title="Quiz de Python - While, For, If", layout="centered")
st.title("Aprende estructuras de control en Python")

# Sección informativa
st.header("¿Cómo funcionan `while`, `for` e `if` en Python?")

st.markdown(
    """
- **`if`**: Permite ejecutar un bloque de código solo si una condición es verdadera.

```python
x = 10
if x > 5:
    print("x es mayor que 5")
```

- **`for`**: Itera sobre una secuencia (lista, tupla, cadena, etc.) ejecutando un bloque de código para cada elemento.

```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```

- **`while`**: Ejecuta un bloque de código repetidamente mientras la condición sea verdadera.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```
    """
)

st.markdown("---")

# Lista de preguntas
preguntas = [
    {
        'pregunta': "¿Cuál estructura se usa para repetir mientras una condición sea verdadera?",
        'opciones': ['for', 'if', 'while', 'switch'],
        'respuesta': 'while'
    },
    {
        'pregunta': "¿Cómo se inicia un bloque condicional en Python?",
        'opciones': ['loop', 'if', 'when', 'case'],
        'respuesta': 'if'
    },
    {
        'pregunta': "¿Cuál de estos no es una estructura de control en Python?",
        'opciones': ['for', 'while', 'elif', 'do-while'],
        'respuesta': 'do-while'
    },
    {
        'pregunta': "¿Qué palabra clave permite agregar una condición alternativa en un `if`?",
        'opciones': ['else', 'elif', 'except', 'finally'],
        'respuesta': 'elif'
    },
    {
        'pregunta': "¿Cómo se detiene un bucle `while` manualmente?",
        'opciones': ['stop', 'break', 'exit', 'return'],
        'respuesta': 'break'
    },
    {
        'pregunta': "¿Cuál de estas opciones itera sobre los índices de una lista?",
        'opciones': ['for i in lista:', 'for lista in i:', 'while lista:', 'if lista:'],
        'respuesta': 'for i in lista:'
    },
    {
        'pregunta': "¿Qué estructura permite múltiples condiciones secuenciales?",
        'opciones': ['if - elif - else', 'for - else', 'while - else', 'try - except'],
        'respuesta': 'if - elif - else'
    },
    {
        'pregunta': "¿Cómo se recorre una cadena caracter por caracter?",
        'opciones': ['for char in cadena:', 'while cadena:', 'if cadena:', 'loop cadena:'],
        'respuesta': 'for char in cadena:'
    },
    {
        'pregunta': "¿Qué sucede si la condición de un `while` nunca se cumple?",
        'opciones': ['Bucle infinito', 'Se salta el bucle', 'Error de sintaxis', 'Termina el programa'],
        'respuesta': 'Se salta el bucle'
    },
    {
        'pregunta': "¿Qué sentencia se utiliza para pasar a la siguiente iteración en un bucle?",
        'opciones': ['pass', 'continue', 'skip', 'next'],
        'respuesta': 'continue'
    }
]

# Variables de estado
total = 0
respuestas = []

# Crear formulario
datos = {}
for idx, q in enumerate(preguntas):
    datos[idx] = st.radio(q['pregunta'], q['opciones'], key=f"q{idx}")

# Botón para evaluar
efet = st.button("Calcular puntaje")
if efet:
    for idx, q in enumerate(preguntas):
        if datos[idx] == q['respuesta']:
            total += 1
    st.write(f"Tu puntaje es {total} / {len(preguntas)}")
    if total == len(preguntas):
        st.balloons()
