
def __init__(self):
    self.inicializar()

def inicializar(self):
    self.tableroActual = [['.','.','.'],
                        ['.','.','.'],
                        ['.','.','.']]

    self.turnoHumano = 'X'

def printTablero(self):
    for i in range(0, 3):
        for j in range(0, 3):
            print('{}|'.format(self.tableroActual[i][j]), end=" ")
        print()
    print()

def validar(self, px, py):
    if px < 0 or px > 2 or py < 0 or py > 2:
        return False
    elif self.tableroActual[px][py] != '.':
        return False
    else:
        return True
