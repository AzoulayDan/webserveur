# -*- coding: utf-8 -*-
import json, random
from flask import Flask, request
from flask_cors import CORS, cross_origin
from db import Db

app = Flask(__name__)
app.debug = True
CORS(app)

#Vider la base
@app.route('/reset',methods=['GET'])
def reset():
    db = Db()
    db.executeFile("db.sql")
    db.close()
    return "Reset done."

#Liste de tous les utilisateurs
@app.route('/users', methods=['GET'])
def get_users():
    db = Db()
    test = db.select('SELECT * FROM User;')
    db.close()
    return test

@app.route('/inscription', methods=['post'])
def get_players():
    db = Db()                               #Ouverture de la connection avec la base de donnée.
    data = request.get_json()               #Récupération de l'objet Json.

    verif = db.select("SELECT * FROM User where name = '%s';" % (data['name']))

    #Si la taille de mon élement est vide alors cet intitulé n'est pas dans la base.
    if (len(verif) != 0):
        db.close()
        return json.dumps("Ce nom est déja utilisé"), 400, {'Content-Type': 'application/json'}
    else:
        db.execute("INSERT INTO Joueur(name,posX,posY,rayon,budget) VALUES (%s,%s,%s,%s,%s); ",(data['name'], posX, posY, rayon, bugdet))
        db.close()
        # Je récupére l'id du dernier joueur ajouté
        return 0

if __name__ == "__main__":
  app.run()