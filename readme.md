# 🧪 Chemistry Quiz Game

> A **terminal-based Chemistry Quiz Game** built in Python to learn and practice chemistry concepts while having fun.  
> Um **jogo de quiz de química no terminal** feito em Python para aprender e praticar conceitos de química se divertindo.

---

## 🎯 Game Overview / Visão Geral

- 3 difficulty levels: Easy, Medium, Hard  
- Lives system: 3 per level  
- Points awarded for correct answers  
- Ranking system to save your best scores  
- Save & Load game functionality  

🇧🇷 Visão Geral:

- 3 níveis de dificuldade: Fácil, Médio, Difícil  
- Sistema de vidas: 3 por nível  
- Pontos por respostas corretas  
- Sistema de ranking para salvar suas melhores pontuações  
- Funcionalidade de salvar e carregar jogo  

---

## 🕹️ How to Play / Como Jogar

```bash
# Clone this repository
git clone https://github.com/seu_usuario/chemistrygame.git
cd chemistrygame

# Run the game
python main.py

    Enter your name / Digite seu nome

    Choose a menu option / Escolha uma opção do menu:

Option	Description
1	Start Game / Iniciar Jogo
2	Load Saved Game / Carregar Jogo
3	Ranking
4	About the Game / Sobre o Jogo
5	Exit / Sair

    Answer multiple-choice questions (a/b/c/d) / Responda perguntas de múltipla escolha (a/b/c/d)

    Correct answer = points / Resposta correta = pontos
    Wrong answer = lose 1 life / Resposta errada = perde 1 vida

    Game over when all lives are lost / Fim do jogo quando todas as vidas acabarem

    Complete the level to see your score and ranking / Complete o nível para ver sua pontuação e ranking

🏆 Levels & Points / Níveis e Pontuação
Level / Nível	Lives / Vidas	Points per Question / Pontos por Pergunta
Easy 🟢	3	10
Medium 🟡	3	20
Hard 🔴	3	30
🔧 Technologies / Tecnologias

    Python 3.x

    Terminal / Console

    File handling (save/load system) / Manipulação de arquivos (salvar/carregar)

    Functions, loops, dictionaries / Funções, loops, dicionários

💻 Project Structure / Estrutura do Projeto

chemistry-quiz/
├── main.py          # Entry point / Ponto de entrada
├── menu.py          # Game menu / Menu do jogo
├── dificuldades.py  # Difficulty selection / Seleção de dificuldade
├── levels.py        # Level logic / Lógica dos níveis
├── questions.py     # Questions per level / Perguntas por nível
├── utils.py         # Utility functions / Funções utilitárias
├── data.py          # Save & ranking system / Sistema de save e ranking
├── save.txt         # Created after first save / Criado após o primeiro save
├── ranking.txt      # Created after first game / Criado após o primeiro jogo
└── README.md        # This file / Este arquivo

🚀 Features / Funcionalidades

    Multiple-choice quiz 🎓 / Quiz de múltipla escolha

    3 difficulty levels / 3 níveis de dificuldade

    Save & Load progress 💾 / Salvar e carregar progresso

    Ranking leaderboard 🏆 / Ranking de melhores scores

    Animated text effect ✨ / Efeito de texto animado no terminal

    Points system / Sistema de pontuação

    Educational and fun / Educativo e divertido

📚 Example / Exemplo

🎯 CHOOSE DIFFICULTY
1 - 🟢 Easy
3 lives | 10 pts/question

Enter your answer (a/b/c/d): b
✅ Correct!

Lives left: 3 | Score: 10

👩‍💻 Author / Autor

Mali Soares – LinkedIn

Python Developer | Aspiring Remote Dev | Educational Games Enthusiast
📝 License / Licença

MIT License / Licença MIT
