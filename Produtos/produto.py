import json
import os

def salvar_dados(arquivo, produto):
    try:
        with open(arquivo, 'r') as file:
            A_produtos = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        A_produtos = []

    A_produtos.append(produto)

    with open(arquivo, 'w') as file:
        json.dump(A_produtos, file)

def ler_dados():
    try:
        with open('produto.json', 'r') as file:
            tamanho = os.path.getsize('produto.json')
            if not tamanho:
                print(f"\nNão tem produtos cadastrados")
                return []
            else:
                A_produtos = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print(f"\nNão tem produtos cadastrados")
        return []

    return A_produtos


def cadastrar_produto():

    Nome = input("Nome: ")
    Valor  = int(input("Valor do produto: "))
    Fornecedor = input("Fornecedor: ")
    Quantidade = int(input("Informe a quantidade de unidades inical: "))
    Descricao = input("Informe a descrição do produto: ")
    
    produto = {
        'Nome':Nome,
        'Valor': Valor,
        'Fornecedor': Fornecedor,
        'Quantidade': Quantidade,
        'Descricao': Descricao
    }
    
    
    
    print("\nRegistro cadastrado com sucesso!")

    salvar_dados('produto.json', produto)
    
def apresentar_produto():
    Agenda_produtos = ler_dados()
    
    if not(Agenda_produtos):
        return

    encontrar = input("Deseja encontrar um produto especifico? (sim/não): ")
   
    if encontrar == 'sim':

        Nome = input("Informe o nome do produto: ")
        encontrado = False

        for produto in Agenda_produtos:      
         if Nome == produto['Nome']:
            encontrado = True
            print(f"\nNome: {produto['Nome']}")
            print(f"Valor: {produto['Valor']}")
            print(f"Fornecedor: {produto['Fornecedor']}")
            print(f"Quantidade: {produto['Quantidade']}")
            print(f"Descrição: {produto['Descricao']}")
            print(" -" * 20) 

        if encontrado == False:
             print("\nProduto não cadastrado!")
            
    else:
        if not Agenda_produtos:
                print("\nNão há produtos cadastrados.")
        else:
                print("\nProdutos cadastrados:")
        for produto in Agenda_produtos:
            print(f"\nNome: {produto['Nome']}")
            print(f"Valor: {produto['Valor']}")
            print(f"Fornecedor: {produto['Fornecedor']}")
            print(f"Quantidade: {produto['Quantidade']}")
            print(f"Descrição: {produto['Descricao']}")
            print(" -" * 20)



def atualizar_produto():
    
    Agenda_produtos = ler_dados()

    if not Agenda_produtos:
        return

    Nome = input("Informe o nome do produto: ")

    for produto in Agenda_produtos:
        if Nome == produto['Nome']:
            produto['Valor'] = int(input("Informe o novo valor: "))
            produto['Fornecedor'] = input("Informe o novo Fornecedor: ")
            produto['Quantidade'] = int(input("Informe a nova Quantidade: "))
            produto['Descricao'] = input("Informe a nova Descrição: ")

            resposta = input("\nAtualizar produto? (sim/não): ")

            if resposta.lower() == 'sim':
                with open('produto.json', 'w') as file:
                    json.dump(Agenda_produtos, file)

                print("\nProduto Atualizado!")
                return

    print("\nProduto não encontrado!")
