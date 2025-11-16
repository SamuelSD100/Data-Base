import sqlite3

def conectar():
    conexao = sqlite3.connect("loja_tecnologia.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
    """)
    conexao.commit()
    return conexao

def adicionar_produto(conexao):
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))
    estoque = int(input("Quantidade em estoque: "))

    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produtos (nome, categoria, preco, estoque) VALUES (?, ?, ?, ?)",
                   (nome, categoria, preco, estoque))
    conexao.commit()
    print(f"\n Produto '{nome}' adicionado com sucesso!\n")

def listar_produtos(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if produtos:
        print("\n Produtos cadastrados:")
        for p in produtos:
            print(f"ID: {p[0]} | Nome: {p[1]} | Categoria: {p[2]} | Preço: R${p[3]:.2f} | Estoque: {p[4]}")
    else:
        print("\n Nenhum produto encontrado.")
    print()

def atualizar_produto(conexao):
    id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
    novo_preco = float(input("Novo preço: "))
    novo_estoque = int(input("Novo estoque: "))

    cursor = conexao.cursor()
    cursor.execute("UPDATE produtos SET preco = ?, estoque = ? WHERE id = ?",
                   (novo_preco, novo_estoque, id_produto))
    conexao.commit()

    if cursor.rowcount > 0:
        print("\n Produto atualizado com sucesso!\n")
    else:
        print("\n Produto não encontrado.\n")

def remover_produto(conexao):
    id_produto = int(input("Digite o ID do produto que deseja remover: "))
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    conexao.commit()

    if cursor.rowcount > 0:
        print("\n Produto removido com sucesso!\n")
    else:
        print("\n Produto não encontrado.\n")

def menu():
    conexao = conectar()
    while True:
        print("""
     -LOJA TEC-
1. Adicionar produto
2. Listar produtos
3. Atualizar produto
4. Remover produto
0. Sair
=======================
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(conexao)
        elif opcao == "2":
            listar_produtos(conexao)
        elif opcao == "3":
            atualizar_produto(conexao)
        elif opcao == "4":
            remover_produto(conexao)
        elif opcao == "0":
            print(" Encerrando o sistema...")
            break
        else:
            print(" Opção inválida. Tente novamente.")

    conexao.close()

if __name__ == "__main__":
    menu()
