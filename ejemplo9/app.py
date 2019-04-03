from flask import Flask, render_template,abort
app = Flask(__name__)	

notas = [
    {"id":1,"nombre":"Paco Pérez","curso":"4º","nota":"6.25"}, 
    {"id":2,"nombre":"Manuel Rodríguez","curso":"3º","nota":"5.00"},
    {"id":3,"nombre":"María Roldán","curso":"2º","nota":"7.15"}]

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html",lista_notas=notas)

@app.route('/alumno/<int:id>')
def alumno(id):
	for alumno in notas:
		if alumno["id"]==id:
			return render_template("alumno.html",alum=alumno)
	abort(404)
	
app.run(debug=True)