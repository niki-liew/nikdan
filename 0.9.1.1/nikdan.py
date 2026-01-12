import os, time, compiler
from os import system
system("title astn brwn")

code = []
debugMode = False
count = 0
autosave = True

print('nikdan v0.9.1.1')

while True:
    user_input = None

    if debugMode == True:
        time.sleep(1)
        user_input = list(sec_word)
        debugMode = False
    else:
        user_input = list(input('N '))

    count += 1

    command = ''
    word = ''
    dam = 0

    for i in user_input:
        if i != ' ':
            word += i
            dam = 1
        else:
            dam = 0
            command += word
            break

    if dam == 1:
        command = word

    sec_word = ''
    past_command = 0

    for i in user_input:
        if past_command == 0:
            if i == ' ':
                past_command = 1
        else:
            sec_word += i

    if command == 'new':
        code.clear()

    if command == 'list':
        nums = []

        for i in code:
            nums.append(i[0])

        nums.sort()

        for i in nums:
            for j in code:
                if i == j[0]:
                    print(str(j[0]) + ' ' + j[1])

    if command == 'autosave':
        autosave = not autosave
        print('autosave now ' + str(autosave))

    if command == 'cls':
        os.system('cls')

    if command == 'compile':
        if os.path.exists(sec_word):
            compiler.compile(sec_word)

        else:
            print('compilation unsuccessful, file does not exist')

    if autosave == False:
        count = 0

    if count >= 10 and autosave == True:
        count = 0
        file = open('autosave.nikl', 'wt')
        file.write('')
        file = open('autosave.nikl', 'at')

        file.write('/nikdanver/\n')

        for j in code:
            file.write(str(j[0]) + '\n' + j[1] + '\n')

        file.close()

        print('autosave successful')

    if command == 'easteregg':
        print('easter egg')

    if command == 'debug':
        debugMode = True

    if command == 'help':
        print('To write, specifiy line number first, then write. example:')
        print("10 printf('Hello World');\n")
        print('save [arg]    : saves file readable to nikdan')
        print('tsave [arg]   : saves file as is')
        print('load [arg]    : loads nikdan readable files')
        print('remove [arg]  : clears all text in specified line')
        print('run [arg]     : runs specified file')
        print('delete [arg]  : deletes specified file')
        print('compile [arg] : compiles specified file into python. file must be nikl file type')
        print('debug [arg]   : turns on debug mode')
        print('new           : removes all that has been written')
        print('list          : shows what has been written')
        print('exit          : exits')
        print('cls           : clears terminal')
        print('autosave      : toggles autosave')

    if command == 'save':
        file = open(sec_word, 'wt')
        file.write('')
        file = open(sec_word, 'at')

        file.write('/nikdanver/\n')

        nums = []

        for i in code:
            nums.append(i[0])

        nums.sort()

        for i in nums:
            for j in code:
                if i == j[0]:
                    file.write(str(j[0]) + '\n' + j[1] + '\n')

        file.close()

        print('save successful')

    if command == 'tsave':
        file = open(sec_word, 'wt')
        file.write('')
        file = open(sec_word, 'at')

        nums = []

        for i in code:
            nums.append(i[0])

        nums.sort()

        for i in nums:
            for j in code:
                if i == j[0]:
                    file.write(j[1] + '\n')

        file.close()

        print('true save successful')

    if command == 'load':
        if os.path.exists(sec_word):
            code.clear()

            file = open(sec_word, 'r')
            stuff = []

            for i in file:
                for j in i:
                    stuff.append(j)

            worse = ''
            allowed = 0
            numnum = -1
            yumyum = -1

            for i in stuff:
                if i != '\n':
                    worse += i
                else:
                    if worse == '/nikdanver/':
                        allowed = 1
                    else:
                        if worse.isnumeric():
                            numnum = int(worse)
                        else:
                            yumyum = worse

                        if numnum != -1 and yumyum != -1 and allowed == 1:
                            code.append([numnum, yumyum])
                            numnum = -1
                            yumyum = -1

                    worse = ''

            if allowed == 1:
                print('load successful')

            else:
                print('load unsuccessful, file cannot be read by nikdan')
        else:
            print('load uncsuccessful, file does not exist')
    
    if command == 'remove':
        for i in code:
            if sec_word.isnumeric and i[0] == int(sec_word):
                code.remove(i)
                break

    if command == 'exit':
        quit()

    if command == 'run':
        if os.path.exists(sec_word):
            os.startfile(sec_word)
            print('run successful')
        else:
            print('run unsuccessful, file does not exist')

    if command == 'delete':
        if os.path.exists(sec_word):
            os.remove(sec_word)
            print('delete successful')
        else:
            print('delete unsuccessful, file does not exist')

    if command.isnumeric():
        wor = ''
        act = ''
        ln = -1
        past_command = 0
        alr_have = 0

        for i in user_input:
            if past_command == 0:
                if i != ' ':
                    wor += i
                else:
                    past_command = 1
                    ln = int(wor)

                    for j in code:
                        if j[0] == ln:
                            alr_have = 1
            else:
                act += i

        if alr_have == 1:
            for i in code:
                if i[0] == ln:
                    code.remove(i)

        code.append([ln, act])