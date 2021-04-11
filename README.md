# Challenge-2

CSC-4101-S2-Challenge2
Saad Hafez Moulana 1414027


installation of the automata library
Pip install automata-lib
variable “state” has all the states
variable input symbols has two variables 0 that represents false and 1 that represents true 
a is the (idle) state
b is the state (Enter Money)
c is the state (counts money) Machine Counts The Money
d is the state (green light) Green Light for Available Products
e is the state (Choose Item)
f is the state dispense item
g is the state (balance) Return Money If Available
Trap state named as trap

initial_state = 'a', only one initial state which is “a”
final_states ={'g','f'} two different finial states either state “g” or state “f”.
dfa.accepts_input('       ') parameter used to check wether it is true or false .
