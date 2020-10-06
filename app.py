from fssc_lib import fssc, tes
from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
	if request.method == 'POST':
		file=request.files["myfile"]
		akurasi, jumlah_benar=fssc(file,0.2)
		return render_template("index.html", results=jumlah_benar, resultsA=akurasi)

@app.route('/predict',methods=["POST"])
def predict():
	if request.method == 'POST':
		sepalL = request.form['sepalL']
		sepalW = request.form['sepalW']
		petalL = request.form['petalL']
		petalW = request.form['petalW']

		x = tes(float(sepalL),float(sepalW),float(petalL),float(petalW))
		if (x==0):
			x="Iris-setosa"
		elif (x==1):
			x="Iris-versicolor" 
		else:
			x="Iris-virginica"
		return render_template("index.html", sl=sepalL, sw=sepalW, pl=petalL, pw=petalW, hasil=x)


if __name__ == '__main__':
	app.run(debug=True)