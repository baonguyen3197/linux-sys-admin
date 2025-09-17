# Use Python REPL
``python``
python3
>>> xmen_file = open("xmen_base.txt")
>>> xmen_file
<_io.TextIOWrapper name='xmen_base.txt' mode='r' encoding='UTF-8'>
>>> xmen_file.read()
'Storm\nWolverine\nCyclops\nBishop\nNightcrawler\nJean Grey\nRogue\n'
>>> xmen_file.read()
''
>>> xmen_file.seek(0)
0                       # Move the cursor back to the start of the file
>>> xmen_file.read()
'Storm\nWolverine\nCyclops\nBishop\nNightcrawler\nJean Grey\nRogue\n'
>>> xmen_file.seek(6)
6
>>> xmen_file.read()
'Wolverine\nCyclops\nBishop\nNightcrawler\nJean Grey\nRogue\n'
>>> xmen_file.seek(0)
0
>>> for line in xmen_file:
...     print(line, end="")
...
Storm
Wolverine
Cyclops
Bishop
Nightcrawler
Jean Grey
Rogue
>>> xmen_file.close()
>>> xmen_file.read()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> xmen_file
<_io.TextIOWrapper name='xmen_base.txt' mode='r' encoding='UTF-8'>
>>> new_xmen = open("new_xmen.txt", "w")
>>> new_xmen
<_io.TextIOWrapper name='new_xmen.txt' mode='w' encoding='UTF-8'>
>>> new_xmen.write(xmen_base.read())
44
>>> new_xmen.read()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not readable
>>> new_xmen.close()
>>> new_xmen = open(new_xmen.name, "r+")
>>> new_xmen.read()
'Storm\nWolverine\nCyclops\nBishop\nNightcrawler\nJean Grey\nRogue\n'
>>> new_xmen.write("Professor X\n")
14
>>> new_xmen.seek(0)
0
>>> new_xmen.read()
'Storm\nWolverine\nCyclops\nBishop\nNightcrawler\nJean Grey\nRogue\nProfessor X\n'
>>> new_xmen.close() 
>>> xmen_file.close()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
NameError: name 'xmen_file' is not defined
>>> xmen_base.close()
>>> with open("xmen_base.txt", "a") as f:
...     f.write("Gambit\n")
...
17
>>> f
<_io.TextIOWrapper name='xmen_base.txt' mode='a' encoding='UTF-8'>
>>> f.read()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
valueError: I/O operation on closed file.
>>> f = open("xmen_base.txt", "a")
>>> with f:
...     f.write("Iceman\n")
...
6
>>> 