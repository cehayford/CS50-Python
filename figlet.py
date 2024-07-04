from pyfiglet import Figlet
import sys
import random


figlet = Figlet()
if len(sys.argv) == 1:
    isRandfont = True
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    isRandfont = False
else:
    sys.exit(1)

# inp = input("name: ")
figlet.getFonts()

if isRandfont == False:
    try:
        figlet.setFont(font = sys.argv[2])
    except:
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())


inp = input("name: ")
rend = figlet.renderText(inp)
print('Output: {0}'.format(rend))