# modulemadness
Assumptions:

-All the key words (module, connect, process) will be allways in lower case.
-All the connections will be created using previously defined valid modules in the network.
-The connections are not cyclic.
-Input will be always correct.
-This program will always process the output from the last defined module in the network. i.e. The program will make a regression of all the inputs needed to calculate the current output, skipping the modules that are not needed for this (isolated or disconnected modules).
-In the command line, any input different from the three key words (module, connect or process) will finish the program.

To run the program use the command: python3 modulemadness.py