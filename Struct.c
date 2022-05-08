#include <stdio.h>
#include <string.h>

struct banda
{
  char nome[20];
  char estilo[20];
  int integrantes[20];
};
typedef struct banda Banda;

struct tocadas
{
  char nometoc[20];
};
typedef struct tocadas Tocadas;

int main(void)
{
  for (int n1 = 0; n1 <= 4; n1++)
  {

    Banda bandas[5];
    printf("Qual o nome da banda%d ?\n", n1);
    scanf("%s", bandas[n1].nome);

    return 0;
  }