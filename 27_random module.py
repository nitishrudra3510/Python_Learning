##
import random          # ramdom: to create random number or random strings 
random_number = random.randint(0,10)
print(random_number)


rand = random.random() * 100
print(rand)

lst = ["Star Plus", "DD1", "Aaj Tak", "CodewithHarry"]
choice = random.choice(lst)
print(choice)

#Python Random Module:

# random.randint(): method is used to generate random integers between the given range
# syntax: randint(start, end)

r1 = random.randint(5, 15)
print("Random number between 5 and 15 is % s" % (r1))


# randon.random(): method is used to generate floats between 0.0 to 1.
#print(random.random())


# random.choice():  function is used to retur a random items from a list, tupe, or string.
#as a list:
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

# as a tuple:
string = "geeks"
print(random.choice(string))


#shuffling list():  method is used to shuffle a sequence(list). changing the position of the element  of the sequence.
sample_list = [1, 2, 3, 4, 5]
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)


# uniform(): returns random floating number between two numbers both inclusive.
'''
# the application of uniform()
# for using uniform()
import random, math

player1 = 4.50
player2 = 3.78                       # initializing player numbers
player3 = 6.54

winner = random.uniform(2, 9)                 # generating winner random number

diffa = math.fabs(winner - player1)
diffb = math.fabs(winner - player2)    # finding closest 
diffc = math.fabs(winner - player3)
if(diffa < diffb and diffa < diffc):     # printing winner:
    print("The winner of game is : ", end ="")
    print("Player1")
if(diffb < diffc and diffb < diffa):
    print("The winner of game is : ", end ="")
    print("Player2")
      
if(diffc < diffb and diffc < diffa):
    print("The winner of game is : ", end ="")
    print("Player3")
'''


# triangular(): return a random floating point number within   a range with a bias towards one extreme
# sample (): returns a particular length list of items chosen from the sequence
# choises(): returns multiple rando elements from the lists with relacement
# randrange(): returns a arandom number within the range
# seed(): returns a random number generator
random.seed(0)
print(random.randint(0, 5))





 


