# SnapDragon

Build web, desktop, and Android games in Python.

SnapDragon leverages libGDX with Jython to provide powerful, cross-platform capabilities. SnapDragon provides pythonic interfaces and APIs to make game development a breeze. 

# Usage

- Download the latest release (or build from source: from `cli`, run `build.sh` or `build.bat`).
- Copy the binaries somewhere accessible to the shell.
- Run `snap create` to create a new project.
- From the project directory, run `snap build <platform>`. Platforms are `web` (HTML5), `desktop` (builds Linux or Windows, whatever you're running on), and `android`.
- Look in the `dist` folder for the final binaries.

**Note:** For Android development, you first have to run `snap setup` and specify where the Android SDK is.

# API Docs

API documentation is available in the `docs` folder.

# Example Projects

SnapDragon ships with several example projects. Some of these are quick-starts (eg. tower defense), others showcase features (eg. bitmap font text).

To see the full list of available projects, run `snap create`. Enter the path for the new project, and the template number to generate.

# Credits

SnapDragon is possible on the shoulders of open-source projects, great and small. We are thankful to each and every individual contributer (and especially to the founders) of these projects:

- [Jython](https://github.com/jythontools/jython)
- [libGDX](https://github.com/libgdx/libgdx)
- [pythonVSCode](https://github.com/DonJayamanne/pythonVSCode)
- [Visual Studio Code](https://github.com/Microsoft/vscode) 