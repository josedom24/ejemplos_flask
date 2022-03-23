from flask import Flask, render_template,request,abort
app = Flask(__name__)	


@app.route('/',methods=["GET"])
def inicio():
    datos=[
    {"valor":1,"texto":"Windows"},
    {"valor":2,"texto":"Linux"},
    {"valor":3,"texto":"MacOs"}
    ]

    seleccionado="Linux"

    return render_template("inicio.html",datos=datos,seleccionado=seleccionado)

@app.route('/procesar',methods=["POST"])
def procesar():
    
    return render_template("datos.html", datos=request.form)	
app.run(debug=True)