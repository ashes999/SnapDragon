# SnapDragon

Build web, desktop, and Android games in Python.

SnapDragon leverages libGDX with Jython to provide powerful, cross-platform capabilities. SnapDragon provides pythonic interfaces and APIs to make game development a breeze. 

# Usage

- Download the latest release, or build from source (`./build.sh` or `build.bat`).
- Copy the binaries somewhere accessible to the shell. Alternatively, put them in an easily-accessible path.
- Run `snap create` to create a new project.
- From the project directory, run `snap build <platform>`. Platforms are `web` (HTML5), `desktop` (builds Linux or Windows, whatever you're running on), and `android`.

**Note:** For Android development, you first have to run `snap setup` and specify where the Android SDK is.
