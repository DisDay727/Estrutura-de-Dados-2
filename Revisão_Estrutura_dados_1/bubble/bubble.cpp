#include <stdio.h>
#include <cstdlib>   // rand(), srand()
#include <ctime>     // time()
int titan[40];

int main(){
	// 1. Define a "semente" (seed) usando o relógio da máquina
    // Se você não fizer isso, o rand() vai gerar sempre os mesmos números
    srand(time(0));
	int qtd = 40
	, aux,min,troca=0;
	
	//aqui preencher
	for (int i=0;i<qtd;i++){
		// 2. Gera um número aleatório. 
    	// O uso de "% 100 + 1" limita o número entre 1 e 100.
		int random = (rand() % qtd) + 1;
		titan[i]=random;
		printf("\n primeiros titan [%i] ",titan[i]);
	}
	//bubble
	for (int i=0;i<qtd-1;i++){ // o menos um de qtd é para não.
		for (int j=0;j<qtd-i-1;j++){// o menos um de atd é pra não verifica a mesma casa
			if (titan[j]>titan[j+1]){// se a posição for maior que a segunda ele troca de lugar
				aux=titan[j];//primeira posição a segura o valor
				titan[j]=titan[j+1];// vai troca de lugar com o segundo o proximo
				titan[j+1]=aux;// vai troca o segundo lugar pero primeiro
				troca++;
			}
		}
	};
	//imprime o bubble
	printf("\n __Bubble__");
	for (int i=0;i<qtd;i++){
		printf("\n primeiros titan [%i] ",titan[i]);
	};
		printf("\n __trocas [%i] __",troca);
}
