from servidor.Operacoes import dividir, somar, subtrair

class Maquina:
    def __init__(self, operation_signal:str, first_value:float, second_value:float):
        self.operation_signal = operation_signal
        self.first_value = first_value
        self.second_value = second_value
     
    def execute(self,operation_signal:str,first_value:float,second_value:float):
        res = operation_signal

        if res =="+":
            s:object = somar.Somar(first_value,second_value)
            res = s.executar(first_value,second_value)
            print("O valor da operação somar é:", res)
            return res
        elif res =="-":
            s:object = subtrair.Subtrair(first_value,second_value)
            res = s.executar(first_value,second_value)
            print("O valor da operação subtrair é:", res)
            return res 
        elif res =="/":
            s:object = dividir.Dividir(first_value,second_value)
            res = s.executar()
            
        if type(res)==str:
            print (res)
        else:
            print("O valor da operação divisão é:",res)
            return res