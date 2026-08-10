
// trazer pra cá a função de troca///
void troca(int *valor1,int *valor2){
	int aux;
	aux = *valor1; // um ponteiro é um tipo de dado que receber o endereço de memoria de outro.
	*valor1=*valor2;
	*valor2=aux;
}

int main(){
	int num1, num2;
	//O printf permite que seja impreso no console
	printf ("informe num1: ");
	scanf("%i", &num1); // o scanf vai permiti a coleta de dados preenchido pelo usuario.
	printf("informe num2: ");
	scanf("%i", &num2);// a informação %i, &num2 é para atribuir o valor a variavel. ou array ou veto
	//colocar aqui o codigo para trocar os valores de posição..
	//função
	troca(&num1, &num2);//o & e para converte o int para float
	printf("\n valor de num1: %d ",num1);//O \n é para quebra linha, e o %d para atribui a variavel ou array do num 1
	printf("\n valor de num2: %d ",num2);
}
