# CalculSistemasNumericos
#Diccionario de Hexadecimal
Hexa = {'a': 10, 10: "a",
        'b': 11, 11: "b",
        'c': 12, 12: "c",
        'd': 13, 13: "d",
        'e': 14, 14: "e",
        'f': 15, 15: "f" }


def Agarre(n, arg):
    arg = str(arg)
    partes = []
    L = len(arg)
    r = int(L/n)
    s = L%n

    if s!=0:
        p = arg[0:s]
        partes.append(p)

    if r!=0:
        for i in range(1, r+1):
            p = arg[s+(n*(i-1)) : s+n*i]
            partes.append(p)

    return partes

def BoBi( numbin ):
    l = len(numbin)
    a = int(l/4) +1
    f = 4*a - l
    ordenado=""

    if l%4 != 0:
        ordenado = f*"0" + numbin
    else:
        ordenado = numbin

    numbin = Agarre(4, ordenado)
    ordenado=""

    for i in numbin:
        ordenado = ordenado + " " + i
    ordenado=ordenado[1:]

    return ordenado


#Convertir de _tipo1_ a _tipo2_, cada uno con sus datos
def Converter(tipo1, dat1, tipo2):
    hexCambio = False

    if tipo1 == tipo2:
        dat2 = dat1
        return dat2

    elif tipo1 == "D":
            # Se hace la división y resto con cada uno de los otros
            if tipo2 == "B":
                div = 2
            elif tipo2 == "O":
                div = 8
            elif tipo2 == "H":
                div = 16
                hexCambio = True

            dat2 = ""
            coci = 1
            dat1 = int(dat1)
            while coci != 0:
                coci = int(dat1/div)
                rest = dat1%div

                if hexCambio:
                    rest = Hexa.get(rest, rest)

                dat2 = str(rest) + dat2
                dat1 = coci
            return dat2


    elif tipo2 == "D":
        #Para todas las transformaciones HACIA decimal, se hace una conversion simple con exponentes

        if tipo1 == "B":
            base = 2
        elif tipo1 == "O":
            base = 8
        elif tipo1 == "H":
            base = 16
            hexCambio = True
        dat1 = str(dat1)
        l = len(dat1)
        dat2 = 0

        for i in range(l):
            if hexCambio:
                cambio = Hexa.get(str(dat1[l-1-i]),dat1[l-1-i])
                cambio = int(cambio)
                dat2 = dat2 + (cambio)*(base**i)
            else:    
                dat2 = dat2 + int(dat1[l-1-i])*(base**i)
        dat2 = str(dat2)
        return dat2


    elif tipo1 == "B":
        if tipo2 == "O":
            Ag_n = 3
        elif tipo2 == "H":
            Ag_n = 4
            hexCambio = True
        dat1 = Agarre(Ag_n, dat1)
        dat2 = ""
        for i in dat1:
            cambio = str(Converter("B", i, "D"))
            if hexCambio:
                cambio = Hexa.get(int(cambio),cambio)
            dat2 = dat2 + cambio
        return dat2


    elif tipo2 == "B":
        if tipo1 == "H":
            hexCambio = True
        dat2 = ""
        for i in range( 0, len(dat1) ):
            cambio = dat1[i]
            if hexCambio:
                cambio = Hexa.get(cambio, cambio)
            cambio = Converter("D", cambio, "B")
            dat2 = dat2 + cambio
        return dat2


    elif tipo1 == "O" or tipo1 == "H":
        if tipo2 == "H":
            hexCambio = True
        dat2 = Converter(tipo1, dat1, "B")
        dat2 = Converter("B", dat2, tipo2)
        return dat2

if __name__ == "__main__":
    tipo1 = input()
    dat1 = input()
    tipo2 = input()

    dat2 = Converter(tipo1, dat1, tipo2)
    print(dat2)
