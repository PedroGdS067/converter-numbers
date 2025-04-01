from customtkinter import *

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
    texto_relatorio1.configure(text="")
    texto_relatorio2.configure(text="")
    texto_relatorio3.configure(text="")
    texto_relatorio4.configure(text="Número inválido!")
    
# Função para converter o número
def converter():
    model = w.get()
    numero = original.get()
    if model == "DECIMAL":
        try:
            numero = int(numero)
            texto_relatorio1.configure(text=numero)
            texto_relatorio2.configure(text=decimalTohexadecimal(numero))
            texto_relatorio3.configure(text=hexadecimalTobinary(decimalTohexadecimal(numero)))
            texto_relatorio4.configure(text="")
        except:
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
            texto_relatorio1.configure(text=binaryTodecimal(numero))
            texto_relatorio2.configure(text=decimalTohexadecimal(binaryTodecimal(numero)))
            texto_relatorio3.configure(text=numero)
            texto_relatorio4.configure(text="")
    elif model == "HEXADECIMAL":
        for i in numero:
            if i.upper() not in he:
                invalido()
                break
            else:
                texto_relatorio1.configure(text=hexadecimalTodecimal(numero))
                texto_relatorio2.configure(text=numero)
                texto_relatorio3.configure(text=hexadecimalTobinary(numero))
                texto_relatorio4.configure(text="")

# Função para alterar a interface
def troca_cor():
    set_appearance_mode(w2.get())
    
# Criando a janela principal
def interface():
    color1="#4158D0"
    color2="#171717"
    global original, w, texto_relatorio1, texto_relatorio2, texto_relatorio3, texto_relatorio4, w2
    janela = CTk()
    janela.geometry("600x300")

    set_appearance_mode("dark")

    janela.title("Conversor de números")

    variable = StringVar(janela)
    variable.set('DECIMAL')
    w = CTkComboBox(janela, values = ["DECIMAL", "HEXADECIMAL", "BINÁRIO"])
    w.place(relx=0.05, rely=0.2, anchor="w")
    original = CTkEntry(janela, placeholder_text="Digite o número aqui", width=200, font=("Arial", 20))
    original.place(relx=0.5, rely=0.2, anchor="center")

    variable2 = StringVar(janela)
    variable2.set('DECIMAL')
    w2 = CTkComboBox(janela, values = ["dark", "light" ])
    w2.place(relx=0.05, rely=0.9, anchor="w")
    botao_troca_cor = CTkButton(janela, text="Trocar", corner_radius=32, hover_color=color2, 
                          border_color=color1, border_width=2, command=troca_cor)
    botao_troca_cor.place(relx=0.55, rely=0.9, anchor="e")

    botao_conversor = CTkButton(janela, text="Converter", corner_radius=32, hover_color=color2, 
                          border_color=color1, border_width=2, command=converter)
    botao_conversor.place(relx=0.95, rely=0.2, anchor="e")

    texto1 = CTkLabel(janela, text="Número em decimal: ", font=("Arial", 20))
    texto1.place(relx=0.05, rely=0.5, anchor="w")
    texto2 = CTkLabel(janela, text="Número em hexadecimal: ", font=("Arial", 20))
    texto2.place(relx=0.05, rely=0.6, anchor="w")
    texto3 = CTkLabel(janela, text="Número em binário: ", font=("Arial", 20))
    texto3.place(relx=0.05, rely=0.7, anchor="w")
    texto_relatorio1 = CTkLabel(janela, text="", font=("Arial", 20))
    texto_relatorio1.place(relx=0.5, rely=0.5, anchor="w")
    texto_relatorio2 = CTkLabel(janela, text="", font=("Arial", 20))
    texto_relatorio2.place(relx=0.5, rely=0.6, anchor="w")
    texto_relatorio3 = CTkLabel(janela, text="", font=("Arial", 20))
    texto_relatorio3.place(relx=0.5, rely=0.7, anchor="w")
    texto_relatorio4 = CTkLabel(janela, text="", font=("Arial", 20), text_color="red")
    texto_relatorio4.place(relx=0.5, rely=0.8, anchor="center")

    janela.mainloop()

# Iniciando a interface
if __name__ == "__main__":
    interface()