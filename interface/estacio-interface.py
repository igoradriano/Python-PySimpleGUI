import PySimpleGUI as sg

# 1) CRIANDO UMA CLASSE
class TelaPython:  
    def __init__(self): # 2) CONSTRUTOR DA CLASSE NÃO VAI RECEBER NENHUM INPUT DO USUÁRIO
        # ----------------------------------------------------------------------------------------------------------
        # 3) ESCOLHENDO O TEMA DA JANELA
        sg.theme('DarkBrown4') 
        # Você pode usar o comando sg.theme_previewer() para ter uma prévia de todos principais temas ou
        # Usar uma variável para armazenar o nome de todos os temas disponívels  --> theme_list = sg.theme_list() 
        # E depois imprimir a variável --> print(theme_list) 
        # ----------------------------------------------------------------------------------------------------------
        # 4) CRIANDO O LAYOUT DA JANELA:
            # O PySimpleGUI utiliza uma abordagem de linhas e colunas, então é recomendável primeiramente desenhar como você vai querer o layout da sua Janela. 
            # Basicamente você 
        layout = [  
            # A) Abaixo 'sg.Text' é utilizado para inserir texto, dentro dele passamos como parâmetros o primeiro size que é o número de cactéres que vai ter o Nome do Campo (nesse caso 'Nome' e 'Idade' terão 5 caractéres de espaço para comportá-los, uma meneira de alinhar os textos), utilizamos a vírgula para indicar o início de uma nova coluna, então passamos o comando 'sg.Input' para receber valores e o segundo size, que é o número de caractéres que vai ter o campo de input de valores, passamos então em uma nova coluna uma chave 'key' para identificar esta linha inteira, onde mais tarde utilizares essa chave.
            # B) O 'sg.Checkbox' é utilizado como o próprio nome sugere, para mostrar na tela caixas de marcação, passamos como parâmetros o nome e um identificador.
            # C) O 'sg.Radio' é similar ao Checkbox, mas no Radio somente uma opção pode ser selecionada. Passamos novamente o nome que aparecerá na tela, um nome para identificar todos os Radios que correspodem a uma mesma situação e uma key para identificalos.
            # D) O 'sg.Slider' é utilizado para imprimri uma colina de deslizar, passamos um range para o valor inicial e final dessa coluna, o defalt_value é o valor padrão quando a tela abrir, o orientation pode ser h = horizontal, v = vertical, size é o tamanho dele dentro da Janela, e o key novamente o idenidentificador.
            # E) O 'sg.Button' sugestivamente é utilizado para mostrar um botão, passamos como parâmetro o Nome que aparecerá dentro do botão.
            # F) O 'sg.Output' é utilizado para mostrar uma tela onde poderemos colocar saídas para o usuário, pode funcionar como uma tela de log, ou algo de tipo. Basta passar o tamanho que deseja das coordenadas (x,y)
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(20,1),key="nome")], 
            [sg.Text("Idade",size=(5,0)),sg.Input(size=(20,1),key='idade')],
            [sg.Text("Quais provedores de e-mail são aceitos?")], # veja que aqui passamos apenas uma coluna nesta linha
            [sg.Checkbox('Gmail',key='gmail'), sg.Checkbox('Outlook',key='outlook'), sg.Checkbox("Yahoo",key='yahoo')],
            [sg.Text('Aceita cartão ?')],
            [sg.Radio('Sim','cartões',key='aceita_cartao_sim'),sg.Radio('Não','cartões',key='nao_aceita_cartao')], 
            [sg.Text("Qual seu nível de satisfação?")],
            [sg.Slider(range=(0,10),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')], 
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,15))] 
        ]
        #---------------------------------------------------------------------------------------------------------------
        # 5) CRIANDO A JANELA
        # 'sg.Window' Passa o nome da Janela que será mostrado na Barra superior.
        # '.layout' é um método do PySimpleGUI para passar as linhas do layout criado anteriormente.
        # A janela está no escopo self para ser acessada em todo local onde eu tenha a propriedade self.
        self.janela = sg.Window("Dados do Usuário").layout(layout) 
        #---------------------------------------------------------------------------------------------------------------

        # 6) CRIANDO UM MÉTODO PARA INCIAR A JANELA 
        # Com 'while True' garanto que a Janela não será fechada assim que os dados forem inseridos e apertarmos o botão enviar, no caso ele ficará em um loop a procura de valores até fecharmos a tela.
    def Iniciar(self):
        while True:   
            # Extrair os dados da tela
            # O método Read vai passar as informações inseridas na tela para o Button e values.
            self.Button, self.values = self.janela.Read()
            print("-"*35) 
            print("Dados Imputados")
            # Finalmente utilizaremos as key's criadas anteriormente como identificadores. Para acessar a Key dentro do for, e imprimir seu nome e seu valor
            for key,value in self.values.items():  
                print(f'{key}:{value}')
            print("-"*35)
 # E agora é só instanciar atribuindo a uma variável a Classe anteriormente criada
tela = TelaPython()
tela.Iniciar()  # E chamar o método iniciar para a Tela ser exibida

