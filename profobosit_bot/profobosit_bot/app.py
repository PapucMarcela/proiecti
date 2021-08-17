from flask import Flask, render_template, request

app = Flask(__name__)

def ml(v,w,b,g,mf):
	wfhy = ["Da","da","dA","DA","Yes","Desigur","Si clar lucru","100%","Bineinteles","Dap","Cred ca da","Daaaaaa"]
	wfhn = ["Nu", "nu","nU","NU","NO","no","nO","nup","inca nu","Am uitat","Din pacate nu"]
	m = ["m","M","Mascul","Mujic","Barbat","Baiat","Barbatos","Om serios","Masculin"]
	f = ["f","F","Femele","Feminin","Femeie","Fata","Fetita","Mandra"]
	scor = 0 
	if (int(v)<25 and int(v)>17): scor +=0
	if (int(v)>25 and int(v)<64): scor -=1
	if (int(v)>63): scor -=2
	if w in wfhy: scor +=1
	if w in wfhn: scor -=1
	if (float(b)>=0.5): scor+=1
	if (float(b)<0.5): scor-=1
	if g in m : scor+=1
	if g in f : scor-=1
	if int(mf) >= 8 : scor -=2
	if (int(mf)<8 and int(mf)>=5): scor-=1
	if (int(mf)<5 and int(mf)>=2): scor+=0
	if (int(mf)<2): scor+=1
	return scor


def mls(scor):
    if (scor==0 or scor==1):
        return "Nu sunteti obosit. Continuati sa lucrati mai departe"
    if (scor==-1):
	    return "Sunteti obosit,totusi mai puteti lucra. "
    if (scor==-2):
	    return "Sunteti destul de obosit. Ar trebui sa faceti o pauza"
    if (scor<-2):
	    return "Sunteti foarte obosit. Faceti o pauza!"
    if (scor >= 2):
        return "Nu sunteti obosit deloc. Chiar deloc. Puteti lucra inca mult si bine"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form',methods=["POST"])
def form():
	nume = request.form.get("nume")
	prenume = request.form.get("prenume")
	varsta = request.form.get("varsta")
	wfh = request.form.get("wfh")
	br = request.form.get("br")
	gen = request.form.get("gen")
	mfs = request.form.get("mfs")
	return render_template("form.html",nume=nume,prenume=prenume,scor=ml(varsta,wfh,br,gen,mfs), chat = mls(ml(varsta,wfh,br,gen,mfs))) 




if __name__ == "__main__":
    app.run(debug=True)