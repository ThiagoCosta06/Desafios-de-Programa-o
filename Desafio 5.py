#O grafo da questão passado para dicionario
morse = {
    "": {".": "E", "-": "T", "?": "ET"},
    "E": {".": "I", "-": "A", "?": "IA"},
    "T": {".": "N", "-": "M", "?": "NM"},
    "I": {".": "S", "-": "U", "?": "SU"},
    "A": {".": "R", "-": "W", "?": "RW"},
    "N": {".": "D", "-": "K", "?": "DK"},
    "M": {".": "G", "-": "O", "?": "GO"}
}

#quais as possiveis palavras baseado no estado atual e o acento morse seja ".", "-", "?"
def possibilidades(estadoAtual, word):
    possiveis = morse[estadoAtual][word]
    return possiveis

#função para as transformações de codimo morse para as palavras
def possibilities(word: str) -> list[str]:
    resultado = []
    estadoAtual = ""
    #se o codigo morse tem somente um acento("." ou "-" ou "?")
    if len(word) == 1:
        estadoAtual = possibilidades(estadoAtual, word[0])
        for letra in estadoAtual:
            resultado.append(f"{letra}")
    #se o codigo morse tem dois acentos("..", "-.", ".-", "??", etc)
    if len(word) == 2:
        estadoAtual = possibilidades(estadoAtual, word[0])
        #para descobrir as palavras finais no nivel 2
        for nivel2 in estadoAtual:
            possiveis = possibilidades(nivel2, word[1])  
            for letra in range(len(possiveis)):
              resultado.append(f"{possiveis[letra]}")
    #se o codigo morse tem três acentos("..-", "-.-", "?.?", "???", entre outros)
    if len(word) == 3:
        estadoAtual = possibilidades(estadoAtual, word[0])
        nivel2 = ""
        #para descobrir as possibilidades no nivel 2 do grafo
        for letra in estadoAtual:
            estadoAtual = possibilidades(letra, word[1])
            nivel2 = nivel2 + estadoAtual
        #para descobrir as palavras finais no nivel 3
        for nivel3 in nivel2:
            estadoAtual = possibilidades(nivel3, word[2])
            for fim in estadoAtual:
                resultado.append(f"{fim}")

    return resultado

print(possibilities("?-?"))

#obs: não consegui mudar o nome da função principal(possibilities) nem a da secundaria(possibilidades), em razão disso acabou ficando muito parecido o nome das funções e talvez um pouco confuso, peço perdão porém não consegui alterar o nome das funções sem que alterasse o resultado na hora de fazer a submissão. 