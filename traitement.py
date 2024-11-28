import mysql.connector

bd=mysql.connector.connect(
    
    database="bdd_exercice_securite",
    host="localhost",
    username="root",
    password=""
)

#unsertions dans la base de de donnée

def inserer_etudiant(nom,post_nom,prenom):
    req="INSERT INTO etudiant(nom,post_nom,	prenom) VALUES(%s,%s,%s)"

     #creer la curseur,il permet d'executer la requete sql

    curseur=bd.cursor()

    #fournir les données a inserer sous forme d'un tuple
    donnees=(nom,post_nom,prenom)

    #execution de la requete sql par le curseur
    curseur.execute(req,donnees)

     #enrregistrer de maniere permanente dans la table
    bd.commit()

    # selections  tous les etudiants se trouvant dans la base de donnée
def select_etudiants_bdd():
    req="SELECT *FROM etudiant"
    curseur=bd.cursor()
    curseur.execute(req)
    donnees=curseur.fetchall()
    return donnees

    # selections  un etudiant se trouvant dans la base de donnée en fonction de son id

def affiche_on_etudiant(id_etudiant):
    req="SELECT * FROM etudiant WHERE id_etudiant=%s"
    curseur=bd.cursor()
    donnees=(id_etudiant,)
    curseur.execute(req,donnees)
    resultat=curseur.fetchall()
    return resultat

def modifier_etudiant(id_etudiant,nom,post_nom,	prenom):
    req="UPDATE etudiant SET nom=%s,post_nom=%s,prenom=%s WHERE id_etudiant=%s"
    donnees=(nom,post_nom,prenom,id_etudiant)
    curseur=bd.cursor()
    curseur.execute(req,donnees)
    bd.commit()
#modifier_etudiant(1,"franck","franck","franck")

# suppression d'un etudiant
def supprimer_etudiant(id_etudiant):
    req="DELETE FROM etudiant WHERE id_etudiant=%s"
    curseur=bd.cursor()
    donnees=(id_etudiant,)
    stock=curseur.execute(req,donnees)
    return ""






