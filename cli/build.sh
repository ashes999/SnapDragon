#!/bin/sh

rm -rf build
rm -rf dist

pyinstaller main.py --onefile --noconsole