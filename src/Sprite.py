from kivy.core.image import Image
from kivy.properties import StringProperty
from kivy.core.window import Window
import os.path

class Sprite():
	# Directory of images
	imgdir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "res", "img")
	
	# Directory of any other sprites
	player = os.path.join(imgdir, "Player.png")
	tile = os.path.join(imgdir, "Tile.png")
	
	# Initialize textures
	player_texture = Image(player).texture
	tile_texture = Image(tile).texture
