""" The "Rotors" class is the main class written to handle the three rotors  with their turnover notches
 ."""
class Rotors:

    """
    each rotor has an object
    Rotors class
    contains : rotors and turnovers 
    """
    
    """ init method of rotors method will be called automatically when the 
    object of class Rotors will be created"""
    def __init__(self, list_maping: list, turnovernotch: list = [], starting_position: str = "a"):
        
        """ord() is a method that will convert the alpahebet characters to its unicode in each rotor and then be put in a list
        it will be saved in int_mapping variable which shows that the characters from the input string are mapped to the 
        numbers (unicode).
        Right now, int mapping has the following output:
        int_maping = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 22, 14, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        """
        int_maping = [ord(char.lower()) - ord("a") for char in list_maping]
        """making a dictionary for all the 3 rotors, dictionary consists if a tuple for each
        the dictionay contains the 26 alphabets as keys and the rotor aplhabet order as the values
        The self.rotor_forwardd has the following dictionary in it:
        self.rotor_forwardd = {0: 4, 1: 10, 2: 12, 3: 5, 4: 11, 5: 6, 6: 3, 7: 16, 8: 21, 9: 25, 10: 13, 11: 19, 12: 22, 13: 14, 14: 24, 15: 7, 16: 23, 17: 20, 18: 18, 19: 15, 20: 0, 21: 8, 22: 1, 23: 17, 24: 2, 25: 9}
        """
        self.rotor_forwardd = dict ( zip ( range (26), int_maping))
        
        """ Now we specify the rotor backward leg. it will just reverse the output of the forward leg of the rotors.
        The self.rotor_backwardd has the following dictionary in it:
        {4: 0, 10: 1, 12: 2, 5: 3, 11: 4, 6: 5, 3: 6, 16: 7, 21: 8, 25: 9, 13: 10, 19: 11, 22: 12, 14: 13, 24: 14, 7: 15, 23: 16, 20: 17, 18: 18, 15: 19, 0: 20, 8: 21, 1: 22, 17: 23, 2: 24, 9: 25}
        We can clearly see that the keys are replaced with values. 4 was the value and 0 was the key in foward. but in 
        backward 4 has become key and 0 as value.
        """
        #making a dictionary of the backwards by reversing the rotor forward dictionary
        self.rotor_backwardd = {v:k for k,v in self.rotor_forwardd.items()}
        
        """ now we are setting the offset value which shows that when the rotor will rotate. as we can see in the
        parameters list of def __init__ method that:
        starting_position: str = "a"  
        which is converted to 97 after applying ord on it as:
        self.rotor_offset = ord ( starting_position ) - ord("a")
                          =  97 - ord("a")
                          = 97 - 97
                           = 0
         So, the current offset is the 0.
        
        """ 
        #assigning rotor offset for when each rotation takes place
        self.rotor_offset = ord ( starting_position ) - ord("a")
        
        """ In the first time,  self.turnovernotch = ['t']
        we got this from the main program. see the following lines:
        
        def MainProgram():
            enigma_rotor_I = Rotors(list("ekmflgdqvzntwoyhxuspaibrcj"), turnovernotch=["t"]) #right rotor and its turnover
            
        so in it, turnovernotch is set as ['t'] so here below,
        self.turnovernotch = ['t']        
        """
        self.turnovernotch = turnovernotch
        
    
   # """ The function below is holding the corresponding mapping of ROTORS"""
    def Rotor_maping(self, charactervalue, backwardd=False):
        #rotor map that contains both the rotor forwad and backward
        """ below is to select which mapping of rotor to use. backward or forward. if the backward parameter in above is = True
         #then the backward mapping will be used. otherwise the backward mapping will be used. 
        """
        Rotor_map = self.rotor_backwardd if backwardd else self.rotor_forwardd
        
        """ the offsetted_num is having the  charactervalue which is in def __getitem__ function:
            char_value = ord(character.lower()) - ord("a")
            it will be added to the self.rotor_offset and then the modulus with 26 will be computed. 26 = total number of characters in string        
        """
     
        offsettednumber = (charactervalue + self.rotor_offset) %26
        
        """ the rotor mapping (backward or forward) will be set for offsetted number of times/ for example if 
        offsetted_num = 3 then 
        rotor_internal_mapping = Rotor_map[3]
        and Rotor_map is having backward. it will be:
        rotor_internal_mapping = [backward, backward, backward]
        """
        internalmapingrotor = Rotor_map[offsettednumber]
        
        """ the next ending position of the rotors is being decided by: subtracting the internal mapping and the offset and then
        modulus by 26. and then it is returned. 
        """
        next_endingposition = (internalmapingrotor - self.rotor_offset)%26
        return next_endingposition

        #""" the rotor rotation is performed in rotor setting. It is rotated either by following a certain pattern
          #or it is fixed. 
        #"""
    def rotor_rotation(self):
        
        self.rotor_offset = (self.rotor_offset + 1) % 26
        
    #""" the below function shows the currentplace of the rotor. it takes the rotor offset and the unicode value of character a.
        #then there summation will be converted to the chr to see the current place. for example:
        #string = "ABFFJFJFGJJHG"
        #rotor_offset = 3
        #ord("a") = 97
        #97 + 3 = 100. Now the current place of the rotor will be the character from the string having unicode as 100. 
    #"""

    def currentplace(self):
        return chr(self.rotor_offset + ord("a"))

    """ the final positioning of the rotor will be decided by computing the offset that how to set position from
        current character char to the next one.
    """
    def positioning(self, char):
        self.rotor_offset = ord(char) - ord("a")

""" class of the reflector to inverse the encrypted character
"""
class Reflectors:
    def __init__ (self, list_maping: list):
        #making a list for the reflector's letters order 
        """ making list here like rotors class. it is having below values:
        {0: 0, 1: 9, 2: 3, 3: 10, 4: 18, 5: 8, 6: 17, 7: 20, 8: 23, 9: 1, 10: 11, 11: 7, 12: 22, 13: 19, 14: 12, 15: 2, 16: 16, 17: 6, 18: 25, 19: 13, 20: 15, 21: 24, 22: 5, 23: 21, 24: 14, 25: 4}
        """
        int_maping = [ord(character.lower()) - ord("a") for character in list_maping]
        #"""selftwowaymaping is a dictionary that contains the 26 alpahbets as keys and the reflector aplhabet order as the values
        #it is holding following values:
        #{0: 24, 1: 17, 2: 20, 3: 7, 4: 16, 5: 18, 6: 11, 7: 3, 8: 15, 9: 23, 10: 13, 11: 6, 12: 14, 13: 10, 14: 12, 15: 8, 16: 4, 17: 1, 18: 5, 19: 25, 20: 2, 21: 22, 22: 21, 23: 9, 24: 0, 25: 19}
        #"""
               
        self.twowaymaping = dict( zip( range (26), int_maping))
        
        

 #""" #the below function performs the two way mapping: forward and backward """
    def Reflctor_maping(self, number):
        return self.twowaymaping[number]

#""" this is the main enigma class """#
class EnigmaMachine:

#"""  it holds the reflectors, the 3 rotors in the contructor """#
    def __init__(
        self,
        reflector: Reflectors,
        third_rotor: Rotors, #the rotor on the left
        second_rotor: Rotors, #middle rotor
        first_rotor: Rotors, #right rotor
        two_step: bool = False,
    ):
    
    #"""setting the parameters to the class variables """
        self.third_rotor = third_rotor
        self.second_rotor = second_rotor
        self.first_rotor = first_rotor
        self.reflector = reflector

        self.two_step = two_step
    def __getitem__(self, character):
        #if the user inputted any character not in the 26 alpahets(numbers or special characters) it will be returned as it is
        if not character.isalpha():
            return character

         #"""  here below, the whole mechnism of rotor mapping is applied. it is taking the characters and mapping them 
         #using three rotors and one reflector
         
        self.rotation_mechanism()

        character_value = ord(character.lower()) - ord ("a")
        result = self.first_rotor.Rotor_maping(character_value)
        result = self.second_rotor.Rotor_maping(result)
        result = self.third_rotor.Rotor_maping(result)
        result= self.reflector.Reflctor_maping(result)
        result = self.third_rotor.Rotor_maping(result, backwardd=True)
        result = self.second_rotor.Rotor_maping(result, backwardd=True)
        result = self.first_rotor.Rotor_maping(result, backwardd=True)
        final_character = chr(result + ord("a"))
        return final_character

    #""" below function is to set the rotation mechanism of the rotors"""
    def rotation_mechanism(self):
        #"""setting the parameters to the class variables """
        third = self.third_rotor
        second = self.second_rotor
        first = self.first_rotor
        #""" the second and third is set to False and first is set to True because only one will be set as True for rotation """ 
        secondshouldrotate = False
        thirdshouldrotate = False

        #""" applying the two step to provide to the reflector and switching on and off their values according to that"""
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
        
        
      #"""performing the rotor rotation in second and third rotors"""
        first.rotor_rotation()
        if secondshouldrotate:
            second.rotor_rotation()
        if thirdshouldrotate:
            third.rotor_rotation()

        #""" the function below is displaying the current position of each of these 3 rotors. and printing  """
    def display_place(self):
        leftrotor = self.third_rotor.currentplace()
        midrotor = self.second_rotor.currentplace()
        rightrotor = self.first_rotor.currentplace()

        print(f"{leftrotor.upper()}{midrotor.upper()}{rightrotor.upper()}")

    #""" the function below is to set the positions of all three rotors: left right and middle. """
    def positioning(self, place):
        Left, Middle, Right = [char.lower() for char in place]
        #"""left right and Middle all are holding 'a'  """ 
        
        #""" applying the first, second and third rotor to the Left, Middle and Right reflectors"""
        self.third_rotor.positioning(Left)
        self.second_rotor.positioning(Middle)
        self.first_rotor.positioning(Right)

    #""" perform the actual encryption through the enigma machine"""
    def encryption(self, txt):
        return "".join([ self [character ] for character in txt])

def MainProgram():

    #""" This is the main program. to deal with all three rotors """
#"""# The rotors in enigma machine are identified with the roman letters. So these are named as: 
#"I", "II", "III", "IV", "V" """    
# Assigning the Rotors and their notches
    
            #""" As a rotor performs encryption so as if we compare self.chars with rotors we get below:
        #self.chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #rotor I = "PEZUOHXSCVFMTBGLRINQJWAYDK"
        #rotor II = "ZOUESYDKFWPCIQXHMVBLGNJRAT"
        #rotor III = "EHRVXGAOBQUSIMZFLYNWKTPDJC"
        
        #so it means the encryption for letter "A" (see the first letter of self.chars) will be encrypted as:
            #i)  "P" for rotor I ((see the first letter of rotor I)
            #ii) "Z" for rotor II ((see the first letter of rotor II)
            #iii) "E" for rotor III ((see the first letter of rotor III)
           #then same for the next characters one by one.
        
    enigma_rotor_I = Rotors(list("ekmflgdqvzntwoyhxuspaibrcj"), turnovernotch=["t"]) #right rotor and its turnover
    enigma_rotor_II = Rotors(list("bdfhjlcprtxvznyeiwgakmusoq"), turnovernotch=["e"]) # middle rotor and its turnover
    enigma_rotor_III = Rotors(list("ajdksiruxblhwtmcqgznpyfvoe"), turnovernotch=["g"]) # left rotor and its turnover
    enigma1_main_reflector = Reflectors(list("yruhqsldpxngokmiebfzcwvjat")) #wide B reflector

    """ #Giving the reflectors and rotors to the enigma machine"""#
    enigma_components = EnigmaMachine(
        enigma1_main_reflector,
        enigma_rotor_I,
        enigma_rotor_II,
        enigma_rotor_III,
        two_step=True,
    )
    """starting the enigma machine program """
    print (" #############################   WELCOME TO THE FAMOUS ENIGMA MACHINE  !!!! ########################")
    """taking input from the user in string"""
    condition = False
    while (condition == False):

        input_data = input("***************************PLEASE ENTER YOUR TEXT***************************************:  ")
        #""" Performing encryption"""

        for i in range (0,len(input_data)):
        
            if input_data[i].isalpha() or input_data[i].isspace() == True:
                enigma_components.positioning("aaa")
                encrypted_data = enigma_components.encryption(input_data)
                condition = True
        
            elif (input_data[0].isalpha() or input_data[0].isspace() == False):
                print("You have entered invalid characters. Please enter only alphabets")
                break
        
    condition = False

    print(f"{input_data} 'HAS BEEN ENCODED INTO:' {encrypted_data} ")
    print("-------------------------------------------------------------------------------------------------------")

    enigma_components.positioning("aaa")
    decrypted_data = enigma_components.encryption(encrypted_data)

    print(f"{encrypted_data} 'HAS BEEN DECODED INTO:' {decrypted_data} ")
    print ("#####################################  THE END  ########################################")
    


#Running the main program
if __name__ == "__main__"  :
    MainProgram()

