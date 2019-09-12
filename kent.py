import random
import dula
import roulette
class Jumble_Game():
    
    def __init__(self,player):
        self.player = player
    
    def play(self):
        Hp = 3
        Score = 0
        temp_cat= []
        print('********************************************************')
        print('Legend:')
        print('    Category 1(ANIMALS) press 1')
        print('    Category 2(COUNTRIES) press 2')
        print('    Category 3(DINOSAURS) press 3')
        print('[CAUTION!!! Answer with care!!]')
        print('********************************************************')
        y = int(input('Enter a number(1-3) : '))
        if y == 1:
            temp_cat.append('hyena')
            temp_cat.append('moose')
            temp_cat.append('skunk')
            temp_cat.append('peacock')
            temp_cat.append('wildebeest')
        if y == 2:
            temp_cat.append('cuba')
            temp_cat.append('chad')
            temp_cat.append('ukraine')
            temp_cat.append('bahrain')
            temp_cat.append('afghanistan')
        if y == 3:
            temp_cat.append('aardonyx')
            temp_cat.append('triceratops')
            temp_cat.append('tyrannosaurus')
            temp_cat.append('apatosaurus')
            temp_cat.append('brachiosaurus')
        
        while True :
            
            while True :
                print('Health Points : ',Hp)
                list1 = temp_cat
                x = list1[0]
                o = x.upper()
                char_word = list(o)
                random.shuffle(char_word)
                name1 = ','.join(char_word)
                if y == 1 :
                    print('')
                    print(char_word)
                    input_word = input('Enter a word : ')
                        
                    if input_word == x :
                        print('Correct!')
                        Score = Score + 1
                        list1.remove(x)
                    else :
                        select1 = dula.select(x)
                        select1.Hint1()
                        
                if y == 2 :
                    
                    print(char_word)
                    input_word = input('Enter a word : ')
                    if input_word == x :
                        print('Correct!')
                        Score = Score + 1
                        list1.remove(x)
                    else :
                        select1 = dula.select(x)
                        select1.Hint2()
                        
                if y == 3 :
                    #y = [element.upper() for element in char_word]
                    print(char_word)
                    input_word = input('Enter a word : ')
                    
                    if input_word == x :
                        print('Correct!')
                        Score = Score + 1
                        list1.remove(x)
                    else :
                        select1 = dula.select(x)
                        select1.Hint3()
                        
                if input_word != x :
                    break
                
                if (len(list1)) == 0 :
                    print('CONGRATULATIONS!! YOU CLEARED THE CATEGORY!!')
                    break
                
            if (len(list1)) == 0 :
                print('SCORE : ',Score)
                break
            
            Hp = Hp - 1   
            if Hp == 0:
                print('GAMEOVER!!! prepare for punishment!!')
                print('SCORE : ',Score)
                print('********************************************************')
                k = roulette.RR(Hp)
                k.kapoy()
                break

kent = Jumble_Game('casssie')
kent.play()