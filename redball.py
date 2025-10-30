import random

balls = ['Red', 'Red', 'Blue', 'Blue', 'Green', 'Green']

first_ball = random.choice(balls)
balls.remove(first_ball)

second_ball = random.choice(balls)

print('First ball drawn:', first_ball)
print('Second ball drawn:', second_ball)

if first_ball == 'Red':
    remaining_red = balls.count('Red')
    total_remaining = len(balls)
    probability = remaining_red/total_remaining
    print(f'\nConditional Probability (2nd Red | 1st Red) = {probability:.2f}')
else:
    print('\nSince first ball is not Red, the condition doesnt apply.') 