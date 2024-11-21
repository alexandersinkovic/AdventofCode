
#pattern = ['0','1','0','-1']
newPattern = ''
#for c in pattern:
#    newPattern = newPattern + c*3
#print(newPattern)
#print(len(input))
def doStuff(input):    
    for i in range(0,len(input)):
        pat = ''
        minus = "1"
        while len(pat) < len(input)+1:
            pat = pat + '0' * (i+1)
            pat = pat + minus * (i+1)
            minus = str(int(minus) * -1)
        pat = pat[1:len(input)+1:]
        print(pat)

def splitInput(input):
    for i in range(0,len(input)):
        print(input[i::i+1])

#splitInput(test1)
doStuff(test1)