from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
# oyunun oynanacağı ekran boyutunu ayarlıyorum.
screen.setup(width=600,height=600)
# arkaplan rengini belirliyorum.
screen.bgcolor("black")
# oyunun başlığını belirliyorum.
screen.title("SNAKE GAME")
screen.tracer(0)

# ilgili sınıflardan nesnelerimi oluşturuyorum.
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# tuş dinlemeyi açıyoruz : listen 
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# oyun_devam_durumu değişkenini oluşturuyorum. bunu oyunumun sonlanmasında ve daha bir çok yerde kullanacağım.
oyun_devam_durumu = True

while oyun_devam_durumu:
    screen.update()
    time.sleep(0.1)
    # time.sleep ekranın o hareket boyunca uyuma süresi
    snake.move()
    # ekran uyuyor yılan hareket ediyor ekran güncelleniyor yani yılanın segmentlerinin teker teker hareket etmesini oyuncuya göstermeden gerçekleştiriyorum.



    # yeme uzaklık durumu belirli bir değerden küçük olursa yediğini varsayabiliriz. bu durumda yem yenilenecek yılanın boyu uzayacak ve skor arttırılacak.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.skor_arttirma()


    # yılanın belirlenen 600-600 lük alanın duvarına değmesi durumudur.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        oyun_devam_durumu = False
        scoreboard.game_over()

    # başı hariç diğer segmentlerin baş ile arasındaki uzaklık 10 dan küçükse yılanın başı kuyrukta bir segmentine değmiştir diyebilirim. bu durumda oyun sona erecektir game_over fonksiyonu çalışır.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            oyun_devam_durumu = False
            scoreboard.game_over()

# screen.exitonclick()  yardımıyla ekran biz tıklayıncaya kadar açık kalır.
screen.exitonclick()



