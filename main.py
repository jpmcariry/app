from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.metrics import sp
from kivy.core.window import Window
from sqlite3 import connect


path = r'source/Database'
conn = connect(path + '/data.db')
cursor = conn.cursor()
cursor.execute("""
create table if not exists cadastro(
    restart integer default 0
);
""")
#Window.fullscreen = True
'''from kivy.core.image import Image as CoreImage
data = io.BytesIO(open("img/Mapa.jpg", "rb").read())
im = CoreImage(data, ext="jpg",pos_hint={'x':0.0, 'y':0.0})'''
'''from kivy.utils import platform
if platform == 'android':
    system = "android"
elif platform == "linux" or platform == "linux2" or platform == "darwin":
    system = "linux"
elif platform == "win32":
    system = "Win"
system="android"'''

class WindowManager(ScreenManager):
    pass
# Create the screen manager
screen_manager = WindowManager()

class Sprite(Image):
    def __init__(self, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.size = self.texture_size

screen_status=1
class Play(Screen):
    pass
class Play_Layout(FloatLayout):
    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None
        print("closed")
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if(text=="1"):
            print(text)
            self.personagem.source = "atlas://source/img/anim/saitama.atlas/parado"
        if (text == "2"):
            print(text)
            self.personagem.source = "atlas://source/img/anim/saitama.atlas/frente"
        if (text == "3"):
            print(text)
            self.personagem.source = "atlas://source/img/anim/saitama.atlas/tras"
        if (text == "4"):
            print(text)
            self.personagem.source = "atlas://source/img/anim/saitama.atlas/preflash"
        if (text == "5"):
            print(text)
            self.personagem.source = "atlas://source/img/anim/saitama.atlas/flash"
        if (text == "6"):
            print(text)
            self.personagem.source = "atlas://source/img/anim/saitama.atlas/flash2"

        self.keysPressed.add(text)
    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if (text in self.keysPressed):
            self.keysPressed.remove(text)

    def move_x(self, dt):
        self.move[1] = True

    def move_x_sub(self, dt):
        self.move[0] = True

    def move_y(self, dt):
        self.move[2] = True

    def move_y_sub(self, dt):
        self.move[3] = True

    def r_move_x(self, dt):
        self.move[1] = False

    def r_move_x_sub(self, dt):
        self.move[0] = False

    def r_move_y(self, dt):
        self.move[2] = False

    def r_move_y_sub(self, dt):
        self.move[3] = False

    def anima(self, direction):
        try:
            time
        except:
            from time import time
        if (time() >= self.anim_forward):
            if (direction == "direita"):
                print("direita")
                self.anim_forward = (time()) + 0.12
                if (self.last_texture.find("direita") == -1 or self.last_texture=="direita"):
                    print("start")
                    self.personagem.source = "atlas://source/img/anim/saitama.atlas/frente"
                    self.last_texture = "direita1"
                elif (self.last_texture == "direita1"):
                    self.last_texture = "direita2"
                elif (self.last_texture == "direita2"):
                    self.personagem.source = "atlas://source/img/anim/saitama.atlas/parado"
                    self.last_texture = "direita3"
                elif (self.last_texture == "direita3"):
                    self.personagem.source = "atlas://source/img/anim/saitama.atlas/tras"
                    self.last_texture = "direita4"
                elif (self.last_texture == "direita4"):
                    self.personagem.source = "atlas://source/img/anim/saitama.atlas/parado"
                    self.last_texture = "direita"
            if (direction == "esquerda"):
                self.anim_forward = (time()) + 0.12
                if (self.last_texture.find("esquerda") == -1 or self.last_texture == "esquerda"):
                    print("start")
                    self.personagem.source = "atlas://source/img/anim/saitama.atlas/frente"
                    self.last_texture = "esquerda1"
                    self.personagem.angle =32
                elif (self.last_texture == "esquerda1"):
                    self.last_texture = "esquerda2"
                elif (self.last_texture == "esquerda2"):
                    self.personagem.source = "atlas://source/img/anim/saitama.atlas/parado"
                    self.last_texture = "esquerda3"
                elif (self.last_texture == "esquerda3"):
                    self.personagem.source = "atlas://source/img/anim/saitama.atlas/tras"
                    self.last_texture = "esquerda4"
                elif (self.last_texture == "esquerda4"):
                    self.personagem.source = "atlas://source/img/anim/saitama.atlas/parado"
                    self.last_texture = "esquerda"
    def pulo(self):
        print("pulo")
        self.count_pulo+=1
        if(self.count_pulo==0):
            pass

    def update(self, dt=1):
        if(screen_manager.current == "play"):
            global screen_status;
            if(screen_status==1):
                screen_status = 2
                print("dentro play")
                system = "android"
                try:
                    time
                    Builder
                    NumericProperty
                except:
                    from kivy.properties import NumericProperty
                    from time import time
                    from kivy.lang import Builder

                self.kv=Builder.load_string('''
<RotatedImage>:
    canvas.before:
        PushMatrix
        Rotate:
            angle: root.angle
            axis: 0, 0, 1
            origin: root.center
    canvas.after:
        PopMatrix
                ''')

                class RotatedImage(Image):
                    angle = NumericProperty()
                self.last_texture = "parado"
                self.tempo= time()
                self.count_pulo=0
                self.count_fps=0
                self.on_ground=True
                self.anim_forward = self.tempo
                self.fps = Label(text="", pos_hint={'x': 0.45, 'y': 0.45}, font_size=40, color=[0.8, 0.8, 0.0, 1])
                self.move = [False,False,False,False]
                self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
                self._keyboard.bind(on_key_down=self._on_key_down)
                self._keyboard.bind(on_key_up=self._on_key_up)
                self.keysPressed = set()
                self.mapa=RotatedImage(source="source/img/arena/caverna.png")
                self.mapa.size_hint = (1.4,1.0)
                self.mapa.pos_hint={"x":-0.2,"y":0.0}
                self.mapa.allow_stretch = True
                self.mapa.keep_ratio = False
                self.personagem = Image(source="atlas://source/img/anim/saitama.atlas/parado", size_hint=(0.15,0.3))
                self.personagem.pos_hint={"x":0.5-(self.personagem.size_hint_x/2),"y":0.15-(self.personagem.size_hint_y/2)}
                self.personagem.allow_stretch = True
                self.personagem.keep_ratio = False
                self.butao_x = Button(text="direita", size_hint=(0.1, 0.1), pos_hint={'x': 0.2, 'y': 0.05}, opacity=0.55)
                self.butao_x.bind(on_press=self.move_x, on_release=self.r_move_x)
                self.butao_y = Button(text="cima", size_hint=(0.1, 0.1), pos_hint={'x': 0.1, 'y': 0.15}, opacity=0.55)
                self.butao_y.bind(on_press=self.move_y, on_release=self.r_move_y)
                self.butao_x_sub = Button(text="esquerda", size_hint=(0.1, 0.1), pos_hint={'x': 0.0, 'y': 0.05}, opacity=0.55)
                self.butao_x_sub.bind(on_press=self.move_x_sub, on_release=self.r_move_x_sub)
                self.butao_y_sub = Button(text="baixo", size_hint=(0.1, 0.1), pos_hint={'x': 0.1, 'y': 0.0}, opacity=0.55)
                self.butao_y_sub.bind(on_press=self.move_y_sub, on_release=self.r_move_y_sub)
                self.add_widget(self.mapa)
                self.add_widget(self.personagem)
                self.add_widget(self.fps)
                self.add_widget(self.butao_x)
                self.add_widget(self.butao_x_sub)
                self.add_widget(self.butao_y)
                self.add_widget(self.butao_y_sub)
                try:
                    Clock
                except:
                    from kivy.clock import Clock
                finally:
                    Clock.schedule_interval(self.update, 0)
            else:
                try:
                    time
                    Clock
                except:
                    from time import time
                    from kivy.clock import Clock
                print(round(time(),1))
                if self.tempo <= time():
                    self.tempo = self.tempo + 0.5
                    self.count_fps+=1
                    if self.count_fps==2:
                        self.tempo = self.tempo + 1
                        self.fps.text = str(int(Clock.get_fps()))
                        self.count_fps = 0
                currentx = 0
                currenty = 0
                step_size = dt*0.037   # canwalk_map=[[000,-600,000,-400]]
                if(("w" in self.keysPressed and "a" in self.keysPressed) or (
                        self.move[2] == True and self.move[0] == True)):
                    if (self.on_ground == True):
                        self.pulo()
                    currentx += step_size * 2
                elif (("w" in self.keysPressed and "d" in self.keysPressed) or (
                        self.move[2] == True and self.move[1] == True)):
                    if (self.on_ground == True):
                        self.pulo()
                    currentx -= step_size * 2
                elif (("s" in self.keysPressed and "a" in self.keysPressed and "k" in self.keysPressed) or (
                        self.move[3] == True and self.move[0] == True and self.atack == True)):
                    if (self.on_ground == True):
                        self.anima("chute_e")
                elif (("s" in self.keysPressed and "d" in self.keysPressed and "k" in self.keysPressed) or (
                        self.move[3] == True and self.move[1] == True and self.atack == True)):
                    if (self.on_ground == True):
                        self.anima("chute_d")
                elif ("w" in self.keysPressed or self.move[2] == True):
                    if(self.on_ground==True):
                        self.pulo()
                elif ("a" in self.keysPressed or self.move[0] == True):
                    currentx += step_size * 3
                    if (self.on_ground == True):
                        self.anima("esquerda")
                elif ("d" in self.keysPressed or self.move[1] == True):
                    currentx -= step_size * 3
                    if (self.on_ground == True):
                        self.anima("direita")
                elif ("s" in self.keysPressed or self.move[3] == True):
                    if (self.on_ground == True):
                        self.anima("baixo")
                    '''currenty += step_size * 3'''
                else:
                    self.last_texture = "parado"
                    self.personagem.source = "atlas://source/img/anim/saitama.atlas/parado"
                '''print(self.mapa.pos_hint["x"],self.mapa.pos_hint["y"])
                print(self.mapa.pos[0], self.mapa.pos[1])
                print(currentx, currenty)'''
                if(self.mapa.pos_hint["x"]<=-0.4  or self.mapa.pos_hint["x"]>=0.0):
                    if(self.personagem.pos_hint["x"]<=0.02):
                        print("limite esquerdo")
                        if (currentx>0):
                            currentx=0
                        initx = self.personagem.pos_hint["x"]
                        inity = self.personagem.pos_hint["y"]
                        self.personagem.pos_hint = {"x": initx - currentx, "y": inity - currenty}
                    elif(self.personagem.pos_hint["x"]>=0.85):
                        print("limite direito")
                        if(currentx<0):
                            currentx = 0
                        initx = self.personagem.pos_hint["x"]
                        inity = self.personagem.pos_hint["y"]
                        self.personagem.pos_hint = {"x": initx - currentx, "y": inity - currenty}
                    elif(self.personagem.pos_hint["x"]<=0.25 and self.mapa.pos_hint["x"]<=0.0):
                        print("com limite na direita e se movendo pra esquerda")
                        initx = self.mapa.pos_hint["x"]
                        inity = self.mapa.pos_hint["y"]
                        self.mapa.pos_hint = {"x": initx + currentx, "y": inity + currenty}
                    elif(self.personagem.pos_hint["x"] >= 0.6 and self.mapa.pos_hint["x"]>=0.0):
                        print("com limite na esquerda e se movendo pra direita")
                        initx = self.mapa.pos_hint["x"]
                        inity = self.mapa.pos_hint["y"]
                        self.mapa.pos_hint = {"x": initx + currentx, "y": inity + currenty}
                    else:
                        initx = self.personagem.pos_hint["x"]
                        inity = self.personagem.pos_hint["y"]
                        self.personagem.pos_hint = {"x": initx - currentx, "y": inity - currenty}
                else:
                    initx = self.mapa.pos_hint["x"]
                    inity = self.mapa.pos_hint["y"]
                    self.mapa.pos_hint = {"x":initx+currentx, "y":inity+currenty}
        else:
            try:
                self.clear_widgets()
                Clock
            except:
                from kivy.clock import Clock
            finally:
                print("limpo")
                Clock.schedule_interval(self.update, 0)




play = Play(name="play")

class Opcoes(FloatLayout):
    try:
        ObjectProperty
    except:
        from kivy.properties import ObjectProperty
class Main(Screen):
    def join(self, bt):
        try:
            post
            getnode
        except:
            from uuid import getnode
            from requests import post
        if(main.sel_icone.source=="source/img/icone/img_vazia.jpg" or self.sel_txti.text=="Nome do personagem" or self.sel_txti.text==""):
            try:
                Popup
            except:
                from kivy.uix.popup import Popup
            alert= FloatLayout()
            btn = Button(text="Ok",size_hint=(.4,.2), on_press=self.dismiss_popup)
            btn.pos_hint={"x":0.5 - (btn.size_hint[0]/2),"y":0.05}
            if(main.sel_icone.source=="source/img/icone/img_vazia.jpg"):
                alert_msg=Label(text="Selecione um personagem\nantes de jogar!!")
            else:
                alert_msg=Label(text="Escolha um nome para\nseu personagem")
            alert_msg.halign= 'center'
            alert_msg.valign= 'middle'
            alert_msg.font_size=sp(17*Window.size[1]/600)
            alert_msg.size_hint=(0.4, 0.15)
            alert_msg.pos_hint={"x":0.5-(alert_msg.size_hint[0]/2),"y":0.2+btn.size_hint[1]+btn.pos_hint["y"]}

            alert_msg.background_color=(0.5, 1, 0.5, 0.5)
            alert.add_widget(alert_msg)
            alert.add_widget(btn)
            self._popup = Popup(title="Configurações", content=alert,
                                size_hint=(0.5, 0.5))
            self.pos_hint={"x":0.5- (self._popup.size_hint[0] / 2),"y":0.5-(self._popup.size_hint[1]/2)}
            self._popup.open()
        else:
            try:
                self.free
            except:
                difer=2
                alert_msg = Label(text="Use o botão 'Check'!!")
            else:
                if(self.free==False):
                    difer=1
                else:
                    difer=0

            finally:
                if (difer == 0):
                    ip = str(getnode())
                    url = "http://10.0.0.109:5000/match"
                    json = {"user_ip": ip, "server": bt.id, "user_name": self.sel_txti.text,
                            "personagem": selecao.perso_name}
                    headers = {"Content-Type": "application/json"}
                    response = post(url=url, json=json, headers=headers,
                                    verify=False)  # envia token + json ignorando SSl(certificado)
                    play_layout = Play_Layout()
                    play_layout.update()
                    screen_manager.current = "play"
                    play.add_widget(play_layout)
                else:
                    if(difer==2):
                        alert_msg = Label(text="Use o botão 'Check'!!")
                    else:
                        alert_msg = Label(text="Nome indisponivel\nuse o botão 'Check'!!")
                    try:
                        Popup
                    except:
                        from kivy.uix.popup import Popup
                    alert = FloatLayout()
                    btn = Button(text="Ok", size_hint=(.4, .2), on_press=self.dismiss_popup)
                    btn.pos_hint = {"x": 0.5 - (btn.size_hint[0] / 2), "y": 0.05}

                    alert_msg.halign = 'center'
                    alert_msg.valign = 'middle'
                    alert_msg.font_size = sp(17 * Window.size[1] / 600)
                    alert_msg.size_hint = (0.4, 0.15)
                    alert_msg.pos_hint = {"x": 0.5 - (alert_msg.size_hint[0] / 2),
                                          "y": 0.2 + btn.size_hint[1] + btn.pos_hint["y"]}

                    alert_msg.background_color = (0.5, 1, 0.5, 0.5)
                    alert.add_widget(alert_msg)
                    alert.add_widget(btn)
                    self._popup = Popup(title="Configurações", content=alert,
                                        size_hint=(0.5, 0.5))
                    self.pos_hint = {"x": 0.5 - (self._popup.size_hint[0] / 2), "y": 0.5 - (self._popup.size_hint[1] / 2)}
                    self._popup.open()

    def clean(self, instance,value):
        if value:
            self.sel_txti.text=""
        else:
            if(self.sel_txti.text==""):
                self.sel_txti.text = "Nome do personagem"
    def check(self,btn):
        if(main.sel_icone.source=="source/img/icone/img_vazia.jpg" or self.sel_txti.text=="" or self.sel_txti.text=="Nome do personagem"):
            try:
                Popup
            except:
                from kivy.uix.popup import Popup
            alert = FloatLayout()
            btn = Button(text="Ok", size_hint=(.4, .2), on_press=self.dismiss_popup)
            btn.pos_hint = {"x": 0.5 - (btn.size_hint[0] / 2), "y": 0.05}
            if(main.sel_icone.source=="source/img/icone/img_vazia.jpg"):
                alert_msg = Label(text="Selecione um personagem\nantes de jogar!!")
            else:
                alert_msg = Label(text="Escolha um nome para\nseu personagem")
            alert_msg.halign = 'center'
            alert_msg.valign = 'middle'
            alert_msg.font_size = sp(17 * Window.size[1] / 600)
            alert_msg.size_hint = (0.4, 0.15)
            alert_msg.pos_hint = {"x": 0.5 - (alert_msg.size_hint[0] / 2),
                                  "y": 0.2 + btn.size_hint[1] + btn.pos_hint["y"]}
            alert_msg.background_color = (0.5, 1, 0.5, 0.5)
            alert.add_widget(alert_msg)
            alert.add_widget(btn)
            self._popup=Popup(title = "Configurações", content = alert,size_hint = (0.5, 0.5))
            self._popup.open()
        else:
            try:
                getnode
                post
            except:
                from requests import post
                from uuid import getnode
            ip = str(getnode())
            url = "http://10.0.0.109:5000/match"
            json = {"user_ip": ip, "user_name": self.sel_txti.text}
            headers = {"Content-Type": "application/json"}
            response = post(url=url, json=json, headers=headers,
                            verify=False)  # envia token + json ignorando SSl(certificado)
            try:
                Popup
            except:
                from kivy.uix.popup import Popup
            alert = FloatLayout()
            btn = Button(text="Ok", size_hint=(.4, .2), on_press=self.dismiss_popup)
            btn.pos_hint = {"x": 0.5 - (btn.size_hint[0] / 2), "y": 0.05}
            if (response.status_code == 200):
                alert_msg = Label(text="Bem vindo de volta!!")
                self.free = True
            elif (response.status_code == 201):
                alert_msg = Label(text="Nome reservado!!")
                self.free = True
            else:
                alert_msg = Label(text="Nome já usado")
                self.free = False
            alert_msg.halign = 'center'
            alert_msg.valign = 'middle'
            alert_msg.font_size = sp(17 * Window.size[1] / 600)
            alert_msg.size_hint = (0.4, 0.15)
            alert_msg.pos_hint = {"x": 0.5 - (alert_msg.size_hint[0] / 2),
                                  "y": 0.2 + btn.size_hint[1] + btn.pos_hint["y"]}
            alert_msg.background_color = (0.5, 1, 0.5, 0.5)
            alert.add_widget(alert_msg)
            alert.add_widget(btn)
            self._popup=Popup(title = "Configurações", content = alert,size_hint = (0.5, 0.5))
            self._popup.open()


    def change_txti(self, instance, value=False):
        if(len(self.sel_txti.text)>=26):
            self.sel_txti.text = instance.text[:25]
            try:
                Popup
            except:
                from kivy.uix.popup import Popup
            alert = FloatLayout()
            btn = Button(text="Ok", size_hint=(.4, .2), on_press=self.dismiss_popup)
            btn.pos_hint = {"x": 0.5 - (btn.size_hint[0] / 2), "y": 0.05}
            alert_msg = Label(text="O nome deve ter no\nmáximo 25 characters")
            alert_msg.halign = 'center'
            alert_msg.valign = 'middle'
            alert_msg.font_size = sp(17 * Window.size[1] / 600)
            alert_msg.size_hint = (0.4, 0.15)
            alert_msg.pos_hint = {"x": 0.5 - (alert_msg.size_hint[0] / 2),
                                  "y": 0.2 + btn.size_hint[1] + btn.pos_hint["y"]}
            alert_msg.background_color = (0.5, 1, 0.5, 0.5)
            alert.add_widget(alert_msg)
            alert.add_widget(btn)
            self._popup=Popup(title = "Configurações", content = alert,size_hint = (0.5, 0.5))
            self._popup.open()
        else:
            pass
    def jogar(self,btn):
        print("selecao")
        try:
            GridLayout
            TextInput
        except:
            from kivy.uix.textinput import TextInput
            from kivy.uix.gridlayout import GridLayout
        self.sel_txti = TextInput(size_hint=(0.285, 0.085), multiline=False)
        self.sel_txti.pos_hint = {"x": 0.5 - self.sel_txti.size_hint_x, "y": 0.67}
        self.sel_txti.text="Nome do personagem"
        self.sel_txti.bind(focus=self.clean,text=self.change_txti)
        self.sel_btn_check = Button(id="false",text="check", size_hint=(0.1285, 0.085), pos_hint={"x": 0.5, "y": 0.67}, on_press=self.check)
        sel_btn_icone = Button(size_hint=(0.155, 0.17), on_press=selecao.opcoes, opacity=0.3)
        sel_btn_icone.pos_hint = {"x": 0.5 + self.sel_btn_check.size_hint_x, "y": 0.67}
        self.sel_icone = Image(source="source/img/icone/img_vazia.jpg", size_hint=sel_btn_icone.size_hint,
                          pos_hint=sel_btn_icone.pos_hint)
        self.sel_icone.allow_stretch = True
        self.sel_icone.keep_ratio = False

        sel_grid_image = Image(source="source/img/fundo_grid.jpg", size_hint=(0.57, 0.5), allow_stretch=True,
                               keep_ratio=False)
        sel_grid_image.pos_hint = {"x": 0.5 - (sel_grid_image.size_hint_x / 2), "y": 0.17}
        sel_grid = GridLayout(cols=2, size_hint=(0.57, 0.5))
        sel_grid.pos_hint = {"x": 0.5 - (sel_grid.size_hint_x / 2), "y": 0.17}
        for i in range(1, 3 + 1):
            sel_grid.add_widget(Label(text="Server" + str(i)))
            sel_grid.add_widget(Button(id=str(i), text="Entrar" + str(i), on_press=self.join))
        sel_image = Image(source="source/img/fundo.jpg", allow_stretch=True, keep_ratio=False)
        sel_layout = FloatLayout()
        sel_layout.add_widget(sel_image)
        sel_layout.add_widget(self.sel_txti)
        sel_layout.add_widget(self.sel_btn_check)
        sel_layout.add_widget(self.sel_icone)
        sel_layout.add_widget(sel_btn_icone)
        sel_layout.add_widget(sel_grid_image)
        sel_layout.add_widget(sel_grid)
        selecao.add_widget(sel_layout)
        screen_manager.current = selecao.name

    def dismiss_popup(self,btn):
        self._popup.dismiss()
    def resolution(self,op):
        if(self.res.text=="800x600"):
            self.res.text="1080x720"
        elif(self.res.text=="1080x720"):
            self.res.text = "1920x1080"
        else:
            self.res.text = "800x600"
    def opcoes(self,d):
        try:
            GridLayout
            Popup
        except:
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.popup import Popup
        self.op=Opcoes()
        #gd.add_widget(Button(text="gd"))
        self.lb=Label(text="resolução", size_hint= (None,None))
        self.btn=Button(text="confirmar",size_hint=(0.4,0.2),background_color=(0.5,1,0.5,0.5),on_press=self.dismiss_popup)
        self.btn.pos_hint={"x":(0.5-(self.btn.size_hint[0]/2)),"y":0.0}
        self.btn.background_normal=""
        self.gd = GridLayout(cols=2, size_hint=(0.8, 1-self.btn.size_hint_y))
        self.gd.pos_hint={"x":0.1,"y":self.btn.size_hint_y}
        self.gd.background_normal = ""
        self.gd.background_color = (0.5, 1, 0.5, 0.5)
        self.gd.add_widget(Label(text="Resolução"))
        self.res=Button(text="800x600", on_release=self.resolution)
        self.gd.add_widget(self.res)
        self.gd.add_widget(Label(text="rs"))
        self.gd.add_widget(Button(text="Ok"))
        self.op.add_widget(self.gd)
        self.op.add_widget(self.btn)
        content = self.op
        self._popup = Popup(title="Configurações", content=content,size_hint=(0.5,0.5))
        self._popup.pos_hint ={"x":0.5-(self._popup.size_hint[0]/2),"y":0.5-(self._popup.size_hint[1]/2)}
        self._popup.open()

main = Main(name="main")


class Selecao(Screen):
    def jogar(self, btn):
        screen_manager.current = selecao.name

    def dismiss_popup(self, btn):
        print("demiss", self.count)
        if (self.count == 0):
            main.sel_icone.source = self.icone.source = "source/img/icone/goku.png"
            self.perso_name = "Goku"
        if (self.count == 1):
            self.perso_name="Saitama"
            main.sel_icone.source = self.icone.source = "source/img/icone/saitama.jpg"
        self._popup.dismiss()

    def resolution(self, op):
        if (self.res.text == "800x600"):
            self.res.text = "1080x720"
        elif (self.res.text == "1080x720"):
            self.res.text = "1920x1080"
        else:
            self.res.text = "800x600"

    def opcoes(self, d):
        try:
            GridLayout
            Popup
        except:
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.popup import Popup
        self.layout_internal = Opcoes()
        # gd.add_widget(Button(text="gd"))
        self.btn = Button(text="confirmar",font_size=sp(20*Window.size[1]/600), size_hint=(0.4, 0.15), background_color=(0.5, 1, 0.5, 0.5),
                          on_press=self.dismiss_popup)
        self.btn.pos_hint = {"x": (0.5 - (self.btn.size_hint[0] / 2)), "y": 0.1}
        self.btn.background_normal = ""
        self.gd = GridLayout(cols=2, size_hint=(0.5, 0.55 - self.btn.size_hint_y))
        self.gd.pos_hint = {"x": 0.5-(self.gd.size_hint_x/2), "y": self.btn.size_hint_y+self.btn.pos_hint["y"]}
        try:
            source= self.icone.source
            name=self.lb_name_value.text
            ataque=self.lb_ataque_value.text
            vida= self.lb_vida_value.text
        except:
            self.count = 0
            source = "source/img/icone/goku.png"
            name="Goku"
            ataque="120"
            vida="400"
        self.icone = Image(source=source, size_hint=(0.25, 0.25), keep_ratio=False, allow_stretch=True)
        self.icone.pos_hint = {"x": 0.5 - (self.icone.size_hint_x / 2), "y":self.gd.pos_hint["y"]+self.gd.size_hint_y}
        self.count_lb = 3
        self.lb_name = Label(text="Nome:", size_hint=(0.5, 2 + 1 / self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.lb_name_value = Label(text=name, size_hint=(0.5, 2 + 1 / self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.lb_ataque = Label(text="Ataque:", size_hint=(0.5, 2+1/self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.lb_ataque_value = Label(text=ataque, size_hint=(0.5, 2+1/self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.lb_vida = Label(text="Vida", size_hint=(0.5, 2+1/self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.lb_vida_value = Label(text=vida, size_hint=(0.5, 2+1/self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.pass_left = Button(id="left",size_hint=(0.17, 0.3), background_normal="source/img/seta_left.png", on_press=self.passa)
        self.pass_left.pos_hint={"x": 0.02 - (self.pass_left.size_hint_x / 2), "y":0.5-(self.pass_left.size_hint_y/2)}
        self.pass_right = Button(id="right",size_hint=(0.17, 0.3), background_normal="source/img/seta_right.png", on_press=self.passa)
        self.pass_right.pos_hint = {"x": 0.97 - (self.pass_right.size_hint_x / 2),
                                   "y": 0.5 - (self.pass_right.size_hint_y / 2)}
        self.layout = FloatLayout()
        self.layout.orientation = "horizontal"
        self.layout.size_hint = (1, 1)
        self.layout.pos_hint = {"x": 0.5 - (self.layout.size_hint[0] / 2), "y": 0.5 - (self.layout.size_hint[1] / 2)}
        self.layout_image = Image(source="source/img/fundo.jpg", size_hint=(1, 1), keep_ratio=False, allow_stretch=True)
        self.layout_image.pos_hint = {"x": 0.0, "y": 0.0}  # self.layout.pos_hint
        self.layout_internal.size_hint=(self.layout.size_hint[0]*0.8,self.layout.size_hint[1]*0.8)
        self.layout_internal.pos_hint = {"x":self.layout.pos_hint["x"]+((1-self.layout_internal.size_hint_x)/2),"y":self.layout.pos_hint["y"]+((1-self.layout_internal.size_hint_y)/2)}
        self.layout_internal_image = Image(source="source/img/fundo_grid.jpg", size_hint=(0.7,1), keep_ratio=False, allow_stretch=True)
        self.layout_internal_image.pos_hint={"x":0.5-(self.layout_internal_image.size_hint_x/2),"y":0.}
        self.layout_internal.add_widget(self.layout_internal_image)
        self.layout_internal.add_widget(self.pass_left)
        self.layout_internal.add_widget(self.pass_right)
        self.layout_internal.add_widget(self.icone)
        self.layout_internal.add_widget(self.gd)
        self.layout_internal.add_widget(self.btn)
        self.gd.add_widget(self.lb_name)
        self.gd.add_widget(self.lb_name_value)
        self.gd.add_widget(self.lb_ataque)
        self.gd.add_widget(self.lb_ataque_value)
        self.gd.add_widget(self.lb_vida)
        self.gd.add_widget(self.lb_vida_value)
        self.layout.add_widget(self.layout_image)
        self.layout.add_widget(self.layout_internal)
        content = self.layout
        self._popup = Popup(title="Personagem Selection", content=content, size_hint=(0.65,0.8))
        self._popup.pos_hint={"x": 0.5-(self._popup.size_hint_x/2),"y": 0.5-(self._popup.size_hint_y/2)}
        self._popup.open()
    def passa(self, bt):
        if(bt.id=="right"):
            self.count +=1
            if (self.count == 2):
                self.count = 0
        else:
            self.count -=1
            if(self.count==-1):
                self.count=1
        print(self.count)
        if (self.count == 0):
            try:
                self.icone.source = "source/img/icone/goku.png"
            except:
                pass
            self.lb_name_value.text = "Goku"
            self.lb_ataque_value.text = "120"
            self.lb_vida_value.text = "800"
        if (self.count == 1):
            try:
                self.icone.source = "source/img/icone/saitama.jpg"
            except:
                pass
            self.lb_name_value.text = "Saitama"
            self.lb_ataque_value.text = "160"
            self.lb_vida_value.text = "600"




selecao = Selecao(name="selecao")




class Loading(Screen):
    pass

class Loading_Layout(FloatLayout):
    try:
        StringProperty
    except:
        from kivy.properties import StringProperty
    fps = StringProperty(None)

    def __init__(self, **kwargs):
        try:
            Clock
        except:
            from kivy.clock import Clock
        super(Loading_Layout, self).__init__(**kwargs)
        Clock.schedule_once(self.conn, 1)

    def conn(self, dt):
        try:
            post
            getnode
        except:
            from uuid import getnode
            from requests import post
        try:
            ip = str(getnode())
            url = "http://10.0.0.109:5000/register"
            json = {"user_ip": ip, "user_resoluction": "1280x299"}
            headers = {"Content-Type": "application/json"}
            response = post(url=url, json=json, headers=headers,
                                     verify=True)  # envia token + json ignorando SSl(certificado)
            self.text = str(response.json())
        except:
            print("timeout")
            try:
                Clock
            except:
                from kivy.clock import Clock
            Clock.schedule_once(self.conn, 6)
        else:
            '''main_layout_title = Label(text="Fight Battle", font_name="source/font/mv-boli.ttf", color=(0, 0, 0, 1),
                                      size_hint=(0.23, 0.3), font_size=sp(82 * Window.size[1] / 600))
            main_layout_title.pos_hint = {"x": 0.523 - (main_layout_title.size_hint_x / 2), "y": 0.653}'''

            main_layout_btn_jogar_image = Image(source="source/img/bg_botao.jpg", size_hint=(.255, .109),
                                                allow_stretch=True, keep_ratio=False)
            main_layout_btn_opcoes_image = Image(source="source/img/bg_btn_opcoes.jpg", size_hint=(.255, .109),
                                                 allow_stretch=True, keep_ratio=False)

            main_btn_jogar = Button(text="jogar", opacity=0.0, size_hint=(.255, .109), on_press=main.jogar)
            main_layout_btn_jogar_image.pos_hint = main_btn_jogar.pos_hint = {
                "x": 0.522 - float(main_btn_jogar.size_hint_x / 2), "y": 0.415}

            main_btn_opcao = Button(text="opções", opacity=0.0, size_hint=(.255, .109), on_press=main.opcoes)
            main_layout_btn_opcoes_image.pos_hint = main_btn_opcao.pos_hint = {
                "x": 0.522 - float(main_btn_opcao.size_hint_x / 2), "y": 0.29}

            main_image = Image(source="source/img/tela_bg.jpg")
            main_image.allow_stretch = True
            main_image.keep_ratio = False
            main_layout = FloatLayout()
            main_layout.add_widget(main_image)
            main_layout.add_widget(main_layout_btn_jogar_image)
            main_layout.add_widget(main_layout_btn_opcoes_image)
            main_layout.add_widget(main_btn_jogar)
            main_layout.add_widget(main_btn_opcao)
            #main_layout.add_widget(main_layout_title)
            main.add_widget(main_layout)
            screen_manager.current = "main"

loading_bg_image = Image(source="source/img/loading_bg.jpg", size_hint=(1,1), allow_stretch=True, keep_ratio=False)
loading_image = Image(source="source/img/connection.gif",size_hint=(0.2,0.2),anim_delay=0.04, allow_stretch=True,keep_ratio=False)
loading_image.pos_hint = {"x" : 0.65-(loading_image.size_hint_x/2), "y" : 0.5-(loading_image.size_hint_y/2)}
loading_label = Label(text="trying connection: ", font_size = sp(20*Window.size[1]/600))
loading_label.pos_hint = {"x" : 0.45-(loading_label.size_hint_x/2), "y" : 0.5-(loading_label.size_hint_y/2)}
loading_layout =Loading_Layout()
loading_layout.add_widget(loading_bg_image)
loading_layout.add_widget(loading_label)
loading_layout.add_widget(loading_image)

loading = Loading(name="loading")
loading.add_widget(loading_layout)


screen_manager.transition = FadeTransition()
screen_manager.add_widget(loading)
screen_manager.add_widget(main)
screen_manager.add_widget(selecao)
screen_manager.add_widget(play)

from kivy.app import App
class GameApp(App):
    def build(self):
        return screen_manager

if __name__ == '__main__':
    GameApp().run()
