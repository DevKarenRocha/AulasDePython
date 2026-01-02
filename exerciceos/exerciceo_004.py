# DESAFIO 004
# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo  primitivo  
# e as informações possiveis sobre ele 

teste = input('Digite algo:')
print ('O tipo do dado é:', type(teste))
print ('Ele é numero:', teste.isnumeric()) 
print ('Ele é alfabetico:', teste.isalpha())
print ('Ele é alfanumerico:', teste.isalnum())

#------------------------------------------------------------------------------------
#RESPOSTA
 
a = input('digite algo:')
print ('O tipo primitivo desse valor é:', type(a))
print('Só tem espaço?' , a.isspace())
print('É um número?' , a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É Alfanumerico?' , a.isalnum())
print('Esta em maiusculo?', a.isupper())
print('Esta em minuscula?' , a.islower())
print('Esta capitalizada?', a.istitle())

# a = objeto 
# todo objeto tem caractyeristicas e realiza funcionalidades

