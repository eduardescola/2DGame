import pygame
import random

pygame.init()

class window:
    def __init__(self):
        self.anchura, self.altura = 1200, 800
        self.window = pygame.display.set_mode((self.anchura, self.altura)) #finestra principal del còdi.

        self.relog = pygame.time.Clock()
        self.clock = self.relog.tick(30)

    def startFramework(self): 
        self.window.fill((100, 100, 100))
    
    def updateFramework(self):
        pygame.display.flip()


    def endFramework(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True



class mainGame:
    def __init__(self, window, anchura_ventana, altura_ventana):
        self.window = window
        self.anchura = anchura_ventana
        self.altura = altura_ventana 
        self.pathImatge = "imatges/"
        self.bg = pygame.image.load(self.pathImatge + "lienzo.jpg")

        self.personaje = pygame.image.load(self.pathImatge + "personaje_animado.png")
        self.personajeAnchura = self.personaje.get_width()
        self.personajeAltura = self.personaje.get_height()
        self.personajeX, self.personajeY = self.anchura/2 - self.personajeAnchura, 0

        self.cotxeDreta = pygame.image.load(self.pathImatge + "coche_animadoD.png")
        self.cotxeEsquerra = pygame.image.load(self.pathImatge + "coche_animadoE.png")
        self.cotxeAnchura = self.cotxeDreta.get_width()
        self.cotxeAltura = self.cotxeDreta.get_height()
        self.cotxeXInicial, self.cotxeYInicial = -self.cotxeAnchura, 100

        self.cotxeX, self.cotxeY = self.cotxeXInicial, self.cotxeYInicial


        self.yCotxe = [100, 300, 500]

    def draw(self):
        self.window.blit(self.bg, (0, 0))
        self.window.blit(self.cotxeDreta, (self.cotxeX, self.cotxeY))
        self.window.blit(self.personaje, (self.personajeX, self.personajeY))

    def movement_cotxe(self):
        self.cotxeX += 2

        if self.cotxeX > self.anchura:
            self.cotxeX = -self.cotxeAnchura
            self.cotxeY = random.choice(self.yCotxe)

    def movement(self):
        key_pressed = pygame.key.get_pressed()

        if self.personajeX < self.anchura - self.personajeAnchura: 
            if key_pressed[pygame.K_RIGHT]:
                self.personajeX += 0.5

            elif key_pressed[pygame.K_LEFT]:
                self.personajeX -= 0.5

            if self.personajeX < 0:
                self.personajeX = self.personajeAnchura // 2

        else:
            self.personajeX = self.anchura - (self.personajeAnchura + (self.personajeAnchura // 2))


        if self.personajeY >= 0:
            if key_pressed[pygame.K_DOWN]:
                self.personajeY += 0.5

            elif key_pressed[pygame.K_UP]:
                self.personajeY -= 0.5


            if self.personajeY > self.altura - 100:
                self.personajeY = 1

        else:
            self.personajeY = 1 #1 com a mínim del lienzo.


        print(self.personajeX, self.anchura - self.personajeAnchura, self.altura - 100, self.personajeY)



Window = window()
Main = mainGame(Window.window, Window.anchura, Window.altura)


while not Window.endFramework():
    Window.startFramework()

    Main.draw()
    Main.movement_cotxe()
    Main.movement()
    Window.updateFramework()