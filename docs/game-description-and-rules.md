# Game Description

Cifra is a 2 player board game that has the objective of moving more pieces to the opposite side goal.
Cifra Code25 is a version of CIFRA that has a 5x5 board size.

# Game Pieces

Pieces are double sided. One is blank and other side is numbered from 1 to 5.

You can select game style by selecting faces.  The starting position for game play is limitless.

![Game Pieces](https://github.com/gabrieltmjr/FEUP-AI-Project-1/blob/main/docs/img/pieces.jpg)

# Game Modes/Styles

CIFRA has 3 types of game modes: Dash, King and Sum.

## Dash

Dash use the blank faces of pieces. 
It's very simple race game. The Game goal is to move more of your own pieces to the opposite side than your opponent. 

## King

King is simple fight game to capture your opponent's King or to move your own King to opposite side first.  
Since there are two game strategies you must change tactics throughout the game.

## Sum

Sum is basically a race game but you must consider the pieces value(number). The game goal is to obtain more total score of goal pieces than your opponent. So, Even though a player may have fewer goal piece(s) than their opponent, if he/she gets higher total score than opponent, then they win the game.

Players place their pieces blank side at first on the starting line, when game starts they reveal their number faces. Players must think about a deeper strategy considering placement and value of their pieces.

# Game General Rules

1 - Set up board by randomly placing tiles. <br>
2 - Decide the first player, then the second player can choose their color and side. The Opposite side is automatically first player's color and side.<br>
3 - Players take their turn alternately.  During their play the player can move their own piece according to the moving rules.<br>
4 - If a player moves their piece onto the tile which an opponent piece occupies, they can capture it like a Chess piece.<br>
5 - If player moves their piece onto the opposite side, the piece is a goal and fixed there. Both players can't move it nor capture it.<br>
6 - When all alive five pieces of any one of players are captured or goal, then game is over.  <br>
7 - "Dash" Player who has more goal piece(s) wins the game. If they are tie, player who keep living piece on the board wins the game. "Sum" Player who obtain more score of goal pieces wins the game. If they are tie, player who has more goal pieces wins the game. If both are tie, then player who keep living piece on the board wins the game.<br>
8 - "King" Player who capture opponent King or move own King to opposite side goal wins the game, even though two players piece(s) are still alive on the board.<br>

# Moving System and Rules

Each piece moves are complex but you don't have to memorize them because they are defined according to the tile pattern.

1 - Basically any pieces can move to adjacent tile in any of 8 directions, vertically, horizontally and diagonally like chess king.

![Simple Movement Example](https://github.com/gabrieltmjr/FEUP-AI-Project-1/blob/main/docs/img/simple-movement-example.jpg)

2 - Consecutive tiles of the player's color may be counted as one extended tile for movement purposes.  

- In the first example, a blue piece can move up to 3 spaces because the 3 consecutive blue tiles count as one extended tile and therefore, one move.

- In the second example, blue can move one to the left but up to three to the right because the starting tile and the next two blue tiles are considered an extension of the starting tile.

- In the third example both the starting tile and the one to the left and right are considered one long tile so the player may move to adjacent white tiles and consider that a single move.

![Extended Movement Example](https://github.com/gabrieltmjr/FEUP-AI-Project-1/blob/main/docs/img/extended-movement-examples.jpg)

A player can chose to stop moving at any tile in an extended tile path.  For example, in the first example below, the player could move one, two or three spaces to the right.

Each players piece will have different movement options from identical locations based on their color as shown below.

![Different Movement Example](https://github.com/gabrieltmjr/FEUP-AI-Project-1/blob/main/docs/img/different-movement-examples.jpg)

Center tile is neutral color for both players. Any piece must stop there once.

![Central Tile Movement Example](https://github.com/gabrieltmjr/FEUP-AI-Project-1/blob/main/docs/img/central-tile-movement-examples.jpg)

