from utils import escreva, leaving_the_game

nome = ""
pontos = 0
vidas = 5

#salve
def save_game():
    with open("save.txt", "w") as arquivo:
        arquivo.write(f"{nome},{pontos},{vidas}")
#carrega o jogo
def load_game():
    global nome, pontos, vidas
    try:
        with open("save.txt", "r") as arquivo:
            nome, pontos, vidas = arquivo.read().split(",")
            pontos = int(pontos)
            vidas = int(vidas)
        print("📂 Jogo carregado!")
    except FileNotFoundError:
        print("⚠️ Nenhum jogo salvo encontrado.")

#salva atraves da maior pontuação
def save_ranking():
    with open("ranking.txt", "a") as arquivo:
        arquivo.write(f"{nome},{pontos}\n")
#carrega o rank
def load_ranking():
    ranking = []
    try:
        with open("ranking.txt", "r") as arquivo:
            for line in arquivo:
                player, score = line.strip().split(",")
                ranking.append((player, int(score)))
    except FileNotFoundError:
        pass
    return ranking
#organiza o rank por meio dos valores
def organize_ranking():
    ranking = load_ranking()
    ranking.sort(key=lambda x: x[1], reverse=True)

    with open("ranking.txt", "w") as arquivo:
        for player, score in ranking:
            arquivo.write(f"{player},{score}\n")
#mostra o rank
def show_ranking():
    ranking = load_ranking()

    if not ranking:
        print("⚠️ Nenhum ranking encontrado.")
        return

    print("\n🏆 RANKING 🏆")
    for posicao, (player, score) in enumerate(ranking, start=1):
        print(f"{posicao}. {player} — {score} pontos")
        if posicao == 10:
            break
        
def jogar(questions, pontos_por_questao):
    vidas = 3
    pontos = 0

    for q in questions:
        escreva(q["question"])
        for i, option in enumerate(q["options"]):
            escreva(f"{chr(97+i)}) {option}")

        resposta = input("Answer: ").lower()

        if resposta == q["answer"]:
            escreva("✅ Correct!\n")
            pontos += pontos_por_questao
        else:
            vidas -= 1
            escreva("❌ Incorrect!")
            escreva(f"Lives left: {vidas}\n")

        if vidas == 0:
            escreva("💀 GAME OVER!")
            return

    escreva(f"🎉 You finished the level with {pontos} points!")


#cabo 

def game_over():
    escreva(f"\n❌ GAME OVER, {nome}! Try again!")
    save_ranking()
    organize_ranking()
    show_ranking()
    leaving_the_game()
