# Constellation

A framework for creating libGDX-powered games in dynamic languages such as Python and Ruby. 

Constellation provides a framework that:

- Leverages libGDX as a solid, cross-platform game engine
- Provides integration to build libGDX games in Python, Ruby, and *insert your JVM-friendly language here*
- Provides tools to easily build your game against any platform (web, desktop, and mobile)
- Provides templates to create new projects

Currently, Constellation supports:

- Python (via Jython)
- Ruby (via JRuby)

Constellation aims to be a foundational platform for creating more game engines powered by libGDX and your dynamic language of choice. To extend it, plug in your own choice of Java-powered language library.

# Usage

- Download the latest release, or build from source (`./build.sh` or `build.bat`).
- Copy `dist/main` or `dist/main.exe` to your game source code directory (or copy it somewhere where it's accessible to the shell).
- Invoke `main create <language>` to create a new project in a new directory. Valid languages are `python` and `ruby`.
- From the project directory, run `main build <platform>`, substituting `<platform>` with one of: `web`, `desktop`, or `android`.

# Game Engines Built With Constellation

- [SnapDragon](https://github.com/ashes999/SnapDragon):  A Python-based game engine and ECS

# Credits

Constellation wouldn't be possible without the amazing open-source projects listed below. We are thankful to each and every contributer who helped us reach where we are today.

- JRuby
- Jython
- libGDX
