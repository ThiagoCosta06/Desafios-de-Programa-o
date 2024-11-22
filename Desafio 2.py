#Dicionario com os numeros de 0 - 9
numeros = {
    "0": [
        " _ ",
        "| |",
        "|_|" 
        ],
    "1": [
        "   ",
        "  |",
        "  |"
        ],
    "2": [
        " _ ",
        " _|",
        "|_ "
        ],
    "3": [
        " _ ",
        " _|",
        " _|"
        ],
    "4": [
        "   ",
        "|_|",
        "  |"
        ],
    "5": [
        " _ ",
        "|_ ",
        " _|"
        ],
    "6": [
        " _ ",
        "|_ ",
        "|_|"
        ],
    "7": [
        " _ ", 
        "  |",
        "  |"
        ],
    "8": [
        " _ ",
        "|_|",
        "|_|"
        ],
    "9": [
        " _ ",
        "|_|",
        " _|"
        ],
    ":": [
        "   ",
        " . ",
        " . "
        ],    
}

#função para transformar em display de 7 segmentos
def seven_segmentify(num):
    #lista para guardar os resultados de cada linha da transformação de cada numero no formato de display de 7 segmentos
    hora = [[],[],[]]
    casa = 0
    #for para cada letra da string numero passada
    for letra in num:
        for i in range(3):
            #if para caso a primeira caso seja um 0
            if letra == "0" and casa == 0:
              hora[i].append("   ")
            else:
              hora[i].append(numeros[letra][i])
        casa += 1 
    
    #lista para guardar a união de todas a linhas
    result = []
    for linha in hora:
        result.append("".join(linha))
    #resultado Final
    relogio = "\n".join(result)
    
    return relogio
    
output = seven_segmentify("13:24")
print(output)