import sys
from random import randint

joueur_pv = 50
ennemie_pv = 50
#joueur_degat = randint(5 , 10)
#ennemie_degat = randint(5 , 15)
nombre_de_potion = 3
#pv_rendus = randint(15 , 50)
saisie = ""

while (joueur_pv > 0 and ennemie_pv > 0) :
    saisie = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?\n👉 ") 
    if not saisie.isdigit() or int(saisie) <1 or int(saisie) >2 :
        print("Choisissez une action en écrivant 1 ou 2")
        print("-" * 50)
        continue
    saisie = int(saisie)
    print("-" * 50)

    if saisie == 1 :
        joueur_degat = randint(5 , 10)
        ennemie_pv = ennemie_pv - joueur_degat
        ennemie_degat = randint(5 , 15)
        joueur_pv = joueur_pv - ennemie_degat
        
        print (f"""🧙 Vous avez infligé {joueur_degat} points de dégats à l'ennemi ⚔️
🧛 L'ennemi vous a infligé {ennemie_degat} points de dégats ⚔️
🧙 Il vous reste {joueur_pv} points de vie ❤️
🧛 Il reste {ennemie_pv} points de vie à l'ennemi ❤️""")
        print("-" * 50)
        
    else :
        if nombre_de_potion == 0 :
            print("Vous n'avez plus de potion 🧪")
            print("-" * 50)
        else :
            nombre_de_potion -=1
            pv_rendus = randint(15 , 50)
            joueur_pv = joueur_pv + pv_rendus
            print (f"""Vous récupérez {pv_rendus} points de vie ❤️, 
Il vous reste {nombre_de_potion} potions 🧪 dans votre inventaire.""")

            ennemie_degat = randint(5 , 15)
            joueur_pv = joueur_pv - ennemie_degat
            print(f"""🧛 L'ennemi vous a infligé {ennemie_degat} points de dégats ⚔️
🧙 Il vous reste {joueur_pv} points de vie ❤️
🧛 Il reste {ennemie_pv} points de vie à l'ennemi ❤️""")
            print("-" * 50)
            print("Vous passez votre tour...")
            ennemie_degat = randint(5 , 15)
            joueur_pv = joueur_pv - ennemie_degat
            print(f"""🧛 L'ennemi vous a infligé {ennemie_degat} points de dégats ⚔️
🧙 Il vous reste {joueur_pv} points de vie ❤️
🧛 Il reste {ennemie_pv} points de vie à l'ennemi ❤️""")
            print("-" * 50)

if ennemie_pv <= 0 and joueur_pv <= 0 :
    print("Vous avez perdu 💀")
    sys.exit()
elif ennemie_pv <= 0 :
    print("Bravo, vous avez gagné ! 💪")
    sys.exit()
elif joueur_pv <= 0 :
     print("Vous avez perdu 💀")
     sys.exit()

