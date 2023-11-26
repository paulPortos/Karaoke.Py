from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class WindowManager(ScreenManager):
    pass

class Intro_Screen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.Goto_lobby_screen, 6)     
    def Goto_lobby_screen(self, dt): #dl = delta time 
        intro_video = self.ids.intro_video
        intro_video.state = 'stop'
        self.manager.current = 'Lobby_Screen'

class Lobby_Screen(Screen):
    def on_enter(self):
        self.song_numbers = ["110022", "432344", "996576", "560989", "334295", "445566", "997545", "456123", "789879", "741258", "856214", "099892", "139987", "111000"]

    def check_input(self):
        number_input = self.ids.input.text
        if str(number_input) in self.song_numbers:
            print("Running")
            self.manager.get_screen('Game_Screen').number_input = number_input
            self.manager.current = 'Game_Screen'
        else:
            popup = Popup(
                title='KaraokePy',
                content=Label(text="Invalid song number! Please try again."),
                size_hint=(0.4, 0.2)) 
            popup.open()

    def exit_confirmation(self):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Are you sure you want to exit?'))

        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
        yes_button = Button(text='Yes', size_hint_x=0.7)
        no_button = Button(text='No', size_hint_x=0.7)

        buttons_layout.add_widget(yes_button)
        buttons_layout.add_widget(no_button)

        content.add_widget(buttons_layout)

        popup = Popup(
            title='Exit Confirmation',
            content=content,
            size_hint=(0.4, 0.2)
        )

        yes_button.bind(on_release=self.close_app)
        no_button.bind(on_release=popup.dismiss)

        popup.open()

    def close_app(self, instance):
        App.get_running_app().stop()


class Game_Screen(Screen): 
    number_input = ""
    
    def on_enter(self):
        if self.number_input == "110022":
            self.play_video('res/videos/ERE.mp4')
        elif self.number_input == "432344":
            self.play_video('res/videos/wonderful_tonight.mp4')
        elif self.number_input == "334295":
            self.play_video('res/videos/wherever_you.mp4')
        elif self.number_input == "445566":
            self.play_video('res/videos/angels_like.mp4')
        elif self.number_input == "996576":
            self.play_video('res/videos/love_story.mp4')
        elif self.number_input == "560989":
            self.play_video('res/videos/iris.mp4')
        elif self.number_input == "139987":
            self.play_video('res/videos/tadhana.mp4')
        elif self.number_input == "997545":
            self.play_video('res/videos/king_bed.mp4')
        elif self.number_input == "456123": 
            self.play_video('res/videos/the_man.mp4')
        elif self.number_input == "789879":
            self.play_video('res/videos/photograph.mp4')
        elif self.number_input == "741258":
            self.play_video('res/videos/To_the_bone.mp4')
        elif self.number_input == "856214":
            self.play_video('res/videos/Fallen.mp4')
        elif self.number_input == "099892":
            self.play_video('res/videos/zombie.mp4')
        elif self.number_input == "111000":
            self.play_video('res/videos/bubble.mp4')

    VIDEO_CHECK_INTERVAL = 8 #seconds before the program will automatically go to the lobby

    def play_video(self, video_source):
        video_attribute = self.ids.video_attribute
        button_attribute = self.ids.pause_play_button
        video_attribute.source = video_source
        video_attribute.state = 'play'
        if video_attribute.state == 'play':
            button_attribute.background_normal = 'res/BackgroundImage/pause.png'
        Clock.schedule_interval(lambda dt: self.check_video_state(video_attribute), self.VIDEO_CHECK_INTERVAL)

    def check_video_state(self, video_attribute):
        if video_attribute.state == 'stop':
            self.manager.current = 'Lobby_Screen'

    def pause_play(self):
        vid_attribute = self.ids.video_attribute
        pause_play_button = self.ids.pause_play_button

        if vid_attribute.state == 'play':
            pause_play_button.background_normal = 'res/backgroundImage/play.png'
            vid_attribute.state = 'pause'
        else:
            pause_play_button.background_normal = 'res/backgroundImage/pause.png'
            vid_attribute.state = 'play'

    def stop_video(self):
        vid_attribute = self.ids.video_attribute
        vid_attribute.state = 'stop'
        self.manager.current = 'Lobby_Screen'

kv = Builder.load_file("karaokepydesign.kv")

class KaraokepyApp(App):
    def build(self):
        Window.fullscreen = 'auto'
        return kv
        
if __name__ == '__main__':
    KaraokepyApp().run()
