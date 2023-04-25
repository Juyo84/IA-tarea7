import time

class Game: 
    def __init__(self):
        self.inicializar()

    def inicializar(self):
        self.tableroActual = [['.','.','.'],
                            ['.','.','.'],
                            ['.','.','.']]

        self.turnoHumano = 'X'

    def printTablero(self):
        print("0  1  2")
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.tableroActual[i][j]), end=" ")
            print(i)
        print()

    def validar(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.tableroActual[px][py] != '.':
            return False
        else:
            return True
        
    def Comprobaciones(self):
        # Comprobaciones en 
        # Vertical
        for i in range(0, 3):
            if (self.tableroActual[0][i] != '.' and
                self.tableroActual[0][i] == self.tableroActual[1][i] and
                self.tableroActual[1][i] == self.tableroActual[2][i]):
                return self.tableroActual[0][i]

        # Horizontal
        for i in range(0, 3):
            if (self.tableroActual[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.tableroActual[i] == ['O', 'O', 'O']):
                return 'O'

        # Diagonal
        if (self.tableroActual[0][0] != '.' and
            self.tableroActual[0][0] == self.tableroActual[1][1] and
            self.tableroActual[0][0] == self.tableroActual[2][2]):
            return self.tableroActual[0][0]

        # Diagonal inversa
        if (self.tableroActual[0][2] != '.' and
            self.tableroActual[0][2] == self.tableroActual[1][1] and
            self.tableroActual[0][2] == self.tableroActual[2][0]):
            return self.tableroActual[0][2]

        # Espacios vacios 
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.tableroActual[i][j] == '.'):
                    return None

        return '.'

 # Jugador 'X'
    def min(self):

        # Valores posibles para minv:
        # -1 - Gana
        # 0  - Empate
        # 1  - Pierde

        # Inicializamos:
        minv = 2

        qx = None
        qy = None

        resultados = self.Comprobaciones()

        if resultados == 'X':
            return (-1, 0, 0)
        elif resultados == 'O':
            return (1, 0, 0)
        elif resultados == '.':
            return (0, 0, 0)
        
        for i in range(0, 3):
            for j in range(0, 3):
                if self.tableroActual[i][j] == '.':
                    self.tableroActual[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.tableroActual[i][j] = '.'

        return (minv, qx, qy)

    # Jugador 'O' (IA)
    def max(self):

        # Posibles valores de maxv:
        # -1 - Pierde
        # 0  - Empate
        # 1  - Gana

        # Inicializamos:
        maxv = -2

        px = None
        py = None

        resultados = self.Comprobaciones()

        # Si termino el juego, regreamos un valor dependiendo el resultado:
        if resultados == 'X':
            return (-1, 0, 0)
        elif resultados == 'O':
            return (1, 0, 0)
        elif resultados == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.tableroActual[i][j] == '.':
                    self.tableroActual[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.tableroActual[i][j] = '.'
        return (maxv, px, py)

   
    def play(self):
        while True:
            self.printTablero()
            self.resultados = self.Comprobaciones()

            # Si el juego termino, se imprime lo siguiente:
            if self.resultados != None:
                if self.resultados == 'X':
                    print('El ganador es el jugador de X!')
                elif self.resultados == 'O':
                    print('El ganador es el jugador de O!')
                elif self.resultados == '.':
                    print("Empate ._.")

                self.inicializar()
                return

            # Si aun no se termina el juego
            if self.turnoHumano == 'X':

                while True:

                    inicio = time.time()
                    fin = time.time()
                    print('Tiempo de ejecucion: {}s'.format(round(fin - inicio, 7)))

                    px = int(input('Introduce la coordenada en X: '))
                    py = int(input('Introduce la coordenada en Y: '))


                    if self.validar(px, py):
                        self.tableroActual[px][py] = 'X'
                        self.turnoHumano = 'O'
                        break
                    else:
                        print('El movimiento no es valido, ingresa otro!')

            else:
                (m, px, py) = self.max()
                self.tableroActual[px][py] = 'O'
                self.turnoHumano = 'X'

def main():
    g = Game()
    g.play()

if __name__ == "__main__":
    main()