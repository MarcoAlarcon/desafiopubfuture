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

class receitas:
    def __init__(self, valor, dataRecebimento, dataRecebimentoEsperado, descricao, conta, tipoReceita):
        self.valor = valor
        self.dataRecebimento = dataRecebimento
        self.dataRecebimentoEsperado = dataRecebimentoEsperado
        self.descricao = descricao
        self.tipoReceita = tipoReceita
        self.conta = conta

    def cadastrarReceita(valor, dataRecebimento, dataRecebimentoEsperado, descricao, conta, tipoReceita):
        from mysql.connector import Error
        
        dados = valor + ",\'" + dataRecebimento +"\'"+",\'"+ dataRecebimentoEsperado + "\'" + ",\'" + descricao + "\'" + ",\'" + conta + "\'," +"\'" + tipoReceita + "\')"

        declaracao = """insert into receitas
        (valor, dataRecebimento, dataRecebimentoEsperado, descricao, conta, tipoReceita)
        values ("""

        insertSQL = declaracao + dados

        try:
            conexao.conectar()

            inserir_dados = insertSQL
            cursor = con.cursor()
            cursor.execute(inserir_dados)
            con.commit()
            print("\n" + str(cursor.rowcount), "registros inseridos na tabela.")
            cursor.close()
        except Error as erro:
            print("Falha ao inserir dados no MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                print("Conexão ao MySQL finalizada\n")

    def mostrarTodasReceitas():
        from mysql.connector import Error

        try:
            conexao.conectar()
        
            consultaSQL = "select * from receitas"
            cursor = con.cursor()
            cursor.execute(consultaSQL)
            linhas = cursor.fetchall()
            print("\n" + str(cursor.rowcount) + " registors retornados.")

            print("\nSuas receitas cadastradas: ")
            
            for linha in linhas:
                print("Id: ", linha [0])
                print("Valor: ", linha [1])
                dataRecebimentoTratada = tratamento.tratarDateCliente(linha[2])
                print("Data Recebimento: ", dataRecebimentoTratada)
                dataRecebimentoEsperadoTratada = tratamento.tratarDateCliente(linha[3])
                print("Data Recebimento Esperado: ", dataRecebimentoEsperadoTratada)
                print("Descrição: ", linha [4])
                print("Conta: ", linha [5])
                print("Tipo de Receita: ", linha [6], "\n")
        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def alterarReceita(alterarID,alterarCampo,alterarInfo):
        from mysql.connector import Error

        try:
            conexao.conectar()

            alterarSQL = "update receitas set " + alterarCampo + " = " + "\'" + str(alterarInfo) + "\'" + " where id_receita = " + str(alterarID) + ";"
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

    def removerReceita(excluirID):
        from mysql.connector import Error

        try:
            conexao.conectar()

            excluirSQL = "delete from receitas where id_receita = " + excluirID
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

    def listarPorData(dataInicial, dataFinal):
        from mysql.connector import Error

        try:
            conexao.conectar()

            consultaData = "SELECT * FROM receitas WHERE dataRecebimento BETWEEN " + "\'" + dataInicial + "\'" + " AND " + "\'" + dataFinal + "\'"
            cursor = con.cursor()
            cursor.execute(consultaData)
            linhas = cursor.fetchall()
            print("\n" + str(cursor.rowcount) + " registors retornados.")

            print("\nSuas receitas cadastradas entre " + dataInicial + " e " + dataFinal)
            
            for linha in linhas:
                print("Id: ", linha [0])
                print("Valor: ", linha [1])
                dataRecebimentoTratada = tratamento.tratarDateCliente(linha[2])
                print("Data de Recebimento: ", dataRecebimentoTratada)
                dataRecebimentoEsperadoTratada = tratamento.tratarDateCliente(linha[3])
                print("Data de Recebimento Esperado: ", dataRecebimentoEsperadoTratada)
                print("Descrição: ", linha [4])
                print("Conta: ", linha [5])
                print("Tipo de Receita: ", linha [6], "\n")
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

            mostrarTipo = "select distinct tipoReceita from receitas"
            cursor = con.cursor()
            cursor.execute(mostrarTipo)
            linhas = cursor.fetchall()

            print("\nTipos cadastrados: ")
            
            for linha in linhas:
                print(linha[0])

        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def listarPorTipo(tipoReceita):
        from mysql.connector import Error

        try:
            conexao.conectar()

            consultaTipo = "select * from receitas where tipoReceita = " + "\'" + tipoReceita + "\'"
            cursor = con.cursor()
            cursor.execute(consultaTipo)
            linhas = cursor.fetchall()
            print("\n" + str(cursor.rowcount) + " registors retornados.")

            print("\nSuas receitas com o tipo: " + tipoReceita)
            
            for linha in linhas:
                print("Id: ", linha [0])
                print("Valor: ", linha [1])
                dataRecebimentoTratada = tratamento.tratarDateCliente(linha[2])
                print("Data de Recebimento: ", dataRecebimentoTratada)
                dataRecebimentoEsperadoTratada = tratamento.tratarDateCliente(linha[3])
                print("Data de Recebimento Esperado: ", dataRecebimentoEsperadoTratada)
                print("Descrição: ", linha [4])
                print("Conta: ", linha [5])
                print("Tipo de Receita: ", linha [6], "\n")
        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()

    def totalReceitas():
        from mysql.connector import Error

        try:
            conexao.conectar()
        
            somaSaldo = "select sum(valor) from receitas"
            cursor = con.cursor()
            cursor.execute(somaSaldo)
            linhas = cursor.fetchall()

            for linha in linhas:
                soma = linha[0]
                round(soma,2)
                print("Soma dos valores das receitas: R$" + str(soma) + "\n")
            
        except Error as erro:
            print("Erro ao acessar tabela MySQL:{}".format(erro))
        finally:
            if(con.is_connected()):
                con.close()
                cursor.close()