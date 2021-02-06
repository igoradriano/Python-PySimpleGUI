from PySimpleGUI import PySimpleGUI as sg
#devemos instalar no terminal antes de importar a biblioteca, PySimpleGUI

#Layout
sg.theme('Reddit')  # O PySimpletUI tem uma quantidade enorme de temas. Escolhi o "Reddit"
# O PySimpleGUI utiliza uma abordagem de linhas e colunas, no nosso caso precisaremos de 3 linhas e 2 colunas
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario',size=(20,1))],   # O valor que passamos para key serve como identificador
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*',size=(20,1))], #substitui sua senha por asterísticos na tela.
    [sg.Checkbox('Salvar o login?')], #Uma caixinha para marser se quer salvar o login ou não
    [sg.Button('Entrar')]   #Criando um Botão e nele estará escrito Entrar
]

#Janela
janela = sg.Window('Tela de login',layout)    #Título de Janela = Tela de login
#Ler os eventos acontecendo na tela
while True:
    eventos,valores = janela.read()  #recebe "Tela de login" e o objeto layout armazenados dentro de janela
    if eventos == sg.WINDOW_CLOSED:    #quando a janela for fechada quebre o loop
        break
    if eventos=='Entrar':      #se clicarem no botão entrar faça
        if valores['usuario'] == 'igor' and valores['senha'] == '123456': #verificando dados
            print("Bem-vindo a Dev Aprender!")
#note que a penultima linha desconsideramos a existencia de um banco de dados, consideramos que temos armazenado apenas jhonatan como valor e sua senha respectiva.