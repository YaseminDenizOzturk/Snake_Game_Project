from turtle import Turtle
BASLANGİC_DURUMLARİ = [(0,0),(-20,0),(-40,0)]
HAREKET_MESAFESİ = 20
UP = 90
DOWN = 270
LEFT = 180
RİGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.yilanimizi_olusturalim()
        self.head = self.segments[0]
        # yılanın başını segments dizisinin ilk elemanıdır.
    
    # yeni segment ekleme fonksiyonu
    def yilana_segment_ekle(self,position):
        new_segment = Turtle("circle")
        new_segment.color("yellow green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        # append sonuna ekleme fonksiyonudur.

    def yilanimizi_olusturalim(self):
        for position in BASLANGİC_DURUMLARİ:
            # for döngüsü içinde BASLANGİC_DURUMLARİ nın her bir elemanı position dur.
            self.yilana_segment_ekle(position)
            # belirlenen pozisyonlara yeni segment eklenir.
            # yılanın her bir segmentinin uzunluğu 20 varsayıldığı için pozisyonlar 0 ,-20, -40 şeklindedir.


    def extend(self):
        self.yilana_segment_ekle(self.segments[-1].position())

    def move(self):
        # range parametreleri 
        for segment_no in range(len(self.segments) -1,0,-1):
            new_x = self.segments[segment_no -1].xcor()
            new_y = self.segments[segment_no -1].ycor()
            self.segments[segment_no].goto(new_x,new_y)
        self.head.forward(HAREKET_MESAFESİ)
    

    # yılanın kendi üzerinden aşağı giderken yukarı dönemeyeceği için 
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    # yılanın kendi üzerinden yukarı giderken aşağı dönemeyeceği için 
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    # yılanın kendi üzerinden sağa giderken sola dönemeyeceği için 
    def left(self):
        if self.head.heading() != RİGHT:
            self.head.setheading(LEFT)
    # yılanın kendi üzerinden sola giderken sağa dönemeyeceği için 
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RİGHT)

    