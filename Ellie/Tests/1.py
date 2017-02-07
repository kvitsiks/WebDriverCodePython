def squirrel_play(temp, is_summer):
    return temp > 60 and (temp < 90 or (is_summer and temp < 100))

#
#
# import random
# def random_list(full_list):
#     full_list = list(set(full_list))
#     num = random.randint(1, len(full_list))
#     return random.sample(full_list, num)
#
#
#
# def hit_target():
#     x,y = 0,0
# while t.distance(x,y) > t.distance(x+1,y+1):
#     x += 1
#     y += 1
# while t.distance(x,y) > t.distance(x+1,y):
#     x += 1
# while t.distance(x,y) > t.distance(x,y+1):
#     y += 1
# return x,y
#
#
#
# def tri_area(a,b,c):
# 	def trapez(p, q): return (q[0] - p[0]) * ((p[1] + q[1]) / 2.0)
#         return abs(trapez(a, b) + trapez(b, c) + trapez(c, a))
#
#
#
