import random

catergory1 = ['cat','dog','mouse']
catergory2 = ['book','pencil','pen']
catergory3 = ['ball','net','shoes']
y = int(input('enter a number from 1-3 : '))
hp = 3
score = 0
list1 = catergory1
x = random.choice(list1)
char_name2 = list(x)
random.shuffle(char_name2)

while True:
    
    while True:  
        list1 = catergory1
        x = random.choice(list1)
        char_name2 = list(x)
        random.shuffle(char_name2)
        if y == 1:
            String_name1 = ','.join(char_name2)
            #print(x)
            print(char_name2)
            c = input('enter a word : ')
            if c == x :
                print('win!!')
                score = score + 1
                list1.remove(x)
                
            else :
                print("try again!!")
                indexInt = [1,2,3]
                hint = random.choice(indexInt)
                if hint == 1 and x == 'dog' :
                    print('H!NT : IT IS A MAMMAL')
                    indexInt.remove(hint)
                if hint == 2 and x == 'dog' :
                    print('H!NT : IT IS A DOMESTICATED ANIMAL')
                    indexInt.remove(hint)
                if hint == 3 and x == 'dog' :
                    print('H!NT : IT HAS FOUR LEGS')
                    indexInt.remove(hint)
            ########################################################   
                if hint == 1 and x == 'cat' :
                    print('H!NT : IT IS A MAMMAL')
                    indexInt.remove(hint)
                if hint == 2 and x == 'cat' :
                    print('H!NT : IT IS A DOMESTICATED ANIMAL')
                    indexInt.remove(hint)
                if hint == 3 and x == 'cat' :
                    print('H!NT : IT HAS FOUR LEGS')
                    indexInt.remove(hint)
             #######################################################       
                if hint == 1 and x == 'mouse' :
                    print('H!NT : IT IS A TYPE OF RODENT')
                    indexInt.remove(hint)
                if hint == 2 and x == 'mouse' :
                    print('H!NT : IT IS A SMALL ANIMAL')
                    indexInt.remove(hint)
                if hint == 3 and x == 'mouse' :
                    print('H!NT : IT HAS SMALL ROUNDED EARS')
                    indexInt.remove(hint)
                
        if c != x:
            break
    hp = hp - 1
    if hp == 0:
        print('GAMEOVER!!!')
        print('SCORE : ',score)
        break
