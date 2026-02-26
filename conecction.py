import sqlite3 as conector

try:
    #abertura de conexão e aquisição de cursor
    conexao = conector.connect("banco-de-dados.db")
    cursor = conexao.cursor()

    comando = '''CREATE TABLE Pessoa (
                     cpf INTEGER NOT NULL,
                     nome TEXT NOT NULL,
                     nascimento DATE NOT NULL,
                     oculos BOOLEAN NOT NULL,
                     PRIMARY KEY (cpf)
                     );'''
    cursor.execute(comando)

    #efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    #fechamento das conexões
    if conexao:
        conexao.close()
        cursor.close()