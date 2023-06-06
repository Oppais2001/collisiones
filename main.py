
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
import kivy
kivy.require('1.9.0')

class Videogame(App):
    def __init__(self, **kwargs):
        super(Videogame, self).__init__(**kwargs)
        target_width = 2160 #ancho de la pantalla
        target_height = 1080 #alto de la pantalla
        Window.size = (target_width, target_height)#configuracion de la pantalla
        Window.rotation = 0
        self.personaje=AsyncImage(source="./images/0.png",pos=(100,100))
        self.obstaculo=AsyncImage(source="./images/rock.png", pos=(0,0))
        self.button_Arriba=Button(text="Arriba",color=("black"),size_hint=(0.06,0.1),pos_hint={'x':0.12,'y':0.3},background_color=("blue"))
        self.button_Arriba.bind(on_press=self.Arriba)
        self.button_Arriba.bind(on_release=self.Arriba1)
        self.button_Derecha=Button(text="Derecha",color=("black"),size_hint=(0.06,0.1),pos_hint={'x':0.18,'y':0.2},background_color=("blue"))
        self.button_Derecha.bind(on_press=self.Derecha)
        self.button_Derecha.bind(on_release=self.Derecha1)
        self.button_Izquierda=Button(text="Izquierda",color=("black"),size_hint=(0.06,0.1),pos_hint={'x':0.06,'y':0.2},background_color=("blue"))
        self.button_Izquierda.bind(on_press=self.Izquierda)
        self.button_Izquierda.bind(on_release=self.Izquierda1)
        self.button_Abajo=Button(text="Abajo",color=("black"),size_hint=(0.06,0.1),pos_hint={'x':0.12,'y':0.1},background_color=("blue"))
        self.button_Abajo.bind(on_press=self.Abajo)
        self.button_Abajo.bind(on_release=self.Abajo1)
        self.direccion=""
        Clock.schedule_interval(self.update, 0.1)
        

    def build(self):
        layout = FloatLayout()
        layout.add_widget(self.buton10)
        layout.add_widget(self.button_Arriba)
        layout.add_widget(self.button_Abajo)
        layout.add_widget(self.button_Derecha)
        layout.add_widget(self.button_Izquierda)
        layout.add_widget(self.personaje)
        layout.add_widget(self.obstaculo)

        return layout#retorna la pantalla
    def update(self, dt):
        if self.direccion=="derecha":
            x+=10
        elif self.direccion=="izquierda":
            x-=10 
        elif self.direccion=="arriba": 
            y+=10
        elif self.direccion=="abajo":
            y-=10
        
        r1x,r1y=self.personaje.pos
        r1w,r1h=147,147 
        r2x,r2y=self.obstaculo.pos
        r2w,r2h=64,64
        r2y+=30
        
        if (r1x < r2x + r2w and r1x + r1w > r2w and r1y < r2y + r2h and r1y + r1h > r2y):
            print("colision")
            if self.direccion=="derecha":
                if x>0:
                    x=-10
            if self.direccion=="izquierda":
                if x<0:
                    x=10
            if self.direccion=="arriba":
                if y>0:
                    y=-10
            if self.direccion=="abajo":
                if y<0:
                    y=10
        else:
            print("no colision")
        x1,y1=self.personaje.pos
        self.personaje.pos=(x1+x,y1+y)
        
    def Derecha(self, instance):
        self.direccion="derecha"
    def Derecha1(self, instance):
        self.direccion=""
    def Abajo(self, instance):
        self.direccion="abajo"
    def Abajo1(self, instance):
        self.direccion=""
    def Izquierda(self, instance):
        self.direccion="izquierda"
    def Izquierda1(self, instance):
        self.direccion=""
    def Arriba(self, instance):
        self.direccion="arriba"
    def Arriba1(self, instance):
        self.direccion=""



    
if __name__ == '__main__':
    Videogame().run()
