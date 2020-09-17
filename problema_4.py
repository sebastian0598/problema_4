class cuenta:
    def __init__(self):
        self.titular="sebas"
        self.cantidad= 2500000

    def imprimir(self):
        print(f"Titular : {self.titular}")
        print(f"Cantidad : {self.cantidad}")

def main():

    
    cuenta1 = cuenta()
    cuenta1.imprimir()

    

if __name__ == "__main__":
    main()