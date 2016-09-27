#Script pour vérifier une solution du problème ouvert sur les fractions
n=int(input("Quelle est la valeur de n ? \n"))
a=int(input("Quelle est la valeur de a ? \n"))
b=int(input("Quelle est la valeur de b ? \n"))
c=int(input("Quelle est la valeur de c ? \n"))
if 1/a+1/b+1/c==4/n:
    print("Décomposition juste")
else:         
    print("Décomposition fausse")5
    