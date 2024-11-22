#função para calculo total de leds
def calcula_total_leds(altura, largura):
  if altura and largura != 0:
    numLeds = (altura + 1)*(largura + 1)
    return numLeds
  else:
    return 0
  
altura = 2
largura = 4
  
print(f"Numero de total de leds é: {calcula_total_leds(altura, largura)}")