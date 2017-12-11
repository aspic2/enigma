# enigma
Write and decrypt your own enigma cyphers.

## ENIGMA CYPHER ##

Still under construction.

This will be a simple interactive tool where you can type in a message and encode it using WWII enigma cypher.
You will also be able to decrypt messages. The idea was inspired by Youtube's Numberphile and their videos on
the enigma cypher.

## Design strategy ##

1. ~~Create a machine that takes an input letter and manipulates it in steps.
Leave the enigma-specific manipulation for later.~~

2. ~~Create rotors.~~

3. Create rotors with different spin cycles.
  - How can I set the different spin rates if the rotors can be in any order?
    - Can be achieved with a Slots() class that controls spin.

4. Create plugboard manipulations

5. Enigma-fy your tool. (Make sure that manipulations match what the enigma machine would actually do.)
    - Use same 7 rotor options
    - Allow rotors to be "set"
    - Input letter cannot become itself
    - Allow plugboard to be "set"

6. Tests to confirm program.

7. Better User Interface.
