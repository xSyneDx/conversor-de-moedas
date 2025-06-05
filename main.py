from interface import ConversorMoedasApp
from conversor import lista_moedas

if __name__ == "__main__":
    app = ConversorMoedasApp(lista_moedas)
    app.mainloop()


