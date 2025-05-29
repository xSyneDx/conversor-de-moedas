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


def consultar_moeda(moeda_um, moeda_dois):
    moedas_disponiveis = " ".join(lista_moedas)

    if moeda_um not in lista_moedas:
        return f"Moeda '{moeda_um}' não encontrada. Moedas disponíveis: {moedas_disponiveis}"

    if moeda_dois not in lista_moedas:
        return f"Moeda '{moeda_dois}' não encontrada. Moedas disponíveis: {moedas_disponiveis}"

    return True


def converter_moeda(grana, moeda_base, moeda_final):
    response = requests.get(f"https://open.er-api.com/v6/latest/{moeda_base}")
    dados = response.json()

    if response.status_code == 200 and 'result' in dados:
        resultado_verificacao = consultar_moeda(moeda_base, moeda_final)

        if resultado_verificacao is True:
            cotacao = dados['rates'][moeda_final]
            resultado = grana * cotacao
            print(f"\n{grana} {moeda_base} = {resultado:.2f} {moeda_final}")

        else:
            print(resultado_verificacao)

    else:
        print("Erro ao converter moeda.")

if __name__ == "__main__":
    try:
        valor = float(input("Valor a converter: "))
        de = input("De (ex: USD): ").upper()
        para = input("Para (ex: BRL): ").upper()

        converter_moeda(valor, de, para)
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

