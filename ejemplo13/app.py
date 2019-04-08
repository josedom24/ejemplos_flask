from flask import Flask, render_template,request
app = Flask(__name__)	


@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

@app.route('/suma',methods=["GET","POST"])
def suma():
    if request.method=="GET":
        return render_template("formulario.html")    
    else:
        num1=request.form.get("numero1")
        num2=request.form.get("numero2")
        try:
            resultado = int(num1) + int(num2)
        except:
            abort(404)
        return render_template("suma.html", num1=num1, num2=num2,
resultado=resultado)	
app.run(debug=True)