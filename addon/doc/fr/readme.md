# Thunderbird+

* Auteurs : Pierre-Louis Renaud(Thunderbird 78 à 102) & Cyrille Bougot (TB 102), Daniel Poiraud (TB 68 à 91), Yannick (TB 45 à 60) ;
* URL : [Manuel de l'utilisateur][4] ;
  [Historique des changements sur RPTools.org][5] ;
  [Contact][6] ;
* Télécharger la [version stable][1]
* Télécharger la [Dernière version sur RPTools.org][3] ;
* Compatibilité NVDA : 2019.3 et supérieur ;
* Compatibilité  Thunderbird  : versions 102.x ;
* [Ccode source sur gitHub][2]

Note : Cette extension n'est pas compatible avec l'extension Mozilla Apps Enhancements. Si cette dernière est  installée, vous devez la désactiver ou la désinstaller avant d'installer  ThunderbirdPlus ;

## Description

Cette extension améliore  considérablement le confort et l'efficacité d'utilisation du client de messagerie Mozilla Thunderbird avec NVDA.

Les améliorations portent sur les aspects suivants  :

### Confort auditif

* Les alertes  "un tel a demandé un accusé de réception" peuvent être désactivées via une option ;
* Les alertes "Ceci est un brouillon" et "Thunderbird pense que ce message est frauduleux " sont tout simplement passées sous silence ;
* Des options permettent de désactiver l'annonce des noms de listes de diffusion, de supprimer ou regrouper les mentions "RE" et d'épurer les noms des correspondants en supprimant les nombres et autres caractères spéciaux gênants ;

### Navigation dans la fenêtre principale

* Le passage au panneau suivant s'effectue à l'aide de la touche TAB tandis que la touche échappe permet de revenir au panneau précédent. Ceci est plus confortable que F6 et Maj+F6.
* La sélection des onglets avec Contrôle+Tab et Contrôle+un chiffre est vocalisée comme dans cet exemple :  Onglet 1 sur 4, Courrier entrant ;
* Un raccourci-clavier permet de lister les onglets  dans un menu afin d'en activer un facilement ;
* Un raccourci-clavier permet d'afficher le menu contextuel de la barre des onglets ;

### Arborescence des dossiers

* Alt+flèche bas et Alt+flèche haut  permettent de naviguer entre les dossiers avec des messages non-lus ;
* La frappe d'une lettre ou d'un chiffre sélectionne le prochain dossier dont le nom commence par le caractère frappé. Avec la touche Maj, le déplacement s'effectue du bas vers le haut. De plus, le nom du compte auquel le dossier appartient est annoncé ;
* La touche Espace sur un dossier avec des messages non lus sélectionne le premier message non lu dans la liste de messages ;
* Deux  dialogue des comptes et de leurs dossiers associés permet de les filtrer    par mot-clé ou de n'afficher que les dossiers avec des messages non-lus ;

### Liste de messages

* Le choix des colonnes ainsi que leur agencement dans la liste des messages est  rendu accessible par le biais d'un dialogue simple ;
* Consultation des colonnes de la liste de messages : des raccourcis permettent de réécouter, d'épeler ou de copier facilement le nom de l'expéditeur, le sujet ou la date d'un message en pressant un chiffre du clavier alphanumérique : par exemple, 1 ou &  annonce l'expéditeur, 2 appuis épelle le nom et 3 appuis le copie dans le presse-papiers ;
* Consultation des entêtes du volet des entêtes affiché avec F8 : avec Alt+un chiffre, 1 appui énonce un entête contenant les adresses    de l'expéditeur ou des destinataires, 2 appuis ouvre un dialogue permettant de les copier, 3 appuis ouvre le menu contextuel natif de Thunderbird associé à l'entête ;
* Aperçu rapide  épuré du texte du message  avec espace, Alt+flèche bas ou F4 : les grands blocs d'entêtes dans les citations de messages sont remplacés par l'expression "Nom de l'expéditeur a écrit". NVDA annoncera également "lien cliquable" à la place de la longue adresse du lien.
* Aperçu rapide  des citations dans leur ordre chronologique, du bas vers le haut, via Maj+Espace, Alt+flèche haut ou Maj+F4 ;
* Accès aisé aux pièces jointes par le raccourci Alt+page suivante ou le chiffre 1 du clavier alpha-numérique ;

### Barre de filtrage rapide   et gestion des étiquettes de priorité

* Il est possible de naviguer parmi   Les options de filtrage à l'aide des flèches verticales. La touche Entrée permet de cocher ou décocher une option ;
* L'ajout ou le retrait d'étiquettes s'effectue par le simple appui sur Maj+un chiffre du clavier alphanumérique. Par exemple, appuyez sur 4 pour ajouter l'étiquette "A faire" à un message. On peut ensuite filtrer la liste des messages par étiquettes via la barre de filtre rapide qui est désormais accessible ;

### Fenêtre de rédaction d'un message

Alt+1 annonce l'Expéditeur,Alt+2 le destinataire, Alt+3 les pièces jointes,etc. Deux appuis place le focus sur un de ces champs ;

### Dialogue de vérification orthographique

* Le  mot mal orthographié  est annoncé avec ou sans épellation avant le mot suggéré. Les raccourcis NVDA+Tab ou Alt+flèche haut annoncent les mots mal orthographié et de remplacement : 1 appui épelle les mots à une vitesse normale, 2 appuis les épelle rapidement,3 appuis copie le mot mal orthographié dans le presse-papiers pour une analyse dans un autre champ d'édition ;
* Diverses combinaisons de la touche entrée actionnent les boutons Remplacer, Tout remplacer, Ignorer, Tout ignorer ou Ajouter le mot au dictionnaire ont été ajoutés pour un confort accru  de ce dialogue ;

### Mise à jour automatique

ThunderbirdPlus dispose d'un  système indépendant de mise à jour automatique avec des options de désactivation / réactivation et de report ;

### Fonctionnement en duo avec Chichi

ThunderbirdPlus est prévu pour fonctionner harmonieusement avec Chichi, un module complémentaire qui s'installe directement dans Thunderbird.

Lisez à ce sujet la [page de Chichi][7] ;


Et bien d'autres choses que vous découvrirez en lisant le [manuel de l'utilisateur][4] ;

<!-- Traducteurs : Dans les liens 4, 5 et 7 ci-dessous, où vous voyez lang=en,  remplacez en par le code de votre langue -->

[1]: https://github.com/RPTools-org/ThunderbirdPlus/releases/download/v4.9/thunderbirdPlus-4.9-TB102.nvda-addon

[2]: https://github.com/RPTools-org/ThunderbirdPlus/

[3]: https://www.rptools.org/?p=8610

[4]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=manual&lang=fr

[5]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=changes&lang=fr

[6]: https://www.rptools.org/NVDA-Thunderbird/toContact.html

[7]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=chichi&lang=fr
