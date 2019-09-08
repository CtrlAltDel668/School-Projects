import random
class Jumble_Game():

	def __init__(self,player):
		self.player = player

	def selection(self,x):
		self.x = int(input('enter a number from 1-3 : '))
		if x == 1 :
			self.catergory1 = ['cat','dog','mouse']
		if x == 2 :
			self.catergory2 = ['book','pencil','pen']
	 	if x == 3:
	 		self.catergory3 = ['ball','net','shoes']

	def play(self):
		list1 = self.selection()
		y = random.choice(list1)
		char_name2 = list(y)
		random.shuffle(char_name2)

		while True :
			while True :
				list1 = self.selection()
				x = random.choice(list1)
				char_name2 = list(y)
				random.shuffle(char_name2)

				if self.x == 1 :
					String_name1 = ','.join(char_name2)
					print(char_name2)
					c = input('enter a word : ')

					if c == x :
						print('win!!')
						self.player.score()
					else:
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
			self.player.HP()
			if self.player.get_HP() == 0:
				print('GAMEOVER!!!')
        		print('SCORE : ',self.player.get_score())
				break


class player():
	
	def __init__(self,name):
		self.name = name
		self.HP = 3
		self.score = 0

	def get_name(self):
		return self.name
	def get_HP(self):
		return self.HP
	def get_score(self):
		return self.score
	def Hp (self):
		self.HP = self.HP -1
	def score(self):
		self.score = self.score + 1
	#def move(self):
	#	catergory1 = [cat,dog,mouse]
	#	return random.choice(catergory1)
	#	catergory2 = [book,pencil,pen]
	#	return random.choice(catergory2)
	#	catergory3 = [ball,net,shoes]
	#	return random.choice(catergory3)