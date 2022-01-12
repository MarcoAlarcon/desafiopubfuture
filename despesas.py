from typing import ContextManager
from tratamentoDeDados import tratamento


class conexao:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
    
    def conectar():
        import mysql.connector
        global con
        con = mysql.connector.connect(
        host = "localhost",
        database = "projeto_pubfuture",
        user = "root",
        password = "",
        )


class despesas:

    def __ini__(self, valor, dataPagamento, dataPagamentoEsperado, tipoDespesa, conta):
        self.valor = valor
        self.dataPagamento = dataPagamento
        self.dataPagamentoEsperado = dataPagamentoEsperado
        self.tipoDespesa = tipoDespesa
        self.conta = conta

    def cadastrarDespesa(valor, dataPagamento, detaPagamentoEsperado, tipoDespesa, conta):
        
        from mysql.connector import Error

        dados = valor + ",\'" + dataPagamento + "\'" + ",\'" + detaPagamentoEsperado + "\'" + ",\'" + tipoDespesa + "\'" + ",\'" + conta + "\')"

        declaracao = """insert into despesas
        (valor, dataPagamento, dataPagamentoEsperado, tipoDespesa, conta)
        values ("""

        insertSQL = declaracao + dados

        try:
            conexao.conectar()

            inserir_dados = insertSQL
            cursor = con.cursor()
            cursor.execute(inserir_dados)
            con.commit()
            print(cursor.rowcount, " registro inseridos na tabela.")
            cursor.close()
        except Error as erro:
            print("Falha ao inserir dados no MySQL{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                print("con ao MySql finalizada.")
    
    def mostrarTodasDespesas():
        from mysql.connector import Error

        try:
            conexao.conectar()
        
            consultaSQL = "select * from despesas"
            cursor = con.cursor()
            cursor.execute(consultaSQL)
            linhas = cursor.fetchall()
            print("\n" + str(cursor.rowcount) + " registors retornados.")

            print("\nSuas despesas cadastradas: ")
            
            for linha in linhas:
                print("Id: ", linha [0])
                print("Valor: ", linha [1])
                dataPagamentoTratada = tratamento.tratarDateCliente(linha[2])
                print("Data Pagamento: ", dataPagamentoTratada)
                dataPagamentoEsperadoTratada = tratamento.tratarDateCliente(linha[3])
                print("Data Pagamento Esperado: ", dataPagamentoEsperadoTratada)
                print("Tipo de Despesa: ", linha [4])
                print("Conta: ", linha [5], "\n")
        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def alterarDespesa(alterarID,alterarCampo,alterarInfo):
        from mysql.connector import Error

        try:
            conexao.conectar()

            alterarSQL = "update despesas set " + alterarCampo + " = " + "\'" + alterarInfo + "\'" + " where id_despesa = " + str(alterarID) + ";"
            cursor = con.cursor()
            cursor.execute(alterarSQL)
            con.commit()
            print("Registro alterado com sucesso.")
        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def alterarValorDespesa(alterarID,alterarCampo,alterarInfo):
        from mysql.connector import Error

        try:
            conexao.conectar()

            alterarSQL = "update despesas set " + alterarCampo + " = " + alterarInfo + " where id_despesa = " + str(alterarID) + ";"
            cursor = con.cursor()
            cursor.execute(alterarSQL)
            con.commit()
            print("Registro alterado com sucesso.")
        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def removerDespesa(excluirID):
        from mysql.connector import Error

        try:
            conexao.conectar()

            excluirSQL = "delete from despesas where id_despesa =" + str(excluirID)
            cursor = con.cursor()
            cursor.execute(excluirSQL)
            con.commit()
            print("Registro excluido com sucesso.")
        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def totalDespesas():
        from mysql.connector import Error

        try:
            conexao.conectar()
        
            somaSaldo = "select sum(valor) from despesas"
            cursor = con.cursor()
            cursor.execute(somaSaldo)
            linhas = cursor.fetchall()

            for linha in linhas:
                soma = linha[0]
                round(soma,2)
                print("Soma dos valores das suas despesas: R$" + str(soma))

        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))

        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()
    
    def listarPorData(dataInicial, dataFinal):
        from mysql.connector import Error

        try:
            conexao.conectar()

            consultaData = "SELECT * FROM despesas WHERE dataPagamento BETWEEN " + "\'" + dataInicial + "\'" + " AND " + "\'" + dataFinal + "\'"
            cursor = con.cursor()
            cursor.execute(consultaData)
            linhas = cursor.fetchall()
            print("\n" + str(cursor.rowcount) + " registors retornados.")

            print("\nSuas despesas cadastradas entre " + dataInicial + " e " + dataFinal)
            
            for linha in linhas:
                print("Id: ", linha [0])
                print("Valor: ", linha [1])
                dataPagamentoTratada = tratamento.tratarDateCliente(linha[2])
                print("Data de Pagamento: ", dataPagamentoTratada)
                dataPagamentoEsperadoTratada = tratamento.tratarDateCliente(linha[3])
                print("Data de Pagamento Esperado: ", dataPagamentoEsperadoTratada)
                print("Tipo de despesa: ", linha [4])
                print("Conta: ", linha [5], "\n")
        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def mostrarTipo():
        from mysql.connector import Error

        try:
            conexao.conectar()

            mostrarTipo = "select distinct tipoDespesa from despesas"
            cursor = con.cursor()
            cursor.execute(mostrarTipo)
            linhas = cursor.fetchall()

            print("\nTipos cadastrados:")
            
            for linha in linhas:
                print(linha[0])

        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def listarPorTipo(tipoDespesa):
        from mysql.connector import Error

        try:
            conexao.conectar()

            consultaTipo = "select * from despesas where tipoDespesa = " + "\'" + tipoDespesa + "\'"
            cursor = con.cursor()
            cursor.execute(consultaTipo)
            linhas = cursor.fetchall()
            print("\n" + str(cursor.rowcount) + " registors retornados.")

            print("\nSuas despesas com o tipo: " + tipoDespesa)
            
            for linha in linhas:
                print("Id: ", linha [0])
                print("Valor: ", linha [1])
                dataPagamentoTratada = tratamento.tratarDateCliente(linha[2])
                print("Data de Pagamento: ", dataPagamentoTratada)
                dataPagamentoEsperadoTratada = tratamento.tratarDateCliente(linha[3])
                print("Data de Pagamento Esperado: ", dataPagamentoEsperadoTratada)
                print("Tipo de despesa: ", linha [4])
                print("Conta: ", linha [5], "\n")
        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()