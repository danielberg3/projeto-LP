import json
import os

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
        'compras': '',
        'dividas': 0,
    }


    cliente['nome'] = input("Informe o nome: ")
    cliente['CPF'] = input("Informe o CPF: ")
    cliente['endereco'] = input("Informe o Endereço: ")
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
            
            resposta  = input("Ver dados de compra? (sim/não) ")
            if resposta == 'sim':
                if cliente['compras'] == '':
                    print("Não há compras registradas!")
                else:
                    print(f"Dados de compra: {cliente['compras']}")
    
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
            cliente['nome'] = input("Informe o novo nome: ")
            cliente['CPF'] = input("Informe o novo CPF: ")
            cliente['endereco'] = input("Informe o novo endereço: ")
            cliente['telefone'] = input("Informe o novo telefone: \n")

            resposta  = input("Atualizar cliente? (sim/não) ")
           
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

            resposta  = input("Deletar cliente? (sim/não) ")
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

            resposta  = input("Apagar dívidas do cliente? (sim/não) ")
            if resposta == 'sim':
                cliente['dividas'] = 0
                cliente['compras'] = ''
                clientes[indice] = cliente
                with open('cliente.json', 'w') as file:
                    json.dump(clientes, file)

                print("\nDívida apagada!")
                return
    
    if not(encontrado):
        print("Cliente não encontrado!")
        return