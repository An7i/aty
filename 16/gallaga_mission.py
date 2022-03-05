# 주제 : Galaga Game

# 필요 라이브러리 import


# <class Sprite>
# : 게임의 스프라이트를 나타내는 클래스로 공통적으로 사용되는 변수와 메소드를 가지고 있다.
## 'sprite'의 의미
## 1) (장난을 좋아하는) 요정, 도깨비
## 2) (컴퓨터 그래픽스) 영상 속에 작은 2차원 비트맥이나 애니메이션을 합성하는 기술

# class Sprite 만들기
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
    def getwidth(self):
        return self.img.Width()


    # 스프라이트의 세로 길이 반환 메서드(getHeight())
    def getwidth(self):
        return self.img.Height()


    # 스프라이트를 화면에 그리기(draw())
    def draw(self, g):
        g.create_image(self.x, self.y, image__= self.img)


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
    def getX(self):
        return self.y


    # 다른 스프라이트와의 충돌 여부를 계산한다. 충돌이면 true를 반환한다.(checkCollision())
    def checkcollision(self, other):
        p1x = self.x
        p1y = self.y
        p2x = self.x + self.getwidth()
        p2y = self.y + self.getHeight()

        p3x = other.x
        p3x = other.y
        p4x = other.x + other.getWidth()
        p4x = other.y + other.getHeight()

        overlapped = False

        if not (p4 < p1x or p3x > p2x or p2y < p3y or p1y > p4) :
            overlapped = True

        return overlapped



    # 충돌 처리한다. Sprite class에서는 아무 기능이 없으나, 자식 클래스에 오버라이드 된다.(handleCollision())
    
    def handleCollision(self, other):
        pass


# <class StarShipSprite>
# : 우주선(StarShip)을 나타내는 클래스
class StartShipSprite(Sprite):
    def __init__(self):
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

        super.().move()
        self.dx = 0
        self.dy = 0

    def handleCollision(self, other):
        if type(other) == AlienSprite:
            self.game.endGame()

    



# <class AlienSprite>
# : 외계인 우주선을 나타내 는 클래스

# class AlienSprite 만들기
    # AlienSprite 생성자(__init__())




    # 외계인 우주선을 움직이는 메소드(윈도우의 경계에 도달하면 한 칸 아래로 이동한다.)(move())
    
    








# <class ShotSprite>
# : 포탄을 나타내는 클래스

# class ShotSprite 만들기
    # ShotSprite 생성자(__init__())
        
        






    # 화면을 벗어나면 객체를 리스트에서 삭제한다.(move())





    # 충돌을 처리한다. 포탄과 외계인 우주선 객체를 모두 리스트에서 삭제한다.(handleCollision())
   
   




# <class GalagaGame>
# 갤러그 게임을 나타내는 클래스

# class GalagaGame 만들기
    # "이벤트" 관련 매서드들
    ## ↑ 화살표 키 이벤트 처리(keyUp())
    
    


    ## ↓ 화살표 키 이벤트 처리(keyDown())
    


    ## → 화살표 키 이벤트 처리(keyLeft())
    
    

    ## ← 화살표 키 이벤트 처리(keyRight())
   


    ## 스페이스 키 이벤트를 처리(keySpace())
    
    

    ## ESC 키 이벤트를 처리(keyESC())



    # initSprites 메서드: 게임에 필요한 스프라이트를 생성(initSprites())
    
    






    # __init__(): 생성자 메서드
        
        











    # startGame() 메서드: 게임시작 메서드(Enter키의 이벤트 핸들러)
    
    




    # endGame() 메서드: 게임 종료(Game Over의 조건을 충족했을 때 실행되는 메서드)
    
    




    # removeSprite() 메서드: 스프라이트를 리스트에서 삭제
    
    




    # fire() 메서드: 포탄 발사
    
    



    # paint() 메서드: 화면 그리기
    
    





    # gameLoop() 메서드: 게임 루프
        # 1. 스프라이트들이 움직이도록 설정(move)
        
        

        # 2. 스프라이트 리스트 안의 객체끼리의 충돌을 검사한다.(collision)
        
        





        # 3. 배경그리기(paint // gameloop가 실행될 때마다 그려 마치 움직이는 것처럼 보이게 함.)
        

        # 4. 게임 동작 여부를 확인하여 True일때, 10ms 간격으로 self.gameLoop를 실행시킨다.(gameLoop)
        # after 명령: 일정 시간이 지난 후에 특정 함수 또는 메서드를 실행시킨다.





# main문
if __name__ == "__main__":
    pass                # main문 작성시 지워주세요.
    # Tk() 객체 생성
    # 제목 설정

    # GalagaGame 객체 생성
    # gameLoop() 함수를 호출
    # mainloop() 해주기 