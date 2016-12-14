import gym
import universe
import random

env = gym.make('flashgames.CoasterRacer-v0')
observation_n = env.reset()


actions = ['ArrowRight', 'ArrowLeft']
n = 0
start = False
prev_score = []
prev_score.append(-1)
j = 0
total_sum = 0
prev_total_sum = 0
turn = False
prev_event = 'ArrowLeft'

while n < 10000:
	n += 1

	if(n > 1):
		if(observation_n[0] != None):
			prev_score = reward_n[0]

			if(turn):
				if(prev_event == 'ArrowLeft'):
					event = 'ArrowRight'
				else:
					event = 'ArrowLeft'
				prev_event = event

				action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
				env.step([[('KeyEvent', event, True)] for ob in observation_n])
				turn = False
	else:

		action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]

	observation_n, reward_n, done_n, info = env.step(action_n)
	#print('reward: ' + str(total_sum) + ' keyEvent: ' + str(action_n) + ' n: ' + str(n))


	#for every ten iterations, sum total observations if lower then change
	if((j >= 15) and (observation_n[0] != None)):
		j = 0
		if((prev_total_sum > total_sum) and turn == False):
			turn = True
		elif((prev_total_sum > total_sum) and turn == True):
			turn = False

		prev_total_sum = total_sum
		total_sum = 0

	if(observation_n[0] != None):
		j+=1
		total_sum += reward_n[0]
	

	#Always press forward

	#If user sees object try to go around

	#if user goes to the left of the road it means there is a turn so 
	# the bot should always try to stay in the middle

	env.render()