# SNAKES AND LADDERS
This project is created using Python Flask Framework.
The code is for Backend Only.

# About this game:
1. It is a single player game (can be extended in future).
2. For Every Player, The dice gets rolled at random.
3. Player moves according to the dice number. 
	In case of ladder, it moves a ladder up. 
	In case of snake, it moves down the snake tail.
4. The dice keeps rolling until a player wins.
5. Lucky moves: 
	Whenever a Ladder is encountered.
	When dice number is exactly equal to number of moves to win.
	When you miss a snake by one or two positions.
6. Unlucky moves:
	Whenever a snake is encountered.
7. Max Climb Distance: Positions moved in the Biggest Ladder encountered.
8. Max Slide Distance: Positions moved down the Biggest Snake encountered.

# How to run:
1. Install Python with Flask
2. Make Changes to config.json (Change LOG_FILE_PATH according to your directory).
3. Run backend\app.py file
4. Open Postman or any other API supporting platform.
5. Hit URL: http://127.0.0.1:5000/ with GET METHOD
	Response expected: "Hello World! The server is up and running."
5. Now Hit URL: http://127.0.0.1:5000/play with POST METHOD
	Set Request Body as:
	{
		"Players": ["Anushka"],
		"BoardSize": 5,
		"Snakes": [[22, 18], [14, 6]],
		"Ladders": [[8, 12], [13, 17]]
	}
	Response expected: Anushka wins.
6. Go to backend\logs folder. Here we will be able to find the logs for the entire game.

# API Contract:
1. Players: List of player names
2. BoardSize: Size of board (Assuming the Board is a square of m x m, Set BoardSize as m)
3. Snakes: List of Position of Snakes on the board in the format [head, tail] where head is the number at which head is faced and tail is the number at which tail ends.
4. Ladders: List of Position of Ladders on the board in the format [start, end] where start is the number at which ladder starts and end is the number at which ladder ends. 
