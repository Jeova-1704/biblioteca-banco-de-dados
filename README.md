# Banco de Dados da Livraria
Este repositório contém o código Python para criar e gerenciar um banco de dados da livraria usando SQLite.

## `Banco.py`
O arquivo `banco.py` contém o código para criar as tabelas do banco de dados da livraria. Ele importa o módulo sqlite3 e estabelece uma conexão com o banco de dados `livraria.db`. Em seguida, são criadas as seguintes tabelas:

<li> categoria: tabela para armazenar informações sobre as categorias dos livros.
<li> membros: tabela para armazenar informações sobre os membros da livraria.
<li>livros: tabela para armazenar informações sobre os livros disponíveis na livraria.
<li> livros_alugados: tabela para armazenar informações sobre os livros alugados pelos membros.
Cada tabela é criada usando o comando `CREATE TABLE` e as colunas relevantes são definidas. Além disso, são estabelecidas relações de chave estrangeira entre as tabelas.

## `Views.py`
O arquivo views.py contém o código para manipular os dados do banco de dados da livraria. Ele também importa o módulo sqlite3 e estabelece uma conexão com o banco de dados `livraria.db`. O código inclui várias operações de inserção, atualização e exclusão de dados do banco de dados, que estão atualmente comentadas.

Além disso, o código também executa uma consulta para recuperar todos os registros da tabela livros e exibe os resultados.

## Licença
O arquivo licensa contém a licença do software. O código está licenciado sob a licença MIT, permitindo o uso, cópia, modificação e distribuição do software, desde que a notificação de direitos autorais seja mantida em todas as cópias e que o software seja fornecido "COMO ESTÁ", sem garantias ou condições de qualquer tipo.

## Observações:
É importante destacar que este é o meu primeiro banco de dados e estou aprendendo a usar o SQLite para gerenciar as informações e treinei atualmente para gerenciar informções de uma livraria. O código fornecido é um exemplo inicial para criar as tabelas e realizar operações básicas no banco de dados.
