import random

balls = ['White', 'White', 'Blue', 'Blue', 'Green', 'Green']

first_ball = random.choice(balls)
balls.remove(first_ball)

second_ball = random.choice(balls)

print('First ball drawn:', first_ball)
print('Second ball drawn:', second_ball)

if first_ball == 'White':
    remaining_red = balls.count('White')
    total_remaining = len(balls)
    probability = remaining_red/total_remaining
    print(f'\nConditional Probability (2nd White | 1st White) = {probability:.2f}')
else:
    print('\nSince first ball is not White, the condition doesnt apply.') 