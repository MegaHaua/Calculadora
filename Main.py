from Display import Display
from OperacoesElementares import Operações_Elementares
from Interface import Interface
from Derivada import Derivada
from Limite import Limite
from Integral import Integral


calculadora = Display()
calculadora.config_root()
calculadora.config_notebook()
calculadora.config_entrada()

valor_adicionado = Operações_Elementares(calculadora)
derivada = Derivada(calculadora)
limite = Limite(calculadora)
integral = Integral(calculadora)

interface = Interface(calculadora, valor_adicionado, derivada, limite, integral)
interface.config_button()
interface.config_ajuda()
interface.config_historico()

calculadora.root.mainloop()