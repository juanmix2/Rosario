from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Define las diferentes pantallas

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Botón 1
        btn1 = Button(text='Misterio Gozoso', font_size=24)
        btn1.bind(on_press=lambda x: self.cambiar_pantalla('screen1'))
        layout.add_widget(btn1)

        # Botón 2
        btn2 = Button(text='Misterio Luminoso', font_size=24)
        btn2.bind(on_press=lambda x: self.cambiar_pantalla('screen2'))
        layout.add_widget(btn2)

        # Botón 3
        btn3 = Button(text='Misterio Doloroso', font_size=24)
        btn3.bind(on_press=lambda x: self.cambiar_pantalla('screen3'))
        layout.add_widget(btn3)

        # Botón 4
        btn4 = Button(text='Misterio Glorioso', font_size=24)
        btn4.bind(on_press=lambda x: self.cambiar_pantalla('screen4'))
        layout.add_widget(btn4)
         
        # Botón 5
        btn5 = Button(text='Instruccion', font_size=24)
        btn5.bind(on_press=lambda x: self.cambiar_pantalla('screen5'))
        layout.add_widget(btn5)
        self.add_widget(layout)

    def cambiar_pantalla(self, nombre_pantalla):
        self.manager.current = nombre_pantalla

class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Este misterio se reza los lunes y sabado\n\n1-La encarnacion del hijo de Dios\n2-La visitacion de la Virgen a su prima Santa Isabel\n3-El nacimiento de Jesús en Belén\n4-La presentacion del niño en el templo\n5-El niño perdido y encontrado en el templo ', font_size=32)
        btn_back = Button(text='Volver al Menú', font_size=24)
        btn_back.bind(on_press=lambda x: self.cambiar_a_menu())
        layout.add_widget(label)
        layout.add_widget(btn_back)
        self.add_widget(layout)

    def cambiar_a_menu(self):
        self.manager.current = 'menu'

# Define las demás pantallas de manera similar

class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Este misterio se reza en jueves\n\n1-El bautismo de Jesus en el Jordan\n2-Las bodas de Caná\n3-Anuncio del reinoy necesidad de la conversion\n4-La Transfiguracion del Señor\n5-La institucion de la sagrada eucaristia', font_size=32)
        btn_back = Button(text='Volver al Menú', font_size=24)
        btn_back.bind(on_press=lambda x: self.cambiar_a_menu())
        layout.add_widget(label)
        layout.add_widget(btn_back)
        self.add_widget(layout)

    def cambiar_a_menu(self):
        self.manager.current = 'menu'

class Screen3(Screen):
    def __init__(self, **kwargs):
        super(Screen3, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Este misterio se reza los martes y viernes\n\n1-La oracion de Jesús en el Huerto\n2-La flagelacion del Señor\n3-La coronacion de espinas\n4-Jesús con la crus a cuestas\n5-Jesús muere en la cruz', font_size=32)
        btn_back = Button(text='Volver al Menú', font_size=24)
        btn_back.bind(on_press=lambda x: self.cambiar_a_menu())
        layout.add_widget(label)
        layout.add_widget(btn_back)
        self.add_widget(layout)

    def cambiar_a_menu(self):
        self.manager.current = 'menu'

class Screen4(Screen):
    def __init__(self, **kwargs):
        super(Screen4, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Este misterio se reza los miercoles y domingo\n\n1-La resurreccion del Señor\n2-La Asencion del Señor\n3-La Venida del Espiritu Santo\n4-La Asuncion de la Virgen al Cielo\n5-La Coronación de  la Virgen María', font_size=32)
        btn_back = Button(text='Volver al Menú', font_size=24)
        btn_back.bind(on_press=lambda x: self.cambiar_a_menu())
        layout.add_widget(label)
        layout.add_widget(btn_back)
        self.add_widget(layout)

    def cambiar_a_menu(self):
        self.manager.current = 'menu'
        
class Screen5(Screen):
    def __init__(self, **kwargs):
        super(Screen5, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Por la señal de la Santa Cruz...\nSeñor mío Jesucristo...\nV.Abre Señor mis labios\nR.Y mi boca proclamara tus alabanzas\nV.Ven oh Dios, en mi ayuda\nR.Apresurate Señor a socorrerme\n\nGloria al padre y al hijo y al Espiritu Santo\nComo era en el principio, ahora y siempre,por los siglos de los siglos\nAmen\n\n [i] A continuacion se reza cada uno de los Misterios\nque corresponden al dia, de la siguiente manera se enuncia al misterio[/i]\n\n Padre nuestro\n Ave maria(10 veces)\nGloria', font_size=12, markup=True )
        btn_back = Button(text='Volver al Menú', font_size=24)
        btn_back.bind(on_press=lambda x: self.cambiar_a_menu())
        layout.add_widget(label)
        layout.add_widget(btn_back)
        self.add_widget(layout)

    def cambiar_a_menu(self):
        self.manager.current = 'menu'       

class BotoneraApp(App):
    def build(self):
        sm = ScreenManager()

        # Añadir pantallas al ScreenManager
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        sm.add_widget(Screen3(name='screen3'))
        sm.add_widget(Screen4(name='screen4'))
        sm.add_widget(Screen5(name='screen5'))
        return sm

if __name__ == '__main__':
    BotoneraApp().run()
