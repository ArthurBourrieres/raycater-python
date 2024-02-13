# raycater-python

Objectif: Créér un raycaster de basse fonctionnelle. Un raycaster est un techenique permettant de creer 
un semblent d'environnemment 3D avec un environement en 2D. Pour cela on lence des rayons depuis une camera,
quand le rayon rentre en colition avec une surface on calcule la distance parcourue par le rayon. cela nous permet de
connaitre la distance entre la surface et la camera. en fonction de cette distance on vas tracer sur notre rendue une collon
inversement proportionnelle a la distance. L'image sera d'autan plus nette que l'on tracera de rayon.

Projet fait entierment en python.
L'objectif était de tester le fonctonnement et la logique d'un raycaster
L'algorythme de raycaster a etait entierment fait avec mes connaisence de basse sur les raycasters.
plusieur probleme en l'etat:
-le lancer de rayon est fait pas apres pas, ce qui n'est pas performent et créé des inprecision dans les distance.
-effet vu de poisson, donne l'impression de regarder avec le yeux d'un poisson (centre de l'image bien plus grand que sur les coté

projet considéré comme fini  
