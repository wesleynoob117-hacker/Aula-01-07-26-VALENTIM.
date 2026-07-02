#
# Listar funcionários

from database import conectar

def listar_funcionario():
    #Abrir conexao
    conexao=conectar()
    cursor = conexao.cursor()

    # SQL da consulta

    sql = """
    select
        f.id_funcionario,
        f.nome,
        f.cargo,
        s.nome as Setor
    from funcionario f
    join setor s on f.id_setor = s.id_setor
    """

    #EXECUTA SQL
    cursor.execute(sql)

    #RECUPERAR DADOS 
    dados = cursor.fetchall()

    #EXIBIR RESULTADOS 
    for funcionario in dados:
        print(funcionario)

    #FECHAR A CONEXÃO
    cursor.close()
    conexao.close()


def cadastrar_funcionario(nome,cargo,id_setor):

    

    conexao=conectar()
    cursor = conexao.cursor()
    sql ="""
    INSERT INTO funcionario
        (nome, cargo, id_setor)
    values
    (%s,%s,%s)
    """
    valores =(nome, cargo, id_setor)
    cursor.execute(sql,valores)
    conexao.commit()

    print("funcionario ok")

    cursor.close
    conexao.close

