import gym
import universe
import random

def determine_turn(turn, observation_n, j, total_sum, prev_total_sum, reward_n):
	# For every 15 iterations, sum total observations and take average. If lower than 0, change direction
	# This makes it more accurate since the iterations are very fast.
	if(j >= 15):
		
		if((total_sum / j) == 0):
			turn = True
		else:
			turn = False
		
		total_sum = 0
		j = 0
		prev_total_sum = total_sum
		total_sum = 0
	
	else:
		turn = False
	
	if(observation_n != None):
		j+=1
		total_sum += reward_n
	print(j)

	return(turn, j, total_sum, prev_total_sum)


def main():
	# Init environment
	env = gym.make('flashgames.CoasterRacer-v0')
	observation_n = env.reset()

	# Init starting variables
	n = 0
	j = 0
	total_sum = 0
	prev_total_sum = 0
	turn = False

	# Init keys
	left = [('KeyEvent', 'ArrowUp', True),('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]
	right = [('KeyEvent', 'ArrowUp', True),('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
	forward = [('KeyEvent', 'ArrowUp', True),('KeyEvent', 'ArrowRight', False),('KeyEvent', 'ArrowLeft', False)]
	
	# Run while True
	while True:
		n += 1
		
		# If at least one iteration has been made, check if turn is needed.
		if(n > 1):
			if(observation_n[0] != None):
				prev_score = reward_n[0]

				if(turn):
					# Pick random event
					event = random.choice([left, right])
					action_n = [event for ob in observation_n]
					turn = False
		elif(~turn):
			# If no turn is needed, go straight
			action_n = [forward for ob in observation_n]

		# If there is an observation, game has started and check if turn is needed or ont
		if(observation_n[0] != None):
			turn, j, total_sum, prev_total_sum = determine_turn(turn, observation_n[0], j, total_sum, prev_total_sum, reward_n[0])

		# Save new variables for each iterations
		observation_n, reward_n, done_n, info = env.step(action_n)

		env.render()

if __name__ == '__main__':
    main()