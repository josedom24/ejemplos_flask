from flask import Flask, render_template
app = Flask(__name__)	

@app.route('/')
def inicio():
    persona = "juan"
    num1=10
    num2=14
    return render_template("inicio.html",nombre=persona,edad=12,numero1=num1,numero2=num2,resultado=num1+num2) 

@app.route('/articulos')
def articulos():
    lista = ["sandía","manzana","platano","piña","kiwi"]
    return render_template("articulos.html",lista=lista)

@app.route('/acercade')
def acercade():
    enlaces=[{"url":"http://www.google.es","texto":"Google"},
			{"url":"http://www.twitter.com","texto":"Twitter"},
			{"url":"http://www.facbook.com","texto":"Facebook"},
			{"url":"http://www.josedomingo.org","texto":"Pledin"},
			{"url":"https://dit.gonzalonazareno.org/moodle","texto":"Moodle"}
			]
    return render_template("acercade.html",enlaces=enlaces)


app.run("0.0.0.0",5000,debug=True)