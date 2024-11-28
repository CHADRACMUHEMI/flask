from flask import Flask,render_template,request,redirect
import traitement

#creations de l'instance
app=Flask(__name__)

@app.route('/')
def accueil():
    return render_template("index.html")

#appel de la fonction pour afficher tous les etudiants de la base de donnée

@app.route('/etudiant')
def voir_etudiants():
    etudiants=traitement.select_etudiants_bdd()
    return render_template('etudiant.html',liste_etudiant=etudiants)

# la route qui vous dirige vers l'inscription du formulaire
@app.route('/remplir_inscription')
def inscription():
    return render_template('formulaire_etudiant.html')

@app.route('/affiche_on_etudiant/<id_etudiant>')
def affiche_on_etudiant(id_etudiant):
    etudiant=traitement.affiche_on_etudiant(id_etudiant)
    return render_template("modifier_etudiant.html",etudiant=etudiant)

#modification d'un etudiant
@app.route('/modifier_etudiant/<id_etudiant>',methods=['GET','POST'])
def modifier_etudiant(id_etudiant):
    modif=traitement.modifier_etudiant(id_etudiant,request.form['nom'],request.form['pst'],request.form['prenom'])
    return redirect('/etudiant')

# suppression d'un etudiant
@app.route("/supprimer_on_etudiant/<id_etudiant>")
def supprimer_on_etudiant(id_etudiant):
    etudiant=traitement.supprimer_etudiant(id_etudiant)
    return redirect("/etudiant")


#la route qui vous permet d'inserer le formulaire dans la base de donnée
@app.route('/inserer_etudiant',methods=['GET','POST'])
def insert_etudiants():
    if request.method=='POST':
        nom_etudiant=request.form['nom']
        p_etudiant=request.form['pst']
        prenom_etudiant=request.form['prenom']
        print(f"NOM:{nom_etudiant},POSTNOM:{ p_etudiant},PRENOM:{ prenom_etudiant}")
        traitement.inserer_etudiant(nom_etudiant,p_etudiant, prenom_etudiant)
      
        return redirect('/etudiant')

    



#lancemment du serveur
app.run(debug=True)

