from flask import Flask, render_template

app = Flask(__name__)

# Diccionario completo con las definiciones e información detallada de cada tema
conceptos = {
    "html": {
        "titulo": "¿Qué es HTML?",
        "puertas": [
            {"titulo": "Definición", "contenido": "HTML (HyperText Markup Language) es el lenguaje estándar de marcado utilizado para estructurar y organizar el contenido de las páginas web."},
            {"titulo": "Estructura", "contenido": "Organiza la información mediante una jerarquía de elementos y etiquetas semánticas como cabeceras, secciones y pies de página."},
            {"titulo": "Navegador", "contenido": "El navegador web lee este archivo de código plano y lo interpreta visualmente para que el usuario pueda interactuar con él."},
            {"titulo": "Semántica", "contenido": "Permite dar significado al contenido, mejorando notablemente la accesibilidad web y el posicionamiento SEO en buscadores."}
        ]
    },
    "etiquetas": {
        "titulo": "Etiquetas HTML Principales",
        "pasos": [
            {"num": "1", "etiqueta": "<h1> ... </h1>", "desc": "Define el título o encabezado principal de mayor jerarquía visual en la página web."},
            {"num": "2", "etiqueta": "<p> ... </p>", "desc": "Crea bloques de párrafos estructurados para organizar todo el texto y descripciones."},
            {"num": "3", "etiqueta": "<a href='...'> ... </a>", "desc": "Genera hipervínculos o enlaces de navegación hacia otros sitios o páginas internas."},
            {"num": "4", "etiqueta": "<img src='...' alt='...'>", "desc": "Inserta imágenes multimedia indicando su ruta de origen y texto alternativo descriptivo."}
        ]
    },
   "css": {
        "titulo": "CSS y Atributos Visuales",
        "tira": [
             # --- NUEVO BOTÓN/TIRA AGREGADO AQUÍ ---
            {"prop": "Definición", "sintaxis":"CSS (Cascading Style Sheets) es el lenguaje que define el estilo, los colores y el diseño visual de una página web en HTML."},
            {"prop": "color", "sintaxis": "color: #2e7d32;", "uso": "Define el color del texto aplicado a los elementos HTML."},
            {"prop": "background", "sintaxis": "background: #c8e6c9;", "uso": "Modifica el color o imagen de fondo de cualquier contenedor visual."},
            {"prop": "padding", "sintaxis": "padding: 15px;", "uso": "Establece el espacio de relleno interior entre el contenido y su borde."},
            {"prop": "border", "sintaxis": "border: 2px dashed green;", "uso": "Crea un borde decorativo alrededor del elemento visual seleccionado."},
        ]
    },
    "jinja": {
        "titulo": "Motor de Plantillas Jinja",
        "paginas": [
            {"sub": "¿Qué es Jinja?", "texto": "Es un motor de plantillas para Python (utilizado en Flask) que permite insertar variables, condiciones y lógica directamente en el HTML."},
            {"sub": "Variables", "texto": "Se comunican desde Python usando dobles llaves, por ejemplo: {{ nombre_variable }} para inyectar datos dinámicos."},
            {"sub": "Estructuras de Control", "texto": "Permite programar bucles {% for %} y condiciones {% if %} para automatizar la generación de elementos repetitivos."}
        ]
    },
    "sql": {
        "titulo": "Bases de Datos SQL",
        "sobre_info": {
            "titulo_sobre": "Gestión y Consultas Relacionales",
            "contenido": "SQL (Structured Query Language) es el lenguaje estándar para administrar bases de datos relacionales.\n\n• SELECT: Consulta y extrae registros específicos.\n• INSERT: Agrega nuevos datos a la base.\n• UPDATE / DELETE: Modifican o eliminan información guardada."
        }
    },
    "javascript": {
        "titulo": "JavaScript Interactivo",
        "cuadros": [
            {"titulo": "Eventos del DOM", "detalle": "element.addEventListener('click', function() { ... })"},
            {"titulo": "Variables", "detalle": "let usuario = 'Ana'; const activo = true;"},
            {"titulo": "Funciones", "detalle": "function calcular(a, b) { return a + b; }"},
            {"titulo": "Consola", "detalle": "console.log('Depurando código en tiempo real');"}
        ]
    }
}

@app.route('/')
def home():
    # Enviamos el diccionario 'conceptos' como la variable 'd' al index.html
    return render_template('index.html', d=conceptos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)