import json
import os

from Produtos.produto import ler_dados

def salvarDados(arquivo, cliente):
    clientes = []
    try:   
        with open(arquivo, 'r') as file:
            tamanho = os.path.getsize('cliente.json')
            if tamanho:
                clientes = json.load(file)
    except FileNotFoundError:
        with open(arquivo, 'w') as file:
            json.dump([cliente], file)
    else:
        clientes.append(cliente)
        with open(arquivo, 'w') as file:
            json.dump(clientes, file)

def LerDados():
    try:   
        with open('cliente.json', 'r') as file:           
            tamanho = os.path.getsize('cliente.json')
            if not(tamanho):
                print("Não há usuários cadastrados!")
                return 0
            else:
                clientes = json.load(file)
                
    except FileNotFoundError:
        print("Não há usuários cadastrados!")
        return 0
    else:
        return clientes

def cadastrarCliente():

    cliente = {
        'nome': '',
        'CPF': '',
        'endereco': '',
        'telefone': '',
        'compras': [],
        'dividas': 0,
    }


    cliente['nome'] = input("Informe o nome: ").title()
    cliente['CPF'] = input("Informe o CPF: ")
    cliente['endereco'] = input("Informe o Endereço: ").title()
    cliente['telefone'] = input("Informe o telefone: ")

    salvarDados('cliente.json', cliente)
    print("\nCliente cadastrado!")

def buscarCliente():
    
    clientes = LerDados()
    
    if not(clientes):
        return
    
    CPF = input("Informe o CPF buscado: ")
    encontrado = False

    for cliente in clientes:
        if CPF == cliente['CPF']:
            encontrado = True
            print(f"\nCliente: {cliente['nome']}")
            print(f"CPF: {cliente['CPF']}")
            print(f"Endereço: {cliente['endereco']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"Dívidas: {cliente['dividas']} \n")
            
            resposta  = input("Ver dados de compra? (sim/não) ").lower()
            if resposta == 'sim':
                if cliente['compras'] == []:
                    print("Não há compras registradas!")
                else:
                    print("\n")
                    for compra in cliente['compras']:
                        print(compra)
    
    if not(encontrado):
        print("Cliente não encontrado!")
            

def buscarClientes():
    
    clientes = LerDados()
    quantidade = 1
    
    if not(clientes):
        return

    for cliente in clientes:
        print(f"\nCliente {quantidade}")
        print(f"\nCliente: {cliente['nome']}")
        print(f"CPF: {cliente['CPF']}")
        print(f"Endereço: {cliente['endereco']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"Dívidas: {cliente['dividas']} \n")
        quantidade += 1

def atualizarCliente():
    clientes = LerDados()
    encontrado = False
    
    if not(clientes):
        return
    
    CPF = input("Informe o CPF do cliente: ")

    for indice, cliente in enumerate(clientes):
        if CPF == cliente['CPF']:
            encontrado = True
            cliente['nome'] = input("Informe o novo nome: ").title()
            cliente['CPF'] = input("Informe o novo CPF: ")
            cliente['endereco'] = input("Informe o novo endereço: ").title()
            cliente['telefone'] = input("Informe o novo telefone: \n")

            resposta  = input("Atualizar cliente? (sim/não) ").lower()
           
            if resposta == 'sim':
                clientes[indice] = cliente
                with open('cliente.json', 'w') as file:
                    json.dump(clientes, file)

                print("\nCliente Atualizado!")       
                return
    
    if not(encontrado):
        print("Cliente não encontrado!")
        return
    
    


def deletarCliente():
    clientes = LerDados()
    encontrado = False
    
    if not(clientes):
        return
    
    CPF = input("Informe o CPF do cliente: ")

    for indice, cliente in enumerate(clientes):
        if CPF == cliente['CPF']:
            encontrado = True
            print(f"\nCliente: {cliente['nome']}")
            print(f"CPF: {cliente['CPF']}")
            print(f"Endereço: {cliente['endereco']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"Dívidas: {cliente['dividas']} \n")

            resposta  = input("Deletar cliente? (sim/não) ").lower()
            if resposta == 'sim':
                clientes.pop(indice)
                with open('cliente.json', 'w') as file:
                    json.dump(clientes, file)

                print("\nCliente Excluído!")
                return
    
    if not(encontrado):
        print("Cliente não encontrado!")
        return

def somarDividas():
    clientes = LerDados()
    dividas = 0
    
    if not(clientes):
        return
    
    for cliente in clientes:
        dividas += cliente['dividas']
    
    print(f"Dívida total do clientes: {dividas}")


def pagarDivida():
    clientes = LerDados()
    encontrado = False
    
    if not(clientes):
        return
    
    CPF = input("Informe o CPF do cliente: ")

    for indice, cliente in enumerate(clientes):
        if CPF == cliente['CPF']:
            encontrado = True
            print(f"\nCliente: {cliente['nome']}")
            print(f"CPF: {cliente['CPF']}")
            print(f"Endereço: {cliente['endereco']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"Dívidas: {cliente['dividas']} \n")

            if cliente['dividas'] == 0:
                print("O cliente não possui dívidas!")
                return

            resposta  = input("Apagar dívidas do cliente? (sim/não) ").lower()
            if resposta == 'sim':
                cliente['dividas'] = 0
                cliente['compras'] = []
                clientes[indice] = cliente
                with open('cliente.json', 'w') as file:
                    json.dump(clientes, file)

                print("\nDívida apagada!")
                return
    
    if not(encontrado):
        print("Cliente não encontrado!")
        return
        

def registrar_compras():
    
    clientes = LerDados()
    if not(clientes):
        return
    
    produtos = ler_dados()

    if not(produtos):
        return

    encontrado_cliente = False
    encontrado_produto = False

    cliente_CPF = input("Informe o CPF do cliente: ")

    for indice_cliente, cliente in enumerate(clientes):
        if cliente_CPF == cliente['CPF']:      
            
            encontrado_cliente = True      
            produto_comprado = input("Informe o produto comprado: ").title()

            for indice_produto, produto in enumerate(produtos):
                if produto_comprado == produto['Nome']:
                    encontrado_produto = True
                    quantidade = int(input("Informe a quantidade de produtos a serem comprados: "))
                    if quantidade > produto['Quantidade']:
                        print("\nA quantidade informada é maior que o estoque de produtos!")
                        print(f"Quantidade em estoque: {produto['Quantidade']}")
                        return
                    else:
                        novaCompra = "Quantidade: {}, Produto: {}".format(quantidade, produto_comprado)
                        cliente['compras'].append(novaCompra)
                        cliente['dividas'] = cliente['dividas'] + (quantidade * produto['Valor'])
                        produto['Quantidade'] = produto['Quantidade'] - quantidade
                        
                        clientes[indice_cliente] = cliente
                        produtos[indice_produto] = produto
                    

    if  not(encontrado_cliente):
         print("\ncliente não encontrado!")
         return  

    if(encontrado_produto):
        resposta = input("\nDeseja confirmar? (sim/não): ").lower()
        if resposta == 'sim':
            
            with open('cliente.json', 'w') as file:
                json.dump(clientes, file)

            with open('produto.json', 'w') as file:
                json.dump(produtos, file)

            print("\nCompra registrada com sucesso!")
            return
    else:
        print("O produto não foi encontrado no estoque!")
