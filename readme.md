# Hangman Game

## Python script for the hangman game
<p>In this project you will create a Python project implementing the hangman game enabling the player to attempt guessing a hidden word.</br>
The user has attempts at guessing a word represented in a row of dashes and if a player guesses a letter which exists in the word, the program writes it in all correct positions, these attempts are reduced for every wrong character guess the player makes, once all are exhausted, without a matching word having been guessed, the player loses.</br>
</p>

### Logic
<p>The game utilizes the random library and file handling to open the <b>hangman.txt</b> file containing the words.</br>
The random word is stored as a secret word and an array is initialized to store the letters guessed.</br>
A while loop is initiated and conditions provided. The try..except method ensures that the user cannot input more than one letter and the input has to be alphabets.</br>
The letters guessed are appended to the letters guessed array. The failure count is set at 6 and for each wrong letter guessed it is decremented by 1.</br>
The wrong count checks the number of wrong letters guessed. If the count is zero, it means the user has guessed all the letters right and thus has won the game.</p>
