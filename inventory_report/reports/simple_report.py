from datetime import datetime


def string_to_datetime(date, format):
    return datetime.strptime(date, format)


def get_oldest_manufacturing_date(stock):
    format = "%Y-%m-%d"

    fabricacao_mais_antiga = string_to_datetime(
        stock[0]["data_de_fabricacao"],
        format
    )

    for item in stock:
        if string_to_datetime(item["data_de_fabricacao"], format) < fabricacao_mais_antiga:  # noqa: E501
            print()
            fabricacao_mais_antiga = string_to_datetime(
                item["data_de_fabricacao"],
                format
            )

    return fabricacao_mais_antiga.strftime(format)


def get_closest_expiration_date(stock):
    format = "%Y-%m-%d"
    today = datetime.today()
    data_de_validade_mais_proxima = string_to_datetime(
        stock[0]["data_de_validade"],
        format
    )
    for item in stock:
        if string_to_datetime(item["data_de_validade"], format) > today:
            if string_to_datetime(item["data_de_validade"], format) < data_de_validade_mais_proxima:  # noqa: E501
                data_de_validade_mais_proxima = string_to_datetime(
                    item["data_de_validade"], format
                )
    return data_de_validade_mais_proxima.strftime(format)


def get_company_biggest_stock(stock):
    quantidade_de_produto_por_empresa = {}
    for item in stock:
        if item["nome_da_empresa"] in quantidade_de_produto_por_empresa:
            quantidade_de_produto_por_empresa[item["nome_da_empresa"]] += 1
        else:
            quantidade_de_produto_por_empresa[item["nome_da_empresa"]] = 1
    return max(
        quantidade_de_produto_por_empresa,
        key=quantidade_de_produto_por_empresa.get
    )


def retornar_report(oldest_date, closest_date, company_name):
    return (
        f"Data de fabricação mais antiga: {oldest_date}\n"
        f"Data de validade mais próxima: {closest_date}\n"
        "Empresa com maior quantidade de produtos "
        f"estocados: {company_name}\n"
    )


class SimpleReport:
    def __init__(self):
        self.oldest_manufacturing_date = ''
        self.closest_expiration_date = ''
        self.company_biggest_stock = ''

    @classmethod
    def generate(self, stock):
        self.oldest_manufacturing_date = get_oldest_manufacturing_date(stock)
        self.closest_expiration_date = get_closest_expiration_date(stock)
        self.company_biggest_stock = get_company_biggest_stock(stock)
        return retornar_report(
            self.oldest_manufacturing_date,
            self.closest_expiration_date,
            self.company_biggest_stock
        )
