def find_address(list1):
    address1=""
    for index in range(4,7):
        address1=address1+list1[index]
    address2=""
    for index in range(7,11):
        address2=address2+list1[index]
        address=int(address1)+int(address2)
    return address

def find_value(list1,address):
    value=""
    for index in range(1,11):
        value=value+list1[address][index]
    if list1[address][0]=="+":
        value=int(value)
    else:
        value=(-1)*int(value)
    return value 

def find_instruction(list1):
    instruction=""
    for index in range(1,4):
        instruction=instruction+list1[index]
    return instruction    

NameInputFile=raw_input("Enter the name of inputfile:")
inputfile=open(NameInputFile,"r")
ListOfData1=[ ]
line=inputfile.readline()
while line!="\n" and line!="":
    if line[1]=="H" and line[2]=="L" and line[3]=="T":
        start=find_address(list(line.strip()))
    ListOfData1.append(list(line.strip()))
    line=inputfile.readline()
temp1=[ ]
for index in range(0,start):
    temp1.append(['+','0','0','0','0','0','0','0','0','0','0'])
temp2=[ ]
for index in range(start+len(ListOfData1),10000):
    temp2.append(['+','0','0','0','0','0','0','0','0','0','0'])
STORAGE=temp1+ListOfData1+temp2
IC=start
ACC=0
data=STORAGE[IC]
while find_instruction(data)!="HLT":
    
    if find_instruction(data)=="LDA":
        address=find_address(data)
        value=find_value(STORAGE,address)
        ACC=value
        IC+=1
        
    elif find_instruction(data)=="STO":
        address=find_address(data)
        STORAGE[address]=STORAGE[address][0:11-len(str(ACC))]+list(str(ACC))
        IC+=1
        
    elif find_instruction(data)=="ADD":
        address=find_address(data)
        value=find_value(STORAGE,address)
        ACC=ACC+value
        IC+=1
        
    elif find_instruction(data)=="SUB":
        address=find_address(data)
        value=find_value(STORAGE,address)
        ACC=ACC-value
        IC+=1
        
    elif find_instruction(data)=="MPY":
        address=find_address(data)
        value=find_value(STORAGE,address)
        ACC=ACC*value
        IC+=1
        
    elif find_instruction(data)=="DIV":
        address=find_address(data)
        value=find_value(STORAGE,address)
        ACC=ACC/value
        IC+=1
        
    elif find_instruction(data)=="BRU":
        address=find_address(data)
        IC=address
        
    elif find_instruction(data)=="BMI":
        if ACC<0:
            address=find_address(data)
            IC=address
        else:
            IC+=1
    elif find_instruction(data)=="RWD":
        address=find_address(data)
        line=inputfile.readline()
        STORAGE[address]=list(line.strip())
        IC+=1
     
    elif find_instruction(data)=="WWD":
        address=find_address(data)
        value=find_value(STORAGE,address)
        print str(value)+"\n"
        IC+=1
        
    data=STORAGE[IC]

IC=find_address(data)