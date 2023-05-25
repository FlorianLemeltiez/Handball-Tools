

// Header Files
# include <stdio.h>
# include <string.h>

int main (void)
{
    printf ("test \n");

    char valeur [40];
    int compteur = 0;

    int nbr_but;
    int nbr_tir;
    int nbr_arret;
    int victoire = 1;
    int defaite = 0;

    char equipe_A [20];
    char equipe_B [20];

    long joueur [12];
    long officiel [30];

    printf("Veuillez inscrire le nom de l'equipe A : ");
    scanf("%19s", equipe_A);

    printf("%19s \n", equipe_A);

    printf("Veuillez inscrire le nom de l'equipe B : ");
    scanf("%19s", equipe_B);
    printf("%19s \n", equipe_B);


    printf("Veuillez saisir la liste de vos joueurs : \n" "Si vous n'avez plus de joueurs a inserer, tapez 0\n");

    do {
        scanf("%s", valeur);
        printf("Le nom du joueur est %s \n", valeur);
        compteur++;
    } while((compteur < 3) || (strcmp(valeur, "0") != 0));

    return 0;
}