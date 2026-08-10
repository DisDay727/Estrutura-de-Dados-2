#include <stdio.h>
#include <cstdlib>   // rand(), srand()
#include <ctime>     // time()

// Função de troca com a variável 'contador' passada por referência (&)
void troca(int* A, int* B, int& contador) {
	int t = *A;
	*A = *B;
	*B = t;
	contador++; // Conta a troca
}

// Função de partição passando o contador adiante
int particao(int titan[], int baixo, int alto, int& contador) {
	int pivo = titan[alto];
	int i = (baixo - 1);
	for (int j = baixo; j <= alto - 1; j++) {
		if (titan[j] <= pivo) {
			i++;
			troca(&titan[i], &titan[j], contador);
		}
	}
	troca(&titan[i + 1], &titan[alto], contador);
	return (i + 1);
}

// Quick Sort recebendo e repassando o contador
void quicksort(int titan[], int baixo, int alto, int& contador) {
	if (baixo < alto) {
		int p_indice = particao(titan, baixo, alto, contador);
		quicksort(titan, baixo, p_indice - 1, contador);
		quicksort(titan, p_indice + 1, alto, contador);
	}
}

int main() {
	int titan[40];
	int qtd = 40;
	
	// Define a "semente" (seed) usando o relógio da máquina
	// Se você não fizer isso, o rand() vai gerar sempre os mesmos números
	srand(time(0));
	
	// Inicializamos a nossa variável contadora em ZERO
	int total_trocas = 0;
	
	printf("\n__ Vetor Original __");
	// Preenchendo o vetor
	for (int i = 0; i < qtd; i++) {
		// Gera um número aleatório. 
		// O uso de "% 40 + 1" limita o número entre 1 e 40.
		int random = (rand() % 40) + 1;
		titan[i] = random;
		printf("\n titan [%i] = %i", i, titan[i]);
	}

	// Quick sort sendo chamado e recebendo o contador de trocas
	quicksort(titan, 0, qtd - 1, total_trocas);
	
	// Imprime o quick sort
	printf("\n\n__ quick sort __");
	for (int i = 0; i < qtd; i++) {
		printf("\n titan [%i] = %i", i, titan[i]);
	}
	
	// Imprime a variável contadora correta
	printf("\n\n__ trocas [%i] __\n", total_trocas);
	
	return 0;
}
