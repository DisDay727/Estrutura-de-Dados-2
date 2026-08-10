#include <iostream>
#include <cstdlib>   // rand(), srand()
#include <ctime>     // time()
int titan[40];

int main(){
	// 1. Define a "semente" (seed) usando o relógio da máquina
    // Se você não fizer isso, o rand() vai gerar sempre os mesmos números
    srand(time(0));
	int qtd = 40, aux,j,troca=0;
	
	//aqui preencher
	for (int i=0;i<qtd;i++){
		// 2. Gera um número aleatório. 
    	// O uso de "% 100 + 1" limita o número entre 1 e 100.
		int random = (rand() % qtd) + 1;
		titan[i]=random;
		printf("\n primeiros titan [%i] ",titan[i]);
	}

	//insertion sort
	for(int i=1;i<qtd;i++){// moon walke
		aux = titan[i]; // aux vai receber a segunda posição
		j = i-1; // vai receber a primeira posição
		while (j>=0&&titan[j]>aux){ // vai pergunta se j  e maior que zero e se o titan da posição 0 for maior que o titan da segunda posição
			titan[j+1]=titan[j]; // titan da segunda posição vai troca de luja com o ta primeira posição 
			j--;//vai reinicia o j vai para -1
			troca++;
		}
		titan[j+1]=aux;// a primeira posição  vai receber o valor do auxila que veio da segunda posição
		
	}
	//imprime o insertion 
	printf("\n __insertion __");
	for (int i=0;i<qtd;i++){
		printf("\n primeiros titan [%i] ",titan[i]);
	};
	printf("\n __trocas [%i] __",troca);
}
