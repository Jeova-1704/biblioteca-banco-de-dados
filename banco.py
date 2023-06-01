# Importando o sqlite
import sqlite3

# Criando uma conexão / um novo banco de dados
connection = sqlite3.connect('livraria.db')

# ================== Criando tabelas ================== #

# Tabela categoria:
with connection:
    cur = connection.cursor()
    cur.execute("CREATE TABLE categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

# Tabela membro:
with connection:
    cur = connection.cursor()
    cur.execute("CREATE TABLE membros(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, genero TEXT, tel TEXT, endereco TEXT)")

# Tabela livro:
with connection:
    cur = connection.cursor()
    cur.execute("CREATE TABLE livros(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT, editora TEXT, categoria INTEGER, copias INTEGER, adicionado_em DATE, FOREIGN KEY(categoria) REFERENCES categoria(id) ON DELETE CASCADE)")

# Tabela livros alugados:
with connection:
    cur = connection.cursor()
    cur.execute("CREATE TABLE livro_alugado(id INTEGER PRIMARY KEY AUTOINCREMENT, id_livro INTEGER, id_membro INTEGER, alugado_em DATE, data_de_retorno DATE, FOREIGN KEY(id_livro) REFERENCES livros(id) ON DELETE CASCADE, FOREIGN KEY(id_membro) REFERENCES membros(id) ON DELETE CASCADE)")
