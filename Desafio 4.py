#função para o calculo do custo das empresas 
def escolhe_taxi(tf1,vqr1,tf2,vqr2):
    tf1 = float(tf1)
    vqr1 = float(vqr1)
    tf2 = float(tf2)
    vqr2 = float(vqr2)

    # verificações para as possibilidades dos valores tf1, tf2, vqr1, vqr2
    if tf1 == tf2 and vqr1 == vqr2:
        return("Tanto faz")
    elif vqr1 == vqr2:
        if tf1 < tf2:
            return "Empresa 1"
        elif tf1 > tf2:
            return "Empresa 2"
    elif tf1 > tf2 and vqr1 > vqr2:
        return "Empresa 2"
    elif tf2 > tf1 and vqr2 > vqr2:
        return "Empresa 1"
    else:
        #o Km em que uma empresa passa a ficar mais cara que a outra
        pontoDeVirada =  ((tf2 - tf1) / (vqr1 - vqr2))
        
        if pontoDeVirada < 0:
            if vqr1 < vqr2:
                return "Empresa 1"
            else:
                return "Empresa 2"
        else:
            val1 = tf1 + (vqr1 * 0.0)
            val2 = tf2 + (vqr2 * 0.0)
            
            if val1 < val2:
                menorVal = "Empresa 1"
            elif val2 < val1:
                menorVal = "Empresa 2"
            #verificação para saber se o Km é um numero redondo como exemplo 10, 20, 30, 40, etc ou um numero como: 7, 6, 34, 14, etc
            if pontoDeVirada % 10 == 0:
                if menorVal == "Empresa 1":
                    return(f"Empresa 1 quando a distância < {pontoDeVirada:.1f}, Tanto faz quando a distância = {pontoDeVirada:.1f}, Empresa 2 quando a distância > {pontoDeVirada:.1f}")
                else:
                    return(f"Empresa 2 quando a distância < {pontoDeVirada:.1f}, Tanto faz quando a distância = {pontoDeVirada:.1f}, Empresa 1 quando a distância > {pontoDeVirada:.1f}")
            else:
                if menorVal == "Empresa 1":
                    return(f"Empresa 1 quando a distância < {pontoDeVirada:.2f}, Tanto faz quando a distância = {pontoDeVirada:.2f}, Empresa 2 quando a distância > {pontoDeVirada:.2f}")
                else:
                    return(f"Empresa 2 quando a distância < {pontoDeVirada:.2f}, Tanto faz quando a distância = {pontoDeVirada:.2f}, Empresa 1 quando a distância > {pontoDeVirada:.2f}")


print(escolhe_taxi("2.50", "1.00", "5.00", "0.75"))