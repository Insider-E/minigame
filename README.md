# Insider-E: Minigame

Este repositório contém o código-fonte e a documentação para um aplicativo de quiz desenvolvido para a Insider-E, focado em corridas de Fórmula E. O aplicativo permite aos usuários responder perguntas sobre Fórmula E, obter informações sobre a última corrida, visualizar detalhes da próxima corrida e ver o ranking das equipes.

## Funcionalidades

- **Quiz Interativo:** Responda perguntas sobre Fórmula E e acumule pontos.
- **Informações da Última Corrida:** Veja detalhes sobre a última corrida de Fórmula E, incluindo data, ganhador e local.
- **Informações da Próxima Corrida:** Obtenha informações sobre a próxima corrida, incluindo data, hora, local e equipes participantes.
- **Ranking de Equipes:** Veja o ranking das equipes baseado no número de vitórias.

## Arquivos

- `app.py`: Código principal do aplicativo.
- `perguntas.json`: Arquivo JSON contendo as perguntas e respostas do quiz.
- `infoUltimaCorrida.json`: Arquivo JSON contendo informações sobre a última corrida.
- `infoProxCorrida.json`: Arquivo JSON contendo informações sobre a próxima corrida.
- `equipes.json`: Arquivo JSON contendo informações sobre as equipes e seus rankings.

## Requisitos

- Python 3.x
- Biblioteca `textwrap`
- Biblioteca `json`

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/Insider-E/minigame
2. Navegue até o diretório do projeto:
   ```bash
   cd minigame-insider-e
## Utilização

1. Certifique-se de que os arquivos `perguntas.json`, `infoUltimaCorrida.json`, `infoProxCorrida.json` e `equipes.json` estejam no mesmo diretório que `app.py`.

2. Execute o programa:

    ```python
    py app.py
3. Siga as instruções no terminal para interagir com o aplicativo.

## Exemplo de execução
    
    -------------------------------------------------------------
    ----------------SEJA BEM VINDO(A) À INSIDER-E----------------
    -------------------------------------------------------------

    DIGITE SEU NOME: João

    | ----------------------------------------------- |
    |         CÓDIGO        |         OPÇÃO           |
    | ----------------------------------------------- |
    |            1          |          QUIZ           |
    |            2          | INFO. DA ÚLTIMA CORRIDA |
    |            3          | INFO. DA PRÓX. CORRIDA  |
    |            4          |   RANKING DE EQUIPES    |
    | ----------------------------------------------- |

    João, digite o código referente à opção que deseja:

## Integrantes:

- David Murillo de Oliveira Soares (RM 559078)
- Davi dos Reis Garcia (RM 556741)
- Yasmin Gonçalves Coelho (RM 559147)
- Yasmin Naomi Minemoto (RM 559154)


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues para sugestões de melhorias ou para enviar pull requests.

---

Este aplicativo é uma ferramenta interativa e informativa para os fãs da Fórmula E, ajudando-os a testar seus conhecimentos e se manterem atualizados sobre as corridas. Sinta-se à vontade para explorar, utilizar e melhorar este projeto