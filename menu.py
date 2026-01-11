#menu do jogo
from utils import escreva

def show_menu():
    nome = input("Enter your name: ")
    escreva(f"Hello, {nome}! Welcome to the chemistry test!")
    escreva("1. Start game")
    escreva("2. Load game")
    escreva("3. Ranking")
    escreva("4. About the game")
    escreva("5. Exit")