from kivy.properties import StringProperty
import os.path

class Sprite():
	# Directory of images
	imgdir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "res", "img")

	player = os.path.join(imgdir, "player.png")
	
	def update(self, dt):
		pass