// Escreva um algoritmo que solicite ao usauraio um numerio inteiro positivo e apresente ao final a somatoria de todos inteiros positivos a´te o num informado.

#include <stdio.h>
#include <conio.h>

float SomaAtencessoresNormal(int x){
	int soma=0;
	for (int i=1;i<=x;i++){
		soma = soma + i;
	}
	return (soma);
}
float SomaAtencessoresRecursiva(int x){
	int soma;
	if (x==1)
	// condição de parada
	return(1);

	//chamada recursiva
	soma= x + SomaAtencessoresRecursiva(x-1);
	return(soma);
};
int main(){
	float num1;
	
	printf("informe o num1: ");
	scanf("%f",&num1);
	//recebe a função soma
	
	printf("\n A soma: %.2f",SomaAtencessoresNormal(num1));
	printf("\n A soma Recursiva: %.2f",SomaAtencessoresRecursiva(num1));
	getch();
}
