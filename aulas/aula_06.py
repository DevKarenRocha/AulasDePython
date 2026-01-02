#TIPOS PRIMITIVOS
#  teoria

n1 = int(input ('Digite um numero:'))
n2 = int(input ('Digite mais um numero:'))
s = n1 + n2
print('O resultado da soma é:' ,s)

# int = numeros interior (7,-4,0,9875)
# float = numeros reais (4.5 , 0.076 ,7.0)
# bool =  boleanos (True , False)
# str = string ('olá', '7,5', '')

print('a soma vale' , s)
print('a soma vale {}'.format(s))

#--------------------------------------------------------------
#  prática

n3 = input('Digite um numero')
print(type(n3))

n4 = int( input('Digite um numero'))
print(type(n4))

#-------------------------------------------------------------
#DESAFIO 001

numero1 = int(input('Digite um numero:'))
numero2 = int(input('digite mais um numero:'))
soma = numero1 + numero2

print('A soma entre', numero1 ,'e', numero2 , 'é igual a', soma )
print('A soma entre {0} e {1} vale {2}'.format(numero1, numero2, soma))

#-------------------------------------------------------------
#DESAFIO 002

n = float(input('digite um valor:'))
print(n)
print(type (n))

n = int(input('digite um valor:'))
print(n)
print(type (n))

n = bool(input('digite um valor:'))
print(n)
print(type(n))

# Aparece true (verdadeiro) pois ele tenta identificar se 
# há ou não um valor dentro da variavel.se for digitado algum valor 
# ele responde como TRUE e se não for digitado nada FALSE

n = input('digite algo:')
print(n.isnumeric())
print(type(n))

# .isnumeric identifica se o valor pode ser convertido para numero
# Respondendo se é verdadeiro ou falso

n = input('Digite algo: ')
print(n.isalpha())

# .isalpha indentifica se é letra ou não 
# Se for apenas letras sem espaço ou outro caracter apresenta TRUE 
# se houver espaço, numero ou caracter sera apresentado FALSE

n = input('Digite algo: ')
print(n.isalnum())

# .isalnum indentifica se o caracter é alfanumerico ou seja letra e numero 
# se for ele apresenta TRUE se não for ele apresenta FALSE

n = input('Digite algo: ')
print(n.isupper())

# . isupper identifica se esta em letra maiuscula 
# apresenta TRUE apenas de todos as letras estiverem em maiuscula
# se tiver alguma letre em minuscula o resultado será FALSE

#-----------------------------------------------------------
#RESUMO DOS IS 

#  Verifica se todos os caracteres são numéricos (inclui números unicode).
#  "123".isnumeric()      True
#  "²".isnumeric()        True
#  "12.3".isnumeric()     False

#  Verifica se todos os caracteres são dígitos (menos abrangente que isnumeric).
#  "123".isdigit()        True
#  "²".isdigit()          True
#  "12.3".isdigit()       False

# Verifica se só há números decimais (0–9).
# ➡ Mais restrito que os dois acima.
#  "123".isdecimal()      True
#  "²".isdecimal()        False

#  Verifica se só há letras (sem espaços ou números).
# "Python".isalpha()     True
# "Python3".isalpha()    False

#  Verifica se há letras e/ou números, sem símbolos.
# "Python3".isalnum()    True
# "Python 3".isalnum()   False

# Verifica se todas as letras estão em minúsculas.
#"python".islower()     True
#"Python".islower()     False

# Verifica se todas as letras estão em maiúsculas.
# "PYTHON".isupper()    True
# "python".islower()     False
# "Python".islower()     False

# Verifica se o texto está em formato título (Primeira letra maiúscula).
# "Python Developer".istitle()  True

# Verifica se a string contém apenas espaços (ou tabs, quebras de linha).
# "   ".isspace()         True

# Verifica se todos os caracteres são ASCII.
# "Python".isascii()      True
# "ç".isascii()           False

# Verifica se todos os caracteres podem ser exibidos.
# "Hello\n".isprintable()   False

#---------------------------------------------------------------------------



