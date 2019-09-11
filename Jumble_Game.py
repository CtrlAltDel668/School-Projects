import random

class Jumble_game() :
    
    def __init__(self,player):
        self.player = player
        
    def play(self):
        temp_cat = []
        y = int(input('Enter a number : '))
        if y == 1:
            temp_cat.append('cat')
            temp_cat.append('dog')
            temp_cat.append('mouse')
        if y == 2:
            temp_cat.append('pen')
            temp_cat.append('pencil')
            temp_cat.append('bag')
        if y == 3:
            temp_cat.append('ball')
            temp_cat.append('net')
            temp_cat.append('shoes')
            temp_cat.append(catergory3)
        list1 = temp_cat
        x = random.choice(list1)
        char_name2 = list(x)
        random.shuffle(char_name2)
        String_name1 = ','.join(char_name2)
        
        while True :
            while True :
                list1 = temp_cat
                x = random.choice(list1)
                char_name2 = list(x)
                random.shuffle(char_name2)
                
                if y == 1 :
                    String_name1 = ','.join(char_name2)
                    print(char_name2)
                    c = input('Enter a word : ')
                    
                    if c == x :
                        print('win!!')
                        self.player.inc_score()
                        list1.remove(x)
                        #list1.append('')
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
                ############################################################
                        if hint == 1 and x == 'cat' :
                            print('H!NT : IT IS A MAMMAL')
                            indexInt.remove(hint)
                        if hint == 2 and x == 'cat' :
                            print('H!NT : IT IS A DOMESTICATED ANIMAL')
                            indexInt.remove(hint)
                        if hint == 3 and x == 'cat' :
                            print('H!NT : IT HAS FOUR LEGS')
                            indexInt.remove(hint)
                ############################################################
                        if hint == 1 and x == 'mouse' :
                            print('H!NT : IT IS A TYPE OF RODENT')
                            indexInt.remove(hint)
                        if hint == 2 and x == 'mouse' :
                            print('H!NT : IT IS A SMALL ANIMAL')
                            indexInt.remove(hint)
                        if hint == 3 and x == 'mouse' :
                            print('H!NT : IT HAS SMALL ROUNDED EARS')
                            indexInt.remove(hint)
                        self.player.dec_Hp
                    if c != x :
                        break
            if self.player.get_Hp == 0:
                print('GAME OVER!')
                print('SCORE : ', self.player.get_score)
        
        
        
        
        
        
##########################################################################
class player():
    
    def __init__(self,name):
        self.Hp = 3
        self.score = 0
        self.name = name

    def get_name(self):
        return self.name
    def dec_Hp(self):
        self.Hp = self.Hp - 1
    def inc_score(self):
        self.score = self.score + 1
    def get_Hp(self):
        return self.Hp
    def get_score(self):
        return self.score

kent = player('kent')
y =Jumble_game(kent)
y.play()


