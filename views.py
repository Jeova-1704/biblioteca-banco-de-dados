# Importando o sqlite
import sqlite3

# Criando uma conexão / um novo banco de dados
connection = sqlite3.connect('livraria.db')
'''
# inserindo dados categoria
with connection:
    cur = connection.cursor()
    cur.execute("INSERT INTO categoria (nome) VALUES('Romance')")
    cur.execute("INSERT INTO categoria (nome) VALUES('Drama')")
    cur.execute("INSERT INTO categoria (nome) VALUES('Aventura')")
    cur.execute("INSERT INTO categoria (nome) VALUES('terror')")
    cur.execute("INSERT INTO categoria (nome) VALUES('Comendia')")
'''

'''
# inserindo dados membros
valores = ['Jose', 'M', '123456789', 'Brasil, Rio de Janeiro']
with connection:
    cur = connection.cursor()
    query = ("INSERT INTO membros (nome, genero, tel, endereco) VALUES(?, ?, ?, ?)")
    cur.execute(query, valores)
'''
'''
# Inserir livros
valores = ['O perdão da Julieta', 'Davince', 'Pt.Editora', 5, 15, '16/07/2021']
with connection:
    cur = connection.cursor()
    query = ("INSERT INTO livros(titulo, autor, editora, categoria, copias, adicionado_em) VALUES(?, ?, ?, ?, ?, ?)")
    cur.execute(query, valores)
'''
# Inserir livros alugados
'''
valores = [1, 1, '17/07/2021', 17/08/2021]
with connection:
    cur = connection.cursor()
    query = "INSERT INTO livro_alugado(id_livro, id_membro, alugado_em) VALUES(?, ?, ?)"
    cur.execute(query, valores)
'''
'''
# Inserir update
valores = ['A traição da Joana', 2, ]
with connection:
    cur = connection.cursor()
    query = "UPDATE livros SET titulo=? where id =?"
    cur.execute(query, valores)
'''

# deletando valores do banco de dados
valores = [ 1 ]
with connection:
    cur = connection.cursor()
    query = "DELETE FROM livros WHERE id=?"
    cur.execute(query, valores)


cur = connection.cursor()
cur.execute("SELECT * FROM livros")
print(cur.fetchall())
