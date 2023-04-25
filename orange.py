import random

class OrangeTree:
    def __init__(self, height, age, is_pretty):
        self.height = height
        self.age = age
        self.is_pretty = is_pretty

    def is_pretty_tree(self):
        return self.is_pretty

    def grow(self):
        self.height += 1
        self.age += 1

    def produce_oranges(self):
        return random.randint(0, 100)

# create three orange trees with different attributes
tree1 = OrangeTree(5, 2, False)
tree2 = OrangeTree(7, 3, True)
tree3 = OrangeTree(6, 4, False)

# store the trees in a list
orange_trees = [tree1, tree2, tree3]

# randomly select one of the trees to be the "pretty" tree
pretty_tree = random.choice(orange_trees)

# prompt the user to guess which tree is the pretty one
print("Can you guess which orange tree is the pretty one?")

# display the attributes of each tree and ask the user to choose
for index, tree in enumerate(orange_trees):
    print(f"Tree {index + 1}: height={tree.height}, age={tree.age}")
    guess = input("Is this the pretty tree? (y/n) ")

    # check if the user's guess is correct
    if guess.lower() == "y" and tree.is_pretty_tree():
        print("Congratulations, you guessed correctly!")
        break
    elif guess.lower() == "n" and not tree.is_pretty_tree():
        print("Congratulations, you guessed correctly!")
        break
    else:
        print("Sorry, that's not the right answer.")
