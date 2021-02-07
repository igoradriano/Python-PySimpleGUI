import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        # self
        sg.theme('DarkBrown4')
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(20,1),key="nome")],  # O primeiro size é o número de cactéres que vai ter o campo nome, o segundo size é o número de caractéres que vai ter o campo que vamos inserir o valor de nome.
            [sg.Text("Idade",size=(5,0)),sg.Input(size=(20,1),key='idade')],  #através dos identificadores(keys) consigo alterar o nome da chave do dicionário que será impresso pela variável self.values
            [sg.Text("Quais provedores de e-mail são aceitos?")],
            [sg.Checkbox('Gmail',key='gmail'), sg.Checkbox('Outlook',key='outlook'), sg.Checkbox("Yahoo",key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','cartões',key='aceita_cartao_sim'),sg.Radio('Não','cartões',key='nao_aceita_cartao')], #Radio vai dar apenas uma única opção para o usuario marcar, diferente do checkbox. Passamos primeiro os valores que apareceram na tela como opção, depois o nome da ratio, e por ultimo um identificador.
            [sg.Text("Qual seu nível de satisfação?")],
            [sg.Slider(range=(0,10),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')], # Aqui no slider o defalt_value é o valor padrão quando a tela abrirm orientation pode ser h = horizontal, v = vertical, size é o tamanho dele e key o idenidentificador
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,15))] #Tela de log, vai aparecer os processos realizados 
        ]
        # Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout) #janela no escopo self para ser acessada em todo local onde eu tenha a propriedade self.
        
    
    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.Button, self.values = self.janela.Read()# O método read vai passar as informações inseridas na tela para o button e values. O while vai garantir que a tela não feche depois que apertarmos enviar, e fique procurando mais valores dentro de um loop, até fecharmos a tela.
            #print(self.values) 
            #nome =self.values['nome']
            #idade =self.values['idade']
            #aceita_gmail =self.values['gmail']
            #aceita_outlook =self.values['outlook']
            #aceita_yahoo =self.values['yahoo']
            print("-"*35)
            print("Dados Imputados")
            for key,value in self.values.items():
                print(f'{key}:{value}')#Imprimindo todos os valores, primeiro pensei em atribuir os valores a variáveis, mas isso complicaria, para cada nova implementação de dados, deveria criar mais uma nova varável para receber e imprimir o valor. Com o laço for não preciso me preocupar com isso
            print("-"*35)


tela = TelaPython()
tela.Iniciar()

