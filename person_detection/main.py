import os
from detector import detect

for filename in os.scandir('images'):
    detect(filename.path)
