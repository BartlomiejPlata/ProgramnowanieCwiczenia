import os
from detector import detect

for filename in os.scandir('images'):
    print(detect(filename.path))



