import textwrap
import json

#Função para o quiz
def quiz():
    #Abre e lê o arquivo JSON contendo as perguntas e respostas
    f = open('perguntas.json')
    perguntas = json.load(f)
    
    #Pontos acumulados a cada resposta correta
    pontos = 0
        
    #textwrap.dedent = remove a identação do texto, para não ficar bagunçado na exibição no terminal
    print(textwrap.dedent('''
    -------------------------------------------------------------
    ---------------BEM-VINDO(A) AO QUIZ INSIDER-E!---------------
    -------------------------------------------------------------
        
    - Lembre-se de responder sempre com a letra da alternativa correspondente.
    - Cada alternativa correta vale 5 PONTOS.
    '''))
        
    #Percorre o array de perguntas, exibindo e pegando o valor de entrada do usuário como resposta
    for pergunta in perguntas['perguntasQuiz']:
        #' '.join(map(str, pergunta['options'])) = passa por todos os elementos de 'pergunta['options']' usando o map e
        #concatena todos em uma string, separando com espaço
        resposta = input(f'{pergunta['question']}\n{' '.join(map(str, pergunta['options']))}\n')
           
        #Verifica se a resposta digitada está correta e acumula 5 pontos para o usuário 
        if resposta.upper() == pergunta['answer'].upper():
            pontos += 5
        
    #Exibe a pontuação
    print(textwrap.dedent(f'''
    -------------------------------------------------------------
    ---------------SUA PONTUAÇÃO FOI DE {pontos} PONTOS----------------
    -------------------------------------------------------------
    '''))
    
    return pontos
        
#Função para exibir informações sobre a última corrida
def infoUltimaCorrida():
    #Abre e lê o arquivo JSON contendo as informações
    f = open('infoUltimaCorrida.json')
    infoUltimaCorrida = json.load(f)['info']
    
    #textwrap.dedent = remove a identação do texto, para não ficar bagunçado na exibição no terminal
    print(textwrap.dedent(f'''
    -------------------------------------------------------------
    ------------INFORMAÇÕES SOBRE A ÚLTIMA CORRIDA---------------
    -------------------------------------------------------------
    
    - Data: {infoUltimaCorrida['date']}
    
    - Ganhador: {infoUltimaCorrida['winner']}
    
    - Lugar: {infoUltimaCorrida['location']}
    
    {infoUltimaCorrida['summary']}
    
    -------------------------------------------------------------
    '''))
  
#Função para exibir informações sobre a próxima corrida  
def infoProxCorrida():
    #Abre e lê o arquivo JSON contendo as informações
    f = open('infoProxCorrida.json')
    infoProxCorrida = json.load(f)['info']
    
    #textwrap.dedent = remove a identação do texto, para não ficar bagunçado na exibição no terminal
    #', '.join(map(str, infoProxCorrida['teams'])) = passa por todos os elementos de 'infoProxCorrida['teams']' usando o map e
    #concatena todos em uma string separando por vírgula
    print(textwrap.dedent(f'''
    -------------------------------------------------------------
    ------------INFORMAÇÕES SOBRE A PRÓXIMA CORRIDA--------------
    -------------------------------------------------------------
    
    - Data: {infoProxCorrida['date']}
    
    - Hora: {infoProxCorrida['time']}
    
    - Lugar: {infoProxCorrida['location']}
    
    - Equipes participantes:
    
    {', '.join(map(str, infoProxCorrida['teams']))}
    
    -------------------------------------------------------------
    '''))
    
#Função para exibir informações sobre a próxima corrida 
def rankingEquipes():
    #Abre e lê o arquivo JSON contendo as equipes
    f = open('equipes.json')
    equipes = json.load(f)['teams']
    
    #textwrap.dedent = remove a identação do texto, para não ficar bagunçado na exibição no terminal
    print(textwrap.dedent(f'''
    -------------------------------------------------------------
    ---------------------RANKING DE EQUIPES----------------------
    -------------------------------------------------------------
    '''))
    
    #Ordena as equipes por ordem descrescente considerando o número de vitórias (reverse = True)
    equipesOrdenadas = sorted(equipes, key=lambda equipe: equipe['victories'], reverse=True)
    
    #Contador para definir a posição das equipes
    i = 1
    
    #Exibe cada equipe por ordem descrescente considerando o número de vitórias e suas respectivas posições no ranking
    for equipe in equipesOrdenadas:
        print(f'{i}° - {equipe['name']} | {equipe['victories']} vitórias')
        i += 1
    
    print('-------------------------------------------------------------')

print('''
-------------------------------------------------------------
----------------SEJA BEM VINDO(A) À INSIDER-E----------------
-------------------------------------------------------------
    ''')

nome = input('DIGITE SEU NOME: ')

while True:
    #textwrap.dedent = remove a identação do texto, para não ficar bagunçado na exibição no terminal
    opcao = input(textwrap.dedent(f'''

    | ----------------------------------------------- |
    |         CÓDIGO        |         OPÇÃO           |
    | ----------------------------------------------- |
    |            1          |          QUIZ           |
    |            2          | INFO. DA ÚLTIMA CORRIDA |
    |            3          | INFO. DA PRÓX. CORRIDA  |
    |            4          |   RANKING DE EQUIPES    |
    | ----------------------------------------------- |

    {nome}, digite o código referente à opção que deseja: 
    '''))

    #Verifica a opção que o usuário digitou e leva para sua respectiva função,
    #caso a opção for inválida o usuário é informado
    #Em cada opção há uma pergunta para saber se o usuário quer continuar, se for digitado 2 (NÃO),
    #é executado um break no loop e o programa para
    if opcao == '1':
        quiz()
        cont = input('Deseja continuar?\n 1 - SIM\n 2 - NÃO\n')
        if cont == '2':
            break
        
    elif opcao == '2':
        infoUltimaCorrida()
        cont = input('Deseja continuar?\n 1 - SIM\n 2 - NÃO\n')
        if cont == '2':
            break
        
    elif opcao == '3':
        infoProxCorrida()
        cont = input('Deseja continuar?\n 1 - SIM\n 2 - NÃO\n')
        if cont == '2':
            break
        
    elif opcao == '4':
        rankingEquipes()
        cont = input('Deseja continuar?\n 1 - SIM\n 2 - NÃO\n')
        if cont == '2':
            break
        
    else:
        print('***Opção inválida!***')
        

