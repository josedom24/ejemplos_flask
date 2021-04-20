from flask import Flask, render_template,abort
import os
app = Flask(__name__)
	

notas = [
    {"id":1,"nombre":"Paco Pérez","curso":"4º","nota":"6.25"}, 
    {"id":2,"nombre":"Manuel Rodríguez","curso":"3º","nota":"5.00"},
    {"id":3,"nombre":"María Roldán","curso":"2º","nota":"7.15"},
	{"id":1000,"nombre":"José Domingo","curso":"2º","nota":"10"}]

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html",lista_notas=notas)

@app.route('/alumno/<int:id>')
def alumno(id):
	for alumno in notas:
		if alumno["id"]==id:
			return render_template("alumno.html",alum=alumno)
	abort(404)
port=os.environ["PORT"]
app.run("0.0.0.0",int(port),debug=True)

