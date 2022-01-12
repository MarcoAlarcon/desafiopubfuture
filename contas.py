from logging import error

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

class contas:
    def __init__(self, saldo, tipoConta, instituicaoFinanceira):
        self.saldo = saldo
        self.tipoConta = tipoConta
        self.instituicaoFinanceira = instituicaoFinanceira

    def cadastrarConta(saldo, tipoConta, instituicaoFinanceira):
        from mysql.connector import Error
        
        dados = "\'" + saldo + "\'" + ",\'" + tipoConta +"\'"+",\'"+ instituicaoFinanceira + "\')"

        declaracao = """insert into contas
        (saldo, tipoConta, instituicaoFinanceira)
        values ("""

        insertSQL = declaracao + dados

        try:
            conexao.conectar()

            inserir_dados = insertSQL
            cursor = con.cursor()
            cursor.execute(inserir_dados)
            con.commit()
            print(cursor.rowcount, "registro inseridos na tabela.")
            cursor.close()
        except Error as erro:
            print("Falha ao inserir dados no MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                print("Conexão ao MySQL finalizada")

    def mostrarTodasContas():
        from mysql.connector import Error

        try:
            conexao.conectar()
        
            consultaSQL = "select * from contas"
            cursor = con.cursor()
            cursor.execute(consultaSQL)
            linhas = cursor.fetchall()
            print(str(cursor.rowcount) + " registors retornados.")

            print("\nSuas contas cadastradas: ")
            
            for linha in linhas:
                print("Id: ", linha [0])
                print("Saldo: ", linha [1])
                print("Tipo da Conta: ", linha [2])
                print("Instituição financeira: ", linha [3], "\n")
        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def alterarConta(alterarID,alterarCampo,alterarInfo):
        from mysql.connector import Error

        try:
            conexao.conectar()

            alterarSQL = "update contas set " + alterarCampo + " = \'" + alterarInfo +"\'" + " where id_conta = " + str(alterarID)
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

    def alterarValorContas(alterarID,alterarCampo,alterarInfo):
        from mysql.connector import Error

        try:
            conexao.conectar()

            alterarSQL = "update contas set " + alterarCampo + " = " + str(alterarInfo) + " where id_conta = " + str(alterarID) + ";"
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

    def removerConta(excluirID):
        from mysql.connector import Error

        try:
            conexao.conectar()

            excluirSQL = "delete from contas where id_conta =" + str(excluirID)
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

    def listarTotalSaldo():
        from mysql.connector import Error

        try:
            conexao.conectar()
        
            somaSaldo = "select sum(saldo) from contas"
            cursor = con.cursor()
            cursor.execute(somaSaldo)
            linhas = cursor.fetchall()

            for linha in linhas:
                soma = linha[0]
                round(soma,2)
                print("Soma dos saldos das contas: R$" + str(soma))

        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))

        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def transferirSaldo(idContaOrigem,idContaDestino,valor):
        from mysql.connector import Error

        try:
            conexao.conectar()
        
            updateSQL1 = "update contas set saldo = (saldo -" + valor +") where id_conta = " + idContaOrigem
            updateSQL2 = "update contas set saldo = (saldo +" + valor +") where id_conta = " + idContaDestino
            cursor1 = con.cursor()
            cursor2 = con.cursor()
            cursor1.execute(updateSQL1)
            cursor2.execute(updateSQL2)
            con.commit()

            print("Valores transferidos com sucesso.")

        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))

        finally:
            if(con.is_connected()):
                con.close()
                cursor1.close()
                cursor2.close()

    def mostrarInstituicao():
        from mysql.connector import Error

        try:
            conexao.conectar()
        
            consultaSQL = "select distinct instituicaoFinanceira from contas"
            cursor = con.cursor()
            cursor.execute(consultaSQL)
            linhas = cursor.fetchall()
            print(str(cursor.rowcount) + " registors retornados.")

            print("\nInstituições cadastrados:")
            
            for linha in linhas:
                print(linha[0])

        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def listarPorInstituicao(instituicaoFinanceira):
        from mysql.connector import Error

        try:
            conexao.conectar()

            consultaTipo = "select * from contas where instituicaoFinanceira = " + "\'" + instituicaoFinanceira + "\'"
            cursor = con.cursor()
            cursor.execute(consultaTipo)
            linhas = cursor.fetchall()
            print("\n" + str(cursor.rowcount) + " registors retornados.")

            print("\nSuas contas na instituicao : " + instituicaoFinanceira)
            
            for linha in linhas:
                print("Id: ", linha [0])
                print("Instituicao: ", linha [1])
                print("Tipo de Conta: ", linha [2])
                print("Saldo: ", linha [3], "\n")
                
        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()
