# my_name = 'Zed A. Shaw'
# my_age = 35 # not a lie
# my_height = 74 # inches
# my_weight = 180 # lbs
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Brown'
#
# print "My name is %r I live in %s. I like to play %s and to watch %s" % (my_name, my_eyes, my_age, my_weight)
#
# print "Let's talk about %s." % my_name
# print "He's %s inches tall." % my_height
# print "He's %d pounds heavy." % my_weight
# print "Actually that's not too heavy."
# print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# print "His teeth are usually %s depending on the coffee." % my_teeth
#
# # this line is tricky, try to get it exactly right
# print "If I add %d, %d, and %d I get %d." % (
#     my_age, my_height, my_weight, my_age + my_height + my_weight)


# x = "There are %d types of people." % 10
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s." % (binary, do_not)
#
# print x
# print y
#
# print "I said: %r." % x
# print "I also said: '%s'." % y
#
# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! %r"
#
# print joke_evaluation % hilarious
#
# w = "This is the left side of..."
# e = "a string with a right side."
#
# print w + e


# print "Mary had a little lamb."
# print "Its fleece was white as %s." % 'snow'
# print "And everywhere that Mary went."
# print "." * 10  # what'd that do?
#
# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"
#
# # watch that comma at the end.  try removing it to see what happens
# print end1 + end2 + end3 + end4 + end5 + end6,
# print end7 + end8 + end9 + end10 + end11 + end12

# formatter = "%s " "%s " "%s " "%r "
#
# print formatter % (1, 2, 3, 4)
# print formatter % ("fsdf", "afasdf", "three", "four")
# print formatter % (True, False, False, True)
# print formatter % (formatter, formatter, formatter, formatter)
# print formatter % (
#     "I had this thing.", "That you could type up right.",
#     "But it didn't sing.",
#     "So I said goodnight."
# )


# Here's some new strange stuff, remember type it exactly.

# days = "Mon Tue\n Wed Thu Fri Sat Sun"
# months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#
# print "Here are the days: %r and %s" % (days, months)
# print "Here are the months: ", months
#
# print """
# There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.
# """


# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat."
#
# fat_cat = """
# \t\t\tI'll do a list:
# \t1 Cat food
# \t2 Fishies
# \t3 Catnip\n\t4 Grass
# """
#
# print tabby_cat
# print persian_cat
# print backslash_cat
# print fat_cat

# print """
# \t* \\	Backslash (\)
# \t* \'	Single-quote (')
# \t* \"	Double-quote (")
# \t* \a	ASCII bell (BEL)
# \t* \b	ASCII backspace (BS)
# \t* \f	ASCII formfeed (FF)
# \t* \n	ASCII linefeed (LF)
# \t* \N{name}	Character named name in the Unicode database (Unicode only)
# \t* \r	Carriage Return (CR)
# \t	Horizontal Tab (TAB)
# \t* \uxxxx	Character with 16-bit hex value xxxx (Unicode only)
# \t* \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
# \t* \v	ASCII vertical tab (VT)
# \t* \ooo	Character with octal value ooo
# \t*	Character with hex value hh
# """

# age = int(raw_input("How old are you?"))
# height = int(raw_input("How tall are you?"))
# weight = int(raw_input("How much do you weigh?"))
# print "So, you're %s years old, %s cm tall and %s heavy." % (
#     age, height, weight)
# x= float(age + height + weight)/3
# print "Avg is %s" %x

#
# from sys import argv
#
# script, user_name = argv
# prompt = '> '

# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)
#
# print "Where do you live %s?" % user_name
# lives = raw_input(prompt)
#
# print "What kind of computer do you have?"
# computer = raw_input(prompt)
#
# print """
# Alright, so you said %r about liking me.
# You live in %r.  Not sure where that is.
# And you have a %r computer.  Nice.
# """ % (likes, lives, computer)

# for x in range(2, 10):
# 	if 8 % x == 0:
# 		print 8, 'equals', x, '*', 8/x
# 		break

# from sys import argv
# script, filename = argv
# txt = open(filename)
#
# print "Here's your file %r:" % filename
# print txt.read()
#
# print "Type the filename again:"
# file_again = raw_input("> ")
#
# txt_again = open(file_again)
#
# print txt_again.read()


# this one is like your scripts with argv
# def print_two(*args):
#     arg1, arg2 = args
#     print "arg1: %r, arg2: %r" % (arg1, arg2)
#
# # ok, that *args is actually pointless, we can just do this
# def print_two_again(arg1, arg2):
#     print "arg1: %r, arg2: %r" % (arg1, arg2)
#
# # this just takes one argument
# def print_one(arg1):
#     print "arg1: %r" % arg1
#
# # this one takes no arguments
# def print_none():
#     print "I got nothin'."
#
#
# print_two("Zed","Shaw")
# print_two_again("Zed","Shaw")
# print_one("First!")
# print_none()



# def my_function(argi1, argi2, argi3):
#     print argi1, argi2, argi3
#
#
# my_function("tomatoes", "cherry", "")
# my_function(1, 2, 3)
# my_function("cake", 1, 4)

# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print "You have %d cheeses!" % cheese_count
#     print "You have %d boxes of crackers!" % boxes_of_crackers
#     print "Man that's enough for a party!"
#     print "Get a blanket.\n"
#
#
# print "We can just give the function numbers directly:"
# cheese_and_crackers(20, 30)
#
#
# print "OR, we can use variables from our script:"
# amount_of_cheese = 10
# amount_of_crackers = 50
#
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
#
# print "We can even do math inside too:"
# cheese_and_crackers(10 + 20, 5 + 6)
#
#
# print "And we can combine the two, variables and math:"
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# def my_fun(a1,a2,a3):
#     print ("You have 1 %s" % a1)
#     print ("Your 2 function is %s" % a2)
#     print ("Your 3 function is %s" % a3)
#
# print ()
# my_fun("croc", "pop", "sos")
# my_fun(1,2,3)
# my_fun(4*2, 7/7, 5-2)
#
# some_text = 3
# some_text2 =4
# some_text3= 5
# my_fun(some_text+1, some_text2*2, some_text3-1)


# name = raw_input("What is your name? \n")
# profession = raw_input("What is your profisssion? \n")
# print ("So, you are %s and you work as %s. Right?" % (name, profession))
# answer = raw_input()
# print "Cool"
# print ("The length of your name is %s" % len(name) + ' chars')
# myAge_int = int(raw_input('What is your age?'))
# print ('You will be ' + str(int(myAge_int + 1)) + ' in a year.')

print float(3.14)

