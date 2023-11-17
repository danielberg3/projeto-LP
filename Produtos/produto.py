import json
import os

def salvarDados(arquivo, produto):
    A_produtos = []
    try:   
        with open(arquivo, 'r') as file:
            tamanho = os.path.getsize('arquivoproduto.json')
            if tamanho:
                existe = True
                A_produtos = json.load(file)
    except FileNotFoundError:
        with open(arquivo, 'w') as file:
            json.dump([produto], file)
    else:
        A_produtos.append(produto)
        with open(arquivo, 'w') as file:
            json.dump(A_produtos, file)


def LerDados():
    try:   
        with open('arquivoproduto.json', 'r') as file:           
            tamanho = os.path.getsize('arquivoproduto.json')
            if not(tamanho):
                print("Não há produtos cadastrados!")
                return 0
            else:
                A_produtos = json.load(file)
                
    except FileNotFoundError:
        print("Não há produtos cadastrados!")
        return 0
    else:
        return A_produtos
      

def cadastrar_produto():

    Nome = input("Nome: ")
    Valor  = input("Valor do produto: ")
    Fornecedor = input("Fornecedor: ")
    Quantidade = input("Informe a quantidade de unidades inical: ")
    Descricao = input("Informe a descrição do produto: ")
    
    produto = {
        "Nome":Nome,
        "Valor": Valor,
        "Fornecedor": Fornecedor,
        "Quantidade": Quantidade,
        "Descrição": Descricao
    }
    
    print("\nRegistro cadastrado com sucesso!")

    salvarDados('arquivoproduto.json', produto)
    
def apresentar_produto():
    A_produtos = LerDados()

    if not A_produtos:
        print("\nNão há produtos cadastrados.")
    else:
        print("\nProdutos cadastrados:")
    for produto in A_produtos:
         print(f"\nNome: {produto['Nome']}")
         print(f"Valor: {produto['Valor']}")
         print(f"Fornecedor: {produto['Fornecedor']}")
         print(f"Quantidade: {produto['Quantidade']}")
         print(f"Descrição: {produto['Descrição']}")
         print(" -" * 20)



def atualizar_produto():

    A_produtos = LerDados()
    encontrado = False
    
    if not(A_produtos):
        return
    
    Nome = input("Informe o nome do produto: ")

    for indice, produto in enumerate(A_produtos):
        if Nome == produto['Nome']:
            encontrado = True
            produto['Valor'] = input("Informe o novo valor: ")
            produto['Fornecedor'] = input("Informe o novo Fornecedor: ")
            produto['Quantidade'] = input("Informe a nova Quantidade: ")
            produto['Descrição'] = input("Informe a nova Descrição: ")


            resposta  = input("\nAtualizar produto? (sim/não) ")
           
            if resposta == 'sim':
                A_produtos[indice] = produto
                with open('arquivoproduto.json', 'w') as file:
                    json.dump(A_produtos, file)

                print("\nproduto Atualizado!")       
                return
    
    if not(encontrado):
        print("\nproduto não encontrado!")
        return
