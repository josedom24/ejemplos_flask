from flask import Flask, render_template
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	enlaces=[{"url":"http://www.google.es","texto":"Google"},
			{"url":"http://www.twitter.com","texto":"Twitter"},
			{"url":"http://www.facbook.com","texto":"Facebook"},
			{"url":"http://www.josedomingo.org","texto":"Pledin"},
			{"url":"https://dit.gonzalonazareno.org/moodle","texto":"Moodle"}
			]
	return render_template("inicio.html", enlaces=enlaces)
app.run(debug=True)