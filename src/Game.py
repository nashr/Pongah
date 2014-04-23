from kivy.uix.widget import Widget
from Sprite import *

# Root of widgets
class PongahGame(Widget):
	sprite = Sprite()
	
	def update(self, dt):
		pass #self.sprite.update(dt)