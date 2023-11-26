#THIS IS THE DOCUMENTATION OF OUR CODEBASE#
#REVIEW THIS WELL IN ORDER TO GET A DEEP UNDERSTANDING IN OUR APPLICATION#

#MAKE SURE YOU KNOW THE BASICS OF CLASSES, FUNCTION OR METHOD. INHERITANCE, EXCEPTIONS AND THE SELF KEYWORD BEFORE READING THIS DOCUMENTATION, THEN YOU CAN PROCEED READING LINE (6)

#         !!!IMPORTANT!!!
#    READ THE DOCUMENTATION OF KIVY

#LINK:    https://kivy.org/doc/stable/


#As this will give you a understanding of what we utilized using kivy framework and its function.

#THE CODE BELOW HAVE COMMENTS MAKE SURE TO READ EACH COMMENT THAT IS POINTING OUT THE CODE BELOW THE COMMENT

#EXAMPLE

#TO PRINT OUT THE STRING ""
print("")

#IF YOU HAVE QUESTIONS REGARDING HOW WE USE THE CODE JUST MESSAGE AT THE GC.

#Mag co code review naman tayo dito kaya no worries

#CODE MAY CHANGE WITHOUT PRIOR NOTICE, HINDI RIN ITO YUNG MAIN FILE KAYA PWEDE TONG MAGING OUTDATED






# Import necessary modules

# The base class for Kivy Application 
from kivy.app import App
# This manage multiple screen within to our application
from kivy.uix.screenmanager import ScreenManager, Screen
# Load Kivy language(Kv) files into python code 
from kivy.lang.builder import Builder
# Control the window properties like size and title
from kivy.core.window import Window
# Pop-up windows within the application 
from kivy.uix.popup import Popup
# Esssential UI components for text, layout, and buttons 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# Allows scheduling events or updates at specifics intervals
from kivy.clock import Clock


class WindowManager(ScreenManager):
    pass

class Intro_Screen(Screen):
    def on_enter(self):
        # The schedule a transition to the lobby screen after the intro vid (6 sec)
        Clock.schedule_once(self.Goto_lobby_screen, 6)     
    def Goto_lobby_screen(self, dt):
        # The transition to the Lobby Screen/ Stops the intro video from playing 
        intro_video = self.ids.intro_video
        intro_video.state = 'stop' # Make to stop the intro vid 
        self.manager.current = 'Lobby_Screen' # Move to the Lobby Screen

# EXPLANATION 

# 'on_enter' When you start running the code, it will play our intro video. It waits for 6 seconds before going to the lobby.
# 'clock.schedule_once' Its like setting an alarm 
# 'Goto_lobby_screen': This does two things: 
# - Stops the intro video so it doesn't play anymore.
# - Changes what you see on the screen to the lobby area.
# So, when you open this part of the app, It waits a little bit, stops any playing video, and then takes you to the lobby where you can do more things.


class Lobby_Screen(Screen):
    def on_enter(self): # Define valid song numbers 
        self.song_numbers = ["110022", "432344", "996576", "560989", "334295", "445566", "997545", "456123", "789879", "741258", "856214", "099892", "139987", "111000"]
        # The list of valid song numbers 
    def check_input(self):
        # This check if the entered song number is valid 
        number_input = self.ids.input.text
        if str(number_input) in self.song_numbers:
            print("Running") # Move to the Game Scrren if the song number is valid 
            self.manager.get_screen('Game_Screen').number_input = number_input
            self.manager.current = 'Game_Screen'
        else: # If the user enters an invalid number, it will show a pop-up that will tell them that the number is invalid input.
            popup = Popup(
                title='KaraokePy',
                content=Label(text="Invalid song number! Please try again."),
                size_hint=(0.4, 0.2)) 
            popup.open()

# EXPLANATION
# 'on_enter: When you enter this screen, it prepares a list of song numbers that it recognizes.
# check_input: When user types a song number and tries to continue, this checks if the number is one of the recognized songs.
# If it's a song we recognize, it takes them to the Game Screen and tells the Game Screen which song they picked.
# If it's not a song that the program know, it shows a message saying, "Invalid dong number! Try again."



    # This define the exit confirmation pop-up and its functionalities (yes and no buttons)
    # If the user clicks the exit button, there will be a pop-up that will ask the user if she or he truly wants to exit the program.
    def exit_confirmation(self):
        # Creating the layout for the confirmation message and buttons
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Are you sure you want to exit?'))

        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
        yes_button = Button(text='Yes', size_hint_x=0.7)
        no_button = Button(text='No', size_hint_x=0.7)

        buttons_layout.add_widget(yes_button)
        buttons_layout.add_widget(no_button)

        content.add_widget(buttons_layout)

        # The creation of exit conformation pop-up 
        popup = Popup(
            title='Exit Confirmation',
            content=content,
            size_hint=(0.4, 0.2)
        )
       # Connecting buttons to their respective functions
        yes_button.bind(on_release=self.close_app)
        no_button.bind(on_release=popup.dismiss)

        popup.open() # This display the exit confirmation pop-up 

    # This function closes the entire application when 'Yes' is clicked in the exit confirmation
    def close_app(self, instance):
        App.get_running_app().stop() # This completely closes the application


# EXPLANATION
# This code defines a function called exit_confirmation that creates a pop-up 
# Window asking the user to confirm if they want to exit the program. Which is The pop-up 
# includes a message asking for confirmation and two buttons, 'Yes' and 'No'
# Clicking 'Yes' (affirmative) triggers the close_app function, which completely shuts down the application using App.get_running_app().stop().
# Clicking 'No' dismisses the pop-up without taking any action, allowing the user to stay within the application.
# This setup ensures that the user has a chance to confirm their intent to exit the program before it's completely closed down.


class Game_Screen(Screen): 
    number_input = "" # The placeholder for the entered song number 

    def on_enter(self): # Play different videos based on the entered song number (holder)
        if self.number_input == "110022":     # Matches the entered song number to play the corresponding video
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

    # Other elif blocks for different song numbers and their corresponding videos...

    VIDEO_CHECK_INTERVAL = 8 #seconds before the program will automatically go to the lobby
    # The interval before automatically going to the lobby

    def play_video(self, video_source): # For this part this is connected to interval
        video_attribute = self.ids.video_attribute
        video_attribute.source = video_source
        video_attribute.state = 'play'
        Clock.schedule_interval(lambda dt: self.check_video_state(video_attribute), self.VIDEO_CHECK_INTERVAL)

    def check_video_state(self, video_attribute):
        # Check if the video has stopped playing 
        if video_attribute.state == 'stop':
            self.manager.current = 'Lobby_Screen' # if the video is done playing, It will move back to Lobby Screen 

    # The pause and play of the video based on button press 
    def pause_play(self):
        vid_attribute = self.ids.video_attribute
        pause_play_button = self.ids.pause_play_button

        # Toggle between pause and play based on video state . "Toggle" refers to switching between two different states or values when an action is performed. 
        if vid_attribute.state == 'play':
            pause_play_button.background_normal = 'res/backgroundImage/play.png'
            vid_attribute.state = 'pause'
        else:
            pause_play_button.background_normal = 'res/backgroundImage/pause.png'
            vid_attribute.state = 'play'

    # A stop button, once you click the button it will stop the video and move back to the Lobby Screen
    def stop_video(self):
        vid_attribute = self.ids.video_attribute
        vid_attribute.state = 'stop' # Stops the video
        self.manager.current = 'Lobby_Screen' # Moves back to the Lobby Screen 



# Load the design from a Kivy language file 
kv = Builder.load_file("karaokepydesign.kv")

# 'karaokepydesign.kv' defines screens, widgets, and their appearance.
# It separates visual layout from code, making it easy to modify the app's look.
# Using Kivy's syntax, it creates an intuitive interface, allowing changes
# to the UI without affecting the main code, enhancing the app's appearance.



# This define the main Kivy App Class
class KaraokepyApp(App):
    def build(self):
        Window.fullscreen = 'auto' # This set the application window to fullscreen 
        return kv # return the loaded design 
        
# Run the Kivy app
if __name__ == '__main__':
    KaraokepyApp().run() # function to run 

# EXPLANATION 

# This code manages a karaoke-like experience: when a song number is entered, it triggers the corresponding video to play. Each number corresponds to a different video file. 
# You can control the video: start, stop, or pause it. When a video finishes, the system goes back to the main screen(lobby).
# The way the app looks and works is set up using a special file. It's like a simple way to choose and watch videos with easy buttons to control them.