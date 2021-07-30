#Case1_collatz
def collatz(number):
    if number%2==0:
        print(number//2)
        n=number//2
    else:
        print(3*number+1)
        n=3*number+1
    return n
#定义collatz函数
print("Please enter a number")
EnteredNumber=int(input())
while EnteredNumber==1:
    print("The number you entered first can not 1")
    print("Please entered the number again")
    EnteredNumber=int(input())
    continue
while EnteredNumber!=1:
    EnteredNumber=collatz(EnteredNumber)
    continue
print("Well,the number you entered has been calculated to 1 finally")

#Case2_逗号代码
def Confun(list):
    n=len(list)
    i=0
    x='answer is '
    while i<n-1:
        x=x+str(list[i])+', '
        i=i+1
    if i==n-1:
        x=x+"and"+str(list[i])
    return x
spam=['apples','bananas','tofu','cats']
print(Confun(spam))

#Case3_字符网格
 grid = [ ['.', '.', '.', '.', '.','.'],
          ['.', '0', '0', '.', '.','.'],
          ['0', '0', '0', '0', '.','.'],
          ['0', '0', '0', '0', '0','.'],
          ['.', '0', '0', '0', '0','0'],
          ['0', '0', '0', '0', '0','.'],
          ['0', '0', '0', '0', '.','.'],
          ['.', '0', '0', '.', '.','.'],
          ['.', '.', '.', '.', '.','.']]
 c=[]
 c=copy.deepcopy(grid)
 print(c)
 gridLen=len(grid)
 cyctime=len(grid[0])
 print(gridLen)
 print(cyctime) 
# i=0(Can be deleted cause defautly equal 0)
# j=0(Can be deleted cause defautly equal 0)
 for j in range(cyctime):
     if j < cyctime :
         for i in range(gridLen):
             if i < gridLen :
                 print(c[i][j],end=' ')
                 i=i+1
     print('\n')
     j=j+1

#打印字符数量
import pprint
message='it was a bright cold day in APril, and the clocks were striking.'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint(count)

#井字棋盘
theboard={'top-L':' ','top-M':' ','top-R':' ',
'mid-L':' ','mid-M':' ','mid-R':' ',
'bot-L':' ','bot-M':' ','bot-R':' '}
def printboard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+_+_')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+_+_')
    print(board['bot-L']+'|'+board['bot-M']+'|'+board['bot-R'])
turn='x'
for i in range(9):
    printboard(theboard)
    print('Turn for '+turn+' .Move on which space')
    print('Please enter the location on the board')
    move=input()
    theboard[move]=turn
    if turn=='x':
        turn='o'
    else:
        turn='x'
printboard(theboard)
