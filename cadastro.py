#Cadastro de usuário e senha
def cadastrar_usuario():    #Função que irá cadastrar o usuário e a senha
    print("=============Cadastro de Usuário============")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
#O cadastro de usuário e senha irá criar um arquivo chamado usuarios.txt, onde o usuário e a senha serão armazenados
    with open("usuarios.txt", "a") as arquivo:  #Esse "a" significa que o arquivo será aberto em modo de anexação(acrescentar), ou seja, se o arquivo já existir, o novo conteúdo será adicionado ao final do arquivo
        #O arquivo irá armazenar o usuário e a senha separados por vírgula
        arquivo.write(f"{usuario},{senha}\n") #O arquivo.write irá escrever o usuário e a senha no arquivo usuarios.txt, separados por vírgula e com uma quebra de linha no final
        print("Usuário cadastrado com sucesso!")
        
def login ():   #Função que irá fazer o login do usuário
    print("=============login============")
    while True:    
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        
        encontrado = False    #Variável que irá verificar se o usuário e a senha estão corretos
        
        try:
            #O login irá abrir o arquivo usuarios.txt e verificar se o usuário e a senha estão corretos
            with open("usuarios.txt", "r") as arquivo:  #Esse "r" significa que o arquivo será aberto em modo de leitura, ou seja, o conteúdo do arquivo será lido
                for linha in arquivo:
                    u, s = linha.strip().split(",") #O arquivo irá ler o usuário e a senha, separados por vírgula. O strip() irá remover os espaços em branco no início e no final da linha
                    #O split() irá separar o usuário e a senha, criando uma lista com os dois elementos
                    if u == usuario and s == senha: #Se o usuário e a senha estiverem corretos, a variável encontrado irá receber True
                        print("Login bem-sucedido!")
                        encontrado = True   #A variável encontrado irá receber True
                        break
        except FileNotFoundError: #Se o arquivo usuarios.txt não existir, o programa irá imprimir uma mensagem de erro. Esse except FileNotFoundError irá capturar o erro caso as informações do usuário em usuarios.txt não exista
            print("Informações de usuário não encontrado. Cadastre um usuário primeiro.")
            break
        
        if encontrado:  #Se a variável encontrado for True, o usuário e a senha estão corretos
            print("Acesso permitido. Bem-vindo ao sistema!")
            break
        else:
            print("Usuário ou senha inválidos. Tente novamente.\n")
            if input("Deseja tentar novamente? (s/n): ").lower() == 'n':    #Esse .lower() irá transformar a letra em minúscula, ou seja, se o usuário digitar 'S' ou 's', o programa irá entender como 's'. Para não dar erro de digitação
                break
            
#Menu principal
#O MENU PRINCIPAL PRECISA ESTAR EM BAIXO DAS FUNÇÕES PARA QUE ELAS SEJAM RECONHECIDAS QUANDO O USUÁRIO ESCOLHER A OPÇÃO 1, 2 OU 3
while True:
    print("=============Menu Principal==============")
    print("1. Cadastrar Usuário")
    print("2. Fazer Login")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_usuario() #Se o usuário escolher a opção 1, o programa irá chamar a função cadastrar_usuario()
    elif opcao == "2":
        login() #Se o usuário escolher a opção 2, o programa irá chamar a função login()
    elif opcao == "3":
        print("Saindo...")  #Se o usuário escolher a opção 3, o programa irá imprimir a mensagem "Saindo..." e sair do loop
        break
    else:
        print("Opção inválida. Tente novamente.")   #Se o usuário digitar algo que não seja 1,2 ou 3, o programa irá imprimir a mensagem "Opção inválida. Tente novamente.", e o loop irá reiniciar, voltando para o menu principal