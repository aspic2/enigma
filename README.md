# enigma
Write and decrypt your own enigma ciphers.

## ENIGMA CIPHER ##

Still under construction.

This will be a simple interactive tool where you can type in a message and
encode it using WWII enigma cipher. You will also be able to decrypt messages.
The idea was inspired by Youtube's Numberphile videos on the enigma cipher.

## Design strategy ##

1. ~~Create a machine that takes an input letter and manipulates it in steps.
Leave the enigma-specific manipulation for later.~~

2. ~~Create rotors.~~

3. ~~Create rotors with different spin cycles.~~
  - How can I set the different spin rates if the rotors can be in any order?
    - ~~Can be achieved with a Slots() class that controls spin.~~
    - using a count variable in Enigma() and floor division

4. Create plugboard manipulations

5. Enigma-fy your tool.
(Make sure that manipulations match what the enigma machine would actually do.)
    - Use same 7 rotor options
    - ~~Allow rotors to be "set"~~
    - Reverse rotor manipulation
    - Input letter cannot become itself
    - Allow plugboard to be "set"

6. Tests to confirm program.

7. Better User Interface.

8. Revise for more robust tool (each individual module should work independent
  of the other pieces.)


## RESOURCES ##
Original Numberphile videos:
  1. https://www.youtube.com/watch?v=G2_Q9FoD-oQ
  2. https://www.youtube.com/watch?v=V4V2bpZlqx8

Enigma article on Ciphermachines.com
  1. http://ciphermachines.com/enigma
