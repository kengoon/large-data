from kivy.app import App
from kivy.lang import Builder
import scrollview  # noqa


class LargeDataApp(App):
    adding_data = False

    def build(self):
        return Builder.load_file("large_data.kv")

    def add_more_data(self):
        if self.adding_data:
            return
        print("adding more data")
        self.adding_data = True
        for i in range(100):
            self.root.data.append({})
            print("added")
        self.adding_data = False


if __name__ == "__main__":
    LargeDataApp().run()
