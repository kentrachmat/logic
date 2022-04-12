from lark import Lark, Transformer
import formule

grammaire = r"""
CONJ: "/\\" | "∧"
DISJ: "\\/" | "∨"
NEG:  "~" | "¬"
FALSE: "faux" | "⊥"
TRUE: "vrai" | "T"


formules: disjunction            -> une_formule
         | disjunction formules  -> des_formules

disjunction: disjunction DISJ conjunction  -> ou_formule
           | conjunction                   -> ou_vide

conjunction: conjunction CONJ atom         -> et_formule
           | atom                          -> et_vide

atom: NEG atom -> negation
| FALSE    -> faux
| TRUE     -> vrai
| NAME     -> var
| "(" disjunction ")" -> par_atom

%import common.CNAME -> NAME
%import common.WS
%ignore WS
"""


class Formule(Transformer):
    """Classe qui transforme un arbre d'analyse de la grammaire des formules en représentation mémoire des formules.

    """
    def une_formule(self,ch):
        return ch

    def des_formules(self,ch):
        [f,fs] = ch
        return [f]+fs

    def ou_formule(self,ch):
        [d,_,c] = ch
        return formule.Ou(d,c)

    def ou_vide(self,ch):
        [f] = ch
        return f

    def et_formule(self,ch):
        [c,_,a] = ch
        return formule.Et(c,a)

    def et_vide(self,ch):
        [f] = ch
        return f

    def negation(self,ch):
        [_,f] = ch
        return formule.Non(f)

    def faux(self,ch):
        return formule.Faux()

    def vrai(self,ch):
        return formule.Vrai()

    def var(self,ch):
        [nom] = ch
        if nom == "vrai" or nom == "T":
            return formule.Vrai()
        elif nom == "faux" or nom == "⊥":
            return formule.Faux()
        else:
            return formule.Variable(nom)

    def par_atom(self,ch):
        [f] = ch
        return f

analyseur_formules = Lark(grammaire,
                          start='formules',
                          parser='lalr',
                          transformer = Formule()).parse

def formules_depuis_fichier(f):
    """Fonction qui analyse les formules contenues dans le fichier passé en argument et renvoie la liste de ces formules représentées en mémoire par des objets, Et, Ou, Non, ..."""
    with open(f) as f:
        return analyseur_formules(f.read())

