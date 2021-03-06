from inventory_report.reports.simple_report import SimpleReport


def get_details_report(stock):
    produtos_por_empresa = {}
    for item in stock:
        if item["nome_da_empresa"] in produtos_por_empresa:
            produtos_por_empresa[item["nome_da_empresa"]] += 1
        else:
            produtos_por_empresa[item["nome_da_empresa"]] = 1

    details = ''

    for key, value in produtos_por_empresa.items():
        details += (f"- {key}: {value}\n")

    return (
        "Produtos estocados por empresa: \n"
        f"{details}"
        ""
    )


def format_complete_report(simple_report, details_report):
    return (
        f"{simple_report}\n"
        f"{details_report}"
    )


class CompleteReport:
    def __init__(self):
        self.simple_report = ''
        self.details_report = ''
        self.complete_report = ''

    @classmethod
    def generate(self, stock):
        self.simple_report = SimpleReport.generate(stock)
        self.details_report = get_details_report(stock)
        self.complete_report = format_complete_report(self.simple_report, self.details_report)  # noqa: E501
        return self.complete_report
