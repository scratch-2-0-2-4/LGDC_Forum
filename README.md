# LGDC-Forum

### Installation 

``` Bash
pip install lgdc-forum
```

### Connexion

``` Python
lf.login(token="VOTRE_TOKEN", user_id="VOTRE_ID_UTILISATEUR")
```

> [!WARNING]
> Ne montrez **JAMAIS**, à **QUI QUE CE SOIT** votre token.
##### ou
``` Python
lf.login() # Anonyme, ne peux pas poster de messages.
```

### Poster des messages

>[!CAUTION]
> **NE PAS UTILISER À DES FINS DE SPAM SOUS PEINE DE SANCTION !**

#### Poster dans une discussion déjà existante

``` Python
session.post("contenu", id_de_la_discussion)
```

#### Créer une nouvelle discussion

``` Python
session.create_discussion("titre", "contenu", tag_ids=[X, X]) # X = id des tags / sous-tags
```

<details>
<summary>Info sur les tags</summary>
 
| ID | Nom de la catégorie | Type | Usage dans `tag_ids` |
| :--- | :--- | :--- | :--- |
| **1** | Annonces | Principale | `[1]` |
| **2** | Général | Principale | `[2]` |
| **5** | Spoiler Alerte | Principale | `[5]` |
| **6** | Badges | Principale | `[6]` |
| **7** | Blagues | Principale | `[7]` |
| **8** | Pub | Principale | `[8]` |
| **9** | LGDC | Principale | `[9]` |
| **10** | Date de sortie d'un livre | **Sous-catégorie** | `[9, 10]` |
| **11** | Sondages | **Sous-catégorie** | `[9, 11]` |
| **12** | Spoiler Alerte | **Sous-catégorie** | `[9, 12]` |
| **14** | Bugs | **Sous-catégorie** | `[33, 14]` |
| **15** | Remerciements | Principale | `[15]` |
| **16** | Informatique | Principale | `[16]` |
| **17** | Sports | Principale | `[17]` |
| **18** | Images animées | Principale | `[18]` |
| **19** | Jeux vidéos | Principale | `[19]` |
| **20** | Idées pour le site | Principale | `[20]` |
| **21** | Blog | Principale | `[21]` |
| **22** | IMPORTANT !!!!! | **Sous-catégorie** | `[1, 22]` |
| **23** | Musique | Principale | `[23]` |
| **24** | Les Loups Des Découvertes | **Sous-catégorie** | `[25, 24]` |
| **25** | Livres | Principale | `[25]` |
| **26** | Site officiel LGDC anglais | **Sous-catégorie** | `[9, 26]` |
| **27** | Site officiel LGDC Français | **Sous-catégorie** | `[9, 27]` |
| **28** | Info officiel | Principale | `[28]` |
| **29** | LRDF | Principale | `[29]` |
| **31** | Digital Circus | **Sous-catégorie** | `[18, 31]` |
| **33** | Aide | Principale | `[33]` |
| **34** | SPAM | Principale | `[34]` |
| **35** | Thiago Social / Thiago Social 2 | **Sous-catégorie** | `[16, 35]` |

Exemple :

Pour faire une discussion dans "date de sortie d'un livre : sous catégorie de LGDC" et dans "informatique", vous codez :

``` Python
session.create_discussion("titre", "contenu", tag_ids=[9, 10, 16])
```

</details>


### Obtenir le nom à partir de l'ID

``` Python
session.get_username(ID)
```

### Obtenir les groupes de l'utilisateur à partir de son ID

``` Python
session.get_user_groups(ID)
```
: Renvoie la liste des rôles et groupes d'un utilisateur.

### Obtenir TOUS les tags disponnibles

``` Python
session.get_tags()
```

![](https://badgen.net/#github/license/scratch-2-0-2-4/lgdc_forum)
