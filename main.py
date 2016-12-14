import gym
import universe
import random

env = gym.make('flashgames.CoasterRacer-v0')
observation_n = env.reset()

n = 0
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

				# Combining events does not work well for me.. :(
				action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
				env.step([[('KeyEvent', event, True)] for ob in observation_n])
				#action_n = [[('KeyEvent', 'ArrowUp', True), ('KeyEvent', event, True)] for ob in observation_n]
				turn = False
	else:
		# If no turn is needed, go straight
		action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]

	observation_n, reward_n, done_n, info = env.step(action_n)

	#for every 15 iterations, sum total observations if lower then change direction
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

	env.render()