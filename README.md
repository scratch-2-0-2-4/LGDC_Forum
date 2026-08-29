``` Bash
pip install lgdc-forum
```

``` Python
lf.login(token=VOTRE_TOKEN, user_id=VOTRE_ID_UTILISATEUR")
```

``` Python
session.post(contnu, id_de_la_discussion)
```

``` Python
session.create_discussion(titre, contenu, tag_ids=[X, X]) # X = id des tags / sous-tags
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

</details>


``` Python
session.get_username(ID)
```
: Obtient le nom d'utilisateur (pseudo) à partir de son ID.
 
``` Python
session.get_user_groups(ID)
```
: Renvoie la liste des rôles et groupes d'un utilisateur.

``` Python
session.get_tags()
```
: Liste l'ensemble des catégories (tags) disponibles sur le forum.session.get_subcategories(parent_tag_id) : Renvoie uniquement les sous-catégories d'un tag parent spécifique.


session.get_user_data(target_user_id) : Récupère les données brutes JSON de l'API pour un utilisateur.
