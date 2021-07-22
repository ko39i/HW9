_file = open("task1.txt", "r")

text = _file.readlines()

for i, j in enumerate(text):
    if i % 1 == 0:
        del text[i]

_file.close()

_file = open("task1.txt", "w")

for i in text:
    _file.write(i)

_file.close()

_file = open("task1.txt", "r")

text = _file.read()
text = text.replace('\n', '')

_file.close()

_file = open("task1.txt", "w")
_file.write(text)

_file.close()
