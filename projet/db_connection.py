from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['gestion_ouvrage']

auteurs = db['auteurs']
categories = db['categories']
ouvrages = db['ouvrages']

# Insertion d'exemples
auteur_id = auteurs.insert_one({"nom": "AuteurNom", "prenom": "AuteurPrenom"}).inserted_id
categorie_id = categories.insert_one({"nom": "CategorieNom"}).inserted_id

ouvrages.insert_one({
    "titre": "Titre de l'ouvrage",
    "date_publication": "2023-08-05",
    "auteur": {"_id": auteur_id, "nom": "AuteurNom", "prenom": "AuteurPrenom"},
    "categorie": {"_id": categorie_id, "nom": "CategorieNom"}
})
