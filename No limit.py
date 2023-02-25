print("bienvenue sur No limits")

Name = input("Quel est ton prénom ? ")
if Name.upper() == "TAO":
    print("Erreur tu n'es pas autorisé à utiliser l'application"), exit()
print("Hereux que tu sois sur No limits " + Name + ",bien commençons !" )

Genre = input("Es-tu un homme ou une femme ? ")
Poids = round(float(input("Quel est ton poids (en Kg) ? ")))
Taille = float(input("Quel est ta taille (en m) ? "))
Taillecm = Taille*10**2
Age = float(input("Quel age as-tu " + Name + "? "))
Imc = round(Poids/Taille**2)
Lbs = round(Poids/0.45)

Question = input("Veux-tu savoir ton poids en lbs ? ")
if Question.lower().startswith("o"):
    print("Ton poids en lbs est " + str(Lbs) + "lbs")
    print("Ton imc (indice masse corporelle) est de " + str(Imc))
    if Genre.lower().startswith("f"):
        Img = round((1.20 * Imc) + (0.23 * Age) - 5.4)
        print("Et ton Img (indice masse grasse) est de " + str(Img) + "%")
    if Genre.lower().startswith("h"):
        Img = round((1.20 * Imc) + (0.23 * Age) - (10.8 * 1) - 5.4)
        print("Et ton Img (indice masse grasse) est de " + str(Img) + "%")
elif Question.lower().startswith("n"):
    print("Ton imc (indice masse corporelle) est de " + str(Imc))
    if Genre.lower().startswith("f"):
        Img = round((1.20 * Imc) + (0.23 * Age) - 5.4)
        print("Et ton Img (indice masse grasse) est de " + str(Img) + "%")
    if Genre.lower().startswith("h"):
        Img = round((1.20 * Imc) + (0.23 * Age) - (10.8 * 1) - 5.4)
        print("Et ton Img (indice masse grasse) est de " + str(Img) + "%")



act = input("Dans la journée es-tu actif ? (peu,légèrement,modérément,très) ")


if act.lower().startswith("p"):
    if Genre.lower().startswith("h"):
        icjh = round(((10*Poids) + (6.25*Taillecm) -(5*Age)+5) * 1.2)
        print("Tu as besoin de " + str(icjh) + " calories par jour")
        print("cela veut dire que si tu veux perdre tu devras être en dessous de " + str(icjh) + " calories")
        print("inversement, si tu désires prendre du poids")
    if Genre.lower().startswith("f"):
        icjf = round(((10*Poids) + (6.25*Taillecm) -(5*Age)-161) * 1.2)
        print("Tu as besoin de " + str(icjf) + " calories par jour")
        print("cela veut dire que si tu veux perdre tu devras être en dessous de " + str(icjf) + " calories")
        print("inversement, si tu désires prendre du poids")

if act.lower().startswith("l"):
    if Genre.lower().startswith("h"):
        icjh = ((10*Poids) + (6.25*Taillecm) -(5*Age)+5) * 1.375
        print("Tu as besoin de " + str(icjh) + " calories par jour")
        print("cela veut dire que si tu veux perdre tu devras être en dessous de " + str(icjh) + " calories")
        print("inversement, si tu désires prendre du poids")
    if Genre.lower().startswith("f"):
        icjf = round(((10*Poids) + (6.25*Taillecm) -(5*Age)-161) * 1.375)
        print("Tu as besoin de " + str(icjf) + " calories par jour")
        print("cela veut dire que si tu veux perdre tu devras être en dessous de " + str(icjf) + " calories")
        print("inversement, si tu désires prendre du poids")

if act.lower().startswith("m"):
    if Genre.lower().startswith("h"):
        icjh = round(((10*Poids) + (6.25*Taillecm) -(5*Age)+5) * 1.55)
        print("Tu as besoin de " + str(icjh) + " calories par jour")
        print("cela veut dire que si tu veux perdre tu devras être en dessous de " + str(icjh) + " calories")
        print("inversement, si tu désires prendre du poids")
    if Genre.lower().startswith("f"):
        icjf = round(((10*Poids) + (6.25*Taillecm) -(5*Age)-161) * 1.55)
        print("Tu as besoin de " + str(icjf) + " calories par jour")
        print("cela veut dire que si tu veux perdre tu devras être en dessous de " + str(icjf) + " calories")
        print("inversement, si tu désires prendre du poids")

if act.lower().startswith("t"):
    if Genre.lower().startswith("h"):
        icjh = round(((10*Poids) + (6.25*Taillecm) -(5*Age)+5) * 1.725)
        print("Tu as besoin de " + str(icjh) + " calories par jour")
        print("cela veut dire que si tu veux perdre tu devras être en dessous de " + str(icjh) + " calories")
        print("inversement, si tu désires prendre du poids")
    if Genre.lower().startswith("f"):
        icjf = round(((10*Poids) + (6.25*Taillecm) -(5*Age)-161) * 1.725)
        print("Tu as besoin de " + str(icjf) + " calories par jour")
        print("cela veut dire que si tu veux perdre tu devras être en dessous de " + str(icjf) + " calories")
        print("inversement, si tu désires prendre du poids")




pointfort = input("Quel est ton point fort ? (jambes,pec,dos,fesses...) ")

if pointfort.lower().startswith("p") + Genre.lower().startswith("h"):
    print("Ton entrainement sera plus accès sur le dos, les bras ainsi que les épaules.")
elif pointfort.lower().startswith("d") + Genre.lower().startswith("h"):
    print("Ton entrainement sera plus accès sur les bras, les pecs ainsi que les épaules.")
elif pointfort.lower().startswith("b")+ Genre.lower().startswith("h"):
    print("Ton entrainement sera plus accès sur les pecs, le dos ainsi que les épaules.")
elif pointfort.lower().startswith("e")+ Genre.lower().startswith("h"):
    print("Ton entrainement sera plus accès sur les bras, les pecs ainsi que le dos.")
elif pointfort.lower().startswith("j")+ Genre.lower().startswith("h"):
    print("Ton entrainement sera plus accès sur le haut du corps (les bras, les pecs les épaules ainsi que le dos.")


if pointfort.lower().startswith("j") + Genre.lower().startswith("f"):
    print("Ton entrainement sera plus accès sur le dos, les fesses ainsi que les bras.")
elif pointfort.lower().startswith("f") + Genre.lower().startswith("f"):
    print("Ton entrainement sera plus accès sur les bras, les jambes ainsi que le dos.")
elif pointfort.lower().startswith("b")+ Genre.lower().startswith("f"):
    print("Ton entrainement sera plus accès sur les jambes, le dos ainsi que les fesses.")
elif pointfort.lower().startswith("d")+ Genre.lower().startswith("f"):
    print("Ton entrainement sera plus accès sur les bras, les jambes ainsi que les fesses.")






