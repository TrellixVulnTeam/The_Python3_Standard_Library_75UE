import pathlib

p = pathlib.Path('.')
for f in p.iterdir():
    print(f)
    