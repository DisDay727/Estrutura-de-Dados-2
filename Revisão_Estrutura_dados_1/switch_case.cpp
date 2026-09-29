#include <stdio.h>
int main(){
	//Dentro dessa area vai se adicionado todos os dados de uso
	int aux,z,x,y;
	int escolhar;
	char txt;
	printf("Escolhar qual atividade deseja visualizar \n");
	scanf("%i",&escolhar);
	
	//SWITCH CASE
	switch(escolhar){
		case 1:
			printf("informe o numero para se verificado entre par ou impar\n");
			scanf("%i",&aux);
			if (aux/2==0){
				printf("O numero informado foi %i ele é um numero par",aux);
			}else{
				printf("O numero informado foi %i ele é um numero impar",aux);
			}
			break;
		case 2:
			printf("informe o numero inteiro e iremos verifica se esta entre 100 a 200 \n");
			scanf("%i",&aux);
			if (aux>100 && aux<200){
				printf("\n o Numero informado %i esta entre 100 a 200",aux);
			}else{
				printf("\n o Numero informado %i  nao esta entre 100 a 200",aux);
			};
			break;
		case 3:
			printf("\n Essa atividade nao foi realizada");
			break;
		case 4:
			printf("Voce passara 3 notas para o calculo de media e vera se esta aprovado ou não\n");
			scanf("%i",&z);
			scanf("%i",&x);
			scanf("%i",&y);
			if(aux+z+x+y/3>6){
				printf("Vc foi aprovado com a media %i",aux+z+x+y/3);
			}else{
				printf("Vc nao foi aprovado e sua media %i",aux+z+x+y/3);
			};
			break;
		case 5:
			printf("Escolha o numero de 1 a 3 \n");
			scanf("%i",&aux);
			// aqui dentro vc usar dois switch de maneira bem maluca
			switch(aux){
				case 1:
					printf("\n regiao sul");
					break;
				case 2:
					printf("\n regiao Norte");
					break;
				case 3:
					printf("\n regiao centro-oeste");
					break;
				default:
					break;
			}
			break;
		case 6:
			printf("Digite o a sigla de regiao como S para sul N para norte...");
			scanf("\n %c",&txt);
			switch(txt){
				case 's':
					printf("\n regiao sul");
					break;
				case 'n':
					printf("\n regiao Norte");
					break;
				case 'c':
					printf("\n regiao centro-oeste");
					break;
				default:
					break;
			};
			break;
		default:
			printf("\n Digitou errado amigo");
			break;
	}
return 0;
}
