from flask import Flask, redirect, url_for, render_template

# Crear la app de flask
app = Flask(__name__)

# Definir las rutas con el metodo route
@app.route('/')
def index():
    # Uso render_template para cargar un template
    # Al estar dentro de la carpeta template no necesito indicar la ruta
    return render_template('index.html')

#Defino la misma ruta para hacer que el parametro sea opcional
@app.route('/informacion')
# Podemos pasar parametros en la ruta '/<>'
# Tambien podemos definir el formato del parametro 'string:'
@app.route('/informacion/<string:nombre>')
# Para recibir la informacion pasamos los parametros a la funcion
def informacion(nombre = None):
    
    texto = ""
    if nombre != None:
        texto = f'<h3>Bienvenido, {nombre}</h3>'
    # Para pasarle la variable la agrego desp del template
    return render_template('informacion.html', texto=texto)

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None): 

    if redireccion is not None:
        #Podemos redireccionar paginas utilizando redirect
        return redirect(url_for('lenguajes'))

    return '<h1>Pagina de contacto</h1>'

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return '<h1>Pagina de lenguajes</h1>'

# Esto es para identificar el fichero principal
if __name__ == '__main__':
    # Debug True indica que estamos en modo debug
    app.run(debug=True)