import os, shutil

step = 1

if os.path.exists("C:\\astnbrwn") == False:
    os.mkdir("C:\\astnbrwn")

    print(str(step) + " INFO: ", end='')
    step += 1
    print("created astnbrwn folder at C:")

if os.path.exists("C:\\astnbrwn\\nikdan.exe"):
    os.remove("C:\\astnbrwn\\nikdan.exe")

    print(str(step) + " INFO: ", end='')
    step += 1
    print("noticed older nikdan version, removed older nikdan version")
    
shutil.move("source\\nikdan.exe", "C:\\astnbrwn")

print(str(step) + " INFO: ", end='')
step += 1
print("moved nikdan.exe from source to C:\\astnbrwn")

if os.path.exists("C:\\windows\\System32\\nikdan.bat") == False:
    file = open("C:\\windows\\System32\\nikdan.bat", "at")
    file.write("@START C:\\astnbrwn\\nikdan.exe")
    file.close()

    print(str(step) + " INFO: ", end='')
    step += 1
    print("created nikdan.bat at C:\\windows\\System32")

print("installation complete\npress enter to close")
input()