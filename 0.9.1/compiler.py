def compile(bN):
    getToWork = 0
    bleep = ''
    for i in list(bN):
        if i == '.':
            getToWork = 1
        if getToWork == 1:
            bleep += i
            
    if bleep != '.nikl':
        print('compilation into nikl unsuccessful, file needs to be .nikl')
    else:
        print('compilation into nikl successful')

        buffer = open(bN, 'r')
        toTurn = list(buffer.read())
        buffer.close()

        fileName = bN
        file = open(str(fileName) + '.py', 'w')
        file.write('')
        file = open(str(fileName) + '.py', 'a')

        word = ''
        baseMode = -1
        mode = baseMode
        genMode = baseMode

        hasRandom = 0
        hasCLS = 0
        hasDelay = 0
        hasKEY = 0

        arg = None
        arg1 = None
        arg2 = None

        for w in toTurn:
            if w != ' ' and w != '|' and w != '\n':
                word += w
            else:
                if word == 'mri' or word == 'mra':
                    hasRandom = 1
                
                if word == 'cls':
                    hasCLS = 1

                if word == 'delay' or word == 'dllm':
                    hasDelay = 1

                if word == 'gk':
                    hasKEY = 1

                word = ''

        if hasRandom == 1:
            file.write('import random\n')

        if hasCLS == 1:
            file.write('import os\n')

        if hasDelay == 1:
            file.write('import time\n')

        if hasKEY == 1:
            file.write('import keyboard\n')

        word = ''

        for i in toTurn:
            if i != ' ' and i != '|' and i != '\n':
                word += i
            else:
                if word == '>>':
                    file.write('    ')

                if word == 'out':
                    file.write('break\n')

                if word == 'exit':
                    file.write('quit()\n')

                if word == 'termin':
                    file.write('input()\n')

                if word == 'termde':
                    file.write('input()\n')

                if word == 'dllm':
                    file.write('time.sleep(0)\n')

                if word == 'cls':
                    file.write("os.system('cls')\n")

                if word == 'omnipresence':
                    file.write("print('NIKI IS YOUR KING')\n")

                if word == '<>':
                    file.write("# ")

                if word == 'init':
                    mode = 0

                if word == 'initf':
                    mode = 1

                if word == 'termout':
                    mode = 2
                    genMode = 1

                if word == 'if':
                    mode = 3
                    genMode = 0

                if word == 'else':
                    mode = 4

                if word == 'while':
                    mode = 5

                if word == 'mri':
                    mode = 6

                if word == 'mra':
                    mode = 7

                if word == 'gk':
                    mode = 8

                if word == 'delay':
                    mode = 9

                if word == 'include':
                    mode = 10

                if word == 'ret':
                    mode = 11

                if word == 'tostring':
                    mode = 12

                if word == 'tointeger':
                    mode = 13

                if word == 'toarray':
                    mode = 14

                if word == 'uppercase':
                    mode = 15

                if word == 'lowercase':
                    mode = 16

                if word == 'agl':
                    mode = 17

                if word == 'aaae':
                    mode = 18

                if word == 'ac':
                    mode = 19

                if word == 'agi':
                    mode = 20

                if word == 'fopen':
                    mode = 21

                if word == 'fclose':
                    mode = 22

                if word == 'fclear':
                    mode = 23

                if word == 'fwrite':
                    mode = 24

                if mode == -2:
                    if word != '<>':
                        file.write('#'+word)

                if mode == 0:
                    if word != 'init' and word != 'termin' and word != 'termde':
                        file.write(word)

                if mode == 1:
                    if word == 'initf':
                        file.write('def ')
                    else:
                        file.write(word + ':')

                if mode == 2:
                    if word == 'termout':
                        file.write('print(')
                    else:
                        file.write(word)

                if mode == 3:
                    if word == 'if':
                        file.write('if ')
                    else:
                        file.write(word)

                if mode == 4:
                    if word == 'else':
                        file.write('else:')

                if mode == 5:
                    if word == 'while':
                        file.write('while True:')

                if mode == 6:
                    if word == 'mri':
                        file.write('random.randint(')
                    else:
                        file.write(word + ')')

                if mode == 7:
                    if word == 'mra':
                        file.write('random.choice(')
                    else:
                        file.write(word + ')')

                if mode == 8:
                    if word == 'gk':
                        file.write('keyboard.is_pressed(')
                    else:
                        file.write(word + ')')

                if mode == 9:
                    if word == 'delay':
                        file.write('time.sleep(')
                    else:
                        file.write(word + ')')
                if mode == 10:
                    if word == 'include':
                        file.write('import ')
                    else:
                        file.write(word)

                if mode == 11:
                    if word == 'ret':
                        file.write('return ')
                    else:
                        file.write(word)

                if mode == 12:
                    if word != 'tostring':
                        file.write(word + ' = str(' + word + ')')

                if mode == 13:
                    if word != 'tointeger':
                        file.write(word + ' = int(' + word + ')')   

                if mode == 14:
                    if word != 'toarray':
                        file.write(word + ' = list(' + word + ')')

                if mode == 15:
                    if word != 'uppercase':
                        file.write(word + ' = ' + word + '.upper()')   

                if mode == 16:
                    if word != 'lowercase':
                        file.write(word + ' = ' + word + '.lower()')

                if mode == 17:
                    if word == 'agl':
                        file.write('len(')
                    else:
                        file.write(word + ')')

                if mode == 18:
                    if word != 'aaae':
                        if arg == None:
                            arg = word
                        else:
                            arg1 = word
                    if word != 'aaae' and word != arg:
                        file.write(arg + '.append(' + arg1 + ')')
                        arg = None
                        arg1 = None

                if mode == 19:
                    if word != 'ac':
                        file.write(word + '.clear()')

                if mode == 20:
                    if word != 'agi':
                        if arg == None:
                            arg = word
                        else:
                            arg1 = word
                    if word != 'agi' and word != arg:
                        file.write(arg + '.index(' + arg1 + ')')
                        arg = None
                        arg1 = None

                if mode == 21:
                    if word != 'fopen':
                        file.write('open(' + word + ',  "rt")')

                if mode == 22:
                    if word != 'fclose':
                        file.write(word + '.close()')

                if mode == 23:
                    if word != 'fclear':
                        file.write('open(' + word + ',  "wt")\n')
                        file.write(word + '.write("")')

                if mode == 24:
                    if word != 'fwrite':
                        if arg == None:
                            arg = word
                        else:
                            arg1 = word
                    if word != 'fwrite' and word != arg:
                        file.write(arg + '.write(' + arg1 + ')')
                        arg = None
                        arg1 = None

                word = ''
            if i == '|':
                if genMode == 0:
                    file.write(':\n')
                elif genMode == 1:
                    file.write(')\n')
                else:
                    file.write('\n')
                word = ''
                mode = baseMode
                genMode = baseMode

        file.close()