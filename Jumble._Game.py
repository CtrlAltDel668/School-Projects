import random


class Jumble_game():
    def __init__(self, player):
        self.player = player
        self.select = 0
        self.category = []
        self.rand_ = ''


    def play(self):
        self.select = input('enter a number(1-3) : ')
        if self.select == 1 :
            category = ['cat', 'dog', 'mouse']
            self.rand_ = random.choice(category)
        if self.select == 2 :
            category = ['pen', 'pencil', 'bag']
            self.rand_ = random.choice(category)

        char_word = list(self.rand_)
        random.shuffle(char_word)

        while True :
            while True :
                if self.select == 1:
                    category = ['cat', 'dog', 'mouse']
                    self.rand_ = random.choice(category)
                if self.select == 2:
                    category = ['pen', 'pencil', 'bag']
                    self.rand_ = random.choice(category)
                char_word = list(self.rand_)
                random.shuffle(char_word)
                print(char_word)
                input_word = input('Enter a word :')

                if input_word == self.rand_ :
                    print('Correct!')
                    self.player.inc_score()
                else :
                    rand_int = [1, 2, 3]
                    hint = random.choice(rand_int)
                    if hint == 1 and self.rand_ == 'cat':
                        print('H!NT : IT IS A MAMMAL')
                        rand_int.remove(hint)
                    if hint == 2 and self.rand_ == 'cat':
                        print('H!NT : IT HAS FOUR LEGS')
                        rand_int.remove(hint)
                    if hint == 3 and self.rand_ == 'cat':
                        print('H!NT : IT IS A DOMESTIC ANIMAL')
                        rand_int.remove(hint)

                if input_word != self.rand_ :
                    break
            self.player.dec_Hp()
            if self.player.get_Hp() == 0 :
                print('GAME OVER!!')
                break
            print('SCORE: ', self.player.get_score())


class Player():
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


kent = Player('Kent')
game = Jumble_game(kent)
game.play()
