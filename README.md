# MySolutionsCode
My own solutions of different programming tasks.
Here will be descriptions of tasks and the names of the files containing the solution.

Directories:
	
1.JavaSol directory consists of different programms written on Java.
2.PythonSol directory consists of different programms written on Python.

				
# -------------------------------> Java solutions <-------------------------------


1. Name of the file: "DuplicateEncoder.java"
   Task "Duplicate Encoder": 
	
	The goal of this exercise is to convert a string to a new string where 
   	each character in the new string is '(' if that character appears only once in 
   	the original string, or ')' if that character appears more than once in the original
   	string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))((" 





2. Name of the file: "ASum.java"
   Task "Build a pile of Cubes": 
	
	Your task is to construct a building which will be a pile of n cubes.
 
	The cube at the bottom will have a volume of n^3, the cube above will have 
   	volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

	You are given the total volume m of the building. Being given m can you 
   	find the number n of cubes you will have to build?

	The parameter of the function findNb (find_nb, find-nb, findNb) will be 
   	an integer m and you have to return the integer n such as 
   	n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

Examples:

findNb(1071225) --> 45
findNb(91716553919377) --> -1




3. Name of the file: "countPositivesSumNegatives.java"
   Task "Count of positives / sum of negatives":

	Given an array of integers.

	Return an array, where the first element is the count of 
   	positives numbers and the second element is sum of negative numbers.

	If the input array is empty or null, return an empty array

Examples:

input int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15} 
return int[] {10, -65}.




4. Name of the file: "Line.java"
   Task "Vasya - Clerk":

	The new "Avengers" movie has just been released! There are a lot of people
   	at the cinema box office standing in a huge line. Each of them has a single 
  	100, 50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.

	Vasya is currently working as a clerk. He wants to sell a ticket to every 
	single person in this line.

	Can Vasya sell a ticket to each person and give the change if he initially 
	has no money and sells the tickets strictly in the order people follow in the line?

	Return YES, if Vasya can sell a ticket to each person and give the change. 
	Otherwise return NO.

Examples:

Line.Tickets(new int[] {25, 25, 50}) // => YES 
Line.Tickets(new int []{25, 100}) 
         // => NO. Vasya will not have enough money to give change to 100 dollars




5. Name of the file: "WhereIsMyParent.java"
   Task "Where is my parent!?(cry)":

	Mothers arranged dance party for children in school.On that party 
	there are only mothers and their children.All are having great fun 
	on dancing floor when suddenly all lights went out.Its dark night 
	and no one can see eachother.But you were flying nearby and you can 
	see in the dark and have ability to teleport people anywhere you want.

	Legend:
	-Uppercase letters stands for mothers,lowercase stand for their children. 
	I.E "A" mothers children are "aaaa".

	-Function input:String contain only letters,Uppercase letters are unique.

	
	Place all people in alphabetical order where Mothers are followed by their children.
	I.E "aAbaBb" => "AaaBbb".




6. Name of the file: "HanTo.java"
   Task "Tower of Hanoi":

   Read more about this task ===>> https://en.wikipedia.org/wiki/Tower_of_Hanoi





7. Name of the file: "Lab1_ASD.java"
   Task "Inverse words and characters in the sentence":
	
	Given a file containing text.
	7.1 Write down all the words in the sentences backwards into another file.
	7.2 Write down all the characters in the words backwards into another file.
<<<<<<< HEAD


#-------------------------------> Python solutions <-------------------------------


1. Name of the file: "tst_gm.py"
   The first mini game i wrote for interest. Written using Tkinter GUI.
   First experience of use Tkinter.
   Just for interest.  
   Purpose of the game is to go around the obstacles using 2 buttons:
   "to the left" and "to the right".





2. Name of the file: "array_diff.py"
   	
	Your goal in this kata is to implement an difference function, 
	which subtracts one list from another.

	It should remove all values from list a, which are present in list b.

	array_diff([1,2],[1]) == [2]

	If a value is present in b, all of its occurrences must be removed from the other:

	array_diff([1,2,2,2,3],[2]) == [1,3]





3. Name of the file: "cakes.py"
   
	Description:

	Pete likes to bake some cakes. He has some recipes and ingredients. 
	Unfortunately he is not good in maths.
	Can you help him to find out, how many cakes he could bake considering his recipes?

	Write a function cakes(), which takes the recipe (object) and the available ingredients
	(also an object) and returns the maximum number of cakes Pete can bake (integer).
	For simplicity there are no units for the amounts 
	(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
	Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})

# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, 
			{sugar: 500, flour: 2000, milk: 2000})





4. Name of the file: "delete_nth.py"
   	
	Enough is enough!

	Alice and Bob were on a holiday. 
	
	Both of them took many pictures of the places they've been,
	and now they want to show Charlie their entire collection. 
	
	However, Charlie doesn't like this sessions, since the motive usually repeats. 
	
	He isn't fond of seeing the Eiffel tower 40 times.
	
	He tells them that he will only sit during the session if they show the same 
	motive at most N times.
	
	Luckily, Alice and Bob are able to encode the motive as a number.
	
	Can you help them to remove numbers such that their list contains each number 
	only up to N times, without changing the order?

	Task

	Given a list lst and a number N, create a new list that contains each number 
	of lst at most N times without reordering. For example if N = 2, and the input 
	is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead
	to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].


Example

  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]





5. Name of the file: "iq_test.py"
   
	Bob is preparing to pass IQ test.
	The most frequent task in this test is to find out which one of the given
	numbers differs from the others.
	Bob observed that one number usually differs from the others in evenness.
	Help Bob — to check his answers, he needs a program that among the given 
	numbers finds one that is different in evenness, and return a position of this number.

	! Keep in mind that your task is to help Bob solve a real IQ test, 
	which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd





6. Name of the file: "is_valid_ip.py"
   
	Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
	IPs should be considered valid if they consist of four octets, with values 
	between 0..255 (included).

	Input to the function is guaranteed to be a single string.

Examples

// valid inputs:
1.2.3.4
123.45.67.89

// invalid inputs:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

Note: leading zeros (e.g. 01.02.03.04) are considered not valid!





7. Name of the file: "smth.py"
   
	Write a function, persistence, that takes in a positive parameter num 
	and returns its multiplicative persistence,
	which is the number of times you must multiply the digits in num until 
	you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.

 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number





8. Name of the file: "song_decoder.py"
   
	Polycarpus works as a DJ in the best Berland nightclub, 
	and he often uses dubstep music in his performance.
	
	Recently, he has decided to take a couple of old songs 
	and make dubstep remixes from them.

	Let's assume that a song consists of some number of words.
	To make the dubstep remix of this song, Polycarpus inserts 
	a certain number of words "WUB" before the first word of the 
	song (the number may be zero), after the last word (the number may be zero),
	and between words (at least one between any pair of neighbouring words), 
	and then the boy glues together all the words, including "WUB", in one 
	string and plays the song at the club.


For example, a song with words "I AM X" can transform into a dubstep remix as 
"WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music,
he decided to find out what was the initial song that Polycarpus remixed. 
Help Jonny restore the original song.

Input

The input consists of a single non-empty string, consisting only of uppercase English letters, 
the string's length doesn't exceed 200 characters

Output

Return the words of the initial song that Polycarpus used to make a dubsteb remix. 
Separate the words with a space.


Examples

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND





9. Name of the file: "triple_double.py"
   
	Write a function triple_double(num1, num2) which takes in numbers 
	num1 and num2 and returns 1 if there is a straight triple of a number 
	at any place in num1 and also a straight double of the same number in num2.


For example:

triple_double(451999277, 41177722899) == 1 // num1 has straight triple 999s and
                                          // num2 has straight double 99s

triple_double(1222345, 12345) == 0 // num1 has straight triple 2s but num2 has only a single 2

triple_double(12345, 12345) == 0

triple_double(666789, 12345667) == 1

If this isn't the case, return 0





10. Name of the file: "anagrams.py"
   

	What is an anagram? 
	
	Well, two words are anagrams of each other if they both contain the same letters. 


For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false


	Write a function that will find all the anagrams of a word from a list.
	You will be given two inputs a word and an array with words.
	You should return an array of all the anagrams or an empty array if there are none.

For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []





11. Name of the file: "validSolution.py"
   
	Sudoku is a game played on a 9x9 grid.
	The goal of the game is to fill all cells of the grid with digits from 1 to 9,
	so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks)
	contain all of the digits from 1 to 9.
	(More info at: http://en.wikipedia.org/wiki/Sudoku)

	Sudoku Solution Validator

	Write a function validSolution/ValidateSolution/valid_solution() 
	that accepts a 2D array representing a Sudoku board, and returns 
	true if it is a valid solution, or false otherwise. 
	
	!The cells of the sudoku board may also contain 0's, which will represent empty cells. 
	Boards containing one or more zeroes are considered to be invalid solutions.

	The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.





12. Name of the file: "course_work.py"
    Additional files: "course_work_ui.py"
	
	You need to develop a program to manage the database and store data using XML file.





13. Name of the file: "hierarchical.py"
	
	This program is like a "course_work.py", but realization is different and this is a console app.





14. Name of the file: "roman.py"
    Additional files: "romanconvert.py"
    Directory: /Light IT Task

	Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. 
	You don't need to validate the form of the Roman numeral.

	Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, 
	starting with the leftmost digit and skipping any 0s. 
	So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). 
	The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.





15. Name of the file: "same_structure.py"
	
	Complete the function to return True when its argument is an array that 
	has the same nesting structure as the first array.


For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
