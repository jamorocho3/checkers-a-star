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

  def acciones(self, estado): # reglas
    # diagonal

    # if expression:
    pass

  def aplica(self, estado, posicion_pieza, accion):
    # p = posicion, n = vacio
    # p0  n1   p2   n2
    # n3  p5   n4   p7
    # p8  n5   p10  n6
    # n7  p13  n8   p15
    # Destructuring
    p0,n1,p2,n2,n3,p5,n4,p7,p8,n5,p10,n6,n7,p13,n8,p15 = estado
    
    # Movimiento Negras
    if accion == "↗":
      if posicion_pieza == 5:
        return (p0,n1,p5,n2,n3,0,n4,p7,p8,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 8:
        return (p0,n1,p2,n2,n3,p8,n4,p7,0,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 10:
        return (p0,n1,p2,n2,n3,p5,n4,p10,p8,n5,0,n6,n7,p13,n8,p15)
      if posicion_pieza == 13:
        return (p0,n1,p2,n2,n3,p5,n4,p7,p8,n5,p13,n6,n7,0,n8,p15)
    if accion == "↖":
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
    # Movimiento Rojas
    if accion == "↘":
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
    if accion == "↙":
      if posicion_pieza == 2:
        return (p0,n1,0,n2,n3,p2,n4,p7,p8,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 5:
        return (p0,n1,p2,n2,n3,0,n4,p7,p5,n5,p10,n6,n7,p13,n8,p15)
      if posicion_pieza == 7:
        return (p0,n1,p2,n2,n3,p5,n4,0,p8,n5,p7,n6,n7,p13,n8,p15)
      if posicion_pieza == 10:
        return (p0,n1,p2,n2,n3,p5,n4,p7,p8,n5,0,n6,n7,p10,n8,p15)



# Resultados
game = Damas(("R",0,"R",0,0,0,0,0,0,0,0,0,0,"B",0,"B")) # tablero inicial, tablero final, p1, p2

estado_inicial = game.estado_inicial
estado_final = game.estado_final

# posiciones de las fichas dentro de la tupla
black_piece = [i for i, x in enumerate(estado_inicial) if x == 'B']
red_piece = [i for i, x in enumerate(estado_inicial) if x == 'R']

# con acciones buscar pieza puede moverse
black = game.aplica(estado_inicial, 13, "↗")
red = game.aplica(estado_inicial, 2, "↘")


print("# estado inicial: ",estado_inicial)
print("# estado final: ",estado_final)
print("aplica: ",black)


# p0,n1,p2,n2,n3,p5,n4,p7,p8,n5,p10,n6,n7,p13,n8,p15 = red

# tablero = [
#   [p0,n1,p2,n2],
#   [n3,p5,n4,p7],
#   [p8,n5,p10,n6],
#   [n7,p13,n8,p15]
# ]
# print(tabulate(tablero, headers='firstrow', tablefmt='grid'))