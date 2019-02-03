string = ""
f = open("/home/joheen_c/text.txt")
for x in f:
    if "\"text\":" in x:
        string = x
f.close()
string = string.partition("text\": ")[2]
string = string[1:len(string)-2]
string = string.replace('\\n', '\n').replace('\\"', '\"')
string = string.lower()
fout = open("/home/joheen_c/code.c", "w")
fout.write(string)
fout.close()
