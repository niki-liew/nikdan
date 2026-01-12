import os, time
from os import system
import shutil, keyboard
import random

system("title astn brwn")

code = []
count = 0
autosave = False
cdir = os.getcwd() + '\\'
cursors = ['F', 'B', 'R', 'J']
current_cursor = 'N'
tribute = False

tosave = [autosave, current_cursor, tribute]

def save_data(tosave):
    settings = open('settings.nikdan', "wt")
    settings.write('')
    settings = open('settings.nikdan', "at")

    settings.write(str(autosave) + "\n")
    settings.write(str(current_cursor) + "\n")
    settings.write(str(tribute) + "\n")

    settings.close()

def load_data():
    settings = open('settings.nikdan', "rt")

    array = []
    act_array = []

    for i in settings:
        for j in i:
            array.append(j)

    word = ''

    for i in array:
        if i != '\n':
            word += i

        else:
            act_array.append(word)
            word = ''

    return act_array

print('nikdan v0.9.2.1')

if os.path.exists('settings.nikdan') != True:
    settings = open('settings.nikdan', "wt")
    save_data(tosave)

else:
    bruh = load_data()

    for i in bruh:
        if bruh.index(i) == 0:
            autosave = i

        if bruh.index(i) == 1:
            current_cursor = i

        if bruh.index(i) == 2:
            tribute = i

while True:
    user_input = None

    if tribute:
        user_input = list(input(random.choice(cursors) + ' '))

    else:
        user_input = list(input(current_cursor + ' '))
 
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

    # if command == 'compile':
    #     if compiler.activated:
    #         if os.path.exists(sec_word):
    #             compiler.compile(sec_word)

    #         else:
    #             print('compilation unsuccessful, file does not exist')

    #     else:
    #         print('compiler deactivated')

    if autosave == False:
        count = 0

    if count >= 10 and autosave == True:
        count = 0
        file = open(cdir + 'autosave.nikl', 'wt')
        file.write('')
        file = open(cdir + 'autosave.nikl', 'at')

        file.write('/nikdanver/\n')

        for j in code:
            file.write(str(j[0]) + '\n' + j[1] + '\n')

        file.close()

        print('autosave successful')

    if command == 'easteregg':
        print('easter egg')

    if command == 'fcreate':
        os.makedirs(cdir + sec_word) 

        print('folder creation successful')

    if command == 'fdelete':
        if os.path.exists(cdir + sec_word):
            if os.path.isdir(cdir + sec_word):
                shutil.rmtree(cdir + sec_word)
                print('folder deletion successful')
            
            else:
                print('folder deletion unsuccessful, is not folder')

        else:
            print('folder deletion unsuccessful, folder does not exist')

    if command == 'goto':
        if os.path.exists(cdir + sec_word):
            if os.path.isdir(cdir + sec_word):
                cdir += sec_word + '\\'
                print('folder change successful')
            
            else:
                print('folder change unsuccessful, is not folder')

        else:
            print('folder change unsuccessful, folder does not exist')

    if command == 'flist':
        array = os.listdir(cdir)
        
        print(cdir)

        for i in array:
            print('    |__>' + str(i))

    if command == 'debug':
        debugMode = True

    if command == 'fs':
        keyboard.press('f11')

    if command == 'tribute':
        tribute = not tribute

        print('tribute now ' + str(tribute))

    if command == 'setcursor':
        current_cursor = sec_word
        print('cursor setting successful')

    if command == 'help':
        # print('compile [arg] : compiles specified file into python. file must be nikl file type')
        print('to write, specifiy line number first, for example:')
        print('10 printf("%d", nuts);')
        print('\nTERMINAL')
        print('exit             : exits and saves all settings')
        print('cls              : clears terminal')
        print('fs               : toggles fullscreen')
        print('\nSETTINGS')
        print('setcursor [args] : sets cursor to specified')
        print('tribute          : toggles cursor to be the first letter of a random queen member')
        print('autosave         : toggles autosave')
        print('\nTEXT EDITOR')
        print('save [arg]       : saves file as readable to nikdan, and as is')
        print('nsave [arg]      : saves file readable to nikdan')
        print('tsave [arg]      : saves file as is')
        print('load [arg]       : loads nikdan readable files')
        print('remove [arg]     : clears all text in specified line')
        print('new              : removes all that has been written')
        print('list             : shows what has been written')
        print('\nFILE MANAGEMENT')
        print('run [arg]        : runs specified file')
        print('delete [arg]     : deletes specified file / folder')
        print('flist            : lists all sibling files and folders')
        # print('flistspec     : lists all sibling files and folders with additional information')
        print('fcreate [arg]    : creates folder')
        print('goto [arg]       : goes to specified folder')

    # if command == 'flistspec':
    #     array = os.listdir(cdir)
        
    #     print(cdir)

    #     for i in array:
    #         print('    |_> ' + str(i))
    #         # if os.path.isfile:
    #         print('        ' + str(os.path.getsize(i)) + ' bytes')

    if command == 'save':
        file = open(cdir + sec_word + '.nikdan', 'wt')
        file.write('')
        file = open(cdir + sec_word + '.nikdan', 'at')

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

        file = open(cdir + sec_word, 'wt')
        file.write('')
        file = open(cdir + sec_word, 'at')

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

    if command == 'nsave':
        file = open(cdir + sec_word + '.nikdan', 'wt')
        file.write('')
        file = open(cdir + sec_word + '.nikdan', 'at')

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
        file = open(cdir + sec_word, 'wt')
        file.write('')
        file = open(cdir + sec_word, 'at')

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
        if os.path.exists(cdir + sec_word):
            code.clear()

            file = open(cdir + sec_word, 'r')
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

            file.close()

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
        save_data(tosave)
        quit()

    if command == 'run':
        if os.path.exists(cdir + sec_word):
            os.startfile(cdir + sec_word)
            print('run successful')
        else:
            print('run unsuccessful, file does not exist')

    if command == 'delete':
        if os.path.exists(cdir + sec_word):
            if os.path.isfile(cdir + sec_word):
                os.remove(cdir + sec_word)
                print('file deletion successful')

            if os.path.isdir(cdir + sec_word):
                shutil.rmtree(cdir + sec_word)
                print('folder deletion successful')
        else:
            print('file / folder deletion unsuccessful, file / folder does not exist')

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