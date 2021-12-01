
'''
a = [5, 10, 15, 20, 25]

def listchanger(a:list) -> list:
    b = [a[0], a[len(a)-1]]
    return b

print(listchanger(a))

'''

tekst = str(input("wpisz zdanie..."))

def reverseString(mainTekst):
  rev = mainTekst.split()
  length = len(rev)
  result = []
  for x in rev:
    result.append(rev[length -1])
    length -= 1
  return " ".join(result)

print(reverseString(tekst))

# odwracanie tekstu

def reverseWord(w):
  return ' '.join(w.split()[::-1])