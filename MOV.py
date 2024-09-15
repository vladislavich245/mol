from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import txt_instruction, txt_test1 , txt_test3, txt_sits
from ruffier import test


age = 7
name = ''
p1,p2,p3 = 0,0,0

class InstrScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = label(text=txt_instruction)
        lbl1 = Label(text="Введіть ім'я:",halign="right")
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text="Введіть вік:",halign="right")
        self.in.age = TextInput(text='7',multiline=False)
        self.btn = Button(
            text="Почати", size_hint=(0.3,0.2), pos_hint={'center_x': 0.5}
        )
        self.btn.on_press = self.next
        line1=BoxLayout(size_hint=(0.8, None), height='30sp')
        line2=BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_name)
        outer = BoxLayout(orientation='vertical',padding=8,spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget((outer))

    def next(self):
        global name
        name = self.in_name.text
        self.manager.current = 'plural'

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test1)
        line = BoxLayout(size_hint=(0.8,None), height='30sp')
        lbl_result = Label(text='Введіть результат:',halign="right")
        self.in_result = TextInput(text='0',multiline=False)
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)




