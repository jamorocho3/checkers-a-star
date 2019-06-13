# Author: Jerson Morocho
# Date: 04-06-2019
# MIT License

from Problema import *
from tabulate import tabulate


# Heredamos de la clase Problema
class Damas(Problema):
  def __init__(self, tablero_inicial):
    super().__init__(
      estado_inicial = tablero_inicial,
      estado_final = (2,0)
    )

  def acciones(self, estado, posicion_pieza):
    access = list()
    pieza = estado[posicion_pieza] # el tipo de la pieza

    if pieza == "B":
      # B -> derecha
      if posicion_pieza not in (0,2,7,15):
        # 5 -> 2
        if posicion_pieza == 5:
          # posicion libre
          if estado[2] == 0:
            access.append("right_up")
        # 8 -> 5
        if posicion_pieza == 8:
          # posicion libre
          if estado[5] == 0:
            access.append("right_up")
          access.append("double_right_up")
        # 10 -> 7
        if posicion_pieza == 10:
          # posicion libre
          if estado[7] == 0:
            access.append("right_up")
        # 13 -> 10
        if posicion_pieza == 13:
          # posicion libre
          if estado[10] == 0:
            access.append("right_up")
          access.append("double_right_up")
          pass
      # B -> izquierda
      if posicion_pieza not in (0,2,8):
        # 5 -> 0
        if posicion_pieza == 5:
          # posicion libre
          if estado[0] == 0:
            access.append("left_up")
        # 7 -> 2
        if posicion_pieza == 7:
          # posicion libre
          if estado[2] == 0:
            access.append("left_up")
        # 10 -> 5
        if posicion_pieza == 10:
          # posicion libre
          if estado[5] == 0:
            access.append("left_up")
          access.append("double_left_up")
        # 13 -> 8
        if posicion_pieza == 13:
          # posicion libre
          if estado[8] == 0:
            access.append("left_up")
        # 15 -> 10
        if posicion_pieza == 15:
          # posicion libre
          if estado[10] == 0:
            access.append("left_up")
          access.append("double_left_up")

    if pieza == "R":
      
      # R -> izquierda
      if posicion_pieza not in (7,13,15):
        # 0 -> 5
        if posicion_pieza == 0:
          # posicion libre
          if estado[5] == 0:
            access.append("right_down")
          access.append("double_right_down")
        # 2 -> 7
        if posicion_pieza == 2:
          # posicion libre
          if estado[7] == 0:
            access.append("right_down")
        # 5 -> 10
        if posicion_pieza == 5:
          # posicion libre
          if estado[10] == 0:
            access.append("right_down")
          access.append("double_right_down")
        # 8 -> 13
        if posicion_pieza == 8:
          # posicion libre
          if estado[13] == 0:
            access.append("right_down")
        # 10 -> 15
        if posicion_pieza == 10:
          # posicion libre
          if estado[15] == 0:
            access.append("right_down")
      # R -> derecha
      if posicion_pieza not in (0,8,13,15):
        # 2 -> 5
        if posicion_pieza == 2:
          # posicion libre
          if estado[5] == 0:
            access.append("left_down")
          access.append("double_left_down")
        # 5 -> 8
        if posicion_pieza == 5:
          # posicion libre
          if estado[8] == 0:
            access.append("left_down")
        # 7 -> 10
        if posicion_pieza == 7:
          print("aqui")
          # posicion libre
          if estado[10] == 0:
            access.append("left_down")
          access.append("double_left_down")
        # 10 -> 13
        if posicion_pieza == 10:
          # posicion libre
          if estado[13] == 0:
            access.append("left_down")

    return access

  def aplica(self, estado, posicion_pieza, accion):
    # p = posicion, n = vacio
    # p0  n1   p2   n2
    # n3  p5   n4   p7
    # p8  n5   p10  n6
    # n7  p13  n8   p15
    # Destructuring
    p0,n1,p2,n2,n3,p5,n4,p7,p8,n5,p10,n6,n7,p13,n8,p15 = estado
    
    # Movimiento Negras
    if accion == "right_up":
      if posicion_pieza == 5:
        return (p0,n1,p5,n2,n3,0,n4,p7,p8,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 8:
        return (p0,n1,p2,n2,n3,p8,n4,p7,0,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 10:
        return (p0,n1,p2,n2,n3,p5,n4,p10,p8,n5,0,n6,n7,p13,n8,p15)
      if posicion_pieza == 13:
        return (p0,n1,p2,n2,n3,p5,n4,p7,p8,n5,p13,n6,n7,0,n8,p15)

    # Movimientos Dobles 
    if accion == "double_right_up":
      if posicion_pieza == 8:
        return (p0,n1,p8,n2,n3,0,n4,p7,0,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 13:
        return (p0,n1,p2,n2,n3,p5,n4,p13,p8,n5,0,n6,n7,0,n8,p15)

    if accion == "left_up":
      if posicion_pieza == 5:
        return (p5,n1,p2,n2,n3,0,n4,p7,p8,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 7:
        return (p0,n1,p7,n2,n3,p5,n4,0,p8,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 10:
        return (p0,n1,p2,n2,n3,p10,n4,p7,p8,n5,0,n6,n7,p13,n8,p15)
      if posicion_pieza == 13:
        return (p0,n1,p2,n2,n3,p5,n4,p7,p13,n5,p10,n6,n7,0,n8,p15)
      if posicion_pieza == 15:
        return (p0,n1,p2,n2,n3,p5,n4,p7,p8,n5,p10,n6,n7,p15,n8,0)

    # Movimientos Dobles 
    if accion == "double_left_up":
      if posicion_pieza == 10:
        return (p10,n1,p2,n2,n3,0,n4,p7,p8,n5,0,n6,n7,p13,n8,p15)
      if posicion_pieza == 15:
        return (p0,n1,p2,n2,n3,p15,n4,p7,p8,n5,0,n6,n7,p13,n8,0)

    # Movimiento Rojas
    if accion == "right_down":
      if posicion_pieza == 0:
        return (0,n1,p2,n2,n3,p0,n4,p7,p8,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 2:
        return (p0,n1,0,n2,n3,p5,n4,p2,p8,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 5:
        return (p0,n1,p2,n2,n3,0,n4,p7,p8,n5,p5,n6,n7,p13,n8,p15)
      if posicion_pieza == 8:
        return (p0,n1,p2,n2,n3,p5,n4,p7,0,n5,p10,n6,n7,p8,n8,p15)
      if posicion_pieza == 10:
        return (p0,n1,p2,n2,n3,p5,n4,p7,p8,n5,0,n6,n7,p13,n8,p10)

    # Movimientos Dobles 
    if accion == "double_right_down":
      if posicion_pieza == 0:
        return (0,n1,p2,n2,n3,0,n4,p7,p8,n5,p0,n6,n7,p13,n8,p15)
      if posicion_pieza == 5:
        return (p0,n1,p2,n2,n3,0,n4,p7,p8,n5,0,n6,n7,p13,n8,p5)

    if accion == "left_down":
      if posicion_pieza == 2:
        return (p0,n1,0,n2,n3,p2,n4,p7,p8,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 5:
        return (p0,n1,p2,n2,n3,0,n4,p7,p5,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 7:
        return (p0,n1,p2,n2,n3,p5,n4,0,p8,n5,p7,n6,n7,p13,n8,p15)
      if posicion_pieza == 10:
        return (p0,n1,p2,n2,n3,p5,n4,p7,p8,n5,0,n6,n7,p10,n8,p15)

    # Movimientos Dobles 
    if accion == "double_left_down":
      if posicion_pieza == 2:
        return (p0,n1,0,n2,n3,0,n4,p7,p2,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 7:
        return (p0,n1,p2,n2,n3,p5,n4,0,p8,n5,0,n6,n7,p7,n8,p15)

# Resultados

    # p0  n1   p2   n2
    # n3  p5   n4   p7
    # p8  n5   p10  n6
    # n7  p13  n8   p15


# game = Damas(("R",0,"R",0,0,0,0,0,0,0,0,0,0,"B",0,"B")) # tablero inicial
game = Damas((0, 0, 0, 0, 0, 0, 0, 'R', 0, 0, 'B', 0, 0, 0, 0, 0)) # tablero inicial

estado_inicial = game.estado_inicial
estado_final = game.estado_final

# posiciones de las fichas dentro de la tupla
black_piece = [i for i, x in enumerate(estado_inicial) if x == 'B']
red_piece = [i for i, x in enumerate(estado_inicial) if x == 'R']

# con acciones buscar pieza puede moverse
accion = game.acciones(estado_inicial, 7)
black = game.aplica(estado_inicial, 10, "double_left_up")
red = game.aplica(estado_inicial, 7, "double_left_down")
tablero = red


print("# estado inicial: ",estado_inicial)
print("# estado final: ",estado_final)
print("accion: ",accion)
# print("aplica: ",tablero)


p0,n1,p2,n2,n3,p5,n4,p7,p8,n5,p10,n6,n7,p13,n8,p15 = tablero

tablero = [
  [p0,n1,p2,n2],
  [n3,p5,n4,p7],
  [p8,n5,p10,n6],
  [n7,p13,n8,p15]
]
print(tabulate(tablero, headers='firstrow', tablefmt='grid'))