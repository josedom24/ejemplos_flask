from flask import Flask, render_template,request,abort
app = Flask(__name__)	


@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

@app.route('/entrar',methods=["POST"])
def entrar():
    usuario=request.form.get("usuario")
    passwd=request.form.get("pass")
    if passwd=="asdasd":
        return render_template("entrar.html")	
    else:
        return render_template("inicio.html",usuario=usuario)
app.run(debug=True)