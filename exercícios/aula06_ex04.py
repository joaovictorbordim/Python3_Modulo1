#Crie um programa que leia pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

n = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(n))
print('Só tem espaço? ', n.isspace())
print('É número? ' ,n.isnumeric())
print('É alfabeto? ', n.isalpha())
print('Está em maiúscula? ', n.isupper())
print('Está em minúscula? ', n.islower())
