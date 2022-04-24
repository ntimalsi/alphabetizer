Instructions to run Alphabetizer
-----

### Introduction

Alphabetizer program that can read in a series of strings and output the strings with the characters in alphabetical order.


### Programming Language
Python

### Build and Running Instructions For UNIX
**APPROACH 1:**
First, install Python3, set python to Environment variable, install pip3 and install the module **pyinstall** ($ pip3 install pyinstaller) (PyInstaller bundles a Python application and all its dependencies into a single package.)https://pyinstaller.org/en/stable/

1. Go to UNIX shell
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ pyinstaller alphabetizer.py --onefile
  ```

2. Run the file created inside the dist folder in the same project structure

**APPROACH 2:**
1. Go to UNIX shell
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ chmod +x alphabetizer.py
  $ ./alphabetizer or python3 alphabetizer.py
  ```
