#o tempo do efeito da escrita a pagina de carregamento

import time

def escreva(texto, velocidade=0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidade)
    print()

def loading():
    escreva("Loading...")
    time.sleep(1)

def starting_the_game():
    escreva("Starting the game...")
    time.sleep(1)
    
def leaving_the_game():
    escreva("Leaving the game...")
    time.sleep(1)