import pygame
import random

pygame.init()


class window:
    def __init__(self):
        self.anchura, self.altura = 1200, 800
        self.window = pygame.display.set_mode((self.anchura, self.altura)) #finestra principal del còdi.

        self.pathImatge = "imatges/"
        self.bg = pygame.image.load(self.pathImatge + "lienzo.jpg")

        self.relog = pygame.time.Clock()
        self.clock = self.relog.tick(20)

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
        self.cotxeSprite.rect.x += 2

        if self.cotxeSprite.rect.x > self.anchura:
            self.cotxeSprite.rect.y = random.choice(self.yCotxeLlista)
            self.cotxeSprite.rect.x = -self.cotxeAnchura


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


Window = window()
Personatge = personatge(Window.window, Window.anchura, Window.altura)
Cotxe = cotxe(Personatge.personatge, Window.anchura, Window.altura, Window.window)
Collisio = collide(Personatge.personatge, Cotxe.cotxes)


while not Window.endFramework():
    Window.startFramework()
    Window.draw_bg()
    Cotxe.draw()
    Personatge.draw()
    Personatge.movement()
    Cotxe.movement_cotxe()
    Collisio.collide()
    Window.updateFramework()