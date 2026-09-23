Phase 1 — Project Setup
Install Python and Pygame
Create project folder
Set up main.py
Decide screen size and board size
Organize asset folders

Phase 2 — Chess Board
Create an 8×8 board
Create alternating light/dark squares
Add chess coordinates (a–h, 1–8)
Map each board square to screen coordinates

Phase 3 — Chess Pieces
Add images for all 12 piece types
White: King, Queen, Rook, Bishop, Knight, Pawn
Black: King, Queen, Rook, Bishop, Knight, Pawn
Place pieces in their starting positions
Store the board state using an 8×8 structure

Phase 4 — Mouse Interaction
Detect mouse clicks
Identify which square was clicked
Select a piece
Highlight the selected piece
Highlight possible destinations

Phase 5 — Piece Movement
Implement movement rules individually:
Pawn
Knight
Bishop
Rook
Queen
King
Also implement:
Capturing
Turn switching
Prevent moving onto friendly pieces

Phase 6 — Legal Chess Moves
Add the actual chess rules:
Check detection
Prevent moves that leave your own king in check
Checkmate
Stalemate
King safety

Phase 7 — Special Moves
Implement:
Castling
En passant
Pawn promotion

Phase 8 — Game Interface
Add:
Current player's turn
Captured pieces
Move history
Restart game
Undo move
Game-over screen
Check/checkmate notification

Phase 9 — Graphics & Audio
Improve presentation:
Better board design
Piece animations
Move highlighting
Capture effects
Sounds
Background music
Smooth transitions

Phase 10 — Game Modes
Start with:
Player vs Player
Then optionally add:
Player vs Computer
For the computer:
Basic random moves → beginner AI
Minimax → stronger AI
Alpha-beta pruning → improved performance
Evaluation function → stronger chess decisions

Phase 11 — Testing
Test every piece individually and check:
Illegal moves
Captures
Check
Checkmate
Castling
En passant
Promotion
Stalemate
Restart/undo
Edge cases
Phase 12 — Final Project
Clean up the code
Separate board, pieces, game logic, and UI
Add comments/documentation
Create README
Add screenshots
Package the game for demonstration
