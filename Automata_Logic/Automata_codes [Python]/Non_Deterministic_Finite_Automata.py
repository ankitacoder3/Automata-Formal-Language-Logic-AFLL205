'''
# Problem Statement: Write a python program to check whether a string belongs to a particular given regular grammar or not.

'''

# code

print("\n\t Program to check ACCEPTANCE OF STRING , for the given REGULAR GRAMMAR.\n")


# 1- stating the given regular grammar

print("The 'given regular grammar' is: \n \t \t \tS -> aA | ab \n \t \t \t A -> Ab | b\n\n")

print("The regular expression for given regular grammar is: a.(a)*.(b)*.b\n\n")
#{hence basic string : "ab".}


# 2- inputting a string ( to check acceptance of the string )

Input_String = input("Enter the string, that is to be checked, for the above given grammar:\n")

L = len(Input_String)
flag1=0


# 3- checking the string is accepted or not

if( Input_String[0]=='a') :
    
    flag=0

    
    for count in range(1,L):
        
            
        if( Input_String[count]=='b') :
            
            flag=1
            continue

                
        elif((flag==1)and( Input_String[count]=='a')) :

            print("The string does not belong to the specified grammar")
            flag=2
            break

            
        elif( Input_String[count]=='a'):

            continue

            
        elif((flag==2) and (flag1==1)) :

            print("String '",Input_String,"' is NOT ACCEPTED by the 'given regular grammar'\n")


        elif( (Input_String[count]!='a') or ( Input_String[count]!='b')):

            print("INVALID input symbols entered!! TRY AGAIN!")
            print("String '",Input_String,"' is NOT ACCEPTED by the 'given regular grammar'\n")
            flag1=1
            break

            
        else :

            print("String '",Input_String,"' is ACCEPTED by the given regular grammar...!!\n")
            break



# 4- printing the output (accepted or not accepted)

if (flag == 2):

    print("String '",Input_String,"' is NOT ACCEPTED by the 'given regular grammar'\n")


elif (flag1 == 1):
             
    print("INVALID input symbols entered!! TRY AGAIN!")
    print("String '",Input_String,"' is NOT ACCEPTED by the 'given regular grammar'\n")
             
else :
             
    print("String '",Input_String,"' is ACCEPTED by the 'given regular grammar'...!!\n")
         
       
print("\n\t END of program__Thank You.\n")


# 5--  Execution instructions and outputs

'''

AIM- TO CHECK INPUT STRING ACCEPTANCE BY THE GIVEN REGULAR GRAMMAR

   -Execution instructions:
    Input the string
    
    [ when u get this statement : "Enter the string, that is to be checked, for the above given grammar:]

   -outputs:
    It prints if the string is accepted or not , by the given regular grammar'.
   
     [ If the string is accepted ,it prints  that, "string 'xyz' is ACCEPTED by the 'given regular grammar'." (where input string is : 'xyz')
       If the string is NOT accepted , it prints that, "string 'xyz' is NOT ACCEPTED by the 'given regular grammar'" (where input string is : 'xyz') ]


End
'''

# 6-- sample outputs

#output1:
'''
	 Program to check ACCEPTANCE OF STRING , for the given REGULAR GRAMMAR.

The 'given regular grammar' is: 
 	 	 	S -> aA | ab 
 	 	 	 A -> Ab | b


The regular expression for given regular grammar is: a.(a)*.(b)*.b


Enter the string, that is to be checked, for the above given grammar:
aab
String ' aab ' is ACCEPTED by the 'given regular grammar'...!!


	 END of program__Thank You.
'''

#output2:
'''
	 Program to check ACCEPTANCE OF STRING , for the given REGULAR GRAMMAR.

The 'given regular grammar' is: 
 	 	 	S -> aA | ab 
 	 	 	 A -> Ab | b


The regular expression for given regular grammar is: a.(a)*.(b)*.b


Enter the string, that is to be checked, for the above given grammar:
aba
The string does not belong to the specified grammar
String ' aba ' is NOT ACCEPTED by the 'given regular grammar'


	 END of program__Thank You.
'''

#output3:
'''

	 Program to check ACCEPTANCE OF STRING , for the given REGULAR GRAMMAR.

The 'given regular grammar' is: 
 	 	 	S -> aA | ab 
 	 	 	 A -> Ab | b


The regular expression for given regular grammar is: a.(a)*.(b)*.b


Enter the string, that is to be checked, for the above given grammar:
ab
String ' ab ' is ACCEPTED by the 'given regular grammar'...!!


	 END of program__Thank You.
'''
