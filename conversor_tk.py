from tkinter import *
from tkinter import ttk

# Array com os valores hexadecimais, decimais e binários
he = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
dec = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
bina = ['0000','0001','0010','0011','0100','0101','0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

# Função para converter de hexadecimal para decimal
def hexadecimalTodecimal(HexadecimalNumber):
    soma = 0
    for i in range(len(HexadecimalNumber)):
        if HexadecimalNumber[i].upper() in he:
            decima = int(dec[he.index(HexadecimalNumber[i].upper())])
            res = decima*(16**(len(HexadecimalNumber)-1-i))
            soma += res
    return soma

# Função para converter de decimal para hexadecimal
def decimalTohexadecimal(decimalNumber):
    hexa = ""
    sobra = int(decimalNumber)
    while sobra > 16:
        res_inic = sobra
        i = 0
        res = res_inic
        while res//16 > 0:
            i += 1
            res = res/16
        hexa += he[dec.index(int(res))]
        sobra = sobra - (int(res) * 16 ** i)
    hexa += he[dec.index(sobra)]
    return hexa

# Função para converter de hexadecimal para binário
def hexadecimalTobinary(HexadecimalNumber):
    soma = ''
    for i in range(len(HexadecimalNumber)):
        if HexadecimalNumber[i].upper() in he:
            biny = bina[he.index(HexadecimalNumber[i].upper())]
            soma = str(soma) + str(biny)
    for i in soma:
        if i == '1':
            return soma
        soma = soma.replace(i, '', 1)

# Função para converter de binário para decimal
def binaryTodecimal(BinaryNumber):
    soma = 0
    for i in range(len(BinaryNumber)):
        if BinaryNumber[i] == '1':
            res = 2**(len(BinaryNumber)-1-i)
            soma += res
    return soma
    
# Função para exibir mensagem de número inválido
def invalido():
    texto_relatorio1["text"] = ""
    texto_relatorio2["text"] = ""
    texto_relatorio3["text"] = ""
    texto_relatorio4["text"] = "Número inválido!"

# Função para converter o número
def converter():
    model = w.get()
    numero = original.get()
    if model == "DECIMAL":
        if numero.isnumeric():
            texto_relatorio1["text"] = numero
            texto_relatorio2["text"] = decimalTohexadecimal(numero)
            texto_relatorio3["text"] = hexadecimalTobinary(decimalTohexadecimal(numero))
            texto_relatorio4["text"] = ""
        else:
            invalido()

    elif model == "BINÁRIO":
        chave = True
        for i in numero:
            if i != '0' and i != '1':
                invalido()
                break
            elif i == '1':
                chave = False
            elif i == "0" and chave == True:
                numero = numero.replace(i, '', 1)
        else:
            texto_relatorio1["text"] = binaryTodecimal(numero)
            texto_relatorio2["text"] = decimalTohexadecimal(binaryTodecimal(numero))
            texto_relatorio3["text"] = numero
            texto_relatorio4["text"] = ""
    elif model == "HEXADECIMAL":
        for i in numero:
            if i.upper() not in he:
                invalido()
                break
            else:
                texto_relatorio1["text"] = hexadecimalTodecimal(numero)
                texto_relatorio2["text"] = numero
                texto_relatorio3["text"] = hexadecimalTobinary(numero)
                texto_relatorio4["text"] = ""

# Criando a janela principal
def interface():
    global original, w, texto_relatorio1, texto_relatorio2, texto_relatorio3, texto_relatorio4
    janela = Tk()
    janela.title("Conversor de números")

    subtitulo = Label(janela, text="Conversor", font="Arial 20")
    subtitulo.grid(column=0, row=0, pady=10, columnspan = "2")

    choices = ["DECIMAL", "HEXADECIMAL", "BINÁRIO"]
    variable = StringVar(janela)
    variable.set('DECIMAL')
    w = ttk.Combobox(janela, values = choices)
    w.grid(column=0, row=1)
    w.config(width=15, height=3)
    original = Entry(janela, width=30)
    original.grid(column=1, row=1)

    botao_add = Button(janela, text = "Converter", command=converter)
    botao_add.grid(column=0, row=2, pady=10, columnspan = "2")

    texto1 = Label(janela, text="Número em decimal: ")
    texto1.grid(column=0, row=3, pady=10, sticky='w')
    texto2 = Label(janela, text="Número em hexadecimal: ")
    texto2.grid(column=0, row=4, pady=10, sticky='w')
    texto3 = Label(janela, text="Número em binário: ")
    texto3.grid(column=0, row=5, pady=10, sticky='w')

    texto_relatorio1 = Label(janela, text="")
    texto_relatorio1.grid(column=1, row=3, pady=10, sticky='w')
    texto_relatorio2 = Label(janela, text="")
    texto_relatorio2.grid(column=1, row=4, pady=10, sticky='w')
    texto_relatorio3 = Label(janela, text="")
    texto_relatorio3.grid(column=1, row=5, pady=10, sticky='w')

    texto_relatorio4 = Label(janela, text="", font="Arial 20")
    texto_relatorio4.grid(column=0, row=6, pady=10, columnspan= 2)

    janela.mainloop()

# Chamando a função principal
if __name__ == "__main__":
    interface()