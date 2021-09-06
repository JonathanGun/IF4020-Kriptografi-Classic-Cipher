# Kriptografi Tucil 1

You can download the executables via this [link](https://github.com/JonathanGun/IF4020-Kriptografi-Classic-Cipher/releases/latest)

## Installing Requirements
### Linux
```bash
virtualenv -p python3 venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### Windows
```bash
virtualenv -p python3 venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Running Program
### Linux
```bash
source venv/bin/activate
python main.py
```

### Windows
```bash
venv\Scripts\activate
python main.py
```

## Building Exe
```bash
pyinstaller -F -i="icon.ico" main.py --clean -w
```
