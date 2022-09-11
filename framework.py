import pygame
import sys
import random

pygame.init()

global startGame
global modes

global simp
global warrior

simp = True
warrior = False

startGame = False
modes = False


class window:
    def __init__(self):
        self.anchura, self.altura = 1200, 800
        self.window = pygame.display.set_mode((self.anchura, self.altura)) #finestra principal del còdi.

        self.pathImatge = "imatges/"
        self.bg = pygame.image.load(self.pathImatge + "lienzo.jpg")

        self.relog = pygame.time.Clock()
        self.clock = self.relog.tick(30)

    def startFramework(self): 
        self.window.fill((100, 100, 100))
    
    def updateFramework(self):
        pygame.display.flip()

    def endFramework(self):
        global startGame

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    startGame = False

    def draw_bg(self):
        self.window.blit(self.bg, (0, 0))

class personatge:
    def __init__(self, window, anchura_ventana, altura_ventana):
        self.window = window
        self.anchura = anchura_ventana
        self.altura = altura_ventana 
        self.pathImatge = "imatges/"
        self.pathAnimacions= "imatges/animacions/"

        self.dreta = False
        self.esquerra = False
        self.down = False

        self.personatge = pygame.sprite.Sprite()
        self.personatgeImatge = pygame.image.load(self.pathAnimacions + "down1.png")

        self.personatgeDOWN = [pygame.image.load(self.pathAnimacions + "down1.png" ), pygame.image.load(self.pathAnimacions + "down1.png" ), 
                                pygame.image.load(self.pathAnimacions + "down1.png" ), pygame.image.load(self.pathAnimacions + "down1.png" ), 
                                pygame.image.load(self.pathAnimacions + "down1.png" ), pygame.image.load(self.pathAnimacions + "down1.png" ), 
                                pygame.image.load(self.pathAnimacions + "down2.png" ), pygame.image.load(self.pathAnimacions + "down2.png"), 
                                pygame.image.load(self.pathAnimacions + "down2.png" ), pygame.image.load(self.pathAnimacions + "down2.png" ), 
                                pygame.image.load(self.pathAnimacions + "down2.png" ), pygame.image.load(self.pathAnimacions + "down2.png" ),  
                                pygame.image.load(self.pathAnimacions + "down3.png"), pygame.image.load(self.pathAnimacions + "down3.png" ),
                                pygame.image.load(self.pathAnimacions + "down3.png" ), pygame.image.load(self.pathAnimacions + "down3.png" ), 
                                pygame.image.load(self.pathAnimacions + "down3.png" ), pygame.image.load(self.pathAnimacions + "down3.png" )]

        self.personatgeDRETA = [pygame.image.load(self.pathAnimacions + "dreta1.png" ), pygame.image.load(self.pathAnimacions + "dreta1.png" ), 
                                pygame.image.load(self.pathAnimacions + "dreta1.png" ), pygame.image.load(self.pathAnimacions + "dreta1.png" ), 
                                pygame.image.load(self.pathAnimacions + "dreta1.png" ), pygame.image.load(self.pathAnimacions + "dreta1.png" ), 
                                pygame.image.load(self.pathAnimacions + "dreta2.png" ), pygame.image.load(self.pathAnimacions + "dreta2.png"), 
                                pygame.image.load(self.pathAnimacions + "dreta2.png" ), pygame.image.load(self.pathAnimacions + "dreta2.png" ), 
                                pygame.image.load(self.pathAnimacions + "dreta2.png" ), pygame.image.load(self.pathAnimacions + "dreta2.png" ),  
                                pygame.image.load(self.pathAnimacions + "dreta3.png"), pygame.image.load(self.pathAnimacions + "dreta3.png" ),
                                pygame.image.load(self.pathAnimacions + "dreta3.png" ), pygame.image.load(self.pathAnimacions + "dreta3.png" ), 
                                pygame.image.load(self.pathAnimacions + "dreta3.png" ), pygame.image.load(self.pathAnimacions + "dreta3.png" )]

        self.personatgeESQUERRA = [pygame.image.load(self.pathAnimacions + "esquerra1.png" ), pygame.image.load(self.pathAnimacions + "esquerra1.png" ), 
                                pygame.image.load(self.pathAnimacions + "esquerra1.png" ), pygame.image.load(self.pathAnimacions + "esquerra1.png" ), 
                                pygame.image.load(self.pathAnimacions + "esquerra1.png" ), pygame.image.load(self.pathAnimacions + "esquerra1.png" ), 
                                pygame.image.load(self.pathAnimacions + "esquerra2.png" ), pygame.image.load(self.pathAnimacions + "esquerra2.png"), 
                                pygame.image.load(self.pathAnimacions + "esquerra2.png" ), pygame.image.load(self.pathAnimacions + "esquerra2.png" ), 
                                pygame.image.load(self.pathAnimacions + "esquerra2.png" ), pygame.image.load(self.pathAnimacions + "esquerra2.png" ),  
                                pygame.image.load(self.pathAnimacions + "esquerra3.png"), pygame.image.load(self.pathAnimacions + "esquerra3.png" ),
                                pygame.image.load(self.pathAnimacions + "esquerra3.png" ), pygame.image.load(self.pathAnimacions + "esquerra3.png" ), 
                                pygame.image.load(self.pathAnimacions + "esquerra3.png" ), pygame.image.load(self.pathAnimacions + "esquerra3.png" )]

        self.personatge.image = self.personatgeImatge

        self.personatgeAnchura = self.personatge.image.get_width()
        self.personatgeAltura = self.personatge.image.get_height()

        self.personatge.rect = self.personatgeImatge.get_rect()

        self.x = self.anchura/2 - self.personatgeAnchura
        self.y = 0

        self.personatge.rect.x, self.personatge.rect.y = self.x, self.y

        self.count = 0

    def draw(self):

        if self.down:
            self.window.blit(self.personatgeDOWN[self.count], (self.x, self.y))
            self.count += 1


            if self.count > 17:
                self.count = 0

        elif self.dreta:
            self.window.blit(self.personatgeDRETA[self.count], (self.x, self.y))
            self.count += 1


            if self.count > 17:
                self.count = 0


        elif self.esquerra:
            self.window.blit(self.personatgeESQUERRA[self.count], (self.x, self.y))
            self.count += 1


            if self.count > 17:
                self.count = 0


        else:
            self.window.blit(self.personatgeImatge, (self.x, self.y))


    def movement(self):
        key_pressed = pygame.key.get_pressed()

        if self.x < self.anchura - self.personatgeAnchura: 
            if key_pressed[pygame.K_RIGHT]:
                self.x += 0.5
                self.dreta = True
                self.esquerra = False

            elif key_pressed[pygame.K_LEFT]:
                self.x -= 0.5
                self.esquerra = True
                self.dreta = False


            else:
                self.dreta = False
                self.esquerra = False

            if self.x < 0:
                self.x = self.personatgeAnchura // 2

        else:
            self.x = self.anchura - (self.personatgeAnchura + (self.personatgeAnchura // 2))

        if self.y >= 0:
            if key_pressed[pygame.K_DOWN]:
                self.y += 0.5
                self.down = True

            else:
                self.down = False


            if self.y > self.altura - 100:
                self.y = 1

        else:
            self.y = 1 #1 com a mínim del lienzo.

        self.personatge.rect.x = self.x #IMPORTANT
        self.personatge.rect.y = self.y #IMPORTANT


class cotxe:
    def __init__(self, personatge, anchura_ventana, altura_ventana, window):
        
        self.window = window 
        self.anchura = anchura_ventana
        self.altura = altura_ventana 
        self.pathImatge = "imatges/"

        self.personatge = personatge

        self.yCotxeLlista = [100, 300, 500]

        self.cotxes = pygame.sprite.Group()

        self.simp = 2
        self.warrior = 5
        self.velocitat = 2

        self.cotxeSprite = pygame.sprite.Sprite()
        cotxeImatge = pygame.image.load(self.pathImatge + "coche_animadoD.png")
        self.cotxeSprite.image = cotxeImatge

        self.cotxeAnchura = cotxeImatge.get_width()
        self.cotxeAltura = cotxeImatge.get_height()

        self.xCotxe = -self.cotxeAnchura
        self.yCotxe = 100

        self.cotxeSprite.rect = cotxeImatge.get_rect()

        self.cotxeSprite.rect.x = self.xCotxe #IMPORTANT
        self.cotxeSprite.rect.y = self.yCotxe #IMPORTANT

        self.cotxes.add(self.cotxeSprite)

    def movement_cotxe(self):
        global warrior
        global simp

        if warrior:
            self.velocitat = self.warrior
            self.cotxeSprite.rect.x += self.velocitat

        else:
            self.velocitat = self.simp
            self.cotxeSprite.rect.x += self.velocitat

        if self.cotxeSprite.rect.x > self.anchura:
            self.cotxeSprite.rect.y = random.choice(self.yCotxeLlista)
            self.cotxeSprite.rect.x = -self.cotxeAnchura

        print(self.velocitat)

    def draw(self):
        self.cotxes.draw(self.window)


class collide:
    def __init__(self, personatge, cotxes):
        self.personatge = personatge
        self.cotxes = cotxes


    def collide(self):
        if pygame.sprite.spritecollideany(self.personatge, self.cotxes):
            print("eeeee")

        else:
            print("noo")

class menu:
    def __init__(self, window):
        self.pathImatge = "imatges/"
        self.window = window
        self.menu = pygame.image.load(self.pathImatge + "menu.jpg")
        self.cotxe = pygame.image.load(self.pathImatge + "coche_animadoD.png")
        self.anchuraCotxe = self.cotxe.get_width()
        self.xCotxe, self.yCotxe = 750 - self.anchuraCotxe, 200
        self.x, self.y = 0, 0

        self.opcio = 0

        self.exit = False

    def opcions(self):
        global startGame 
        global modes

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_DOWN:
                    self.opcio += 1

                elif event.key == pygame.K_UP:
                    self.opcio -= 1



                elif event.key == pygame.K_RETURN:
                    if self.opcio == 2:
                        sys.exit() #IMPORTANT REVISAAAAAAR!

                    if self.opcio == 0:
                        startGame = True

                    if self.opcio == 1:
                        modes = True


    def draw(self):
        self.window.blit(self.menu, (self.x, self.y))

        if self.opcio == 1:
            self.xCotxe = 650 - self.anchuraCotxe
            self.yCotxe = 400

            self.exit = False

        elif self.opcio == 2:
            self.xCotxe = 750 - self.anchuraCotxe
            self.yCotxe = 600

            self.exit = True

        elif self.opcio == 0:
            self.xCotxe = 725 - self.anchuraCotxe
            self.yCotxe = 200

            self.exit = False


        if self.opcio > 2:
            self.opcio = 0

        elif self.opcio < 0:
            self.opcio = 0

        self.window.blit(self.cotxe, (self.xCotxe, self.yCotxe))


class modes_frame:
    def __init__(self, window):
        self.pathImatge = "imatges/"
        self.window = window
        self.modes = pygame.image.load(self.pathImatge + "modes.jpg")
        self.cotxe = pygame.image.load(self.pathImatge + "coche_animadoD.png")
        self.anchuraCotxe = self.cotxe.get_width()

        self.xModes, self.yModes = 0, 0
        self.xCotxe, self.yCotxe = 750 - self.anchuraCotxe, 200


        self.font = pygame.font.SysFont("arcades", 120)

        self.xFont, self.yFont = 650, 75


        self.opcio = 0

        self.simp = True
        self.warrior = False


    def draw(self):

        self.window.blit(self.modes, (self.xModes, self.yModes))

        if self.opcio == 0:
            self.xCotxe, self.yCotxe = 750 - self.anchuraCotxe, 200


        elif self.opcio == 1:
            self.xCotxe, self.yCotxe = 500 - self.anchuraCotxe, 400
            

        elif self.opcio == 2:
            self.xCotxe, self.yCotxe = 750 - self.anchuraCotxe, 575

        if self.opcio > 2:
            self.opcio = 0

        elif self.opcio < 0:
            self.opcio = 0

        if warrior:
            title = "WARRIOR"
            img = self.font.render(title, True, (64, 255, 0))
            self.window.blit(img, (self.xFont, self.yFont))

        elif simp:
            title = "SIMP"
            img = self.font.render(title, True, (64, 255, 0))
            self.window.blit(img, (self.xFont, self.yFont))

        self.window.blit(self.cotxe, (self.xCotxe, self.yCotxe))

    def opcions(self):
        global modes
        global warrior
        global simp

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_DOWN:
                    self.opcio += 1

                elif event.key == pygame.K_UP:
                    self.opcio -= 1


                elif event.key == pygame.K_RETURN:
                    if self.opcio == 2:
                        modes = False

                    elif self.opcio == 1:
                        warrior = True
                        simp = False

                    elif self.opcio == 0:
                        simp = True
                        warrior = False

                    


Window = window()
Personatge = personatge(Window.window, Window.anchura, Window.altura)
Cotxe = cotxe(Personatge.personatge, Window.anchura, Window.altura, Window.window)
Collisio = collide(Personatge.personatge, Cotxe.cotxes)
Menu = menu(Window.window)
Modes = modes_frame(Window.window)

while not Window.endFramework():
    Window.startFramework()
    if startGame and not modes:
        Window.draw_bg()
        Cotxe.draw()
        Personatge.draw()
        Personatge.movement()
        Cotxe.movement_cotxe()
        Collisio.collide()

    else:
        Menu.draw()
        Menu.opcions()

    if modes:
        Modes.draw()
        Modes.opcions()
    
    
    
    Window.updateFramework()





    #FER QUE TORNI A COMENÇAR DES DE 0.
    #LAG EN MENU