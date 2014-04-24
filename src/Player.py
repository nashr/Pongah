from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.widget import Widget

from Sprite import Sprite

class Player(Widget):
	# Player sprites
	texture = Sprite().player_texture
	curr_texture = ObjectProperty(None)
	
	# Player position
	x = NumericProperty(0)
	y = NumericProperty(0)
	
	# Player state
	state = NumericProperty(0)
	
	def update(self, dt):
		self.state += 1
		self.state %= 8
		
		self.curr_texture = self.texture.get_region(self.state * 48, 0, 48, 48)
