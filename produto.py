class Produto:
    def __init__(self,name,price,quant):
        self.name = name
        self.price = price
        self.quant = quant

    def adicionar_stock(self,quant):
        if quant>0:
            self.quant+=quant
            print(1)
        else:
            print(0)

    def vender(self,quant):
        if quant<= self.quant:
            self.quant-= quant
            print(1)
        else:
            print(0)

    def exibir_info(self):
        print(f"{self.name} {self.price} {self.quant}")

produto1 = Produto("Vaso", 19.99, 100)
produto1.adicionar_stock(-20)
produto1.adicionar_stock(20)
produto1.vender(50)
produto1.vender(100)
produto1.exibir_info()