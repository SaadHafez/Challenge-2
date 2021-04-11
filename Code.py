from automata.fa.dfa import DFA 

dfa = DFA (
    #characters chosen to be represented as the sates 
    states = {'a','b','c','d','e','f','g','trap'},
    input_symbols= {'0','1'},
    transitions = {
        #a is the (idle) state
        'a':{'0':'trap','1':'b'},
        # b is the state(Enter Money)
        'b':{'0':'trap','1':'c'},
        # c is the state (counts money) (Machine Counts The Money)
        'c':{'0':'b','1':'d'},
        # d is the state (green light) (Green Light for Available Products)
        'd':{'0':'trap','1':'e'},
        # e is the state (Choose Item)
        'e':{'0':'trap','1':'f'},
        #f is the state dispense item 
        'f':{'0':'a','1':'g'},
        # g is the state (balance) (Return Money If Available ) 
        'g':{'0':'a','1':'a'},
        # trap state
        'trap':{'0':'trap','1':'trap'}
        
        
        
    },
   initial_state = 'a',
   final_states ={'g','f'}

)
#'1101111' is accepted and when we changed the value to '111110' the output will be  rejected 
if (dfa.accepts_input('1101111')):
    print("Accepted")
    
else:
    print("Rejected")
