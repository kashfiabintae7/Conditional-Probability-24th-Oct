red = 2
blue = 4
white = 9

total = red + blue + white

P_red = red / total
P_blue = blue / total

P_second_red_given_first_blue = P_red

P_first_blue_and_second_red = P_blue * P_red

print(f'Total shirts = {total}')
print(f'P(Second Red | First Blue) = {P_second_red_given_first_blue:.4f}')
print(f'P(First Blue and Second Red) = {P_first_blue_and_second_red:.4f}')