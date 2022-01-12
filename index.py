from logging import info
from receitas import receitas
from despesas import despesas
from contas import contas
from tratamentoDeDados import tratamento


print("\nOlá! Boas vindas ao seu assistente de finanças.")
fim = 1

while fim == 1:

    print("\nInforme a ação desejada:\n1 - Receitas\n2 - Despesas\n3 - Contas")
    seletor = int(input("Digite o número desejado: "))

    if seletor == 1:
        print("\nMenu de Receitas: ")
        print("1 - Cadastrar receita\n2 - Editar receita\n3 - Remover receita\n4 - Listar receitas")
        seletor = int(input("Digite o número desejado: "))
        if seletor == 1:
            valor = input("\nInforme o valor: ")
            dataRecebimento = input("Informe a data do recebimento no formato dd/mm/aaaa: ")
            dataRecebimentoEsperado = input("Informe a data do recebimento esperado no formato dd/mm/aaaa: ")
            descricao = input("Informe uma descrição para a receita: ")
            tipoReceita = input("Informe o tipo de receita.(Ex: Salário, Prêmio, Extra, etc): ")
            conta = input("Informe em qual conta deseja lançar essa receita: ")

            dataRecebimentoTratada = tratamento.tratarDateSQL(dataRecebimento)
            dataRecebimentoEsperadoTratada = tratamento.tratarDateSQL(dataRecebimentoEsperado)
            
            receitas.cadastrarReceita(valor, dataRecebimentoTratada, dataRecebimentoEsperadoTratada, descricao, conta, tipoReceita)

        elif seletor == 2:
            receitas.mostrarTodasReceitas()

            alterarID = int(input("Informe qual o ID da receita que deseja alterar: "))
            alterarCampo = int(input("\nAgora nos informe qual informação deseja alterar:\n1 - Valor\n2 - Data Recebimento\n3 - Data Recebimento Esperado\n4 - Descricao\n5 - Conta\n6 - Tipo de receita\nDigite a opção desejada: "))
            if alterarCampo == 1:
                alterarCampo = "valor"
                alterarInfo = float(input("Informe a nova informação para o campo desejado: "))

                receitas.alterarReceita(alterarID, alterarCampo, alterarInfo)
            elif alterarCampo == 2:
                alterarCampo = "dataRecebimento"
                alterarInfo = input("Informe a data do recebimento no formato dd/mm/aaaa: ")
                infoTratada = tratamento.tratarDateSQL(alterarInfo)

                receitas.alterarReceita(alterarID, alterarCampo, infoTratada)
            elif alterarCampo == 3:
                alterarCampo = "dataRecebimentoEsperado"
                alterarInfo = input("Informe a data do recebimento no formato dd/mm/aaaa: ")
                infoTratada = tratamento.tratarDateSQL(alterarInfo)

                receitas.alterarReceita(alterarID, alterarCampo, infoTratada)
            elif alterarCampo == 4:
                alterarCampo = "descricao"
                alterarInfo = input("Informe a nova informação para o campo desejado: ")
                receitas.alterarReceita(alterarID, alterarCampo, alterarInfo)
            elif alterarCampo == 5:
                alterarCampo = "conta"
                alterarInfo = input("Informe a nova informação para o campo desejado: ")
                receitas.alterarReceita(alterarID, alterarCampo, alterarInfo)
            elif alterarCampo == 6:
                alterarCampo = "tipoReceita"
                alterarInfo = input("Informe a nova informação para o campo desejado: ")
                receitas.alterarReceita(alterarID, alterarCampo, alterarInfo)
                
        elif seletor == 3:
            receitas.mostrarTodasReceitas()

            excluirID = input("Informe qual o ID da receita que deseja excluir: ")
            
            receitas.removerReceita(excluirID)

        elif seletor == 4:
            tipoFiltro = int(input("\nComo gostaria de listar as receitas:\n1 - Por periodo\n2 - Por tipo de receita\n3 - Listar total de receitas registradas\nDigite a opção desejada:"))
            if tipoFiltro == 1:
                dataInicio = input("\nInforme a data incio no formato dd/mm/aaaa: ")
                dataFinal = input("Informe a data final no formato dd/mm/aaaa: ")

                dataInicioTratada = tratamento.tratarDateSQL(dataInicio)
                dataFinalTratada = tratamento.tratarDateSQL(dataFinal)

                receitas.listarPorData(dataInicioTratada, dataFinalTratada)

            elif tipoFiltro == 2:
                receitas.mostrarTipo()

                tipoSelecionado = input("Informe qual tipo gostaria de listar: ")
                
                receitas.listarPorTipo(tipoSelecionado)

            elif tipoFiltro == 3:
                receitas.mostrarTodasReceitas()
                receitas.totalReceitas()
                
    elif seletor == 2:
        print("\nMenu de Despesas: ")
        print("1 - Cadastrar despesa\n2 - Editar despesa\n3 - Remover despesa\n4 - Listar despesas")
        seletor = int(input("Digite o número desejado: "))
        if seletor == 1:
            valor = input("\nInforme o valor: ")
            dataPagamento = input("Informe a data do pagamento no formato dd/mm/aaaa: ")
            dataPagamentoEsperado = input("Informe a data do pagamento esperado no formato dd/mm/aaaa: ")
            tipoDespesa = input("Informe o tipo de despesa.(Ex: Mercado, Contas, Imprevisto, etc): ")
            conta = input("Informe em qual conta deseja lançar essa despesa: ")

            dataPagamentoTratada = tratamento.tratarDateSQL(dataPagamento)
            dataPagamentoEsperadoTratada = tratamento.tratarDateSQL(dataPagamentoEsperado)
            
            despesas.cadastrarDespesa(valor, dataPagamentoTratada, dataPagamentoEsperadoTratada, tipoDespesa,conta)

        elif seletor == 2:

            despesas.mostrarTodasDespesas()

            alterarID = int(input("\nInforme qual o ID da despesa que deseja alterar: "))
            alterarCampo = int(input("\nAgora nos informe qual informação deseja alterar:\n1 - Valor\n2 - Data de pagamento\n3 - Data pagamento esperado\n4 - Tipo de despesa\n5 - Conta\nDigite a opção desejada: "))
            if alterarCampo == 1:
                alterarCampo = "valor"
                alterarInfo = input("\nInforme a nova informação para o campo desejado: ")

                despesas.alterarValorDespesa(alterarID, alterarCampo, alterarInfo)

            elif alterarCampo == 2:
                alterarCampo = "dataPagamento"
                alterarInfo = input("\nInforme a data do recebimento no formato dd/mm/aaaa: ")
                infoTratada = tratamento.tratarDateSQL(alterarInfo)

                despesas.alterarDespesa(alterarID, alterarCampo, infoTratada)

            elif alterarCampo == 3:
                alterarCampo = "dataPagamentoEsperado"
                alterarInfo = input("\nInforme a nova informação para o campo desejado: ")
                infoTratada = tratamento.tratarDateSQL(alterarInfo)

                despesas.alterarDespesa(alterarID, alterarCampo, infoTratada)

            elif alterarCampo == 4:
                alterarCampo = "tipoDespesa"
                alterarInfo = input("\nInforme a nova informação para o campo desejado: ")

                despesas.alterarDespesa(alterarID,alterarCampo,alterarInfo)

            elif alterarCampo == 5:
                alterarCampo = "conta"
                alterarInfo = input("\nInforme a nova informação para o campo desejado: ")
                
                despesas.alterarDespesa(alterarID, alterarCampo, alterarInfo)

        elif seletor == 3:

            despesas.mostrarTodasDespesas()

            excluirID = int(input("Informe qual o ID da receita que deseja excluir: "))

            despesas.removerDespesa(excluirID)

        elif seletor == 4:
            tipoFiltro = int(input("\nComo gostaria de listar as despesas:\n1 - Por periodo\n2 - Por tipo de despesa\n3 - Listar total de despesas registradas\nDigite a opção desejada:"))
            if tipoFiltro == 1:
                dataInicio = input("\nInforme a data incio no formato dd/mm/aaaa: ")
                dataFinal = input("Informe a data final no formato dd/mm/aaaa: ")

                dataInicioTratada = tratamento.tratarDateSQL(dataInicio)
                dataFinalTratada = tratamento.tratarDateSQL(dataFinal)

                despesas.listarPorData(dataInicioTratada, dataFinalTratada)

            elif tipoFiltro == 2:
                despesas.mostrarTipo()

                tipoSelecionado = input("Informe qual tipo gostaria de listar: ")

                despesas.listarPorTipo(tipoSelecionado)

            elif tipoFiltro == 3:
                despesas.mostrarTodasDespesas()
                despesas.totalDespesas()

    elif seletor == 3:
        print("\nMenu de Contas: ")
        print("1 - Cadastrar conta\n2 - Editar conta\n3 - Remover conta\n4 - Listar contas\n5 - Transferir saldo entre contas")
        seletor = int(input("Digite a opção desejado: "))
        if seletor == 1:
            saldo = input("Informe o saldo da conta: ")
            tipoConta = input("Informe o tipo da conta.(Ex: crédito, débito, poupança, etc): ")
            instituicaoFinanceira = input("Informe a instituição financeira: ")
            
            contas.cadastrarConta(saldo, tipoConta, instituicaoFinanceira)

        elif seletor == 2:
            contas.mostrarTodasContas()

            alterarID = int(input("\nInforme qual o ID da conta que deseja alterar: "))
            alterarCampo = int(input("\nAgora nos informe qual informação deseja alterar:\n1 - Saldo\n2 - Tipo de conta\n3 - Instituição financeira\nDigite a opção desejada: "))
            if alterarCampo == 1:
                alterarCampo = "saldo"
                alterarInfo = float(input("Informe a nova informação para o campo desejado: "))

                contas.alterarValorContas(alterarID, alterarCampo, alterarInfo)
            elif alterarCampo == 2:
                alterarCampo = "tipoConta"
                alterarInfo = input("Informe a nova informação para o campo desejado: ")

                contas.alterarConta(alterarID, alterarCampo, alterarInfo)
            elif alterarCampo == 3:
                alterarCampo = "instituicaoFinanceira"
                alterarInfo = input("Informe a nova informação para o campo desejado: ")

                contas.alterarConta(alterarID, alterarCampo, alterarInfo)

        elif seletor == 3:
            contas.mostrarTodasContas()

            excluirID = int(input("Informe qual o ID da conta que deseja remover: "))

            contas.removerConta(excluirID)

        elif seletor == 4:
            tipoFiltro = int(input("\nComo gostaria de listar as despesas:\n1 - Por instituição financeira\n2 - Listar todas as informações\nDigite a opção desejada: "))
            if tipoFiltro == 1:
                contas.mostrarInstituicao()
                
                instituicaoFinanceira = input("\nInforme qual instituição gostaria de listar: ")

                contas.listarPorInstituicao(instituicaoFinanceira)

            elif tipoFiltro == 2:
                contas.mostrarTodasContas()
                contas.listarTotalSaldo()

        elif seletor == 5:
            contas.mostrarTodasContas()

            idContaOrigem = input("Informe o ID da conta origem: ")
            idContaDestino = input("Informe o ID da conta destino: ")
            valor = input("Agora informe o valor a ser transferido: ")

            contas.transferirSaldo(idContaOrigem, idContaDestino, valor)

    fim = int(input("\nGostaria de voltar ao menu?\n1 - Sim\n2 - Encerrar programa\nDigite a opção desejada: "))