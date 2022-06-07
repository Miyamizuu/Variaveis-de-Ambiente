import os

#Definidos na máquina, caso compartilhar a pessoa vai ter que crira a variável
usuario = os.environ['usuario']
senha = os.environ['senha']

print(usuario, senha)