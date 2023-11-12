def remplir_matrice(N, P):
    matrice = [[0] * P for _ in range(N)]
    valeur = 1

    for i in range(N):
        for j in range(P):
            matrice[i][j] = valeur
            valeur += 1

    return matrice

def afficher_matrice(matrice):
    for ligne in matrice:
        print(ligne)

def afficher_matrice_alternative(matrice):
    for i, ligne in enumerate(matrice):
        if i % 2 == 0:
            print(ligne)
        else:
            print(ligne[::-1])

N = int(input("Entrez le nombre de lignes (N) : "))
P = int(input("Entrez le nombre de colonnes (P) : "))

if 0 < N <= 10 and 0 < P <= 10:
    matrice = remplir_matrice(N, P)

    print("Matrice normale :")
    afficher_matrice(matrice)

    print("\nMatrice alternative :")
    afficher_matrice_alternative(matrice)
else:
    print("Les valeurs de N et P doivent être comprises entre 1 et 10.")
