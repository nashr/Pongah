from kivy.app import App
from kivy.clock import Clock

from Game import PongahGame

# Main app
class PongahApp(App):
	def build(self):
		game = PongahGame()
		Clock.schedule_interval(game.update, 1.0 / 30.0)
		return game

# Main program
if __name__ == '__main__':
	PongahApp().run()