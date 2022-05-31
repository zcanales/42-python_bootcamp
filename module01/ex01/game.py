class GotCharacter:
    """A generic class to inherit from to represent a GoT character"""
    def __init__(self, first_name: str = None, is_alive: bool = True):
        print("(Got Character) Constructor called")
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        print("(Stark) Constructor called")
        super(Stark, self).__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
   
    def __doc__(self):
        return( f"A class representing the {self.family_name} family")

    def __del__(self):
        print("(Stark) destructor")

class Lannister(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        print("(Stark) Constructor called")
        GotCharacter.__init__(self, first_name = first_name , is_alive = is_alive)
      #  super().__init__(first_name = first_name , is_alive = is_alive)
        self.house_words = "A Lannister always pays his debts"
        self.family_name = "Lannister"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

if __name__ == '__main__':
    arya = Stark("arya")
    print("Alive :", arya.is_alive)
    arya.die()
    print("Alive :", arya.is_alive)
    print(arya.family_name)
    arya.print_house_words()
    print(arya.__doc__())

    petyr = Lannister("Petyr")
    petyr.print_house_words()

