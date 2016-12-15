import gym
import universe
import random

def determine_turn(turn, observation_n, j, total_sum, prev_total_sum, reward_n):
	#for every 15 iterations, sum total observations if lower then change direction
	if(j >= 20):
		j = 0
		if((prev_total_sum >= total_sum)):
			turn = True

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
	env = gym.make('flashgames.CoasterRacer-v0')
	observation_n = env.reset()

	n = 0
	j = 0
	total_sum = 0
	prev_total_sum = 0
	turn = False

	left = [('KeyEvent', 'ArrowUp', True),('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]
	right = [('KeyEvent', 'ArrowUp', True),('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
	forward = [('KeyEvent', 'ArrowUp', True),('KeyEvent', 'ArrowRight', False),('KeyEvent', 'ArrowLeft', False)]
	
	while True:
		n += 1

		if(n > 1):
			if(observation_n[0] != None):
				prev_score = reward_n[0]

				if(turn):
					# Pick random event
					event = random.choice([left, right])
					action_n = [event for ob in observation_n]
					turn = False
		else:
			# If no turn is needed, go straight
			action_n = [forward for ob in observation_n]

		if(observation_n[0] != None):
			turn, j, total_sum, prev_total_sum = determine_turn(turn, observation_n[0], j, total_sum, prev_total_sum, reward_n[0])
			print(turn)

		print(action_n)
		observation_n, reward_n, done_n, info = env.step(action_n)

		env.render()

if __name__ == '__main__':
    main()