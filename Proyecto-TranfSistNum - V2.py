import tkinter
from CalculSistemasNumericos import Converter, BoBi

# CalculSistemasNumericos
# Diccionario de Hexadecimal

def rotacion(estate):
    if estate=="Binario":
        estate = "Octal"

    elif estate=="Octal":
        estate = "Decimal"

    elif estate=="Decimal":
        estate = "Hexadecimal"

    elif estate=="Hexadecimal":
        estate = "Binario"

    return estate

Letra_pequeña = ("Arial", 12)
Letra_botones = ("Arial", 16, "bold")

FONDO_BOTONES = "#607D80"
COLOR_LABEL = "#080A8A"
FONDO = "#66C6C4"


def prueba():
    print("Sí furufa")


class Calculator:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("500x250")
        self.window.resizable(0,0)
        self.window.title("Transformador Numérico")
        self.window.config(bg=FONDO)

        self.rpta = tkinter.StringVar()
        self.aporte = tkinter.StringVar()
        self.aporte.set("← Elige la base")
        self.rpta.set("Respuesta")

        self.boton1_estate = tkinter.StringVar()
        self.boton2_estate = tkinter.StringVar()
        self.boton1_estate.set("Binario")
        self.boton2_estate.set("Hexadecimal")

        for x in range(1, 5):
            self.window.rowconfigure(x, weight=1)
            self.window.columnconfigure(x, weight=1)

        self.create_tipos_buttons1()
        self.create_tipos_buttons2()

        self.create_entrada_entry()
        self.create_rpta_entry()
   


    #           BOTONES
    def create_tipos_buttons1(self):
        button = tkinter.Button(textvariable=self.boton1_estate, bg="#FFFFFF", height=2, width=10,
        fg=COLOR_LABEL, font=Letra_botones, borderwidth=5, command=Calculator.operacion_aporte)

        button.grid(row=2, column=2)

    def create_tipos_buttons2(self):
        button = tkinter.Button(textvariable=self.boton2_estate, bg="#FFFFFF", height=2, width=10,
        fg=COLOR_LABEL, font=Letra_botones, borderwidth=5, command=Calculator.operacion_rpta)

        button.grid(row=3, column=2)



    #           ENTRADAS
    def create_entrada_entry(self):
        entrada = tkinter.Entry(self.window)
        entrada.config(font=Letra_pequeña, width=20, textvariable=self.aporte, justify="right")

        entrada.grid(row=2, column=3)

    def create_rpta_entry(self):
        rpta = tkinter.Entry(self.window)
        rpta.config( font=Letra_pequeña, width=20, state="readonly", textvariable=self.rpta, justify="right")

        rpta.grid(row=3, column=3)



    #           Operaciones   

    def operacion_aporte():
        calc.boton1_estate.set( rotacion(str(calc.boton1_estate.get())) )
        calc.aporte.set("")
        calc.rpta.set("")

    def operacion_rpta():
        calc.boton2_estate.set( rotacion(str(calc.boton2_estate.get())) )

        tipo1 = calc.boton1_estate.get()
        tipo1 = tipo1[0]
        print(tipo1)

        dat1 = calc.aporte.get()
        print(dat1)

        tipo2 = calc.boton2_estate.get()
        tipo2 = tipo2[0]
        print(tipo2)
        
        dat2=""
        if dat1 != "":
            dat2 = str( Converter(tipo1, dat1, tipo2) )
        if tipo2=="B":
            dat2 = BoBi(dat2)
        print(dat2)
        print ("--------")

        calc.rpta.set(dat2)


    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    calc = Calculator()
    calc.run()
