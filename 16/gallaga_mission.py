# 주제 : Galaga Game

# 필요 라이브러리 import
from tkinter import *
import sys
import pygame

# <class Sprite>
# : 게임의 스프라이트를 나타내는 클래스로 공통적으로 사용되는 변수와 메소드를 가지고 있다.
## 'sprite'의 의미
## 1) (장난을 좋아하는) 요정, 도깨비
## 2) (컴퓨터 그래픽스) 영상 속에 작은 2차원 비트맥이나 애니메이션을 합성하는 기술

# class Sprite 만들기
import pygame.mixer


class Sprite:

    # Sprite 생성자
        # 스프라이트가 가지고 있는 이미지
        # 현재 위치의 x좌표
        # 현재 위치의 y좌표
        # 단위시간에 움직이는 x방향 거리
        # 단위시간에 움직이는 y방향 거리
    def __init__(self, image, x, y):
        self.img = image
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    # 스프라이트의 가로 길이 반환 메소드(getWidth())
    def getWidth(self):
        return self.img.width()


    # 스프라이트의 세로 길이 반환 메서드(getHeight())
    def getHeight(self):
        return self.img.height()


    # 스프라이트를 화면에 그리기(draw())
    def draw(self, g):
        g.create_image(self.x, self.y, image  = self.img)


    # 스프라이트를 움직이는 메소드(move())
    def move(self):
        self.x += self.dx
        self.y += self.dy


    # dx를 설정하는 설정자 메소드(setDx())
    def setDx(self, dx):
        self.dx = dx


    # dy를 설정하는 설정자 메소드(setDy())
    def setDy(self, dy):
        self.dy = dy

    # dx를 반환하는 접근자 메소드(getDx())
    def getDx(self):
        return self.dx


    # dy를 반환하는 접근자 메소드(getDy())
    def getDy(self):
        return self.dy


    # x를 반환하는 접근자 메소드(getX())
    def getX(self):
        return self.x


    # y를 반환하는 접근자 메소드(getY())
    def getY(self):
        return self.y


    # 다른 스프라이트와의 충돌 여부를 계산한다. 충돌이면 true를 반환한다.(checkCollision())
    def checkCollision(self, other):
        p1x = self.x
        p1y = self.y
        p2x = self.x + self.getWidth()
        p2y = self.y + self.getHeight()

        p3x = other.x
        p3y = other.y
        p4x = other.x + other.getWidth()
        p4y = other.y + other.getHeight()

        overlapped = False

        if not (p4x < p1x or p3x > p2x or p2y < p3y or p1y > p4y) :
            overlapped = True

        return overlapped



    # 충돌 처리한다. Sprite class에서는 아무 기능이 없으나, 자식 클래스에 오버라이드 된다.(handleCollision())
    
    def handleCollision(self, other):
        pass


# <class StarShipSprite>
# : 우주선(StarShip)을 나타내는 클래스
class StartShipSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = 0
        self.dy = 0

    # 우주선을 움직이는 메서드. (윈도우 경계를 넘으려고 할 경우, 움직이지 못하게 할 것) (move())
    def move(self):
        if (self.dx < 0 and self.x < 10) or (self.dx > 0 and self.x > 725):
            return
        if (self.dx > 0 and self.x > 525) or (self.dx < 0 and self.x < 10):
            return

        super().move()
        self.dx = 0
        self.dy = 0

    def handleCollision(self, other):
        if type(other) == AlienSprite:
            self.game.endGame()

    



# <class AlienSprite>
# : 외계인 우주선을 나타내 는 클래스
class AlienSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = -10
    def move(self):
        if (self.dx < 0 and self.x < 10) or (self.dx > 0 and self.x > 725):
            self.dx = -self.dx
            self.y += 50
            if self.y > 600:
                self.game.endGame()
        super().move()

# <class ShotSprite>
# : 포탄을 나타내는 클래스
class ShotSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dy = -1
        self.hit_sound = pygame.mixer.Sound('.\sound\hit_sound.mp3')
        self.shot_sound = pygame.mixer.Sound('.\sound\shot_sound.mp3')
        self.shot_sound.play()

    # 화면을 벗어나면 객체를 리스트에서 삭제한다.(move())
    def move(self):
        super().move()
        if self.y < -50:
            self.game.removeSprite(self)

    def handleCollision(self, other):
        if type(other) == AlienSprite:
            self.hit_sound.play()
            self.game.removeSprite(self)
            self.game.removeSprite(other)




    # 충돌을 처리한다. 포탄과 외계인 우주선 객체를 모두 리스트에서 삭제한다.(handleCollision())
   
   




# <class GalagaGame>
# 갤러그 게임을 나타내는 클래스
class GalagaGame():
    def keyUp(self, event):
        self.starship.setDy(-10)

    def keyDown(self, event):
        self.starship.setDy(+10)

    def keyLeft(self, event):
        self.starship.setDx(-10)

    def keyRight(self, event):
        self.starship.setDx(+10)

    def keySpace(self, event):
        self.fire()

    def keyESC(self, event):
        self.master.distroy()

    def initSprites(self):
        self.starship = StartShipSprite(self, self.shipImage, 370, 520)
        self.sprites.append(self.starship)
        for y in range(0,2):
            for x in range(0,12):
                alien = AlienSprite(self, self.alienImage, 100+x*50, 50+y*30)
                self.sprites.append(alien)

    def __init__(self, master):
        self.master = master
        self.sprites = []
        self.canvas = Canvas(master, width=800, height = 600)
        self.canvas.pack()
        self.shotImage = PhotoImage(file = "./image/fire.png")
        self.shipImage = PhotoImage(file="./image/starship.png")
        self.alienImage = PhotoImage(file="./image/alien.png")
        self.running = True
        self.initSprites()

        master.bind("<Up>", self.keyUp)
        master.bind("<Down>", self.keyDown)
        master.bind("<Left>", self.keyLeft)
        master.bind("<Right>", self.keyRight)
        master.bind("<Escape>", self.keyESC)
        master.bind("<space>", self.keySpace)
        master.bind("<Return>", self.startGame)
        self.start_sound = pygame.mixer.Sound('./sound/shot_sound.mp3')
        self.start_sound = pygame.mixer.Sound('./sound/start_sound.mp3')


    # startGame() 메서드: 게임시작 메서드(Enter키의 이벤트 핸들러)
    def startGame(self, event):
        self.sprites.clear()
    # endGame() 메서드: 게임 종료(Game Over의 조건을 충족했을 때 실행되는 메서드)
    
    def endGame(self):
        self.running = False
        sys.exit()
    # removeSprite() 메서드: 스프라이트를 리스트에서 삭제
    def removeSprite(self,sprite):
        if(sprite in self.sprites):
            self.sprites.remove(sprite)
            del sprite
    # fire() 메서드: 포탄 발사
    def fire(self):
        shot = ShotSprite(self, self.shotImage, self.starship.getX()+28, self.starship.getY()-30)
        self.sprites.append(shot)

    def paint(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0,0,800,600, fill="black")
        for sprite in self.sprites:
            sprite.draw(self.canvas)

    def gameLoop(self):
        for sprite in self.sprites:
            sprite.move()

        for me in self.sprites:
            for other in self.sprites:
                if me != other:
                    if me.checkCollision(other):
                        me.handleCollision(other)
                        other.handleCollision(me)

        self.paint()



        if self.running:
            self.master.after(10, self.gameLoop)


# main문
if __name__ == "__main__":
    root = Tk()                # main문 작성시 지워주세요.
    root.title("Galaga Game")
    pygame.init()

    g = GalagaGame(root)
    g.start_sound.play()
    g.gameLoop()
    root.mainloop()

    # GalagaGame 객체 생성
    # gameLoop() 함수를 호출
    # mainloop() 해주기 