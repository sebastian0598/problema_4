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


    

if __name__ == "__main__":
    main()