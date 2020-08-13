#!/usr/bin/env python3
''' Programa que gera a série de Fibonacci
    Autor: Marcos Couto
    Data: 12/08/2020
    email: marcos.datadriven@gmail.com'''


def resultado():   # função que gera a série de Fibonacci
    antecessor = 0   # variáveis iniciais
    sucessor = 1
    # laço de repetição - cria até 50 elementos.
    for x in range(1, 50):
        # Escreve na saída padrão os elementos da série
        print(antecessor)
        soma = antecessor + sucessor
        antecessor = sucessor
        sucessor = soma


resultado()
