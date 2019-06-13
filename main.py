# # Authors: Jerson Morocho, Mauro Morales
# # Date: 04-06-2019
# # MIT License

import sys
import pygame
import time
from pygame.locals import *
from tabulate import tabulate
from random import shuffle
from Damas import Damas


# ------------------------------------------------------
# Variables de la interfaz
size = ANCHO, ALTO = 700, 450

# Funcion principal para el juego
def game():
  pygame.init()

  ventana = pygame.display.set_mode(size)
  pygame.display.set_caption("Problema del 8-Puzzle")
  fps_clock = pygame.time.Clock()
  fondo = pygame.image.load("images/fondo.jpg")
  fuenteGrande = pygame.font.Font("fonts/supercell.ttf", 40)
  fuentePequena = pygame.font.Font("fonts/supercell.ttf", 20)

  game = Damas(('R', None, 'R', None, None, 0, None, 0, 0, None, 0, None, None, 'B', None, 'B')) # tablero inicial
  game = Damas((0, None, 'R', None, None, 'R', None, 0, 0, None, 0, None, None, 'B', None, 'B')) # tablero inicial

  estado_inicial = game.estado_inicial
  # estado_final = game.estado_final
  validation = False
  p = 'B'
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

    time.sleep(2)


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
      # print(tabulate(tablero, tablefmt='grid'))
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

    dibujar(ventana, fondo, fuenteGrande, tablero)
    pygame.display.update()

  while True:
    checkForQuit()
    fps_clock.tick(20)

def dibujar(screen, fondo, fuente, tablero):
  screen.blit(fondo, (0,0))
  screen.blit(fuente.render(str(tablero[0]), 0, (255, 255, 255)), (50,50))
  screen.blit(fuente.render(str(tablero[1]), 0, (255, 255, 255)), (50,150))
  screen.blit(fuente.render(str(tablero[2]), 0, (255, 255, 255)), (50,250))
  screen.blit(fuente.render(str(tablero[3]), 0, (255, 255, 255)), (50,350))

def checkForQuit():
  for event in pygame.event.get(QUIT): # get all the QUIT events
    terminate() # terminate if any QUIT events are present
  for event in pygame.event.get(KEYUP): # get all the KEYUP events
    if event.key == K_ESCAPE:
      terminate() # terminate if the KEYUP event was for the Esc key
    pygame.event.post(event) # put the other KEYUP event objects back

def terminate():
  pygame.quit()
  sys.exit()

if __name__ == "__main__":
  game()