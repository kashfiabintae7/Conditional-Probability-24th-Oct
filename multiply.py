import random

balls = ['Red', 'Red', 'Blue']

first_ball = random.choice(balls)
balls.remove(first_ball)

second_ball = random.choice(balls)

print('First ball drawn:', first_ball)
print('Second ball drawn:', second_ball)

P_A = 2/3

P_B_given_A = 1/2

P_A_and_B = P_A * P_B_given_A

print(f'\nP(First Red) = {P_A:.2f}')
print(f'P(Second Red | First Red) = {P_B_given_A:.2f}')
print(f'P(First red and Second Red) = {P_A_and_B:.2f}')
