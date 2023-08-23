# 22.1. Introduction: Class Inheritance

'''
Consider our Tamagotchi game. Suppose we wanted to make some different kinds of pets that have the same structure as
other pets, but have some different attributes or behave a little differently. For example, suppose that dog pets
should show their emotional state a little differently than cats or act differently when they are hungry or when they
are asked to fetch something.

You could implement this by making an instance variable for the pet type and dispatching on that instance variable in
various methods.
'''

from random import randrange


class Pet:
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Boom Boom Boom']

    def __init__(self, name="Kitty", pet_type="dog"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class
        self.pet_type = pet_type

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            if self.pet_type == "dog": # if the pet is a dog, it will express its mood in different ways from a cat or any other type of animal
                return "happy"
            elif self.pet_type == "cat":
                return "happy, probably"
            else:
                return "HAPPY"
        elif self.hunger > self.hunger_threshold:
            if self.pet_type == "dog": # same for hunger -- dogs and cats will express their hunger a little bit differently in this version of the class definition
                return "hungry, arf"
            elif self.pet_type == "cat":
                return "hungry, meeeeow"
            else:
                return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)


# 22.2. Inheriting Variables and Methods

'''
Inheritance provides us with an easy and elegant way to represent these differences. 
In the definition of the inherited class, you only need to specify the methods and instance variables that are 
different from the parent class (the parent class, or the superclass, is what we may call the class that is inherited 
from.

Here is an example. Say we want to define a class Cat that inherits from Pet. Assume we have the Pet class that we 
defined earlier.

We want the Cat type to be exactly the same as Pet, except we want the sound cats to start out knowing “meow” instead 
of “mrrp”, and we want the Cat class to have its own special method called chasing_rats, which only Cat s have.

We do that by putting the word Pet in parentheses, class Cat(Pet):
'''
#------------- refer to the code above------------------------------append this to it.......
p1 = Pet("Fido")
print(p1) # we've seen this stuff before!

p1.feed()
p1.hi()
print(p1)

cat1 = Cat("Fluffy")
print(cat1) # this uses the same __str__ method as the Pets do

cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi()
print(cat1)

print(cat1.chasing_rats())

#print(p1.chasing_rats()) # This line will give us an error. The Pet class doesn't have this method!

'''
And you can continue the inheritance tree. We inherited Cat from Pet. Now say we want a subclass of Cat called 
Cheshire. A Cheshire cat should inherit everything from Cat, which means it inherits everything that Cat inherits 
from Pet, too. But the Cheshire class has its own special method, smile.
'''

class Cheshire(Cat): # this inherits from Cat, which inherits from Pet

    def smile(self): # this method is specific to instances of Cheshire
        print(":D :D :D")

# Let's try it with instances.
cat1 = Cat("Fluffy")
cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi() # Uses the special Cat hello.
print(cat1)

print(cat1.chasing_rats())

new_cat = Cheshire("Pumpkin") # create a Cheshire cat instance with name "Pumpkin"
new_cat.hi() # same as Cat!
new_cat.chasing_rats() # OK, because Cheshire inherits from Cat
new_cat.smile() # Only for Cheshire instances (and any classes that you make inherit from Cheshire)

# cat1.smile() # This line would give you an error, because the Cat class does not have this method!

# None of the subclass methods can be used on the parent class, though.
p1 = Pet("Teddy")
p1.hi() # just the regular Pet hello
#p1.chasing_rats() # This will give you an error -- this method doesn't exist on instances of the Pet class.
#p1.smile() # This will give you an error, too. This method does not exist on instances of the Pet class.


# intro-9-2: What would print after running the following code:
new_cat = Cheshire("Pumpkin”)
class Siamese(Cat):
  def song(self):
    print("We are Siamese if you please. We are Siamese if you don’t please.")
another_cat = Siamese("Lady")
another_cat.song()
# -> We are Siamese if you please. We are Siamese if you don’t please.
# another_cat is an instance of Siamese, so its song() method is invoked.

# intro-9-3: What would print after running the following code:
new_cat = Cheshire("Pumpkin”)
class Siamese(Cat):
  def song(self):
    print("We are Siamese if you please. We are Siamese if you don’t please.")
another_cat = Siamese("Lady")
new_cat.song()
# -> Error
# You cannot invoke methods defined in the Siamese class on an instance of the Cheshire class. Both are subclasses
# of Cat, but Cheshire is not a subclass of Siamese, so it doesn't inherit its methods.

# 22.3. Overriding Methods

# Here’s the original Pet class again.

from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

'''
Now let’s make two subclasses, Dog and Cat. Dogs are always happy unless they are bored and hungry. Cats, on the other 
hand, are happy only if they are fed and if their boredom level is in a narrow range and, even then, only with 
probability 1/2.
'''

class Cat(Pet):
    sounds = ['Meow']

    def mood(self):
        if self.hunger > self.hunger_threshold:
            return "hungry"
        if self.boredom <2:
            return "grumpy; leave me alone"
        elif self.boredom > self.boredom_threshold:
            return "bored"
        elif randrange(2) == 0:
            return "randomly annoyed"
        else:
            return "happy"

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"

c1 = Cat("Fluffy")
d1 = Dog("Astro")

c1.boredom = 1
print(c1.mood())
c1.boredom = 3
for i in range(10):
    print(c1.mood())
print(d1.mood())

# 22.4. Invoking the Parent Class’s Method

# when the parent class has a useful method, but you just need to execute a little extra code when running the
# subclass’s method

#...refer to the Pets Class again, then see append code below

from random import randrange

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

d1 = Dog("Astro")

d1.feed()


# a better way to invoke a superclass’s method

'''
Let’s say we want to create a subclass of Pet, called Bird, and we want it to take an extra parameter, chirp_number, 
with a default value of 2, and have an extra instance variable, self.chirp_number. Then, we’ll use this in the hi 
method to make more than one sound.
'''

class Bird(Pet):
    sounds = ["chirp"]
    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name) # call the parent class's constructor
        # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
        super().__init__(name)
        self.chirp_number = chirp_number # now, also assign the new instance variable

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

b1 = Bird('tweety', 5)
b1.teach("Polly wanna cracker")
b1.hi()


# 22.5. Tamagotchi Revisited

'''
Using what we know about class inheritance, we can make a new version of the Tamagotchi game, where you can adopt 
different types of pets that are slightly different from one another.

And now we can play the Tamagotchi game with some small changes, such that we can adopt different types of pets. 
'''

import sys
sys.setExecutionLimit(60000)
from random import randrange

class Pet(object):
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.update_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.update_boredom()

    def feed(self):
        self.update_hunger()

    def update_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def update_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

class Cat(Pet):
    sounds = ['Meow']

    def mood(self):
        if self.hunger > self.hunger_threshold:
            return "hungry"
        if self.boredom <2:
            return "grumpy; leave me alone"
        elif self.boredom > self.boredom_threshold:
            return "bored"
        elif randrange(2) == 0:
            return "randomly annoyed"
        else:
            return "happy"

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

class Bird(Pet):
    sounds = ["chirp"]
    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name) # call the parent class's constructor
        # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
        self.chirp_number = chirp_number # now, also assign the new instance variable

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.update_boredom()

class Lab(Dog):
    def fetch(self):
        return "I found the tennis ball!"

    def hi(self):
        print(self.fetch())
        print(self.sounds[randrange(len(self.sounds))])

class Poodle(Dog):
    def dance(self):
        return "Dancin' in circles like poodles do."

    def hi(self):
        print(self.dance())
        Dog.hi(self)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

pet_types = {'dog': Dog, 'lab': Lab, 'poodle': Poodle, 'cat': Cat, 'bird': Bird}
def whichtype(adopt_type="general pet"):
    return pet_types.get(adopt_type.lower(), Pet)

def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                # figure out which class it should be
                if len(words) > 2:
                    Cl = whichtype(words[2])
                else:
                    Cl = Pet
                # Make an instance of that class and append it
                animals.append(Cl(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback+= "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()

play()

#---------------------------- week 2 assessment -----------------------------------------------------

# Q1
'''
The class, Pokemon, is provided below and describes a Pokemon and its leveling and evolving characteristics. 
An instance of the class is one pokemon that you create.

Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, the boost values are 
different.

For the subclass Grass_Pokemon, add another method called action that returns the string "[name of pokemon] knows a 
lot of different moves!". Create an instance of this class with the name as "Belle". Assign this instance to 
the variable p1.
'''


class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return "{} knows a lot of different moves!".format(self.name)


p1 = Grass_Pokemon('Belle')

# Q2
'''
Modify the Grass_Pokemon subclass so that the attack strength for Grass_Pokemon instances does not change until they reach level 10. At level 10 and up, their attack strength should increase by the attack_boost amount when they are trained.

To test, create an instance of the class with the name as "Bulby". Assign the instance to the variable p2. Create another instance of the Grass_Pokemon class with the name set to "Pika" and assign that instance to the variable p3. Then, use Grass_Pokemon methods to train the p3 Grass_Pokemon instance until it reaches at least level 10

'''

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"
    attack_boost = 10

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

p2 = Grass_Pokemon('Bulby')
p3 = Grass_Pokemon('Pika')


# Q4
'''
Along with the Pokemon parent class, we have also provided several subclasses. Write another method in the parent class that will be inherited by the subclasses. Call it opponent. It should return which type of pokemon the current type is weak and strong against, as a tuple.

Grass is weak against Fire and strong against Water

Ghost is weak against Dark and strong against Psychic

Fire is weak against Water and strong against Grass

Flying is weak against Electric and strong against Fighting

For example, if the p_type of the subclass is 'Grass', .opponent() should return the tuple ('Fire', 'Water')
'''


class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.ptype = None
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

    def opponent(self):
        if self.ptype == "Grass":
            return ("Fire", "Water")
        elif self.p_type == "Ghost":
            return ("Dark", "Psychic")
        elif self.p_type == "Fire":
            return ("Water", "Grass")
        else:
            return ("Electric", "Fighting")


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def opponent(self):
        if self.p_type == "Grass":
            return ("Fire", "Water")


class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3


class Fire_Pokemon(Pokemon):
    p_type = "Fire"

    def opponent(self):
        if self.p_type == "Fire":
            return ("Water", "Grass")


class Flying_Pokemon(Pokemon):
    p_type = "Flying"

    def opponent(self):
        if self.p_type == "Flying":
            return ("Electric", "Fighting")

# alternatively...?

    class Pokemon():
        attack = 12
        defense = 10
        health = 15
        p_type = "Normal"

        def __init__(self, name, level=5):
            self.name = name
            self.level = level
            self.weak = "Normal"
            self.strong = "Normal"

        def train(self):
            self.update()
            self.attack_up()
            self.defense_up()
            self.health_up()
            self.level = self.level + 1
            if self.level % self.evolve == 0:
                return self.level, "Evolved!"
            else:
                return self.level

        def attack_up(self):
            self.attack = self.attack + self.attack_boost
            return self.attack

        def defense_up(self):
            self.defense = self.defense + self.defense_boost
            return self.defense

        def health_up(self):
            self.health = self.health + self.health_boost
            return self.health

        def update(self):
            self.health_boost = 5
            self.attack_boost = 3
            self.defense_boost = 2
            self.evolve = 10

        def __str__(self):
            self.update()
            return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

        def opponent(self, p_type):
            if self.ptype == "Grass":
                return ("Fire", "Water")
            elif self.p_type == "Ghost":
                return ("Dark", "Psychic")
            elif self.p_type == "Fire":
                return ("Water", "Grass")
            else:
                return ("Electric", "Fighting")

        def opponent(self, p_type):

        if self.p_type == "Grass":
            return ("Fire", "Water")
        elif self.p_type == "Ghost":
            return ("Dark", "Psychic")
        elif self.p_type == "Fire":
            return ("Water", "Grass")
        else:
            return ("Electric", "Fighting")

    class Grass_Pokemon(Pokemon):
        attack = 15
        defense = 14
        health = 12
        p_type = "Grass"

        def update(self):
            self.health_boost = 6
            self.attack_boost = 2
            self.defense_boost = 3
            self.evolve = 12

        def opponent(self):
            if self.p_type == "Grass":
                return ("Fire", "Water")

    class Ghost_Pokemon(Pokemon):
        p_type = "Ghost"

        def update(self):
            self.health_boost = 3
            self.attack_boost = 4
            self.defense_boost = 3

        def opponent(self):
            if self.p_type == "Ghost":
                return ("Dark", "Psychic")

    class Fire_Pokemon(Pokemon):
        p_type = "Fire"

        def opponent(self):
            if self.p_type == "Fire":
                return ("Water", "Grass")

    class Flying_Pokemon(Pokemon):
        p_type = "Flying"

        def opponent(self):
            if self.p_type == "Flying":
                return ("Electric", "Fighting")

