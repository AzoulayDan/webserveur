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
@app.route('/inscrit', methods=['GET'])
def get_users():
    db = Db()
    test = db.select('SELECT * FROM inscrit;')
    db.close()
    return json.dumps(test), 201, {'Content-Type': 'application/json'}


@app.route('/inscription', methods=['post'])
def ajout_inscrit():
    db = Db()                               #Ouverture de la connection avec la base de donnée.
    data = request.get_json()               #Récupération de l'objet Json.

    verif = db.select("SELECT * FROM User where name = '%s';" % (data['name']))

    #Si la taille de mon élement est vide alors cet intitulé n'est pas dans la base.
    if (len(verif) != 0):
        db.close()
        return json.dumps("Ce nom est déja utilisé"), 400, {'Content-Type': 'application/json'}
    else:
        db.execute("INSERT INTO inscrit(id_joueur) VALUES (%s); ",(data['name']))
        db.close()
        # Je récupére l'id du dernier joueur ajouté
        return json.dumps('OK'), 201, {'Content-Type': 'application/json'}

#En cours#
@app.route('/gettimage', methods=['get'])
def envoyerimagegoogle():

input_file

output_filename

		"""Translates the input file into a json output file.

		Args:
			input_file: a file object, containing lines of input to convert.
			output_filename: the name of the file to output the json to.
		"""
		request_list = []
		for line in input_file:
			image_filename, features = line.lstrip().split(' ', 1)

			with open(image_filename, 'rb') as image_file:
				content_json_obj = {
					'content': base64.b64encode(image_file.read()).decode('UTF-8')
				}

			feature_json_obj = []
			for word in features.split(' '):
				feature, max_results = word.split(':', 1)
				feature_json_obj.append({
					'type': get_detection_type(feature),
					'maxResults': int(max_results),
				})

			request_list.append({
				'features': feature_json_obj,
				'image': content_json_obj,
			})

		with open(output_filename, 'w') as output_file:
			json.dump({'requests': request_list}, output_file)


	DETECTION_TYPES = [
		'TYPE_UNSPECIFIED',
		'FACE_DETECTION',
		'LANDMARK_DETECTION',
		'LOGO_DETECTION',
		'LABEL_DETECTION',
		'TEXT_DETECTION',
		'SAFE_SEARCH_DETECTION',
	]


	def get_detection_type(detect_num):
		"""Return the Vision API symbol corresponding to the given number."""
		detect_num = int(detect_num)
		if 0 < detect_num < len(DETECTION_TYPES):
			return DETECTION_TYPES[detect_num]
		else:
			return DETECTION_TYPES[0] 
  
  
  




        #nomfichier = chemin + "/" + str(name)
        #return send_file(nomfichier), 200, {'Content-Type': 'image/jpeg'}

    #Post vers google







    return 0

if __name__ == "__main__":
  app.run()