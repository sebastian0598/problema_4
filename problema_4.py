class cuenta:
    def __init__(self):
        self.titular="sebas"
        self.cantidad= 2500000

    def imprimir(self):
        print(f"Titular : {self.titular}")
        print(f"Cantidad : {self.cantidad}")

class caja_ahorro(cuenta):
    def __init__(self):
        super().__init__()
            
    def mostrar_caja(self):
        super().imprimir()


class plazo_fijo(cuenta):
    def __init__(self):
        super().__init__()
        self.plazo ="tres meses"
        self.interes = 0.2
        
    
    def im_interes(self):
        self.importe = (self.cantidad*self.interes)/100
        return self.importe

    def mostrar_datos(self):
        self.intereses = self.im_interes()
        print(" Datos del titular")
        super().imprimir()
        print(f"EL plazo de pago es de {self.plazo}")
        print(f"La cuota de Interes es del {self.interes}")
        print(f"El total de intereses es de: {self.intereses}")

def main():

    interes1 =plazo_fijo()
    interes1.mostrar_datos()
    cuenta1 = cuenta()
    cuenta1.imprimir()
    caja1 =caja_ahorro()
    caja1.mostrar_caja()

    

if __name__ == "__main__":
    main()