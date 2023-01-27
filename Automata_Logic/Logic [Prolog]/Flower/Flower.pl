%FLOWER.PL

%FACTS:

%facts in FOL form		%facts in english sentence form

uni(papaya).	 	%Papaya is a unisexual flower.
uni(whitemulberry).		%White mulberry is a unisexual flower.
uni(watermelon).		%Watermelon is a unisexual flower.
bi(tulip). 			%Tulip is a bisexual flower.
bi(sunflower).	 	%Sunflower is a bisexual flower.
bi(lily).			%Lily is a bisexual flower.



%RULES:

%rules in FOL form		%rules in english sentence form
male(X) :- bi(X).		%If X is a bisexual flower, then X is male.
female(X) :- bi(X).		%If X is a bisexual flower, then X is female.


%As bisexual flowers, are both male and female.

%For unisexual flowers , it may be male or female
%so we cannot conclude anything, without more facts or rules,  for unisexual flowers.
