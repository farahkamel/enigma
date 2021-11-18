class Rotors:
    def __init__(
        self, list_maping: list, turnovernotch: list = [], starting_position: str = "a"
    ):
        int_maping = [ord(char.lower()) - ord("a") for char in list_maping]
        self.rotor_forwardd = dict ( zip ( range (26), int_maping))
        self.rotor_backwardd = {v:k for k,v in self.rotor_forwardd.items()}
        self.rotor_offset = ord ( starting_position ) - ord("a")
        self.turnovernotch = turnovernotch

    def Rotor_maping(self, charactervalue, backwardd=False):
        Rotor_map = self.rotor_backwardd if backwardd else self.rotor_forwardd

        offsetted_num = (charactervalue + self.rotor_offset) %26
        rotor_internal_mapping = Rotor_map[offsetted_num]
        next_endingposition = (rotor_internal_mapping - self.rotor_offset)%26
        return next_endingposition

    def rotor_rotation(self):
        self.offset = (self.rotor_offset + 1) % 26

    def currentplace(self):
        return chr(self.rotor_offset + ord("a"))

    def positioning(self, char):
        self.offset = ord(char) - ord("a")


class Reflectors:
    def __init__ (self, list_maping: list):
        int_maping = [ord(char.lower()) - ord("a") for char in list_maping]
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