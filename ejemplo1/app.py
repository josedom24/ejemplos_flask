from flask import Flask, render_template
app = Flask(__name__)	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/articulos/')
def articulos():
    return render_template("articulos.html")

@app.route('/acercade')
def acercade():
    return render_template("acercade.html")


app.run(debug=True)