from flask import Flask, render_template,request,abort
app = Flask(__name__)	


@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

@app.route('/entrar',methods=["GET","POST"])
def entrar():
    datos=[
    {"valor":1,"texto":"Windows"},
    {"valor":2,"texto":"Linux"},
    {"valor":3,"texto":"MacOs"}
    ]
    if request.method=="GET":
        return render_template("formulario.html",datos=datos)
    else:
        usuario=request.form.get("usuario")
        passwd=request.form.get("pass")
        so=request.form.get("sistema")
        if passwd=="asdasd":
            return render_template("entrar.html")	
        else:
            return render_template("formulario.html",datos=datos,usuario=usuario,seleccionado=int(so),error=True)

app.run(debug=True)