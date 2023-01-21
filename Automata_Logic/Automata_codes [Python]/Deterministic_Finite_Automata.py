'''
# Problem Statement: Design a DFA to accept the language L={a^i b^j c^k | i>1, j>=3, k mod 3 = 2} over the input symbols (sigma)= {a,b,c}.

'''

# [ L = {a^i b^j c^k | i>1, j>=3, k mod 3 = 2} ]
# [ Basic string is: aabbbcc ]



# 1--defining the states

# (For the below given functions, variable 'dfa' represents 'state of DFA';)
#   [dfa = state of DFA ] 


# STARTING STATE FUNCTION : STATE q0
#  [q0 over the input symbols {b,c} goes to 'dead state'.] 
def q0(c): 
    if (c == 'a'): 
        dfa = 1
    elif (c == 'b'): 
        dfa = 8
    elif (c == 'c'): 
        dfa = 8
        
    # -1 is used to check for any invalid input symbols  
    else: 
        dfa = -1
    return dfa
    
# FIRST STATE FUNCTION : STATE q1 
#  [q1 over the input symbols {b,c} goes to 'dead state'.] 
def q1(c):  
    if (c == 'a'): 
        dfa = 2
    elif (c == 'b'): 
        dfa = 8
    elif (c == 'c'): 
        dfa = 8
    else: 
        dfa = -1
    return dfa

# SECOND STATE FUNCTION : STATE q2
#  [q2 over the input symbol {c} goes to 'dead state'.] 
def q2(c):  
    if (c == 'a'): 
        dfa = 2
    elif (c == 'b'): 
        dfa = 3
    elif (c == 'c'): 
        dfa = 8
    else: 
        dfa = -1
    return dfa

# THIRD STATE FUNCTION : STATE q3
#  [q3 over the input symbols {a,c} goes to 'dead state'.] 
def q3(c):  
    if (c == 'a'): 
        dfa = 8
    elif (c == 'b'): 
        dfa = 4
    elif (c == 'c'): 
        dfa = 8
    else: 
        dfa = -1
    return dfa

# FOURTH STATE FUNCTION : STATE q4
#  [q4 over the input symbols {a,c} goes to 'dead state'.] 
def q4(c):  
    if (c == 'a'): 
        dfa = 8
    elif (c == 'b'): 
        dfa = 5
    elif (c == 'c'): 
        dfa = 8
    else: 
        dfa = -1
    return dfa 

# FIFTH STATE FUNCTION : STATE q5 
#  [q5 over the input symbol {a} goes to 'dead state'.] 
def q5(c):  
    if (c == 'a'): 
        dfa = 8
    elif (c == 'b'): 
        dfa = 5
    elif (c == 'c'): 
        dfa = 6
    else: 
        dfa = -1
    return dfa     

# SIXTH STATE FUNCTION : STATE q6
#  [q6 over the input symbols {a,b} goes to 'dead state'.] 
def q6(c):  
    if (c == 'a'): 
        dfa = 8
    elif (c == 'b'): 
        dfa = 8
    elif (c == 'c'): 
        dfa = 7
    else: 
        dfa = -1
    return dfa

# SEVENTH STATE FUNCTION : STATE q7
#  [q7 over the input symbols {a,b} goes to 'dead state'.] 
def q7(c):  
    if (c == 'a'): 
        dfa = 8
    elif (c == 'b'): 
        dfa = 8
    elif (c == 'c'): 
        dfa = 5
    else: 
        dfa = -1
    return dfa

# DEAD STATE FUNCTION : STATE qD
#  [qD over the input symbols {a,b,c} goes to 'dead state' itself.] 
#  [The 'dead state' is taken care of by the state, dfa = -1.]
def qD(c):
    dfa = -1
    return dfa 



# 2--CHECKING if string is accepted or not

def Check_string(Input_String): 
        
    # store length of Input_String  in variable 'l'
    l = len(Input_String) 
        
    # 'dfa' variable tells the number associated with / the state of the present dfa
    dfa = 0
    for i in range(l):
        
        if (dfa == 0):  
            dfa = q0(Input_String[i])  

        elif (dfa == 1):  
            dfa = q1(Input_String[i])  
    
        elif (dfa == 2) : 
            dfa = q2(Input_String[i])  
    
        elif (dfa == 3) : 
            dfa = q3(Input_String[i])  
    
        elif (dfa == 4) : 
            dfa = q4(Input_String[i])  
     
        elif (dfa == 5) : 
            dfa = q5(Input_String[i])  
    
        elif (dfa == 6):  
            dfa = q6(Input_String[i])
            
        elif (dfa == 7):  
            dfa = q7(Input_String[i])
            
        else: 
            return 0
        
    if(dfa == 7) : 
        return 1
    else: 
        return 0


# 3--Transition_table
def Transition_table():
    print("\n\nThe transition table of this dfa is as follows:\n(here, qD is the dead state)\n")
    print("\t ---------------------------------")
    print("\t \t TRANSITION TABLE\n")
    print("\t _________________________________")
    print("\t |Delta\t | a \t | b \t | c \t |")
    print("\t _________________________________")
    print("\t | ->q0\t | q1 \t | qD \t | qD \t |")
    print("\t _________________________________")
    print("\t | q1 \t | q2 \t | qD \t | qD \t |")
    print("\t _________________________________")
    print("\t | q2 \t | q2 \t | q3 \t | qD \t |")
    print("\t _________________________________")
    print("\t | q3 \t | qD \t | q4 \t | qD \t |")
    print("\t _________________________________")
    print("\t | q4 \t | qD \t | q5 \t | qD \t |")
    print("\t _________________________________")
    print("\t | q5 \t | qD \t | q5 \t | q6 \t |")
    print("\t _________________________________")
    print("\t | q6 \t | qD \t | qD \t | q7 \t |")
    print("\t _________________________________")
    print("\t | * q7\t | qD \t | qD \t | q5 \t |")
    print("\t _________________________________")
    print("\t | qD \t | qD \t | qD \t | qD \t |")
    print("\t _________________________________")
    print()
    return 0


# 4-- Extended transition function

# 4[a]--Dead state function 'REPRESENTATION':{state qd}   (used for 'Extended_transition_func' function)
# (ie, 'qd' function is used inside the 'Extended_transition_func' function.)
def qd(c):
    dfa = 8
    return dfa

# 4[b]--'loop1' for 'Extended_transition_func' function.
# (ie, 'loop1' function is used inside the 'Extended_transition_func' function.)
def loop1(i,j,Input_String,flag1,flag2,flag3,dfa,di):
        
        if (dfa == 0):  
            dfa = q0(Input_String[j])
            print("D*(q0,lambda) =  q0")
            di="q0"
            return str(dfa),di

        elif (dfa == 1):
            dfa = q1(Input_String[j])
            print("D*(q0,",Input_String[0:i],") =  D ( D*(qo,lambda),",Input_String[i-1]," ) = D (",di,",",Input_String[i-1],") = q1 ")
            di="q1"
            return str(dfa),di

        elif (dfa == 2) :
            dfa = q2(Input_String[j])
            if (flag1==1):
                di="q2"
            else:
                di="q1"
            print("D*(q0,",Input_String[0:i],") =  D ( D*(qo,",Input_String[0:i-1],"),",Input_String[i-1]," ) = D (",di,",",Input_String[i-1],") = q2 ")
            flag1=1
            di="q2"
            return str(dfa),di
            
        elif (dfa == 3) : 
            dfa = q3(Input_String[j])
            print("D*(q0,",Input_String[0:i],") =  D ( D*(qo,",Input_String[0:i-1],"),",Input_String[i-1]," ) = D (",di,",",Input_String[i-1],") = q3 ")
            di="q3"
            return str(dfa),di
    
        elif (dfa == 4) : 
            dfa = q4(Input_String[j])
            print("D*(q0,",Input_String[0:i],") =  D ( D*(qo,",Input_String[0:i-1],"),",Input_String[i-1]," ) = D (",di,",",Input_String[i-1],") = q4 ")
            di="q4"
            return str(dfa),di
     
        elif (dfa == 5) : 
            dfa = q5(Input_String[j])
            if (flag2==1):
                di="q5"
            elif (flag3==1):
                di="q7"
            else:
                di="q4"
            print("D*(q0,",Input_String[0:i],") =  D ( D*(qo,",Input_String[0:i-1],"),",Input_String[i-1]," ) = D (",di,",",Input_String[i-1],") = q5 ")
            flag2=1
            di="q5"
            return str(dfa),di
    
        elif (dfa == 6):  
            dfa = q6(Input_String[j])
            print("D*(q0,",Input_String[0:i],") =  D ( D*(qo,",Input_String[0:i-1],"),",Input_String[i-1]," ) = D (",di,",",Input_String[i-1],") = q6 ")
            di="q6"
            return str(dfa),di
            
        elif (dfa == 7):  
            dfa = q7(Input_String[j])
            print("D*(q0,",Input_String[0:i],") =  D ( D*(qo,",Input_String[0:i-1],"),",Input_String[i-1]," ) = D (",di,",",Input_String[i-1],") = q7 ")
            flag3=1
            flag2=0
            di="q7"
            return str(dfa),di

        elif (dfa == 8):  
            dfa = qd(Input_String[j])
            print("D*(q0,",Input_String[0:i],") =  D ( D*(qo,",Input_String[0:i-1],"),",Input_String[i-1]," ) = D (",di,",",Input_String[i],") = qD ")
            print("\n The last stage which was shown was \"Dead state or Trap state\" (qD).\n The DFA shall be roaming in the dead state.")
            return str(-2),str(8)

        elif (dfa == -1):
            print("ERROR! Invalid Input Symbols Given!\n ( String NOT ACCEPTED, as this language is over the symbols:{a,b,c}.")
            return str(-1), str(-1)
        
        else: 
            return str(0)



# 4[c]--Extended transition function
def Extended_transition_func(Input_String):
    print("\nThe extended transition function for the given string is:\n(here, Delta* is represented as D*, Delta is represented as D)\n")
        
    l = len(Input_String)
    dfa = 0
    flag1=0
    flag2=0
    flag3=0
    di="q0"
    j=0
    
    for i in range(l):
            value=loop1(i,j,Input_String,flag1,flag2,flag3,dfa,di)
            dfa=int(value[0])
            di=value[1]
            j+=1
    value=loop1(i+1,j-1,Input_String,flag1,flag2,flag3,dfa,di)
        
    if(dfa == 7) :
        print("\n The final state (q7) 'is reached'. \n Hence, the given string is 'ACCEPTED', by this DFA.")
        return 1
    else:
        print("\n The final state (q7) 'is not reached'.\n Hence, the given string is 'NOT ACCEPTED', by this DFA.")
        return 0


    
# 5--main code

# i-Checking if input string is accepted or not
print("\n\t Program to check acceptance of a string, for this particular dfa.\n")
print("\n 1-\"To check\" if the input 'string is accepted' by this dfa.\n")
Input_String = input("Enter String:")
print()
if (Check_string(Input_String)) : 
    print("String '",Input_String,"' is ACCEPTED.\n")
else: 
    print("String '",Input_String,"' is NOT ACCEPTED.\n")

# ii-Transition table
Input_Table = input("\n 2-To view the \"Transition Table\" enter 'y', else enter 'n' :")
if (Input_Table=='y') :
    Transition_table()

# iii-Extended transition function
Input_extended = input("\n 3-To view the \"Extended Transition Functions\" enter 'y', else enter 'n' :")
if (Input_extended=='y') :
    Extended_transition_func(Input_String)
print("\n\t END of program__Thank You.\n")


# 6--  Execution instructions and outputs

'''
While Running the program:

1- TO CHECK INPUT STRING ACCEPTANCE (BY THIS DFA)

   -Execution instructions:
    When the user gets ["Enter String:"] on the screen,
     the user should input any string (over the input symbols:{a,b,c}).

   -outputs:
     If the string is accepted , it prints (on the screen) that, "string 'xyz' is ACCEPTED." (where input string is : 'xyz')
     If the string is NOT accepted , it prints (on the screen) that, "string 'xyz' is NOT ACCEPTED." (where input string is : 'xyz')
     
    
2- TO VIEW TRANSITION TABLE:

   -Execution instructions:
     When the user gets ["2-To view the "Transition Table" enter 'y', else enter 'n' :"] on the screen,
        the user should enter 'y' from the keyboard, to view the Transition table;
        else, the user should enter 'n' from the keyboard, (to 'NOT' view the Transition table);

   -outputs:
     If 'y' is given as input , it prints (on the screen), the "TRANSITION TABLE" (for this DFA).
     If 'n' is given as input , it DOESN'T print the "TRANSITION TABLE" (for this DFA).

3- TO VIEW EXTENDED TRANSITION FUNCTIONS:

   -Execution instructions:
     When the user gets ["3-To view the "Extended Transition Functions" enter 'y', else enter 'n' :"] on the screen,
        the user should enter 'y' from the keyboard, to view the Extended Transition Functions;
        else, the user should enter 'n' from the keyboard (to 'NOT' view the Extended Transition Functions);

   -outputs:
     If 'y' is given as input , it prints (on the screen), the "EXTENDED TRANSITION FUNCTIONS" (for the given input string and this DFA).
     If 'n' is given as input , it DOESN'T print the "EXTENDED TRANSITION FUNCTIONS" (for the given input string and this DFA).


End
'''

'''
Sample output:


	 Program to check acceptance of a string, for this particular dfa.


 1-"To check" if the input 'string is accepted' by this dfa.

Enter String:aabbbcc

String ' aabbbcc ' is ACCEPTED.


 2-To view the "Transition Table" enter 'y', else enter 'n' :y


The transition table of this dfa is as follows:
(here, qD is the dead state)

	 ---------------------------------
	 	 TRANSITION TABLE

	 _________________________________
	 |Delta	 | a 	 | b 	 | c 	 |
	 _________________________________
	 | ->q0	 | q1 	 | qD 	 | qD 	 |
	 _________________________________
	 | q1 	 | q2 	 | qD 	 | qD 	 |
	 _________________________________
	 | q2 	 | q2 	 | q3 	 | qD 	 |
	 _________________________________
	 | q3 	 | qD 	 | q4 	 | qD 	 |
	 _________________________________
	 | q4 	 | qD 	 | q5 	 | qD 	 |
	 _________________________________
	 | q5 	 | qD 	 | q5 	 | q6 	 |
	 _________________________________
	 | q6 	 | qD 	 | qD 	 | q7 	 |
	 _________________________________
	 | * q7	 | qD 	 | qD 	 | q5 	 |
	 _________________________________
	 | qD 	 | qD 	 | qD 	 | qD 	 |
	 _________________________________


 3-To view the "Extended Transition Functions" enter 'y', else enter 'n' :y

The extended transition function for the given string is:
(here, Delta* is represented as D*, Delta is represented as D)

D*(q0,lambda) =  q0
D*(q0, a ) =  D ( D*(qo,lambda), a  ) = D ( q0 , a ) = q1 
D*(q0, aa ) =  D ( D*(qo, a ), a  ) = D ( q1 , a ) = q2 
D*(q0, aab ) =  D ( D*(qo, aa ), b  ) = D ( q2 , b ) = q3 
D*(q0, aabb ) =  D ( D*(qo, aab ), b  ) = D ( q3 , b ) = q4 
D*(q0, aabbb ) =  D ( D*(qo, aabb ), b  ) = D ( q4 , b ) = q5 
D*(q0, aabbbc ) =  D ( D*(qo, aabbb ), c  ) = D ( q5 , c ) = q6 
D*(q0, aabbbcc ) =  D ( D*(qo, aabbbc ), c  ) = D ( q6 , c ) = q7 

 The final state (q7) 'is reached'. 
 Hence, the given string is 'ACCEPTED', by this DFA.

	 END of program__Thank You.

>>> 
