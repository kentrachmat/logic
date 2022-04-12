"""
Author : Benedictus Kent Rachmat
Groupe : 6B
TP3 Logique
"""
from analyseur import formules_depuis_fichier

from formule import *

for num,f in enumerate(formules_depuis_fichier("formules.txt")):
    print ('No.',num+1)
    print ("String     : "+f.to_string())
    print ("Hauteur    : "+str(f.hauteur()))
    print ("Variables  : "+str(f.variables()))
    print ("Evaluation {a:1, b:0, c:1, d:0} : "+str(f.eval({'a':1,'b':0,'c':1,'d':0})))
    # ou on peut aussi le faire avec boolean -> {'a':True, 'b':False, 'c':True, 'd':False}
    print ("Pousse Negation (True)   : "+f.pousse_negation(True).to_string())
    print ("Pousse Negation (False)  : "+f.pousse_negation(False).to_string())
    print()
