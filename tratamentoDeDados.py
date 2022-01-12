class tratamento:
    def __init__(self, valor, data, descricao, conta, tipoReceita):
        self.valor = valor
        self.data = data
        self.descricao = descricao
        self.conta = conta
        self.tipoReceita = tipoReceita

    def tratarDateSQL(data):
        arrData = data.split("/")
        dataTratada = arrData[2] + "-" + arrData[1] + "-" + arrData[0]
        return dataTratada

    def tratarDateCliente(info):
        arrData = str(info).split("-")
        dataTratada = arrData[2] + "/" + arrData[1] + "/" + arrData[0]
        return dataTratada
