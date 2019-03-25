from flask import Flask, render_template,abort
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

@app.route('/<operador>/<int:op1>/<int:op2>',methods=["GET","POST"])
def saluda(operador,op1,op2):
	if operador=="sumar":
		op = "+"
		resultado = op1 + op2
	elif operador=="restar":
		op = "-"
		resultado = op1 - op2
	elif operador=="multiplicar":
		op = "*"
		resultado = op1 * op2
	elif operador=="dividir":
		op = "/"
		try:
			resultado = op1 / op2
		except:
			abort(404)
	else:
		abort(404)
	return render_template("operar.html",num1=op1,num2=op2,op=op,res=resultado)


app.run(debug=True)