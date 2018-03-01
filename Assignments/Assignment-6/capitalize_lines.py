lines=[]
print ("Enter the lines:\t")
while True :
    line=input()
    line=line.upper()
    if line:
        lines.append(line)
    else:
        break


text='\n'.join(lines)
print (text)