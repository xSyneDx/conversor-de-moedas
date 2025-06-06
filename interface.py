import customtkinter as ctk
from conversor import ConversorMoedas

class ConversorMoedasApp(ctk.CTk):

    def __init__(self, lista_moedas):
        super().__init__()
        self.title("Conversor de Moedas")
        self.geometry("400x350")
        self.conversor = ConversorMoedas()

        self.title_label = None
        self.result_label = None
        self.botao_converter = None
        self.combo_para = None
        self.combo_de = None
        self.entrada_valor = None

        self.lista_moedas = lista_moedas
        self.criar_widgets()

    def criar_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="Meu Incrível Conversor", font=("Arial", 20))
        self.title_label.pack(pady=15)

        self.entrada_valor = ctk.CTkEntry(self, placeholder_text="Valor", width=200)
        self.entrada_valor.pack(pady=15)

        self.combo_de = ctk.CTkComboBox(self, values=self.lista_moedas, width=200)
        self.combo_de.pack(pady=10)
        self.combo_de.set("USD")

        self.combo_para = ctk.CTkComboBox(self, values=self.lista_moedas, width=200)
        self.combo_para.pack(pady=10)
        self.combo_para.set("BRL")

        self.botao_converter = ctk.CTkButton(self, text="Converter", command=self.converter, width=200)
        self.botao_converter.pack(pady=15)

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack()

    def converter(self):
        try:
            valor_str = self.entrada_valor.get().replace(",",".")
            valor = float(valor_str)
            moeda_base = self.combo_de.get()
            moeda_final = self.combo_para.get()

            resultado = self.conversor.converter_moeda(valor, moeda_base, moeda_final)
            self.result_label.configure(text=resultado)
        except ValueError:
            self.result_label.configure(text="Insira um valor válido")