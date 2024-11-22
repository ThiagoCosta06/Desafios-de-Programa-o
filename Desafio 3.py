#Função que retorna se a seta encontrada aponta para a ultima coordenada da cobra já encontrada
def pointsAt(signal, lastFound, foundNow):
    if signal == ">" and foundNow[1] + 1 == lastFound[1]:
        return True
    elif signal == "<" and foundNow[1] - 1 == lastFound[1]:
        return True
    elif signal == "^" and foundNow[0] - 1 == lastFound[0]:
        return True
    elif signal == "v" and foundNow[0] + 1 == lastFound[0]:
        return True
    else:
        return False
    

#Função que retorna todos os possiveis caminhos(Cima, Baixo, Esquerda, Direita) com base nas coordenadas da ultima seta("<", ">", "^", "v") encontrada
def Directions(lastFound, lines, columns):
    up, down, left, right = True, True, True, True
    if lastFound[0] == 0:
        up = False
    if lastFound[0] == lines - 1:
        down = False
    if lastFound[1] == 0:
        left = False
    if lastFound[1] == columns -1:
        right = False
    
    return up, down, left, right

#com base nas posiveis direções verifica onde encrontra setas e quando encontrar, verifica se está seta está apontando para a ultima posição da cobra já encontrada anteriormente, se estiver é por que está no caminho correto, além disso faz verificações para se a seta encontrada já foi visitada anteriormente
def LastSignal(up, down, left, right, grid, lastFound, visited):
    if up and grid[lastFound[0]- 1][lastFound[1]] in [">", "<", "^", "v"]:
        signal = grid[lastFound[0]- 1][lastFound[1]]
        foundNow = [lastFound[0]- 1, lastFound[1]]
        if foundNow in visited:
            pass
        else:
            points = pointsAt(signal, lastFound, foundNow)
            if points:
                return True, foundNow
    if down and grid[lastFound[0]+ 1][lastFound[1]] in [">", "<", "^", "v"]:
        signal = grid[lastFound[0]+1][lastFound[1]]
        foundNow = [lastFound[0]+1, lastFound[1]]
        if foundNow in visited:
            pass
        else:
            points = pointsAt(signal, lastFound, foundNow)
            if points:
                return True, foundNow
    if left and grid[lastFound[0]][lastFound[1]-1] in [">", "<", "^", "v"]:
        signal = grid[lastFound[0]][lastFound[1]-1]
        foundNow = [lastFound[0], lastFound[1]-1]
        if foundNow in visited:
            pass
        else:
            points = pointsAt(signal, lastFound, foundNow)
            if points:
                return True, foundNow
    if right and grid[lastFound[0]][lastFound[1]+1] in [">", "<", "^", "v"]:
        signal = grid[lastFound[0]][lastFound[1]+1]
        foundNow = [lastFound[0], lastFound[1]+1]
        if foundNow in visited:
            pass
        else:
            points = pointsAt(signal, lastFound, foundNow)
            if points:
                return True, foundNow
    
    return False, ""

#função principal para encontrar a cobra por completo
def find_snake_on_grid(grid: list[str]) -> list[list[int]]:    
    lines = len(grid)
    columns = len(grid[0])
    snake = []
    lastFound = []
    visited = []
    found = False

    #achando a cabeça da cobra
    for i in range(lines):
        if found:
            break
        for j in range(columns):
            if grid[i][j] == "h":
                lastFound = [i, j]
                snake.append([lastFound[1], lastFound[0]])
                visited.append(lastFound)
                found = True

    #achando o caminho completo da cobra e inscrevendo na lista snake
    while found:
        up, down, left, right = Directions(lastFound, lines, columns)
        found, lastFound = LastSignal(up, down, left, right, grid, lastFound, visited)
        visited.append(lastFound)
        if found:
            snake.append([lastFound[1], lastFound[0]])
        else:
            break
        
    return snake

grid = [
            "v<<",
            "vh<",
            ">>^",
        ]

print(find_snake_on_grid(grid))