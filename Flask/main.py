from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Aprendiendo Flask'

@app.route('/informacion/<string:nombre>/<int:apellidos>')
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


if __name__ == '__main__':
    app.run(debug=True)