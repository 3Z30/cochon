# MESSE Théo
# Cochon qui rit


import random
import time


def game():
    print("Bienvenue. Vous allez jouer à \"Cochon qui rit\" !")
    if (input("Souhaitez-vous voir les règles du jeu ? Tapez \"o\" pour les voir\n> ").lower() == "o"):
        print("""\n*** Règles : ***
Le but du jeu est de reconstituer son cochon
Pour cela, vous allez jeter 3 dés à chaque tour
Suivant votre lancer, vous pourrez récupérer
différentes parties du corps de votre cochon
Le joueur va devoir récupérer le corps, 4 pattes, 2 oreilles, 2 yeux et 1 queue
Pour commencer, faire un 6 pour récupérer le corps de votre cochon
Faire un as pour récupérer une patte, une oreille ou un oeil
Faire deux as pour la queue
Tant qu'un joueur fait des as, il peut relancer
*** A vous de jouer ***\n""")

    won = False
    players = {}

    # Définir le nombre de joueurs
    while True:
        players_count = int(input("Combien de joueurs ? (2-4)\n> "))
        if (2 <= players_count <= 4):
            break

    # Initialise un dictionnaire pour chaque joueur contenant ses données
    # {Nom: [Corps trouvé ; Nombre d'as ; Nombre de coups]}
    for i in range(players_count):
        players[input(f"Nom du joueur {i + 1} ?\n> ")] = [False, 0, 0]

    while (not won):
        for player in players:
            time.sleep(0.25)
            play_again = True

            while (play_again):
                if won:
                    break

                play_again = False

                # Lance les dés pour le joueur
                dices = [random.randint(1, 7) for _ in range(3)]

                print(f"\n{player}, ton lancer donne: {dices}")

                # Incrémente le compteur de tours
                players[player][2] += 1

                for j in dices:

                    # Si le joueur n'a pas encore trouvé le corps et fait 6 sur un dé
                    if (not players[player][0] and j == 6):
                        players[player][0] = True
                        print(f"Bravo, {player} tu récupères le corps")
                        time.sleep(0.50)

                    # Si le corps a été trouvé et tombe sur un as
                    elif (players[player][0] and j == 1):

                        # On incrémente le compteur d'as
                        players[player][1] += 1

                        print(f"Bravo, {player} tu as fait un as. Tu en a maintenant {players[player][1]}.")

                        # Si le joueur n'a pas gagné et a fait un as, il rejoue
                        if (players[player][1] < 10):
                            play_again = True
                            print(f"{player}, c'est encore à toi de jouer !")


                        # Sinon on le fait gagner
                        else:
                            won = True
                            print(f"Félicitations {player} !! Tu remportes la partie après {players[player][2]} coups !")

                        time.sleep(0.50)

    if (input("\n\nSouhaitez-vous refaire une partie ? \"o\" pour oui.\n> ").lower() == "o"):
        print("\n### Nouvelle partie ###\n")
        game()
    else:
        print("\nAu revoir")


game()
