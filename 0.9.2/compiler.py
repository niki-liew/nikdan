import os, time

activated = False

c_i_c = ['mri', 'mra', 'gk', 'agl', 'fopen', 'termin']

keywords = ['~', '!']

commands_ = [['init',        '~'],
            ['initf',        'def ~:'],
            ['termout',      'print(~)'],
            ['if',           'if ~:'],
            ['else',         'else:',],
            ['while',        'while:'],
            ['mri',          'random.randint(~)'],
            ['mra',          'random.choice(~)'],
            ['gk',           'keyboard.is_pressed(~)'],
            ['delay',        'time.sleep(~)'],
            ['include',      'import ~'],
            ['ret',          'return ~'],
            ['tostring',     'str(~)'],
            ['tointeger',    'int(~)'],
            ['toarray',      'list(~)'],
            ['uppercase',    '~ = ~.upper()'],
            ['lowercase',    '~ = ~.lower()'],
            ['agl',          'len(~)'],
            ['aaae',         '~.append(!)'],
            ['ac',           '~.clear()'],
            ['agi',          '~.index(!)'],
            ['fopen',        'open(~, "rt")'],
            ['fclose',       '~.close()'],
            ['fwrite',       '~.write(!)'],
            ['<>',           '# ~'],
            ['>>',           '    '],
            ['out',          'break'],
            ['exit',         'quit()'],
            ['termin',       'input()'],
            ['termde',       'input()'],
            ['dllm',         'time.sleep(0)'],
            ['cls',          'os.system("cls")'],
            ['omnipresence', 'print("NIKI IS YOUR KING")'],]

def in_com(args):
    has_command = False
    command = ''
    argus = ''

    for i in list(args):
        if has_command == False:
            if i != ' ':
                command += i
            
            else:
                for j in c_i_c:
                    if command == j:
                        has_command = True
                        break

        else:
            argus += i

    return [command, argus]

def commands(command, args, name):
    file = open(name + '.py', 'at')

    def printf(stuff):
        file.write(stuff)
        print(stuff, end='')

    def enter():
        file.write('\n')
        print('\n')

    has_more_than_one_arg = False
    p_args = []
    ignore_space = False
    buf_word = ''

    for i in list(args):
        if ignore_space:
            if i == "'":
                buf_word += i
                p_args.append(buf_word)
                ignore_space = False

            else:
                buf_word += i

        else:
            if i == ' ':
                p_args.append(buf_word)
                buf_word = ''

            else:
                buf_word += i

            if i == "'":
                ignore_space = True
                buf_word += i

    cc = False
    proc_c = ''

    e_command = ''
    e_args = ''
    has_command = False

    for i in commands_:
        if i[0] == command:
            for j in list(i[1]):
                if j == '!':
                    has_more_than_one_arg = True
                    break

    for i in commands_:
        if i[0] == command:
            for j in list(i[1]):
                if has_more_than_one_arg:
                    for b, a in keywords:
                        if j == a and has_command == False:
                            printf(p_args[b])

                        else:
                            printf(j)

                            if j != '~' and j != ')':
                                proc_c += j

                        if list(i[1])[-1] == j:
                            enter()

                else:
                    if j == keywords[0] and has_command == False:
                        printf(args)

                    else:
                        printf(j)

                        if j != '~' and j != ')':
                            proc_c += j

                    if list(i[1])[-1] == j:
                        enter()

                sub = ''

                for aaa in list(i[1]):
                    if aaa != ' ' and aaa != '~':
                        sub += aaa

                    else:
                        break

                # if proc_c == sub and cc == False: WHAT IS THE ISSUE???????????????
                #     cc = True

                if cc:
                    for i in list(args):
                        if has_command == False:
                            if i != ' ':
                                e_command += i
                            else:
                                has_command = True
                        else:
                            e_args += i

                    allowed_r = False

                    for i in c_i_c:
                        if i == e_command:
                            allowed_r = True
                        
                    if allowed_r:
                        cc = False
                        commands(e_command, e_args, name)

    file.close()
    
def compile(start, name):
    file = open(name + '.py', 'wt')
    file.write('')
    file.close()
    file = open(start, 'rt')

    args = ''
    sentences = []
    buf_sentence = ''
    command = ''
    has_command = False

    for sentence in list(file):
        for i in sentence:
            if i == '\n' or i == '|':
                if i == '|':
                    buf_sentence += i
                    sentences.append(buf_sentence)
                    buf_sentence = ''

                else:
                    sentences.append(buf_sentence)
                    buf_sentence = ''
            
            else:
                buf_sentence += i

    for sentence in sentences:
        for i in sentence:
            if has_command == False:
                if i != ' ':
                    command += i
                else:
                    has_command = True
            else:
                if i != '|':
                    args += i
                else:
                    commands(command, args, name)

                    has_command = False
                    command = ''
                    args = ''

def protection(file):
    if os.path.exists(file):
        word = ''

        for i in list(file):
            if i == '.':
                word = ''
            else:
                word += i
        
        if word == 'nikl':
            name = []
            crea = []
            word = ''
            real = ''

            for i in list(file):
                if i == '.':
                    name.append(word)
                    word = ''
                else:
                    word += i

            for i in name:
                crea.append(i)
                crea.append('.')

            crea.pop()

            for i in crea:
                real += i

            compile(file, real)

    else:
        print('compilation unsuccessful, file does not exist')

# protection('bruh.nikl')