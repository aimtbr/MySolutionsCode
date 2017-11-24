# MySolutionsCode
Own solutions of different programming tasks.

Here will be a description of tasks and the name of the file containing the solution.


-------------------------------> Java solutions <-------------------------------


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