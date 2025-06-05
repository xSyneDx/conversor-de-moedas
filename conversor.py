import requests


lista_moedas = ["USD", "AED", "AFN", "ALL", "AMD", "ANG", "AOA",
                "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT",
                "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
                "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF",
                "CHF", "CLP", "CNY", "COP", "CRC", "CUP", "CVE",
                "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN",
                "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL",
                "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD",
                "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS",
                "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD",
                "JOD", "JPY", "KES", "KGS", "KHR", "KID", "KMF",
                "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR",
                "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD",
                "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK",
                "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK",
                "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP",
                "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB",
                "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD",
                "SHP", "SLE", "SLL", "SOS", "SRD", "SSP", "STN",
                "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP",
                "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX",
                "UYU", "UZS", "VES", "VND", "VUV", "WST", "XAF",
                "XCD", "XCG", "XDR", "XOF", "XPF", "YER", "ZAR",
                "ZMW", "ZWL"]


def formatar_moeda(valor):
    return "{:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")


class ConversorMoedas:
    def converter_moeda(self, valor, moeda_base, moeda_final):
        try:
            grana = float(valor)

            if moeda_base == "" or moeda_final == "":
                return "Selecione as moedas."

            response = requests.get(f"https://open.er-api.com/v6/latest/{moeda_base}")
            dados = response.json()

            if response.status_code == 200 and dados['result'] == 'success':
                if moeda_final in dados['rates']:
                    cotacao = dados['rates'][moeda_final]
                    resultado = grana * cotacao
                    grana_fmt = formatar_moeda(grana)
                    resultado_fmt = formatar_moeda(resultado)
                    return f"{grana_fmt} {moeda_base} = {resultado_fmt} {moeda_final}"
                else:
                    return f"Moeda {moeda_final} não disponível."
            else:
                return "Erro ao consultar API."

        except ValueError:
           return "Insira um valor válido."