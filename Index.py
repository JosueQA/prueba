from flask import Flask, render_template
            # el metodo render_template, nos permite importar alguna plantilla

app = Flask(__name__)

@app.route('/')

# Utilizamos el @ para crear nuestras url´s, se le llama decurador
# El método router nos indica la extension del link, nos agrega rutas por ejm google.com/route
# / es simplemente la pagina principal, es lo primero que vera el usuario
def home():
    # return 'Home page'
        # Creamos una funcion llamada home, que cuano se entre a la ruta establecida recibirá "Home page"
    return render_template('home.html')
        # Usamos el metodo render_template para que incorpore la plantilla que emos creado llamada home.html
        # Las plantillas deben estar en su propia carpeta

@app.route('/about')
    # Creamos una extensión del url, la cual se llamará about
def about():
    return render_template('About.html')
    # La extensión del link sera /about

if __name__ == '__main__':
    app.run(debug=True)
    # Estos comandos son para que esto se tome como una aplicacion y se mantenga corriendo
    # debug quiere decir que por cada cambio que haga se reiniciara automaticamente