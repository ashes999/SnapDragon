from com.badlogic.gdx import ApplicationAdapter
from com.badlogic.gdx import Gdx
from com.badlogic.gdx.graphics import GL20
from com.badlogic.gdx.graphics import Texture
from com.badlogic.gdx.graphics.g2d import SpriteBatch

class MainGame:
	def __init__(self):
		self.batch = SpriteBatch()
		self.img = Texture("badlogic.jpg")

	def render(self):
		Gdx.gl.glClearColor(1, 0, 0, 1)
		Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT)
		self.batch.begin()
		self.batch.draw(self.img, 0, 0)
		self.batch.end()

	def dispose(self):
		self.batch.dispose()
		self.img.dispose()
