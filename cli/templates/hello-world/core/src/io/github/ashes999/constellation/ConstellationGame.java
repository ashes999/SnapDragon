package io.github.ashes999.constellation;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;

import org.python.core.PyObject;
import org.python.util.PythonInterpreter;

public class ConstellationGame extends ApplicationAdapter {
	
	PyObject mainGame;
	
	@Override
	public void create() {
		PythonInterpreter interpreter = new PythonInterpreter();
		System.out.println(interpreter.eval("1 + 2"));
		//interpreter.execfile("main_game.py"); // TODO: put in Android > assets and load ...
		// TODO: interpret as subclass of ApplicationAdapter
		// TODO: forget that, toss out the base class
		//this.mainGame = interpreter.eval("MainGame()");
	}

	@Override
	public void render() {
		//mainGame.invoke("render");
	}
	
	@Override
	public void dispose() {
		//mainGame.invoke("dispose");
	}
}
