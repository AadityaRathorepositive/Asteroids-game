
store={}

def get_book_text(get_book_path):
    with open(get_book_path) as main:
        file_content= main.read()
        def count_word():
            splitted_words=file_content.split()
            i=0
            for splitted_words[i] in splitted_words:
                i+=1
            return i
        return_i=count_word()
        count_of_each_word(file_content)
    return return_i



def count_of_each_word(file_content):
    file_content_in_lower=file_content.lower().split()
    for word in file_content_in_lower:
        for letter in word:
            if letter.isalpha() and letter not in store:
                store[letter]=1    
            elif letter in store:
                store[letter]=store[letter]+1


#count_char=get_book_text()

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        self.__num_arrows-=1
hero1=Archer("ahshjld",11)
hero1.get_name()

class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        pass

    def triple_shot(self, target):
        pass

#print(sorted_list)


class Animal:
    def __init__(self, name):
        self.name  = name
    def walk(self):
        print('walking...')
    def eat(self):
        print('eating')
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def go_for_a_walk(self):
        print('ready for a walk')
        self.walk()
        
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def eat(self):
        print("Nom nom nom...")
class Kitten(Cat):
    def __init__(self, name, color):
        super().__init__(name, color)
    def eat(self):
        print("I eat slowly")
        return super().eat()
    
    
a = Dog('name', 'breed')
a.go_for_a_walk()

b = Kitten('nams', 'sjn')
b.eat()
b.walk()

# tommy.walk()
# pixie.walk()

# tommy.go_for_a_walk()
# tommy.eat()
# pixie.eat()
