from servidor.gestor import maquina

class Interface:
	def __init__(self):
		pass
	def execute(self):
		print("Qual é o cálculo que quer efetuar? x + - /")
		res:str = input()
		print("Preciso que introduza dois valores:")
		x:float = float(input("x="))
		y:float = float(input("y="))
		# chamar maquina.py
		_maquina = maquina.Maquina(res,x,y)
		_maquina.execute(res,x,y) ## tem que se usar valor objecot, corrigir
