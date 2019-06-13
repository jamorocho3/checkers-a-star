# # Authors: Jerson Morocho, Mauro Morales
# # Date: 04-06-2019
# # MIT License

import time
from tabulate import tabulate
from random import shuffle
from Damas import Damas

# Resultados
# game = Damas(('R', None, 'R', None, None, 0, None, 0, 0, None, 0, None, None, 'B', None, 'B')) # tablero inicial
game = Damas((0, None, 'R', None, None, 'R', None, 0, 0, None, 0, None, None, 'B', None, 'B')) # tablero inicial

estado_inicial = game.estado_inicial
estado_final = game.estado_final
validation = False
p = 'B'
coord = (0,0)
cchevishev= list()

cont = 0

def distanciaChevishev(punto_1, punto_2):
  x1,y1 = punto_1
  x2,y2 = punto_2
  return max(abs(x2 - x1), abs(y2 - y1))

while validation == False:
  # posiciones de las fichas dentro de la tupla
  piece = [i for i, x in enumerate(estado_inicial) if x == p]

  #    0  1  2  3
  # 0  00    02
  # 1     11    13
  # 2  20    22
  # 3     31    33
  # el for recorre las posiciones disponibles
  for pos in piece:
    if p == 'B':
      if pos == 0:
        dis = distanciaChevishev((0,0),(0,0))
      if pos == 2:
        dis = distanciaChevishev((0,2),(0,2))
      if pos == 5:
        dis =  distanciaChevishev((1,1),(0,2))
      if pos == 7:
        dis = distanciaChevishev((1,3),(0,2))
      if pos == 8:
        dis = distanciaChevishev((2,0),(0,2))
      if pos == 10:
        dis = distanciaChevishev((2,2),(0,2))
      if pos == 13:
        dis = distanciaChevishev((3,1),(0,2))
      if pos == 15:
        dis = distanciaChevishev((3,3),(0,2))
    elif p == 'R':
      if pos == 0:
        dis = distanciaChevishev((0,0),(3,1))
      if pos == 2:
        dis = distanciaChevishev((0,2),(3,1))
      if pos == 5:
        dis = distanciaChevishev((1,1),(3,1))
      if pos == 7:
        dis = distanciaChevishev((1,3),(3,1))
      if pos == 8:
        dis = distanciaChevishev((2,0),(3,1))
      if pos == 10:
        dis = distanciaChevishev((2,2),(3,1))
      if pos == 13:
        dis = distanciaChevishev((3,1),(3,1))
      if pos == 15:
        dis = distanciaChevishev((3,3),(3,3))
    cchevishev.append(dis)

  time.sleep(1)


  print("max de chevishev ", p, max(cchevishev))

  if max(cchevishev) != 0:
    shuffle(piece)
    posicion_pieza = piece[0]
    # con acciones buscar pieza puede moverse
    # print(estado_inicial,posicion_pieza)
    accion = game.acciones(estado_inicial, posicion_pieza)
    # si la pieza sin movimientos
    if accion == []:
      posicion_pieza = piece[1]
      accion = game.acciones(estado_inicial, posicion_pieza)
    aplica = game.aplica(estado_inicial, posicion_pieza, accion[0])


    p0,n1,p2,n2,n3,p5,n4,p7,p8,n5,p10,n6,n7,p13,n8,p15 = estado_inicial

    tablero = [
      [p0,n1,p2,n2],
      [n3,p5,n4,p7],
      [p8,n5,p10,n6],
      [n7,p13,n8,p15]
    ]
    print(tabulate(tablero, tablefmt='grid'))
    print("Turno:", p, posicion_pieza," Accion: ", accion)

  # B se convirtió en reina
  elif max(cchevishev) == 0:
    print("B es reina")
    validation = True


  estado_inicial = aplica
  cchevishev = []
  if p == 'B': p = 'R'
  elif p == 'R': p = 'B'
  cont = cont + 1
  print("Movimiento ==> ", cont)