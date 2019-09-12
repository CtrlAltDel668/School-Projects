import random
import threading

class RR() :
	def __init__(self,v):
		self.v = v
	def kapoy (self):
		print('Russian Roulette is starting!!')
		if self.v == 0 :
			def random1():
				print('Randomizing your punishment...')
			timer = threading.Timer(1.0, random1)
			timer.start() 
			def random2():
				print('Randomizing your punishment....')
			timer = threading.Timer(2.0, random2)
			timer.start()
			def random3():
				print('Randomizing your punishment.....')
			timer = threading.Timer(3.0, random3)
			timer.start()
			def start ():
				punishment_ = ['[Shout you name 3 times]','[Kiss the forehead of your friend]','[Roll 3 times]',
							'[Confess you embarassing moments in the past]',
							'[Bang your head in the door]','[Slap your face 3 times]','[Imitate an animal for 10 secs]',
							'[Sing your favorite song]',
							'[Dance for 20 secs]','[Say HI! to a random person]']
				rand_punishment = random.choice(punishment_)
				print('***********************')
				print(rand_punishment)
				print('***********************')
			timer = threading.Timer(4.0, start)
			timer.start()

