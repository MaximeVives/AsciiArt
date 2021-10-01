# AsciiArt
## Présentation

Ce projet est issu du site coding game et du puzzle [Ascii-art](https://www.codingame.com/training/easy/ascii-art]). 



## But du programme

L'art ASCII permet de représenter des formes en utilisant des caractères. Dans notre cas, ces formes sont précisément des mots. Par exemple, le mot "MANHATTAN" pourra être affiché ainsi en art ASCII :

 ```python
 
  
  #   #     #     # # #   #   #     #     # # #   # # #     #     # # # 
  # # #   #   #   #   #   #   #   #   #     #       #     #   #   #   # 
  # # #   # # #   #   #   # # #   # # #     #       #     # # #   #   # 
  #   #   #   #   #   #   #   #   #   #     #       #     #   #   #   # 
  #   #   #   #   #   #   #   #   #   #     #       #     #   #   #   # 
  
 
 ```

Il faut donc écrire un programme capable d'afficher une ligne de texte en art ASCII dans un style qui est fourni en entrée.

## Les entrées du programme

**Ligne 1 :** la largeur **L** d'une lettre représentée en art ASCII. Toutes les lettres font la même largeur.

**Ligne 2 :** la hauteur **H** d'une lettre représentée en art ASCII. Toutes les lettres font la même hauteur.

**Ligne 3 :** La ligne de texte **T**, composée de **N** caractères ASCII

**Lignes suivantes :** La chaîne de caractères _ABCDEFGHIJKLMNOPQRSTUVWXYZ?_ représentée en art ASCII.



## Les sorties du programme

Le texte **T** en art ASCII.
Les caractères de a à z seront affichés en art ASCII par leur équivalent en majuscule.
Les caractères qui ne sont pas dans les intervalles [a-z] ou [A-Z], seront affichés par le point d'interrogation en art ASCII.

### Exemple 1 

Entrée

```
4
5 
E
    #     # #       # #   # #     # # #   # # #     # #   #   #   # # #     # #   #   #   #      #   #     
  #   #   #   #   #       #   #   #       #       #       #   #     #         #   #   #   #      # # #    
  # # #   # #     #       #   #   # #     # #     #   #   # # #     #         #   # #     #      # # #    
  #   #   #   #   #       #   #   #       #       #   #   #   #     #     #   #   #   #   #      #   #    
  #   #   # #       # #   # #     # # #   #         # #   #   #   # # #     #     #   #   # # #  #   #     
  
  
  
  # # #     #     # #       #     # #       # #   # # #   #   #   #   #   #   #   #   #   #   #   # # #   # # #   
  #   #   #   #   #   #   #   #   #   #   #         #     #   #   #   #   #   #   #   #   #   #       #       #   
  #   #   #   #   # #     #   #   # #       #       #     #   #   #   #   # # #     #       #       #       # #   
  #   #   #   #   #         # #   #   #       #     #     #   #   #   #   # # #   #   #     #     #               
  #   #     #     #           #   #   #   # #       #     # # #     #     #   #   #   #     #     # # #     #    
```

Sortie

```
# # # 
#   
# #  
#   
# # # 
```

### Exemple 2

Entrée

```
4
5
MANHATTAN
    #     # #       # #   # #     # # #   # # #     # #   #   #   # # #     # #   #   #   #      #   #     
  #   #   #   #   #       #   #   #       #       #       #   #     #         #   #   #   #      # # #    
  # # #   # #     #       #   #   # #     # #     #   #   # # #     #         #   # #     #      # # #    
  #   #   #   #   #       #   #   #       #       #   #   #   #     #     #   #   #   #   #      #   #    
  #   #   # #       # #   # #     # # #   #         # #   #   #   # # #     #     #   #   # # #  #   #     
  
  
  
  # # #     #     # #       #     # #       # #   # # #   #   #   #   #   #   #   #   #   #   #   # # #   # # #   
  #   #   #   #   #   #   #   #   #   #   #         #     #   #   #   #   #   #   #   #   #   #       #       #   
  #   #   #   #   # #     #   #   # #       #       #     #   #   #   #   # # #     #       #       #       # #   
  #   #   #   #   #         # #   #   #       #     #     #   #   #   #   # # #   #   #     #     #               
  #   #     #     #           #   #   #   # #       #     # # #     #     #   #   #   #     #     # # #     #    
```

Sortie

```
 #   #     #     # # #   #   #     #     # # #   # # #     #     # # # 
 # # #   #   #   #   #   #   #   #   #     #       #     #   #   #   # 
 # # #   # # #   #   #   # # #   # # #     #       #     # # #   #   # 
 #   #   #   #   #   #   #   #   #   #     #       #     #   #   #   # 
 #   #   #   #   #   #   #   #   #   #     #       #     #   #   #   # 
```

