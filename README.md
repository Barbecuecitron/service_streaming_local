# WebApp en cours de construction

Un bien modeste utilitaire de lecture vidéo crée avec flask, permettant de lire depuis n'importe quel appareil connecté au routeur, (smartphone, tablette, pc portable) le fichier vidéo de votre choix, présent dans un dossier ciblé de votre machine.

```"C:/Users/MyUser/Videos"``` ou ```"C:/Users/MyUser/Films"```

Le tout tourne sur un petit serveur Flask local, dont le transfert est rendu possible grâce à l'ouverture d'un port TCP permettant à notre "serveur" (l'ordinateur contenant les vidéos) d'accepter requêtes sur le dit port, par l'intermediaire de l'ip machine principale (un pc dans lequel se trouve vos vidéos par exemple, ou un serveur local tournant sur Raspberry). 

Compte-tenu de sa nature, il est un modeste challenge technique plus qu'une idée révolutionnaire de la startup nation,
je vous déconseille à ce titre de l'utiliser dans un contexte non sécurisé, (lieux publics par exemple).

Il peut en revanche s'avérer utile, si vous souhaitez terminer le Seigneur Des Anneaux version longue depuis le confort de votre lit, ou sur vos toilettes directement depuis votre smartphone.

S'il n'est pour l'instant pas terminé, il est totalement fonctionnel et s'accompagnera d'un tutoriel rendant sa configuration & son utilisation simples & efficaces.