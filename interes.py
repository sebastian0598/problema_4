class caja_ahorro(cuenta):
    def __init__(self):
        super().__init__()
            
    def mostrar_caja(self):
        super().imprimir()
    
def main():

   
    caja1 =caja_ahorro()
    caja1.mostrar_caja()


    

if __name__ == "__main__":
