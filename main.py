from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class QueryApp(App):
    def build(self):
        lay = BoxLayout(orientation='vertical')
        self.inp = TextInput(hint_text='输入API地址')
        self.lbl = Label(text='结果将显示在此')
        btn = Button(text='查询')
        btn.bind(on_press=self.go)
        lay.add_widget(Label(text='隐私查询工具'))
        lay.add_widget(self.inp)
        lay.add_widget(btn)
        lay.add_widget(self.lbl)
        return lay

    def go(self, _):
        url = self.inp.text.strip()
        if not url:
            self.lbl.text = '请输入API地址'
            return
        try:
            r = requests.get(url, timeout=10)
            self.lbl.text = r.text[:300]
        except Exception as e:
            self.lbl.text = str(e)

if __name__ == '__main__':
    QueryApp().run()
