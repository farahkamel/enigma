class Rotors:
    def __init__(
        self, list_maping: list, turnovernotch: list = [], starting_position: str = "a"
    ):
        #ord() is a method that will convert the alpahebet characters to its unicode in each rotor and then be put in a list
        int_maping = [ord(char.lower()) - ord("a") for char in list_maping]
        #making a dictionary for all the 3 rotors, dictionary consists if a tuple for each
        #the dictionay contains the 26 alphabets as keys and the rotor aplhabet order as the values
        self.rotor_forwardd = dict ( zip ( range (26), int_maping))
        #making a dictionary of the backwards by reversing the rotor forward dictionary
        self.rotor_backwardd = {v:k for k,v in self.rotor_forwardd.items()}
        #assigning rotor offset for when each rotation takes place
        self.rotor_offset = ord ( starting_position ) - ord("a")
        self.turnovernotch = turnovernotch
        

    def Rotor_maping(self, charactervalue, backwardd=False):
        #rotor map that contains both the rotor forwad and backward
        Rotor_map = self.rotor_backwardd if backwardd else self.rotor_forwardd
     
        offsetted_num = (charactervalue + self.rotor_offset) %26
        rotor_internal_mapping = Rotor_map[offsetted_num]
        next_endingposition = (rotor_internal_mapping - self.rotor_offset)%26
        return next_endingposition


    def rotor_rotation(self):
        self.rotor_offset = (self.rotor_offset + 1) % 26
        

    def currentplace(self):
        return chr(self.rotor_offset + ord("a"))

    def positioning(self, char):
        self.rotor_offset = ord(char) - ord("a")


class Reflectors:
    def __init__ (self, list_maping: list):
        #making a list for the reflector's letters order 
        int_maping = [ord(char.lower()) - ord("a") for char in list_maping]
        #selftwowaymaping is a dictionary that contains the 26 alpahbets as keys and the reflector aplhabet order as the values
        self.twowaymaping = dict( zip( range (26), int_maping))
      
        
        for k, v in self.twowaymaping.items():
            if self.twowaymaping[v] != k:
                raise ValueError("Error. The Reflector only works with two way mapping.")

    def Reflctor_maping(self, number):
        return self.twowaymaping[number]


class EnigmaMachine:
    def __init__(
        self,
        reflector: Reflectors,
        third_rotor: Rotors,
        second_rotor: Rotors,
        first_rotor: Rotors,
        two_step: bool = False,
    ):
        self.third_rotor = third_rotor
        self.second_rotor = second_rotor
        self.first_rotor = first_rotor
        self.reflector = reflector

        self.two_step = two_step

    def __getitem__(self, character):
        #if the user inputted any character not in the 26 alpahets(numbers or special characters) it will be returned as it is
        if not character.isalpha():
            return character

        self.rotation_mechanism()

        char_value = ord(character.lower()) - ord("a")
        result = self.first_rotor.Rotor_maping(char_value)
        result = self.second_rotor.Rotor_maping(result)
        result = self.third_rotor.Rotor_maping(result)
        result= self.reflector.Reflctor_maping(result)
        result = self.third_rotor.Rotor_maping(result, backwardd=True)
        result = self.second_rotor.Rotor_maping(result, backwardd=True)
        result = self.first_rotor.Rotor_maping(result, backwardd=True)
        final_character = chr(result + ord("a"))
        return final_character

    def rotation_mechanism(self):
        third = self.third_rotor
        second = self.second_rotor
        first = self.first_rotor

        secondshouldrotate = False
        thirdshouldrotate = False

        if self.two_step:
            if first.currentplace() in first.turnovernotch:
                secondshouldrotate = True
            if second.currentplace() in second.turnovernotch:
                secondshouldrotate = True
                thirdshouldrotate = True

        else:
            if first.currentplace() in first.turnovernotch:
                secondshouldrotate = True
                if second.currentplace() in second.turnovernotch:
                    thirdshouldrotate = True

        first.rotor_rotation()
        if secondshouldrotate:
            second.rotor_rotation()
        if thirdshouldrotate:
            third.rotor_rotation()

    def show_place(self):
        leftrotor = self.third_rotor.currentplace()
        midrotor = self.second_rotor.currentplace()
        rightrotor = self.first_rotor.currentplace()

        print(f"{leftrotor.upper()}{midrotor.upper()}{rightrotor.upper()}")

    def positioning(self, place):
        Left, Middle, Right = [char.lower() for char in place]

        self.third_rotor.positioning(Left)
        self.second_rotor.positioning(Middle)
        self.first_rotor.positioning(Right)

    def encryption(self, txt):
        return "".join([ self [character ] for character in txt])


def MainProgram():
    # Assigning the Rotors and their notches
    enigma_rotor_I = Rotors(list("ekmflgdqvzntwoyhxuspaibrcj"), turnovernotch=["t"]) #right rotor and its turnover
    enigma_rotor_II = Rotors(list("bdfhjlcprtxvznyeiwgakmusoq"), turnovernotch=["e"])# middle rotor and its turnover
    enigma_rotor_III = Rotors(list("ajdksiruxblhwtmcqgznpyfvoe"), turnovernotch=["g"])# left rotor and its turnover
    enigma1_main_reflector = Reflectors(list("yruhqsldpxngokmiebfzcwvjat")) #wide B reflector

    enigma_components = EnigmaMachine(
        enigma1_main_reflector,
        enigma_rotor_I,
        enigma_rotor_II,
        enigma_rotor_III,
        two_step=True,
    )
    #starting the program
    print (" #############################   WELCOME TO THE FAMOUS ENIGMA MACHINE  !!!! ########################")

    input_data = input("***************************PLEASE ENTER YOUR TEXT***************************************:  ")

    enigma_components.positioning("aaa")
    encrypted_data = enigma_components.encryption(input_data)

    print(f"{input_data} 'HAS BEEN ENCODED INTO:' {encrypted_data} ")
    print("-------------------------------------------------------------------------------------------------------")

    enigma_components.positioning("aaa")
    decrypted_data = enigma_components.encryption(encrypted_data)

    print(f"{encrypted_data} 'HAS BEEN DECODED INTO:' {decrypted_data} ")
    print ("#####################################  THE END  ########################################")
    
#Running the main program
if __name__ == "__main__"  :
    MainProgram()