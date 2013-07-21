import sys

def usage():
    sys.stdout.write("Prints prime numbers below n\n")
    sys.stdout.write("Usage: \n")
    sys.stdout.write("\tpython %s n\n"%sys.argv[0])

if len(sys.argv) != 2 :
    usage()
    sys.exit(1)

maxi = int(sys.argv[1])
premiers = [i+1 for i in range(maxi)]
premiers.remove(1)

a = 2 # boucle de parcours
while a < maxi :
    # on teste si chaque entier est un multiple de l'entier courant
    for nombre in premiers:
    #on enlève ceux qui le sont
        if nombre%a == 0 and nombre !=a :
            premiers.remove(nombre)
    a+=1

sys.stdout.write("Il a %d nombres premiers inférieurs à %d.\n"%(len(premiers),maxi))
print(premiers)
