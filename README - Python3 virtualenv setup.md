# Python3 Virtualenv Setup

#### Requirements
* Python 3
* Pip 3
```
$ brew install python3
```
Pip3 is installed with Python3


#### Installation
To install virtualenv via pip run:
```
$ pip3 install virtualenv
```
#### Usage:
#### Creation of virtualenv:
```
$ virtualenv -p python3 <desired-path>
```

#### Activate the virtualenv:
```
$ source <desired-path>/bin/activate
```

#### Deactivate the virtualenv:
```
$ deactivate
```

#### Example
```
C:\Home> where python
C:\Users\June\AppData\Local\Programs\Python\Python39\python.exe
C:\Users\June\AppData\Local\Microsoft\WindowsApps\python.exe

// create a virtual environment named 'venv', feel free to name it anything you like
virtualenv venv -p C:\Users\June\AppData\Local\Programs\Python\Python39\python.exe

// activate the virtual environment
C:\Home> .\venv\Scripts\activate
// check the python version
(venv) C:\Home> python --version
// list all packages installed by default
(venv) C:\Home> pip list
// deactivate the virtual environment
(venv) C:\Home> deactivate
```
