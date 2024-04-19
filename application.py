import customtkinter
import google.auth
from google.cloud import datastore

# Définissez le chemin d'accès à la clé de compte de service
#key_path = r'C:\UQAC\Session Hiver 2024\InfoNuagique\Projet\bddr-infonuagique-a3a6e2eb7b73'

# Créez un client Datastore à l'aide de la clé de compte de service
#client = datastore.Client.from_service_account_json(key_path)
#print(client)
# Liste des pays disponibles
pays = ["France", "Belgium", "United States", "Nigerian"]

# Création de la fenêtre principale de l'application
app = customtkinter.CTk()
app.title('cloudDataBaseMovies')
app.geometry('400x150')

# Création d'un menu déroulant pour sélectionner le pays
variable = customtkinter.StringVar(app)
variable.set(pays[0])
menu = customtkinter.CTkComboBox(app, values=pays)
menu.set(pays[0])
menu.pack(pady=20)

# Création d'une fonction pour afficher les films du pays sélectionné
#def afficher_films():
    # Récupération du pays sélectionné
    #pays_selectionne = variable.get()

    # Requête pour récupérer les films du pays sélectionné dans la base de données
    #query = client.query(kind='Film')
    #query.add_filter('pays', '=', pays_selectionne)
    #films = list(query.fetch())

    # Création d'un cadre pour afficher les films
    #frame_films = customtkinter.CTkFrame(app)
    #frame_films.pack(pady=20)

    # Affichage des films dans le cadre
    #for film in films:
    #    titre = film['titre']
    #    duree = film['duree']
    #    synopsis = film['synopsis']
    #    cast = film['cast']

        # Création d'un cadre pour afficher les informations du film
        #frame_film = customtkinter.CTkFrame(frame_films)
        #frame_film.pack(pady=10)

        # Création d'une étiquette pour afficher le titre en gras
        #label_titre = customtkinter.CTkLabel(frame_film, text=titre, font=('bold', 14))
        #label_titre.pack()

        # Création d'une étiquette pour afficher la durée
        #label_duree = customtkinter.CTkLabel(frame_film, text=duree)
        #label_duree.pack()

        # Création d'une étiquette pour afficher le synopsis
        #label_synopsis = customtkinter.CTkLabel(frame_film, text=synopsis)
        #label_synopsis.pack()

        # Création d'une étiquette pour afficher le cast
        #label_cast = customtkinter.CTkLabel(frame_film, text=cast)
        #label_cast.pack()

# Création d'un bouton pour afficher les films du pays sélectionné ,command=afficher_films
bouton = customtkinter.CTkButton(app, text="Afficher les films" )
bouton.pack()

# Démarrage de la boucle principale de l'application
app.mainloop()
