from Clientes.cliente import cadastrarCliente
from Clientes.cliente import buscarCliente
from Clientes.cliente import buscarClientes
from Clientes.cliente import atualizarCliente
from Clientes.cliente import deletarCliente
from Clientes.cliente import somarDividas
from Clientes.cliente import pagarDivida
from Produtos.produto import hello2







while True:

    print("SISTEMA \n")

    print("1  - Cadastrar cliente")
    print("2  - Buscar por cliente")
    print("3  - Buscar por clientes")
    print("4  - Atualizar cliente")
    print("5  - Deletar cliente")
    print("6  - Ver a soma de todas as dívidas dos clientes cadastrados")
    print("7  - Registrar compras do cliente")
    print("8  - Pagamento de dívida do cliente")
    print("9  - Cadastrar produtos")
    print("10 - Atualizar produto")
    print("11 - Ver o estoque")
    print("12 - Sair \n\n")

    resposta = int(input("Informe o número da ação escolhida: "))
    
    if resposta == 1:
        cadastrarCliente()
    elif resposta == 2:
        buscarCliente()
    elif resposta == 3:
        buscarClientes()
    elif resposta == 4:
        atualizarCliente()
    elif resposta == 5:
        deletarCliente()
    elif resposta == 6:
        somarDividas()
    elif resposta == 7:
        print("")
    elif resposta == 8:
        pagarDivida()
    elif resposta == 9:
        print("")
    elif resposta == 10:
        print("")
    elif resposta == 11:
        print("")
    elif resposta == 12:
        print("")
    else:
        print("Informe uma opção válida!")