from flask import Flask

# Crear la app de flask
app = Flask(__name__)

# Definir las rutas con el metodo route
@app.route('/')
def index():
    return 'Aprendiendo Flask'

# Podemos pasar parametros en la ruta '/<>'
# Tambien podemos definir el formato del parametro 'string:'
@app.route('/informacion/<string:nombre>/<int:apellidos>')
# Para recibir la informacion pasamos los parametros a la funcion
def informacion(nombre, apellidos):
    return f'''
                <h1>Pagina de informacion</h1>'
                <p>Esta es la pagina de informacion</p>
                <h3>Bienvenido, {nombre} {apellidos}</h3>
    '''

@app.route('/contacto')
def contacto():
    return '<h1>Pagina de contacto</h1>'

@app.route('/lenguajes')
def lenguajes():
    return '<h1>Pagina de lenguajes</h1>'

# Esto es para identificar el fichero principal
if __name__ == '__main__':
    app.run(debug=True) # Debug True indica que estamos en modo debug