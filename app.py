import textwrap
import json

def quiz():
    f = open('perguntas.json')
    perguntas = json.load(f)
    
    pontos = 0
        
    print(textwrap.dedent('''
    -------------------------------------------------------------
    ---------------BEM-VINDO(A) AO QUIZ INSIDER-E!---------------
    -------------------------------------------------------------
        
    - Lembre-se de responder sempre com a letra da alternativa correspondente.
    - Cada alternativa correta vale 5 PONTOS.
    '''))
        
    for pergunta in perguntas['perguntasQuiz']:
        resposta = input(f'{pergunta['question']}\n{' '.join(map(str, pergunta['options']))}\n')
            
        if resposta.upper() == pergunta['answer'].upper():
            pontos += 5
        
    print(textwrap.dedent(f'''
    -------------------------------------------------------------
    ---------------SUA PONTUAÇÃO FOI DE {pontos} PONTOS----------------
    -------------------------------------------------------------
    '''))
    
    return pontos
        
def infoUltimaCorrida():
    f = open('infoUltimaCorrida.json')
    infoUltimaCorrida = json.load(f)['info']
    
    print(textwrap.dedent(f'''
    -------------------------------------------------------------
    ------------INFORMAÇÕES SOBRE A ÚLTIMA CORRIDA---------------
    -------------------------------------------------------------
    
    - Data: {infoUltimaCorrida['date']}
    
    - Ganhador: {infoUltimaCorrida['winner']}
    
    - Lugar: {infoUltimaCorrida['location']}
    
    {infoUltimaCorrida['summary']}
    '''))
    
def infoProxCorrida():
    f = open('infoProxCorrida.json')
    infoProxCorrida = json.load(f)['info']
    
    print(textwrap.dedent(f'''
    -------------------------------------------------------------
    ------------INFORMAÇÕES SOBRE A PRÓXIMA CORRIDA--------------
    -------------------------------------------------------------
    
    - Data: {infoProxCorrida['date']}
    
    - Hora: {infoProxCorrida['time']}
    
    - Lugar: {infoProxCorrida['location']}
    
    - Equipes participantes:
    
    {', '.join(map(str, infoProxCorrida['teams']))}
    '''))
    
    
print('''
-------------------------------------------------------------
----------------SEJA BEM VINDO(A) À INSIDER-E----------------
-------------------------------------------------------------
    ''')

nome = input('DIGITE SEU NOME: ')

while True:
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

    if opcao == '1':
        quiz()
    elif opcao == '2':
        infoUltimaCorrida()
    elif opcao == '3':
        infoProxCorrida()
        

    break

