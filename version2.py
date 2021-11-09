class Rotors:
    def __init__(self,list_maping:list, turnovernotch: list = [], starting_position: str="a" 
    ):
        int_mapping=[ ord(char.lower( )) - ord( "a" ) for char in list_maping ]
        self.rotor_forwardd=dict(zip(range(26), int_mapping))
        self.rotor_backwardd={v:k for k,v in self.rotor_forwardd.items()}
        self.rotor_offset=ord(starting_position) - ord("a")
        self.turnovernotch = turnovernotch
       

    def Rotor_maping(self,character_value, backward=False):
        Rotor_map=self.rotor_backwardd if backward else self.rotor_forwardd
        offsetted_number=(character_value + self.rotor_offset)%26
        rotor_internal_settings=Rotor_map[offsetted_number]


        ending_position=(rotor_internal_settings - self.rotor_offset)%26
        return ending_position


    def rotor_rotation(self):
        self.rotor_offset=(self.rotor_offset + 1) %26


    def current_place(self):
        return chr(self.rotor_offset + ord (" a "))


    def positioning(self,char):
        self.rotor_offset=ord(char)-ord("a")


class Reflectors:
    def __init__ (self, list_maping:list ):
        int_mapping=[ ord ( char.lower()) - ord ( "a" ) for char in list_maping ]
        self.twowaymaping= dict( zip ( range( 26 ) , int_mapping ) )

        for k , v in self.twowaymaping.items():
            if self.twowaymaping [ v ] !=k :
                raise ValueError (" Error. The Reflector only works with two way mapping.")

    def Reflector_maping(self,number):
        return self.twowaymaping [number]


