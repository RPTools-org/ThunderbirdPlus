<!--  Translators :
Merci de ne pas traduire ni supprimer les 2 balises HTML suivantes :
<br> : retour à la ligne utilisé dans les éléments de listes
<a name="un-ID_personnel> : utilisé avant les titres repris dans la table des matières

Raccourcis-clavier spéciaux, automatiquement  détectés par l'addon  :
Puissance 2 : Dans toutes les langues, il faut renseigner le libellé de lla touche qui se trouve au-dessus de Tab.
égal : il faut toujours renseigner    la première touche à gauche de backspace.
parenthèse droite : renseignez la deuxième touche à gauche de backspace.
-->
# ThunderbirdPlus

* Auteur : Pierre-Louis Renaud(Thunderbird 78 à 102) & Cyrille Bougot (TB 102), Daniel Poiraud (TB 68 à 91), Yannick (TB 45 à 60) ;
* URL :  [Contact en Français et en Anglais](https://www.rptools.org/NVDA-Thunderbird/toContact.html) ;
* Téléchargeer  la [version stable][1]
* Télécharger la [Dernière version sur RPTools.org](https://www.rptools.org/?p=8610)
* Compatibilité NVDA : 2019.3 et supérieur ; 
* Compatibilité  Thunderbird  : versions 102.x ;
* [Historique des changements sur RPTools.org](https://www.rptools.org/NVDA-Thunderbird/changes.php?lg=fr) ;
* [Code source sur gitHub][2]

Note : Cette extension n'est pas compatible avec l'extension Mozilla Apps Enhancements. Si cette dernière est  installée, vous devez la désactiver ou la désinstaller avant d'installer  ThunderbirdPlus ;
<br>

## Description

Cette extension améliore  considérablement le confort et l'efficacité d'utilisation du client de messagerie Mozilla Thunderbird avec NVDA.

Les améliorations portent sur les aspects suivants  :

### Confort auditif

* Les alertes  "un tel a demandé un accusé de réception" peuvent être désactivées via une option ;
* Les alertes "Ceci est un brouillon" et "Thunderbird pense que ce message est frauduleux " sont tout simplement passées sous silence ; 
* Des options permettent de désactiver l'annonce des noms de listes de diffusion, de supprimer ou regrouper les mentions "RE" et d'épurer les noms des correspondants en supprimant les nombres et autres caractères spéciaux gênants ;  

### Navigation dans la fenêtre principale

* Le passage au panneau suivant s'effectue à l'aide de la touche TAB tandis que la touche échappe permet de revenir au panneau précédent. Ceci est plus confortable que F6 et Maj+F6. 
*  La sélection des onglets avec Contrôle+Tab et Contrôle+un chiffre est vocalisée comme dans cet exemple :  Onglet 1 sur 4, Courrier entrant ; 
* Un raccourci-clavier permet de lister les onglets  dans un menu afin d'en activer un facilement ;
* Un raccourci-clavier permet d'afficher le menu contextuel de la barre des onglets ;

### Arborescence des dossiers

* alt+flèche bas et Alt+flèche haut  permettent de naviguer entre les dossiers avec des messages non-lus ;
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

<!-- Translators : étiquettes = tags -->
### Barre de filtrage rapide   et gestion des étiquettes de priorité

* Il est possible de naviguer parmi   Les options de filtrage à l'aide des flèches verticales. La touche Entrée permet de cocher ou décocher une option ;
* l'ajout ou le retrait d'étiquettes s'effectue par le simple appui sur Maj+un chiffre du clavier alphanumérique. Par exemple, appuyez sur 4 pour ajouter l'étiquette "A faire" à un message. On peut ensuite filtrer la liste des messages par étiquettes via la barre de filtre rapide qui est désormais accessible ;


### Fenêtre de rédaction d'un message

Alt+1 annonce l'Expéditeur,Alt+2 le destinataire, Alt+3 les pièces jointes,etc. Deux appuis place le focus sur un de ces champs ;

### Dialogue de vérification orthographique : 

* le  mot mal orthographié  est annoncé avec ou sans épellation avant le mot suggéré. Les raccourcis NVDA+Tab ou Alt+flèche haut annoncent les mots mal orthographié et de remplacement : 1 appui épelle les mots à une vitesse normale, 2 appuis les épelle rapidement,3 appuis copie le mot mal orthographié dans le presse-papiers pour une analyse dans un autre champ d'édition ; 
* diverses combinaisons de la touche entrée actionnent les boutons Remplacer, Tout remplacer, Ignorer, Tout ignorer ou Ajouter le mot au dictionnaire ont été ajoutés pour un confort accru  de ce dialogue ; 

### Mise à jour automatique

ThunderbirdPlus dispose d'un  système indépendant de mise à jour automatique avec des options de désactivation / réactivation et de report ;

### Fonctionnement en duo avec Chichi 

ThunderbirdPlus est prévu pour fonctionner harmonieusement avec Chichi, un module complémentaire qui s'installe directement dans Thunderbird.

Lisez à ce sujet la [page de Chichi](https://www.rptools.org//Outils-DV/thunderbird-chichi.html) ;

### A propos des Langues

Certaines fonctionnalités ne fonctionneront pas correctement sir ThunderbirdPlus n'est pas traduite dans la langue que vous utilisez pour NVDA et Thunderbird.

* les alertes  ne seront pas interceptées. Il s'agit des alertes de brouillon, de demande d'accusé de réception, de message frauduleux, de  mise à jour, etc. ;
* l'amélioration du fonctionnement de la recherche de modules complémentaires  pour Thunderbird ne fonctionnera pas ;

A ce jour, l'extension est disponible dans les langues suivantes :

[Version originale en Français](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_fr.html) : par le développeur ;

Traductions par ordre d'ancienneté :

* [Portugais](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_pt_PT.html) : par Rui Fontes de chez TifloTecnia.com et membre de l'équipe NVDA Portugal ;
* [Espagnol](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_es.html) : par Rémy Ruiz ;
* [Anglais](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_en.html) : par Bachir Benanou ;


Merci aux traducteurs.


## Navigation entre les panneaux de l'onglet  des messages (Tab, Echappe) 

Il s'agit ici de l'onglet qui contient les panneaux suivants : l'arborescence des dossiers, la liste des messages et du volet des entêtes 'et d'aperçu du message (affiché ou masqué avec la touche F8).   

* TAB : passer au panneau suivant. Ce raccourci sera pour certains plus ergonomique que F6 ;
* Échappe : revenir au panneau précédent. Equivalent à Maj+F6 ;

Remarque : 

Lors de la tabulation à partir de la liste de messages pour atteindre le texte, la zone des entêtes est sautée. Pour atteindre   cette zone d'entêtes, pressez Alt+un chiffre du clavier alphanumérique trois fois rapidement puis Échappe pour quitter le menu contextuel de l'entête.  Ces raccourcis Alt+chiffre réduisent la nécessité de se rendre dans la zone d'entêtes. Pour plus de détails, voyez la section "Consultation des entêtes" plus bas.  


<a name="threadTree">

## Liste des messages, volet d'aperçu et fenêtre séparée de lecture 

Certains des raccourcis suivants sont communs à ces trois contextes, d'autres concernent un contexte en particulier.

<a name="attach">

### Accès aux pièces jointes (Alt+Page suivante) 

* Alt+page suivante ou Alt+p : si le panneau d'aperçu est affiché (via F8), Ouvre la liste des pièces jointes  du message sélectionné ;
* Alt+9 ou le chiffre 1 ou 2 : uniquement depuis la liste de messages, un appui énonce le nombre de pièces jointes, deux appuis ouvre la liste des pièces jointes  ;

<a name="readPreview">

### Lecture rapide et épurée   des messages 

* Les commandes de lecture rapide  d'un message sont disponibles  dans trois contextes : depuis la liste de messages, d'un message ouvert dans un onglet ou dans une fenêtre séparée ;
* Elles sont maintenant toutes compatibles avec les messages provenant de Framalistes ;
* La plupart des  raccourcis-clavier  de lecture rapide ont été concentrés  pour limiter au maximum le déplacement des mains durant une  séance  de lecture de nombreux messages ;
* Un seul appui sur la  touche principale d'un raccourci  lance la lecture épurée  du message, c'est à dire avec les entêtes des citations fortement raccourcis.
* Un double appui lance la lecture  du message dans sa forme originelle. Le terme de "lecture non filtrée" est synonyme ;

<a name="readFromList">

#### Lecture rapide des messages 'depuis la liste sans la quitter (Espace, F4 ou Alt+flèche bas) 

Pour profiter de cette fonctionnalité, vous devez d'abord afficher le volet de lecture  des messages avec la touche F8. En pressant cette touche, vous entendrez si ce volet est présent ou absent ;

Placez-vous ensuite dans la liste des messages et Utilisez  les touches suivantes :

* Espace, Alt+Flèche bas  ou F4 : lecture  du corps du message sans quitter  la liste. Après lecture d'un message, presser flèche vers le bas puis Espace ou Alt+flèche bas ou F4 pour écouter le message suivant ;
* En double frappe,  affiche la liste des liens du message si Chichi est actif. Si un article de flux RSS est sélectionné, il sera ouvert dans le navigateur Internet ;
* Maj+espace, Alt+Flèche haut ou Maj+f4 : idem mais lecture des citations dans leur ordre chronologique (du bas vers le haut) ;

Et pour compléter les commandes disponibles depuis la liste de messages, citons ici  :

* lettre n ou Alt+Flèche droite : sélectionne le prochain message non lu, même au travers des dossiers ;
* Alt+Page suivante ou Alt+p depuis la liste de messages : permet d'atteindre directement la zone des pièces jointes, sans devoir tabuler dans le texte ;  

<a name="readFromWinTab">

### Lecture rapide d'un message dans une fenêtre séparée ou un onglet de message (F4 ou Alt+Flèche bas) 

A l'ouverture d'un message dans une nouvelle fenêtre, le corps du message est lu automatiquement par défaut. Les raccourcis suivants vous permettent  néanmoins de réécouter le message à tout moment.

* F4 ou Alt+flèche bas : lecture rapide  du corps du message ;
* Maj+F4 ou Alt+flèche haut : idem mais en sens inverse ;

Remarques :

* Pour rappel,  un double appui sur ces raccourcis lance la lecture du message original ;
* La lecture automatique peut bloquer NVDA sur certains PC, surtout si le compte est configuré en IMAP. Pour tenter de résoudre ce problème, le raccourci Alt+d ouvre une boîte de saisie qui vous permet d'allonger le délai entre l'ouverture de la fenêtre et le début de la lecture automatique ;<br>
Si le réglage de ce délai ne résout pas le problème, vous pouvez désactiver cette lecture automatique via le menu [Maj+Puissance2](keyEquiv_fr.html#aboveTab)  / Options pour la fenêtre principale / fenêtre séparée de lecture : ne pas lire automatiquement le  message si provoque des blocages de NVDA ;
* Pour profiter au mieux de la lecture épurée et vous protéger du même coup des contenus distants qui ne respectent pas votre vie privée, affichez le corps des messages en HTML simple. Pour ce faire, ouvrez le menu Affichage, descendez sur Corps du message et dans le sous menu, validez l'option HTML simple.


Consultation  des colonnes et entêtes :

Il convient ici de faire la distinction entre colonnes et entêtes : le mot "colonne" est utilisé plus bas pour désigner la valeur d'une cellule d'une ligne dans le tableau des messages. Le  mot "entête" concerne  quant à lui le message lui-même. Les entêtes  sont consultables aussi bien dans le volet d'aperçu du message que  dans l'onglet ou fenêtre séparée d'un message ouvert ;

<a name="readCols">

### Consultation des colonnes : un chiffre du clavier alphanumérique 

Ces touches concernent les colonnes de la liste des messages uniquement. Pressez un chiffre du clavier alphanumérique sans presser la touche Maj :
* Un simple appui : énonce le nom et la valeur de la colonne correspondante ;
* Deux appuis sur un chiffre : épelle la valeur de la colonne correspondante ;
* Trois appuis rapides : copie la valeur de la colonne  dans le presse-papiers. Pour copier les adresses des divers expéditeur et destinataires, utilisez la consultation des entêtes vue plus bas ; 

<a name="readHeaders">

### Consultation des entêtes : Alt+un chiffre du clavier alphanumérique 

Ces raccourcis sont utilisables depuis la fenêtre principale si le panneau d'aperçu est affiché (via F8)  et depuis l'onglet ou la fenêtre séparée d'un message ouvert. Un appui énonce l'entête et deux appuis affiche un menu contextuel selon le cas ;

* Alt+1 : annonce le nom de l'expéditeur et  son adresse mail, Deux appuis   ouvre une  boîte d'édition de ces valeurs. Vous pouvez les modifier puis presser Entrée pour les copier dans le presse-papiers. 3 appuis : ouvre le menu contextuel de l'entête ;
* Alt+2 : Sujet avec le nom de la liste de diffusion le cas échéant ;
* Alt+3 : date du message ;
* Alt+4 pour : destinataires principaux du message,  Si plusieurs destinataires,  3 appuis positionne le focus sur le premier destinataire, ensuite tab  permet de passer au suivant, applications sur chaque destinataire affiche le menu contextuel ;
* Alt+5 : destinataires en copie ; 
* Alt+6 : destinataires en copie cachée ;
* Alt+7 : adresse "répondre à" ;
* Alt+8 : utilisateur, si les entêtes complets sont activés  via le menu Affichage / entêtes  / complets ; 
* Alt+9 : 1 appui annonce le nombre de pièces jointes, 2 appuis ouvre la liste des pièces jointes ;
* Alt+0 : liste  des étiquettes de priorité placées sur le message ;
* Alt+ [Parenthèse droite](keyEquiv_fr.html#bs2) ou Alt+fin : énonce une version abrégée de la barre d'état : nombre de messages non lus,  nombre total de messages ainsi que l'expression de filtrage rapide ; 
* Alt+ [Egal](keyEquiv_fr.html#bs1) : ouvre le menu contextuel des onglets ;
* Contrôle + [Egal](keyEquiv_fr.html#bs1) :  Affiche la liste des onglets ouverts dans un menu qui permet de sélectionner l'onglet choisi ;  

<a name="tags">

### Ajout et retrait d'étiquettes de priorité : Maj+un chiffre du clavier alphanumérique 

Cette fonctionnalité permet de marquer un message comme important ou à faire, par exemple. Ensuite, la barre de filtrage rapide permettra d'afficher seulement les messages ayant une ou plusieurs étiquettes. Par exemple, afficher  uniquement les messages importants dans la liste de messages ;

Pour vérifier les étiquettes déjà placées sur le message, pressez Alt+0 du clavier alphanumérique. 

Pour ajouter ou retirer une étiquette, pressez Maj+ un chiffre de 1 à 9 ; 


<a name="qfb">

### Barre de filtrage rapide (lettre f ou Contrôle+Maj+K) 

* lettre F ou Contrôle+Maj+K : affiche la barre de  filtrage rapide de message dans le dossier courant ;
* Filtrage par mot-clé : entrez un mot-clé puis pressez Tab pour parcourir la liste filtrée avec les flèches ;
* La flèche bas depuis la zone de saisie du mot-clé vous donne  accès à la liste des options  ci-dessous : 

    * 1 : Conserver les filtres lors des changements de dossier c
    * 2 : Afficher seulement les messages non lus l
    * 3: Afficher seulement les messages suivis
    * 4 : Afficher seulement les messages des personnes présentes dans mon carnet d’adresses d
    * 5: Afficher seulement les messages ayant des étiquettes é
    * 6 : Afficher seulement les messages ayant des pièces jointes j
    * etc.

* Pressez entrée  pour activer ou désactiver un ou plusieurs de ces critères ;
* Alt+fin ou Alt+ [Egal](keyEquiv_fr.html#bs1) : permet d'entendre un résumé des filtres actifs ainsi que le nombre de messages filtrés. Ces deux raccourcis fonctionnent également à partir de la liste de messages, pas seulement à partir de la barre de filtrage rapide ;

<br>
- lorsqu'un filtre rapide est actif, un fichier audio WAV est joué quand la liste ou l'onglet auquel elle appartient reçoit le focus. Le son ressemble à un souffle ;<br>
Le fichier filter.wav se trouve dans le dossier :<br> 
"%appdata%\\NVDA\\TB+sounds" <br>
Vous pouvez y placer un son à votre goût  pour autant que votre fichier se nomme : filter.wav. Après ce changement, il faut relancer NVDA ;v

<a name="tagFilter">

#### Filtrage Par étiquette 

lorsque le focus est placé sur la zone d'édition de la barre de filtre rapides :

*  Pressez  la flèche bas jusqu'à entendre "étiquettes" puis pressez Entrée pour cocher cette option ;
*  Pressez ensuite la touche Tab    pour atteindre la liste déroulante des modes de filtrage par étiquettes. Si vous choisissez par exemple "à faire", seuls les messages étiquetés  comme "à faire" seront listés dans le tableau des messages ;

<a name="colLayout">

### Agencement des colonnes (Alt+c) 

Le raccourci Alt+c affiche un dialogue qui permet de modifier  l'ordre des colonnes de la liste de messages et d'ajouter ou supprimer des colonnes.

Pour l'utiliser, placez-vous d'abord dans la liste des messages ou l'arborescence des dossier  puis pressez Alt+c ;

Le dialogue d'agencement des colonnes apparaît. Il se compose de la liste des colonnes ainsi que des   boutons "Aide", "colonnes" et "Fermer".

Le bouton "colonnes ..."     affiche le menu "Choisir les colonnes à afficher" natif de Thunderbird  

Lorsque vous vous trouvez dans la liste des colonnes, les raccourcis-clavier suivants sont disponibles :

* Flèche gauche  : affiche le menu de cases à cocher nommé "Choisir les colonnes à afficher". Ce raccourci correspond au bouton "Colonnes ..." ;
* Espace : pour déplacer la colonne sélectionnée, pressez Espace puis placez-vous   sur une autre colonne et pressez à nouveau Espace pour placer  la colonne à cet endroit. Cette opération est similaire à un couper-coller ;

Vous disposez également de ces raccourcis de déplacements directs :

* Contrôle + flèche haut ou flèche bas  :  monte ou descend  la colonne sélectionné  d'une position ;
* Contrôle + Début ou Fin : déplace la colonne sélectionnée  en haut ou en bas de la liste ;
* Contrôle + Page précédent ou page suivante : monte ou descend  la colonne sélectionné  de trois positions ;

Pour réaliser ces déplacement, Les colonnes sont en réalité déplacées en effectuant un glisser-déposer à la souris.  Un bip  d'une millisecondes se produit tous les 10 déplacement du pointeur ;

Lorsque le menu "Choisir les colonnes à afficher" est   présent, vous disposez des  nouveaux raccourcis-clavier  suivants :

* Flèche droite : affiche le dialogue d'agencement des colonnes ;
* Espace : coche ou décoche la colonne sélectionnée dans le menu. La touche Entrée produit encore le même comportement ;

Avec les flèches gauche et droite, il est donc très aisé de basculer entre le menu de choix des colonnes et le dialogue de leur agencement ;

<a name="smartReply">

### SmartReply : répondre à toutes les  listes de diffusion  en pressant  Contrôle+r 

Si vous êtes de ceux qui oublient de presser Contrôle+Maj+l pour répondre à une  liste de diffusion comme GoogleGroups, cette fonction vous évitera de répondre en privé à l'expéditeur d'un message sans vous en rendre compte. 

vous pourrez toujours presser Contrôle+r   comme suit :

* en simple frappe : pour répondre à la liste ;
* en double frappe : pour répondre en privé à l’expéditeur du message ;
* en simple frappe pour répondre à l'expéditeur d'un message ne provenant pas d'une liste ;

Remarques : 

La distinction entre simple ou double frappe sur ces raccourcis  fonctionne  sur  GoogleGroups, Framalistes et FreeLists.

Avec un seul appui,  sur une de ces trois listes, vous entendrez "à la list" avant l'ouverture de la fenêtre de rédaction. 

il conviendra aussi de ne pas utiliser la commande Répondre à tous" pour répondre à une liste  pour que l'expéditeur ne reçoive pas votre réponse en privé ; 

Et enfin, si vous souhaitez retrouver le comportement habituel de Contrôle+r :

* Pressez [Maj+Puissance2](keyEquiv_fr.html#aboveTab)  pour afficher le menu des Options ;
* Sélectionnez "Désactivations   pour Chichi et pour Thunderbird+ sous-Menu" ;
* Pressez Entrée pour décocher "Liste messages : pas de  SmartReply" ;

### Raccourcis a, j, m vocalisés

* a : Archive le message sélectionné, avec vocalisation. Pressez Contrôle+z pour annuler  cette opération ;
* j : marque ce message comme indésirable, avec vocalisation ;
* Maj+j : marque ce message comme acceptable, avec vocalisation ;
* m : marque les messages sélectionnés comme non lus. Maj+m les marque comme lus ; 

<a name="folderTree">

## Arborescence des Dossiers 

<a name="unreadFolders">

### Navigation rapide entre les dossiers contenant des messages non-lus (Alt+Flèche bas, Alt+Flèche haut) 

Lorsque vous vous trouvez dans l'arborescence des dossiers,  vous pouvez presser :

* Alt+flèche bas :   pour aller au prochain dossier avec des messages non-lus ;
* Alt+flèche haut : pour aller au précédent dossier avec des messages non lus ;
* Espace, Chichi non installé   : si le dossier sélectionné contient des messages non lus, sélectionne le premier message non lu de la liste ;
* Espace, Chichi installé  : idem sauf que si le dossier ne comporte pas de messages non lus, Chichi affichera la liste des dossiers non lus.<br>
En pressant entrée sur un dossier non lu dans cette liste, le premier message non lu de ce dossier sera activé dans la liste des messages ; <br>
Ceci vous permet de prendre rapidement connaissance des dossiers qui ont reçu des messages avant de décider par lequel vous souhaitez  commencer la lecture ;<br>

Dans cet ordre d'idées, voyez aussi ces deux dialogues :

* Dialogue des Listes filtrées des compte et dossiers (F12) 
* Liste des dossiers de l'arborescence principale, selon 4 types (F7, NVDA+F7 ou Maj+F12)

Note : avec un grand nombre de dossiers, Chichi est instantané, contrairement à ces deux dialogues ; 

<a name="folderDlg">

### Dialogue des Listes filtrées des  compte et dossiers (F12) 

Ce dialogue affiche les comptes et leurs dossiers associés dans deux listes séparées. Vous pouvez les filtrer sur base d'un mot-clé ou  restreindre la liste des dossiers à ceux comportant  des messages non lus.

Configuration du mode d'affichage par défaut  :

Si vous prévoyez d'afficher la plupart du temps les dossiers avec des messages non lus uniquement, placez vous d'abord dans l'arborescence des dossiers ou la liste des messages, Pressez ensuite le raccourci [Maj+Puissance2](keyEquiv_fr.html#aboveTab) et dans le sous-menu des options pour la fenêtre principale, validez l'élément intitulé : Afficher seulement les dossiers avec messages non lus.

Utilisation de base du dialogue :

* Depuis la fenêtre principale, pressez F12 pour afficher le dialogue. 
* Si vous avez configuré  l'affichage par défaut des  dossiers avec messages non lus, ceux-ci seront affichés dans la liste nommée   : Dossiers des comptes ;
* Dans le cas contraire, tous les dossiers de tous les comptes seront repris dans cette liste ;
* Vous pouvez vous déplacer dans cette liste en pressant la première lettre du nom d'un dossier ;
* Notez que  les dossiers qui ne sont pas affichés dans l'arborescence ne seront pas repris ici non plus. Cela se produit par exemple lorsque des dossiers appartiennent à un compte réduit dans l'arborescence des comptes et dossiers ;
* Si vous avez trouvé  le dossier qui vous intéresse à ce stade,  pressez Entrée dessus pour le sélectionner dans l'arborescence.  Vous pouvez aussi presser Alt+g pour simuler un simple clic-gauche sur le dossier ou Alt+d pour simuler un simple clic-droit ;


Basculer les modes d'affichage :

* Pour vous rappeler à tout moment dans quel mode d'affichage vous vous trouvez, pressez la touche "Retour arrière"   (backspace). Après avoir entendu l'information, pressez à nouveau cette touche pour revenir à la liste des dossiers ;
* Pour basculer l'affichage du mode "seulement avec dossiers non lus" au mode "tous les dossiers" et vice-versa, pressez F12 ;
* Dans le mode "tous les dossiers", les comptes sont affichés dans la liste de gauche et les dossiers du compte sélectionné dans celle de droite. Pour passer d'une liste à l'autre, utilisez  les flèches gauche et droite ;
* un compte virtuel nommé "Tous les comptes" est sélectionné et le focus est placé dans la liste des dossiers qui reprend tous les dossiers de tous les comptes. A chaque dossier dans cette liste, le nom du compte auquel il appartient est mentionné ; 


Utilisation du filtrage par mot-clé :

* Au préalable, vous aurez fort probablement avantage à passer en mode "Tous les dossiers" comme expliqué ci-dessus ;
* Ci-dessous, vous pouvez utiliser indifféremment les touches "Page précédente" et "Page suivante" ; 
* Depuis une liste, pressez la touche "Page précédente" pour remonter au champ d'édition de l'expression de filtrage ;
* Entrez une expression et validez-la ensuite avec la touche "Page Suivante"  pour exécuter le filtrage;
* Les résultats sont affichés dans la liste des dossiers. Si aucun dossier n'a été trouvé, vous entendrez : Aucun résultat. Si vous vous ne vous y attendiez pas, vous avez peut-être oublié de basculer dans le mode d'affichage de tous les dossiers ; 
-Enfin, pressez  entrée sur le dossier désiré pour le sélectionner dans l'arborescence des dossiers. Comme signalé plus haut, vous pouvez simuler un clic-gauche ou droit sur le dossier en pressant Alt+g ou Alt+d ;


#### Exclusion de certains dossiers de la liste des dossiers avec non lus 

Comme évoqué ci-dessus, vous pouvez  exclure des dossiers rarement ou jamais consultés de la liste des dossiers avec des messages non lus.

Il suffit pour cela de renommer un dossier à exclure en ajoutant  un tiret à la fin de son nom.

Il est nécessaire de signaler ici que si ce dossier renommé faisait partie d'un filtre de messages, Thunderbird modifiera automatiquement ce filtre pour tenir compte de ce changement


<a name="foldersList">

### Liste des dossiers de l'arborescence principale, selon 4 types (F7, NVDA+F7 ou Maj+F12) 

Lorsque vous vous trouvez dans l'arborescence des dossiers ou la liste  des messages, cette commande affiche un dialogue avec une liste des dossiers qui peut adopter les quatre présentations   suivantes : 

* Avec messages non-lus seulement (liste plate), Alt+n ;
* Tous les dossiers (liste plate), Alt+t ;
* Avec messages non-lus seulement (arborescence complète), Alt+o ;
* Tous les dossiers (arborescence complète), Alt+u ;


Pour les dossiers avec des messages non lus, les dossiers Brouillons, Corbeille et ceux dont le nom se termine par un tiret sont exclus de la liste ;

Pour activer un de ces types, vous pouvez presser le raccourci-clavier associé ou Maj+Tab puis les touches fléchées pour changer de mode.

Le type choisi sera mémorisé   et activé lors du prochain affichage de ce dialogue ;

Vous pouvez également filtrer la liste par mot-clé. Pressez Tab ou Alt+e vide pour atteindre la zone de saisie.

La navigation dans une  liste plate ou une arborescence  s'effectue avec les flèches haut et bas ainsi que par l'initiale d'un nom de dossier;

Pour activer dans l'arborescence principale le dossier sélectionné, pressez simplement Entrée dessus.

Astuce :   si vous avez pressé Entrée sur un dossier avec des messages non lus, pressez ensuite Espace pour sélectionner le premier message non lu dans le tableau des messages ;
<br>
Remarque :

Les raccourci-clavier qui permettent d'afficher ce dialogue peuvent être supprimés et un autre peut être ajouté  via  le dialogue de configuration des gestes de commande de NVDA. Procédez comme suit :

* Placez d'abord la fenêtre de Thunderbird au premier plan ;
* Ouvrez le menu NVDA et  sélectionnez "Préférences" ;
* Dans le sous-menu, validez sur : Gestes de commande" ;
* Dans le dialogue, pressez la lettre t jusqu'à entendre : Thunderbird ;
* Pressez la flèche droite pour développer cette branche ;
* Descendez sur l'élément : "Afficher la liste des dossiers de l'arborescence principale de Thunderbird, selon plusieurs types. réduit 2 sur 4 niveau 1" puis pressez flèche droite pour développer ce niveau ;
* Tabulez jusqu'au bouton "Ajouter", validez puis pressez un geste de commande dans le nouveau dialogue ;
* Pressez Entrée pour valider votre choix ;
* De retour dans la liste des commandes, vérifiez la présence de votre nouveau geste de commande ;
* Fermez  le dialogue via le bouton OK.

<a name="alerts">

## Les alertes accessibilisées 

Pour les alertes qui requièrent votre intervention,   les boutons sont accessibles et la navigation entre eux  peut s'effectuer avec les touches fléchées :

* installation de modules pour Thunderbird : le bouton "Installer"  est sélectionné et il suffit de presser Entrée dessus pour poursuivre l'installation ;
* Nouvelle mise à jour de Thunderbird : cette alerte est également accessibilisée ;
* Demande d'un accusé de réception du message : celle-ci peut être ignorée via une option du menu [Maj+Puissance2](keyEquiv_fr.html#aboveTab) / options pour la fenêtre principale ;;
* Blocage  de l’affichage des contenus distants dans les messages : le bouton "Options" est sélectionné  et la phrase suivante est ajoutée au message : Conseil : Ouvrez le menu Affichage, descendez sur Corps du message et validez HTML simple dans le sous-menu. En appliquant les réglages proposés,  cette alerte ne s'affichera plus ;

Pour les alertes gênant   le parcours de la liste de messages :

* Alerte Ceci est un brouillon : cette alerte inutile     est supprimée ;
* Thunderbird pense que ce message est frauduleux : cette annonce  est remplacée par deux tonalités brèves d'une fréquence proche de la voix humaine (200 Hertz). Pour rendre le message acceptable ou indésirable, pressez la touche [Puissance2](keyEquiv_fr.html#aboveTab) et sélectionnez l'action désirée dans le sous-menu "Alerte" ;

<a name="tabs">

## Raccourcis clavier des onglets 

Outre de nouvelles commandes, les onglets sont annoncés comme dans cet exemple : Onglet 1 sur 4, Courrier entrant.

* Contrôle+Tab et Contrôle+Maj+Tab : va à l'onglet suivant ou précédent ;
* Contrôle+un chiffre : sélectionne  l'onglet correspondant à son  numéro d'ordre dans la barre d'onglets.  Si vous pressez un chiffre supérieur au nombre d'onglets ouverts, vous serez placé dans le dernier ;
* Contrôle + [Egal](keyEquiv_fr.html#bs1) : affiche la liste des onglets ouverts dans un menu. Pressez entrée sur un nom d'onglet pour vous placer dans celui-ci ; 
* Alt + [Egal](keyEquiv_fr.html#bs1) : affiche le menu contextuel de la barre des onglets. Il comporte notamment les commandes : Fermer l'onglet actif et Fermer mes autres onglets ;  
* Contrôle+w, Contrôle+retour arrière ou Contrôle+F4 : ferme l'onglet actif ; 
* Contrôle+j : ouvre l'onglet "Fichiers enregistrés" qui regroupe les pièces jointes et téléchargements enregistrées sur votre disque dur ;

<a name="tabAddons">

## Onglet des modules complémentaires

L'extension  facilite la recherche et l'installation de modules complémentaires pour Thunderbird.

* Dans l'onglet "Modules complémentaires, entrez un nom de module puis pressez Entrée ;
* L'extension attendra que l'onglet des résultats de recherche s'ouvre   puis tentera de sélectionner le premier module complémentaire trouvé ;
* plus concrètement, vous pouvez lire l'exemple de [l'installation du module Start With Inbox](#stwInstall) ;

<!-- Translators : fenêtre de rédaction = Write window -->
<a name="writeWnd">

## Fenêtre de rédaction 

A l'ouverture de la fenêtre de rédaction, rien de particulier ne se remarque bien que les raccourcis clavier suivants soient disponibles :

* Echappe : referme la fenêtre de rédaction ;
* Consultation des zones d'adressage : un appui sur Alt + un chiffre annonce l'entête, deux appuis  donne  le focus à la zone de saisie correspondante :<br>
Alt+1: Expéditeur :  une de vos adresses mail figurant   dans  la liste de vos adresses de messagerie ;<br>
Alt+2 : pour :<br>
Alt+3 : les noms des  pièce jointes. Deux appuis donne le focus à la liste des pièces jointes ;<br>
les autres chiffres donnent accès aux entêtes facultatifs comme : copie à, copie cachée à et répondre à ;
* [Puissance2](keyEquiv_fr.html#aboveTab) dans le texte du message : affiche le menu contextuel suivant : - Barre d'outils Courrier puis dans le sous menu : Envoyer, Orthographe, Joindre, Sécurité, Enregistrer.<br>
Mise en forme du texte puis dans le sous-menu : (Styles de) Paragraphe, Appliquer ou enlever une liste à puces, Appliquer ou enlever une liste numérotée, Polices, Retraits, insérer un lien, une image, une ancre, une ligne horizontale ou un tableau. 

<br>
Remarque : ce menu s'obtient en une ou deux frappes sur la touche [Puissance2](keyEquiv_fr.html#aboveTab) en fonction du réglage dans le menu des options pour la fenêtre de rédaction obtenu en pressant  une ou deux fois rapidement [Maj+Puissance2](keyEquiv_fr.html#aboveTab) ;

<a name="spellDlg">

### Dialogue de vérification orthographique : F7 

Des raccourcis-clavier qui limitent le déplacement des mains ont été ajoutés. Lorsque le focus est placé dans le champ d'édition du mot de remplacement, vous pouvez presser les raccourcis-clavier suivants :

* Entrée : Actionne le bouton "Remplacer" ;
* Maj+Entrée : Actionne le bouton "Tout remplacer" ;
* Contrôle+Entrée : Actionne le bouton "Ignorer" ;
* Maj+Contrôle+Entrée : Actionne le bouton "Tout ignorer" ;
* Alt+Entrée : actionne le bouton "Ajouter le mot au dictionnaire" ;


Pour bien retenir ces combinaisons de la touche Entrée,  Contrôle  se rapporte à  l'action "Ignorer" et la présence de Maj    indique "toutes les occurrences".


De plus, le raccourcis  Alt+flèche haut  épelle les mots :

* 1 appui épelle les mots à un débit normal ;
* 2 appuis épelle rapidement les mots ;
* 3 appuis copie le mot mal orthographié dans le presse-papiers en vue de l'analyser dans un autre champ d'édition ;

<a name="menus">

## Menus des options et commandes de ThunderbirdPlus 

<a name="optMenu">

### Menu des Options([Maj+Puissance2](keyEquiv_fr.html#aboveTab)) 
 

Options pour la fenêtre principale : 

* Regrouper les mentions 'RE' multiples en une seule :par exemple, Re: Re: Re: sera transformé en 3Re: ;
* Supprimer les mentions 'RE' dans la colonne sujet s : 
* Supprimer les 2 points dans les mentions 'RE' : 
* Nettoyer les noms des correspondants dans la liste de messages : supprime les chiffres et certains caractères spéciaux afin de rendre l'écoute des noms des correspondants moins fatigante ;
* Ajouter une ponctuation entre les colonnes : une virgule est ajoutée entre certaines colonnes afin de marquer une petite pause entre elles  lors de l'annonce d'une ligne de la liste de messages ;
* Masquer les noms de listes de diffusion : supprime l'annonce des noms de listes entre crochets ou accolades pour une écoute plus agréable lorsque vous utilisez un dossier différent pour chaque liste de diffusion. Sinon, le nom d'une liste de diffusion n'est énoncé qu'une seule fois s'il apparaît plusieurs fois dans l'objet d'un message ; 
* Editer les mots à masquer dans l'objet de messages : ouvre une boîte de saisie qui permet d'ajouter ou supprimer des mots à ne pas annoncer dans les objets des messages. Par exemple, ajoutez * pour que *** Spam *** soit annoncé comme Spam ;
* Annoncer 'indésirable' si affiché dans la colonne 'Statut indésirable' : si la colonne "statut indésirable" est présente dans le tableau des messages, cette option permet ou non d'annoncer "Indésirable"  ; 
* Espace sur un dossier avec non lus  cherche le premier message non lu depuis le début de la liste de messages : Par défaut, le script relatif à cette option envoie la commande "n" pour sélectionner le prochain message non lu dans la liste de messages. Thunderbird ne sélectionne pas forcément le premier message non lu de la liste. En cochant cette option, l'extension sélectionnera le premier message non lu du dossier en faisant un détour qui peut s'entendre sur certains PC ;
* Ne pas utiliser la navigation par initiale dans l'arborescence des dossiers : cette option est utile  si vous utilisez le module complémentaire "Quick folder key navigation" ;
* Navigation par initiales indirecte : permet d'afficher une boîte de saisie de nom de dossier  dès que vous pressez une lettre ou un chiffre dans l'arborescence des dossiers. Si cette option est désactivée, vous pouvez afficher cette zone de recherche en pressant la lettre z ; 
* Ignorer les demandes d'accusé de réception : si cette option est activée, le volet de demande d'accusé  de réception sera  passé sous silence  lorsqu'un message sera  sélectionné dans la liste de messages ;   
* Ne pas émuler Maj+F6 avec échappe :désactive l'utilisation de la touche échappe lors de la navigation entre les panneaux de la fenêtre principale ; 
* Afficher seulement les dossiers avec non lus dans la boite de dialogue 'Dossiers de l'arborescence' a :permet de n'afficher que les dossiers avec  des messages non lus chaque fois que vous affichez ce dialogue via la touche F12 ;
* fenêtre séparée de lecture : ne pas lire automatiquement le  message si provoque des blocages de NVDA : Par défaut, lorsqu'on ouvre un message en pressant Entrée depuis la liste de messages, une lecture épurée du message se lance à l'ouverture de la nouvelle fenêtre. Sur certains ordinateur et lorsque le compte de messagerie est configuré en IMAP, NVDA peut se bloquer. Lorsque cette option est cochée, cette lecture automatique est désactivée pour éviter tout blocage.<br>
Si vous constatez effectivement un blocage   à l'ouverture de cette fenêtre, vous pouvez allonger le délai avant que la lecture automatique ne commence. Pour cela, pressez Alt+d pour saisir une autre valeur. Si vous ne parvenez pas à supprimer ce blocage, cochez alors cette option ; 

<br>
Options pour la fenêtre de rédaction : 

* Vérification orthographique : épeler le mot mal orthographié et le mot suggéré : cette option modifie les annonces dans le dialogue de vérification orthographique ;
* Activer l'amélioration de la Vérification orthographique pendant la saisie:  la commande relative à cette option ne fonctionne pas encore dans la version 2022.1 de NVDA ;
* La touche Échap ferme le message en cours de rédaction ; coché l
* Simple frappe pour  afficher  les menu contextuel, double frappe pour écrire [Puissance2](keyEquiv_fr.html#aboveTab) ou [Maj+Puissance2](keyEquiv_fr.html#aboveTab) ou leurs remplaçants : cette option permet d'afficher le menu contextuel  en frappant la touche  [Puissance2](keyEquiv_fr.html#aboveTab), ce qui sera plus pratique si vous écrivez très rarement les caractères [Puissance2](keyEquiv_fr.html#aboveTab) et [Maj+Puissance2](keyEquiv_fr.html#aboveTab) ;

<br>
Options de mise à jour :

Cette option permet de désactiver les mises à jour automatiques de Thunderbird+ ou de les réactiver ;

<br>
Désactivations   pour Chichi et Thunderbird+ :

Le but principal de ces options est de permettre une bonne cohabitation entre Thunderbird+ et Chichi en évitant les fonctionnalités en double. Mais vous pouvez les utiliser sans Chichi pour répondre à vos préférences ;

Le terme "dossiers" ci-dessous désigne l'arborescence des dossiers ;

* Dossiers : Espace ne sélectionne pas le prochain message non lu dans la liste et n'affiche pas la liste de dossiers non lus d : Chichi ne dispose pas encore d'équivalent en fonctionnement autonome  ;
* Dossiers : pas de navigation par initiales d : en activant cette option, Chichi sera utilisée.  Il  ne fonctionne que de haut en bas et n'énonce pas le nom du compte auquel appartient le dossier activé ; 
* Liste messages : Espace ne lit pas le message du volet d'aperçu l : si vous cochez cette option,  ce sera Chichi qui énoncera  le message du volet d'aperçu. Contrairement à Thunderbird+, cette lecture ne sera pas épurée. En revanche, F4 et Alt+flèche bas continueront à faire appel à la lecture épurée de Thunderbird+ ; 
* Liste messages : pas de SmartReply : désactive la fonctionnalité qui permet de répondre à une liste de diffusion avec Contrôle+r en simple frappe ou à l'expéditeur  avec Contrôle+r en double frappe ,
* Liste messages : ne pas gérer la barre de filtrage rapide : supprime l'accès aux options de filtrage avec la flèche bas ;
* fenêtre principale : Tab ne passe pas au volet suivant : cette option concerne la navigation entre l'arborescence des dossiers, la liste des messages et le volet des entêtes et du message ;
* Fenêtre principale : rétablir le comportement par défaut de la touche échappe. Ceci concerne notamment la navigation entre les volets cités ci-dessus ;
* Permettre    la fermeture de Thunderbird avec Contrôle+w ou Contrôle+F4 :  en cochant cette option, ces deux raccourcis ferment Thunderbird lorsqu'il ne reste plus qu'un seul onglet d'ouvert. Ce comportement   est gênant pour certaines personnes ;

<br>
Sauvegarde et restauration des options :

* Sauvegarder la configuration actuelle s : copie le fichier .ini  de l'extension dans un fichier .inibak ;
* Restaurer la configuration sauvegardée r : copie le fichier .inibak  sur le fichier .INI et recharge les paramètres ;
* Réinitialiser la configuration r : recharge les paramètres par défaut de l'extension. Au préalable, effectue  une sauvegarde s'il n'en existe pas encore ;

<a name="cmdMenu">

### Menu  des Commandes (Puissance2) 

* Choisir et agencer  les colonnes de la liste de messages : Affiche  le menu  de cases à cocher de Thunderbird nommé "Choisir les colonnes à afficher". A partir d'un nom de colonne, pressez la flèche droite pour ouvrir  le dialogue d'agencement des colonnes ;
* Ecrire au support :  en Français ou en Anglais. Cette commande ouvre une fenêtre de rédaction pré-adressée  au support de l'extension. Ceci ne fonctionne que si Thunderbird est correctement défini comme votre client de messagerie par défaut ;

<a name="startup">

## Amélioration du démarrage de Thunderbird

Nativement, après la dernière fermeture de Thunderbird, celui-ci démarre sur le dernier onglet actif et sans rien activer, ce qui est plutôt désagréable.

Pour obtenir un démarrage confortable, Il existe deux modules complémentaires qui s'installent directement sur Thunderbird :

* Chichi développé par Yannick : ce module est recommandé parce qu'il offre beaucoup d'autres  fonctionnalités d'accessibilité et que ThunderbirdPlus est conçu pour interagir avec lui ;
* Start with inbox : si vous n'utilisez pas Chichi, ce module fait du bon travail ; 

<a name="chichi">

### Avec Chichi 

Pour utiliser Chichi, lisez  la section Téléchargement et installation et la section Définir le dossier de démarrage de la [page de Chichi](https://www.rptools.org//Outils-DV/thunderbird-chichi.html) ;

<a name="stwi">

### Avec Start with inbox 

En octobre 2022,  La dernière version  de ce module pour Thunderbird 102 était la 2.5.2.

Caractéristiques :

* Installation : via une recherche sur son nom dans l'onglet Modules complémentaires" de Thunderbird ; 
* Dossier de démarrage : toujours le même, le dossier courrier entrant du compte choisi dans les réglages du module ou le dossier unifié ;
* Auto-focus : sur le dernier message de la liste de messages ou sur le dossier "Courrier entrant" de l'arborescence, selon le réglage dans les options du module. Cette seconde option est sélectionnée par défaut ; 
* Réglages : accès moins aisé. Il faut se rendre dans l'onglet Modules complémentaires, sélectionner "Start with inbox" dans la liste des extensions installées puis  presser entrée sur le bouton   "Options des modules", ce qui ouvre une nouvel on glet "Settings Start with inbox" ,
<br>Une liste déroulante permet de choisir le compte de messagerie pour lequel le dossier courrier entrant sera sélectionné  au démarrage de Thunderbird ,
<br>Trois boutons radio vous permettront de choisir le focus entre le dernier message ou le premier message non lu de la liste de messages ou le dossier dans l'arborescence ;

<a name="stwInstall">

Installation :

* dans Thunderbird, ouvrez le menu "Outils" puis validez sur : Modules complémentaires et thèmes ;
* Dans la page du Gestionnaire de modules,, placez-vous dans le champ de recherche. En mode navigation, vous pouvez presser la lettre e pour l'atteindre rapidement ;
* écrivez : Start with Inbox puis pressez Entrée ;
* Si vous disposez de Thunderbird+4, Attendez un instant qu'il sélectionne le module recherché dans l'onglet de résultats ;
* Sinon, sélectionnez manuellement l'onglet "Start with inbox :: Recherche :: Modules pour Thunderbird" par exemple.   pressez ensuite la touche 3 ou guillemet jusqu'à atteindre le titre de niveau 3 intitulé par le nom du module que vous avez recherché ; 
* Avec la flèche bas, Descendez  jusqu'au lien "Ajouter à Thunderbird" puis pressez Entrée dessus ;
* Suivez la procédure puis redémarrez Thunderbird ;
* Si tout s'est bien passé, Thunderbird s'ouvrira sur l'onglet principal et donnera le focus à la liste de messages ;

Régler les options de Start with Inbox :

* Retournez dans l'onglet "Gestionnaire de modules complémentaires" ;
* Le cas échéant, quittez le champ de recherche afin de vous placer en mode navigation ;
* Pressez autant de fois que nécessaire la touche 3 pour atteindre le titre de niveau 3 intitulé    "Start with Inbox dans la liste des modules installés ;
* Validez ensuite sur le bouton : Options des modules. Ceci ouvre un nouvel onglet intitulé : Start with Inbox, Settings ;
* Voici ce qui est affiché  par défaut :

<!-- Translators : pour l'anglais, mettez  la section "Interprétation en Français" en commentaire pour montrer aux autres traducteurs ce qu'ils devraient faire -->
En anglais :

Start with Inbox - Settings 

Please select the account, for which its inbox shall be displayed after start of Thunderbird. 

liste déroulante : \<votre premier compte de messagerie\>

Select and put the focus on:

bouton radio   cliquable non coché :the latest* message. 

bouton radio non coché cliquable the inbox folder in the folder tree. 
vide
bouton radio coché :the first unread message. 

* Definition of "latest": The last message that was put into the inbox (independent from the date 
of the message). 

If the inbox contains no messages, the inbox folder in the folder tree will be selected and 
focused.


Interprétation en français : 

Start with Inbox - Réglages  ;

Sélectionnez le compte dont  le dossier Courrier entrant  sera affiché au démarrage de Thunderbird ; 

liste déroulante : \<votre premier compte de messagerie\>

Sélectionner puis placer le focus sur :

bouton radio   cliquable non coché :Le dernier message de la liste ;

bouton radio non coché cliquable Le dossier Courrier entrant dans l'arborescence des dossiers ;

bouton radio coché :Le premier message non lu de la liste ;

Si le dossier Courrier entrant ne contient aucun message, ce dossier recevra le focus dans l'arborescence des dossiers ; 


Après avoir effectué vos réglages, redémarrez Thunderbird.


Lanceur intégré de Thunderbird avec AltGr+[Puissance2](keyEquiv_fr.html#aboveTab) :

Pour plus de commodité et de rapidité, vous pouvez lancer Thunderbird en pressant AltGr+[Puissance2](keyEquiv_fr.html#aboveTab). 

Ce raccourci est configurable via le gestionnaire de gestes de commandes de NVDA qui offre une plus grande liberté de choix de   touches de modification que les raccourcis de Windows, limités à AltGr ;

Procédez comme suit pour  ajouter un autre geste de commande :

* Placez  d'abord la fenêtre de Thunderbird au premier plan ;
* Ouvrez le menu NVDA et  sélectionnez "Préférences" ;
* Dans le sous-menu, pressez Entrée sur : Gestes de commande" ;
* Dans le dialogue, pressez la lettre t jusqu'à entendre : "Thunderbird, Lanceur" ;
* Pressez la flèche droite pour développer cette branche ;
* Descendez sur l'élément : "Lance Thunderbird" puis pressez flèche droite pour développer ce niveau ;
* Tabulez jusqu'au bouton "Ajouter", validez puis pressez un geste de commande dans le nouveau dialogue ;
* Pressez Entrée pour valider votre choix ;
* De retour dans la liste des commandes, vérifiez la présence de votre nouveau geste de commande ;
* Fermez  le dialogue via le bouton OK.

Remarques :

* Le lanceur de Thunderbird n'est prévu que pour la version installée de Thunderbird dont les chemins de Thunderbird.exe sont prévisible. 
* Dans une configuration Windows 64 bits,  l'extension ne lancera pas la version 32 bits de Thunderbird  si les deux versions, 64 et 32 bits, sont toutes deux installées sur votre système ; 


<!-- links section -->


[1]: https://github.com/RPTools-org/ThunderbirdPlus/releases/download/v4.7/thunderbirdPlus-4.7-TB102.nvda-addon

[2]: https://github.com/RPTools-org/ThunderbirdPlus/

[3]: https://addons.nvda-project.org/files/get.php?file=tbp
