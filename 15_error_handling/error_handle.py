#option: 01 to open a file
file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()

#option: 02
with open('youtube.txt', 'w') as file:
    file.write('chai aur python')