from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from Player import Player

# Root of widgets
class PongahGame(Widget):
	player = ObjectProperty(None)
	
	def update(self, dt):
		self.player.update(dt)
