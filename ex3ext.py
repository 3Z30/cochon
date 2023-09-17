# MESSE Théo
# Cochon qui rit


import random
import time


class Player:

    def getMax(self):
        i = 0
        if (self.parts["oeil"] == 2):
            i += 1
        if (self.parts["oreille"] == 2):
            i += 1
        if (self.parts["patte"] == 4):
            i += 1
        return i

    def __init__(self, name):
        self.name = name
        self.parts = {'oeil': 0, 'oreille': 0, 'patte': 0, 'queue': 0}
        self.has_body = False
        self.shot = 0

def print_rules():
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

def game():
    print("Bienvenue. Vous allez jouer à \"Cochon qui rit\" !")
    if (input("Souhaitez-vous voir les règles du jeu ? Tapez \"o\" pour les voir\n> ").lower() == "o"):
        print_rules()

    won = False
    players = []

    # Définir le nombre de joueurs
    while True:
        players_count = int(input("Combien de joueurs ? (2-4)\n> "))
        if (2 <= players_count <= 4):
            break

    # Initialise une liste avec une instance de la classe 'Player' par joueur
    for i in range(players_count):
        players.append(Player(input(f"Nom du joueur {i + 1} ?\n> ")))

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
                nb_as = dices.count(1)

                print(f"\n{player.name}, ton lancer donne: {dices}")

                # Incrémente le compteur de tours
                player.shot += 1

                # Si le joueur n'a pas encore trouvé le corps et fait 6 sur un dé
                if (not player.has_body and dices.count(6) >= 1):
                    player.has_body = True
                    print(f"Bravo, {player.name} tu récupères le corps")

                # Si le corps a été trouvé et tombe sur un as
                if (player.has_body and nb_as >= 1):
                    print(f"Bravo, {player.name} tu as fait {nb_as} as.")

                    # Tant que l'utilisateur n'a pas utilisé tous les as
                    while (nb_as > 0):

                        if ((player.getMax() >= 3) and (nb_as < 2)):
                            break

                        print(f"\nIl te reste {nb_as} as à utiliser.")

                        while True:
                            # On affiche les parties que l'utilisateur possède
                            print("\nTu as actuellement {} oreille(s), {} patte(s), {} queue, {}"
                                  .format(player.parts["oreille"], player.parts["patte"],
                                          player.parts["queue"], player.parts["oeil"])
                                  + (" oeil\n" if player.parts["oeil"] == 1 else " yeux\n"))

                            # On lui demande quelle partie ajouter
                            to_add = input("Quelle partie veux-tu ajouter: \n\toeil, patte, oreille"
                                           + (", queue\n> " if nb_as > 1 else "\n> ")).lower()

                            # On vérifie que ce qu'il demande est bien une partie qui existe
                            if (to_add in player.parts.keys()):
                                break
                            else:
                                print(f"\"{to_add}\" n'est pas une partie valide !")

                        # S'il choisit d'ajouter la queue
                        if (to_add == "queue"):

                            # On vérifie qu'il a assez d'as
                            if (nb_as > 1):

                                # On vérifie qu'il n'a pas déjà la queue
                                if (player.parts["queue"] == 0):

                                    # On retire deux as et on lui ajoute la queue
                                    player.parts["queue"] += 1
                                    nb_as -= 2 if player.getMax() != 3 else nb_as

                                    # On affiche les parties que l'utilisateur possède
                                    print("\nTu as maintenant: {} oreille(s), {} patte(s), {} queue, {}"
                                          .format(player.parts["oreille"], player.parts["patte"],
                                                  player.parts["queue"], player.parts["oeil"])
                                          + (" oeil\n" if player.parts["oeil"] == 1 else " yeux\n"))

                                else:
                                    print("Tu as déjà une queue, tu ne peux pas en avoir plus.")
                            else:
                                print("Il te faut au moins 2 as pour prendre la queue.\n")

                        else:

                            # Si l'utilisateur choisit d'ajouter une oreille ou un oeil et qu'il ne les a pas déjà
                            if ((to_add == "oreille" or to_add == "oeil") and player.parts[to_add] < 2):
                                # On utilise un as du lancé et on ajoute la partie demandée
                                player.parts[to_add] += 1
                                nb_as -= 1 if player.getMax() != 3 else nb_as

                                # On affiche les parties que l'utilisateur possède
                                print("\nTu as maintenant: {} oreille(s), {} patte(s), {} queue, {}"
                                      .format(player.parts["oreille"], player.parts["patte"],
                                              player.parts["queue"], player.parts["oeil"])
                                        + (" oeil\n" if player.parts["oeil"] == 1 else " yeux\n"))

                            # Si l'utilisateur choisit d'ajouter une patte et qu'il n'en a pas déjà 4
                            elif ((to_add == "patte") and player.parts["patte"] < 4):
                                # On utilise un as du lancé et on ajoute la partie demandée
                                player.parts[to_add] += 1
                                nb_as -= 1 if player.getMax() != 3 else nb_as

                                # On affiche les parties que l'utilisateur possède
                                print("\nTu as maintenant: {} oreille(s), {} patte(s), {} queue, {}"
                                      .format(player.parts["oreille"], player.parts["patte"],
                                              player.parts["queue"], player.parts["oeil"])
                                      + (" oeil\n" if player.parts["oeil"] == 1 else " yeux\n"))

                            # Sinon, c'est qu'il a forcément déjà le nombre maximum de la partie demandée
                            else:
                                print(f"Tu as déjà {player.parts[to_add]} {to_add}, tu ne peux pas en avoir plus !")

                    # Si le joueur n'a pas gagné et a fait un as, il rejoue
                    if (player.getMax() == 3 and player.parts["queue"] == 1):
                            won = True
                            print(f"Félicitations {player.name} !! Tu remportes la partie après {player.shot} coups !")
                    else:
                        play_again = True
                        print(f"{player.name}, c'est encore à toi de jouer !")

    if (input("Souhaitez-vous refaire une partie ? \"o\" pour oui.\n> ").lower() == "o"):
        print("\n### Nouvelle partie ###\n")
        game()
    else:
        print("\nAu revoir")


game()
