import json
import os

def salvarDados(arquivo, produto):
    A_produtos = []
    try:   
        with open(arquivo, 'r') as file:
            tamanho = os.path.getsize('produto.json')
            if tamanho:            
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
        with open('produto.json', 'r') as file:           
            tamanho = os.path.getsize('produto.json')
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
        "Descricao": Descricao
    }
    
    print("\nRegistro cadastrado com sucesso!")

    salvarDados('produto.json', produto)
    
def apresentar_produto():
    A_produtos = LerDados()
    

    encontrar = input("Deseja encontrar um produto especifico? (sim/não): ")
   
    if encontrar == 'sim':

        Nome = input("Informe o nome do produto: ")
        encontrado = False

        for produto in A_produtos:      
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
        if not A_produtos:
                print("\nNão há produtos cadastrados.")
        else:
                print("\nProdutos cadastrados:")
        for produto in A_produtos:
            print(f"\nNome: {produto['Nome']}")
            print(f"Valor: {produto['Valor']}")
            print(f"Fornecedor: {produto['Fornecedor']}")
            print(f"Quantidade: {produto['Quantidade']}")
            print(f"Descrição: {produto['Descricao']}")
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
            produto['Descricao'] = input("Informe a nova Descrição: ")


            resposta  = input("\nAtualizar produto? (sim/não) ")
           
            if resposta == 'sim':
                A_produtos[indice] = produto
                with open('produto.json', 'w') as file:
                    json.dump(A_produtos, file)

                print("\nproduto Atualizado!")       
                return
    
    if not(encontrado):
        print("\nproduto não encontrado!")
        return
