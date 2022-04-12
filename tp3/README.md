# Pour commencer

Commencez par "forker" le dépôt, puis clonez le. Invitez ensuite votre chargé de
TD/TP pour lui donner accès à votre travail.

Pour pouvoir travailler, il faut installer le module lark-parser:

```shell
pip install lark-parser
```


Les fichiers avec lesquels vous allez travailler pour ce TP sont : 

- formule.py : définition d'une structure de données construire à partir d'objet
  pour représenter les formules. Les classes qui permettent de construire des
  formules sont:
  - Et : pour construire des conjonctions
  - Ou : pour construire des disjonctions
  - Non : pour construire de négations
  - Vrai : pour construire des tautologies
  - Faux : pour construire des contradictions
  - Variables : pour construire des variables propositionnelles.
  Par exemple Et(Non(Variables("b"), Ou(Variable("a",Non(Variable("c"))))))
  représente la formule : 
  ¬ b ∧ (a ∨ ¬ c)
  
- tp.py : fichier dans lequel vous testerez les fonctionnalités que vous
  implémenterez pendant le TP.
  
- formules.txt : fichier dans lequel vous pourrez écrire des formules avec
  lesquelles vous pourrez tester votre travail. Les formules n'utilisent que les
  opérateurs suivantes:
  - conjonction notée : /\ ou ∧
  - disjonction notée : \/ ou 
  - négation notée : ~ ou ¬
  - tautologie notée : vrai ou T
  - contradiction notée : faux ou ⊥
  Quelques exemples de formules sont déjà notés dans le fichier.
  
  La fonction /formules_depuis_fichier/, importée du module analyseur, lit les
  formules écrites dans un fichier, contruit les structures correspondantes à
  l'aide des classes du fichier formule.py et les place dans une liste.
  
# Objectifs du TP

Le TP a pour objectifs d'implémenter diverses opérations sur les formules. Il
s'agit pour cela d'implémenter des méthodes pour chacune des classes du fichier
formule.py.

## Exemple des objets vers les chaînes
  
  Le fichier contient un exemple d'implémentation d'une transformation de la
  représentation /objet/ des formules vers une représentation en chaîne de
  caractères. Cette implémentation est réalisée avec la méthode to_string()
  définie pour chacune des classes.
  
  - Étudiez cette implémentation dans le fichier formule.py
  - Voyez comment elle est utilisée dans le fichier tp.py pour imprimer à
    l'écran, après transformation, les formules du fichier formules.txt
    
## Calcul de la hauteur d'une formules
   
   En vous inspirant de la méthode to_string(), implémentez une méthode dans
   chacune des classe qui calcule la hauteur d'une formule comme cela est défini
   dans le cours.
   
## Variables apparaissant dans une formules

   De façon similaire, implémentez les méthodes /variables/ qui calculent
   l'ensemble des variables contenues dans une formule (nous voulons les noms de
   ces variables). Pour cela, vous pourrez utiliser la structure d'ensemble
   python :
   - pour créer un ensemble vide, il suffit d'utiliser l'expression set()
   - pour créer un ensemble ne contenant qu'un élément x, il suffit d'utiliser
     l'expression set(x)
   - pour calculer l'union de deux ensemble e1 et e2, il suffit d'utiliser l'une
     des deux expressions suivantes :
     1. e1.union(e2)
     2. e1 | e2
     
## Évaluation d'une formule

   En suivant la même approche que précédemment implémentez les méthodes /eval/
   qui, étant une valuation, calcule la valeur de vérité d'une formule. Les
   valuations serons représentées par des dictionnaires qui à des chaînes de
   caractères, les nom des variables, associent un booléen, leur valeur de
   vérité.
   
   Par exemple la valuation qui à a associe vrai, à b faux et à c vrai s'écrit
   en python:
   {'a' : True, 'b' : False, 'c' : True}
   Enfin, pour récupérer la valeur associée à un nom x dans un dictionnaire d,
   il suffit d'écrire d[x].
   
## Pousser les négations

   Enfin, implémentez les méthodes /pousse_negation/ qui produisent une formule
   équivalente à la formule de départ, mais dont toutes les négations ne portent
   que sur des variables.
   
   Par exemple, il faut que cette méthode transforme la formule
   ~(~a \/ ~(~(a /\ b) \/ c))
   en a /\ (a /\ b /\ ~c)
   
   La méthode /pousse_negation/ prend un argument booléen neg qui permet de se
   rappeler si on est passé à travers un nombre paire ou impaire de négation au
   cours de la traversée de la formule.
   

