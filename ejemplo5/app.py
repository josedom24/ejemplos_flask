from flask import Flask, render_template, request
app = Flask(__name__)	

notas = [
    {"id":1,"nombre":"Paco Pérez","curso":"4º","nota":"6.25"}, 
    {"id":2,"nombre":"Manuel Rodríguez","curso":"3º","nota":"5.00"},
    {"id":3,"nombre":"María Roldán","curso":"2º","nota":"7.15"}]

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/lista_url')
def lista_url():
    return render_template("lista_url.html",lista_notas=notas)


@app.route('/lista_dinamica')
def lista_dinamica():
    return render_template("lista_dinamica.html",lista_notas=notas)


@app.route('/alumno')
def alumno():
    id=int(request.args.get("id"))
    for alumno in notas:
        if alumno["id"]==id:
            return render_template("alumno.html",alum=alumno)
    return abort(404)



@app.route('/alumno/<id>')
def alumno_dinamico(id):
	for alumno in notas:
		if alumno["id"]==int(id):
			return render_template("alumno.html",alum=alumno)
	return abort(404)


app.run("0.0.0.0",5000,debug=True)