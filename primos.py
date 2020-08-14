#!/usr/bin/env python3

''' Programa que gera a lista de números primos
    Autor: Marcos Couto
    Data: 14/08/2020
    email: marcos.datadriven@gmail.com'''


def resultado():                 # função que gera a lista números primos
    # variáveis iniciais
    numerador = 50               # intervalo de pesquisa 0 a 50.
    dividendo = numerador - 1
    for y in range(1, numerador):
        for x in range(1, numerador):
            resultado = numerador % dividendo

            if resultado == 0:
                if dividendo == 1:
                    print(numerador)
                    numerador -= 1
                    dividendo = numerador - 1

                else:
                    numerador -= 1
                    dividendo = numerador - 1

            if resultado != 0:
                dividendo -= 1


resultado()
