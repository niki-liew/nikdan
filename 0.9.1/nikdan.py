import os, time, compiler

code = []
debugMode = 0

print('nikdan v0.9.1')

while True:
    user_input = None

    if debugMode == 1:
        user_input = list('run n.nikl.py')
        time.sleep(1)
    else:
        user_input = list(input('N '))

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

    if command == 'cls':
        os.system('cls')

    if command == 'compile':
        compiler.compile(sec_word)

    if command == 'save':
        file = open('nikdanver' + sec_word, 'wt')
        file.write('')
        file = open('nikdanver' + sec_word, 'at')

        file.write('/nikdanver/\n')

        for j in code:
            file.write(str(j[0]) + '\n' + j[1] + '\n')

        file.close()
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

        print('save successful')

    if command == 'load':
        code.clear()

        file = open('nikdanver' + sec_word, 'r')
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
            print('load unsuccessful')
    
    if command == 'remove':
        for i in code:
            if sec_word.isnumeric and i[0] == int(sec_word):
                code.remove(i)
                break

    if command == 'exit':
        quit()

    if command == 'run':
        print('running')
        exec(open(sec_word).read())

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