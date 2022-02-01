
import datetime


def get_oldest_manufacturing_date(stock):
    fabricacao_mais_antiga = datetime.strptime(
        stock[0]["data_de_fabricacao"], "%Y-%m-%d"
    )
    for item in stock:
        if datetime.date(item["data_de_fabricacao"]) < fabricacao_mais_antiga:
            fabricacao_mais_antiga = datetime.date(
                item["data_de_fabricacao"]
            )
    return fabricacao_mais_antiga


def get_closest_expiration_date(stock):
    validade_mais_proxima = datetime.date(
        stock[0]["data_de_validade"]
    )
    for item in stock:
        if datetime.date(item["data_de_validade"]) > validade_mais_proxima:
            validade_mais_proxima = datetime.date(
                item["data_de_validade"]
            )
    return validade_mais_proxima

def get_company_biggest_stock(stock):
    quantidade_de_produto_por_empresa = {}
    for item in stock:
        if item["nome_da_empresa"] in quantidade_de_produto_por_empresa:
            quantidade_de_produto_por_empresa[item["nome_da_empresa"]] += 1
        else:
            quantidade_de_produto_por_empresa[item["nome_da_empresa"]] = 1
    print(max(quantidade_de_produto_por_empresa, key=quantidade_de_produto_por_empresa.get))
    
    
class SimpleReport:
    def __init__(self):
        self.oldest_manufacturing_date = ''
        self.closest_expiration_date = ''
        self.company_biggest_stock = ''

    @classmethod
    def generate(self, stock):
        self.oldest_manufacturing_date = get_oldest_manufacturing_date(stock)
        self.closest_expiration_date = self.get_closest_expiration_date(stock)
        self.company_biggest_stock = self.get_company_biggest_stock(stock)
        return self.retornar_report()
