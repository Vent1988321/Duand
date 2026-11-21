from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class QueryApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.url_input = TextInput(hint_text='输入API地址 (如 http://xxx.com/query)', size_hint_y=None, height=50)
        self.result_label = Label(text='结果将显示在此', size_hint_y=0.6)

        btn = Button(text='查询', size_hint_y=None, height=50)
        btn.bind(on_press=self.do_query)

        layout.add_widget(Label(text='隐私查询工具', font_size='24sp'))
        layout.add_widget(self.url_input)
        layout.add_widget(btn)
        layout.add_widget(self.result_label)
        return layout

    def do_query(self, instance):
        url = self.url_input.text.strip()
        if not url:
            self.result_label.text = '请输入API地址'
            return
        try:
            r = requests.get(url, timeout=10)
            self.result_label.text = r.text[:500] if r.text else '无返回'
        except Exception as e:
            self.result_label.text = f'错误: {e}'

if __name__ == '__main__':
    QueryApp().run()
