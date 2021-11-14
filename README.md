#  Enigma Machine Stimulator
Abstract


Enigma machine is a cipher device that was used during World war 2 (WWII). t was made to cipher (encode) messages and to protect communications between the Nazis at that time. The enigma machine works by scrambling the 26 alphabets using the rotor mechanism to do so. When a text is being entered, 26 lights light at each key press. Any plain text entered in the enigma machine it gets encoded into a cipher text. On the other hand, entering a cipher text gets transferred to a readable plain text. The design of the enigma machine consists of keyboard, 3 rotors connected together along the spindle, stepping components and a lamp for each alphabet.  
During the WWII, the enigma machine was so hard to break as it had number of combinations of settings available that made it hard to break to the encoders. The operator used to regularly change changing cipher by changing the positions of the rotating wheels and plug board. In 1932 the enigma machine was cracked by a mathematician who understood the wiring pattern inside the enigma.

![image](https://user-images.githubusercontent.com/74532447/141681664-536e1d6a-7d86-4dd6-9af5-59545d1eec2e.png)


Introduction

The Enigma machine simulator python code that I have designed models the recreation of the popular enigma machine that was built during WWII by the Germans in order to cipher their communications. The enigma machine that I have designed consists of 3 rotors & their turnover notches, reflector setup (movement from the rotor on the right to the rotor on the left, then to the reflector then one time left to right), rotating wheels and ring offset for the double stepping that has been implemented in the machine. 
The program consists of 3 classes: Rotors, Reflectors and EnigmaMachine. 


•	The “Rotors” class is the main class that is built to deal with the 3 rotors from which the rotors are set to scrambled 26 positions that corresponds to the English alphabets.
•	The “Reflectors” class handles the reflector setup for the two-way mapping (forward and backward)


•	The “EnigmaMachine” class is the main enigma class that connects all the python code together in order to create the enigma machine as a whole. The EnigmaMachine class contains the function used for the rotation mechanism of the rotors.


The enigma stepping used in this Enigma machine is double stepping (called in the code: ‘two_step’) in which the middle rotor (second rotor) steps two times (on 2 successive keyboard presses) if the left rotor makes a step. Double stepping simply works when the first rotor rotates on every keypress one step as there’s no other rotor before it. Then the second rotor rotates on every last keypress (26th) whenever the first rotor is in its turnover notched position (“t”) and lastly the third rotor only rotates when the second rotor is in the turnover notched place when this happens it would keep on rotating twenty six times in a row until the middle rotor would move from the turnover notched place again.

The rotor offset is assigned so that in every rotation that takes place, the offset will now what the result will be and the place in which it enters the next rotor.

The enigma machine allows the user to input any plain text (only letters in the alphabet) and turn them into ciphered text. The output will show both the encryption and decryption.



