# ♟️ Pygame Chess Game

## 6-Person Group Development Plan

## 1. Project Goal

Develop a complete **Chess game using Python and Pygame** with a graphical user interface.

### Core Features

* 8×8 chessboard
* Graphical chess pieces
* Mouse-based interaction
* Piece selection
* Legal piece movement
* Capturing
* Turn management
* Check
* Checkmate
* Stalemate
* Castling
* En passant
* Pawn promotion
* Game-over screen
* Restart game
* Move history

### Optional Features

* Player vs Computer
* Multiple AI difficulty levels
* Chess clock
* Save/load game
* Sound effects
* Animations
* Themes

> **Priority:** Complete a functional two-player chess game before working on optional features.

---

# 2. Team Division

| Member       | Module                    | Main Responsibility                                   |
| ------------ | ------------------------- | ----------------------------------------------------- |
| **Member 1** | Board System              | Board creation, coordinates and board-state handling  |
| **Member 2** | Piece Rendering & GUI     | Piece graphics, mouse interaction and visual effects  |
| **Member 3** | Piece Movement Engine     | Movement rules for all six pieces                     |
| **Member 4** | Chess Rules Engine        | Check, checkmate, stalemate and special rules         |
| **Member 5** | Game Controller & UI      | Turns, game flow, menus, move history and game states |
| **Member 6** | Testing, Integration & AI | Integration, testing, debugging and optional AI       |

This is much better than assigning one or two chess pieces to each person.

---

# 3. Overall Architecture

The application should eventually work like this:

```text
                         CHESS GAME
                              │
             ┌────────────────┼────────────────┐
             ↓                ↓                ↓
          BOARD            MOVEMENT           RULES
             │                │                │
          Member 1         Member 3         Member 4
             │                │                │
             └────────────────┼────────────────┘
                              ↓
                       GAME CONTROLLER
                              │
                           Member 5
                              │
             ┌────────────────┴────────────────┐
             ↓                                 ↓
          PYGAME GUI                       GAME STATE
             │
          Member 2

                    INTEGRATION / TESTING
                           Member 6
```

---

# 4. Shared Board Representation

This must be decided **before development begins**.

Use an 8×8 board.

Recommended notation:

```text
White:
WP = White Pawn
WR = White Rook
WN = White Knight
WB = White Bishop
WQ = White Queen
WK = White King

Black:
BP = Black Pawn
BR = Black Rook
BN = Black Knight
BB = Black Bishop
BQ = Black Queen
BK = Black King

Empty:
--
```

Starting position:

```text
BR BN BB BQ BK BB BN BR
BP BP BP BP BP BP BP BP
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
WP WP WP WP WP WP WP WP
WR WN WB WQ WK WB WN WR
```

### Important

All six members must use the **same board representation**.

Do not create separate board systems.

---

# 5. Recommended Project Structure

Start simple, then separate modules as the project grows.

```text
ChessGame/
│
├── main.py
│
├── board.py
├── pieces.py
├── movement.py
├── rules.py
├── game.py
├── ui.py
├── ai.py
│
├── assets/
│   ├── pieces/
│   ├── sounds/
│   ├── fonts/
│   └── images/
│
├── tests/
│
├── requirements.txt
└── README.md
```

Not every file needs to be created immediately.

---

# 6. PHASE 1 — Project Setup

## All Members

Before implementing features:

* Create GitHub repository
* Install Python
* Install Pygame
* Clone repository
* Decide project structure
* Decide board representation
* Decide naming conventions
* Create `.gitignore`
* Test that everyone can run Pygame

### Git branches

```text
main
│
├── board
├── gui
├── movement
├── rules
├── game-controller
└── testing-ai
```

### Phase complete when

Everyone can:

1. Clone the repository
2. Run the project
3. Make a branch
4. Commit changes
5. Push changes

---

# 7. PHASE 2 — Board System

## 👤 Member 1

Build the foundation of the chessboard.

### Tasks

* Create Pygame window
* Define window dimensions
* Create 8×8 board
* Calculate square size
* Draw alternating colors
* Add board coordinates
* Create initial board arrangement
* Store board state
* Convert board coordinates → screen coordinates
* Convert screen coordinates → board coordinates

### Example concept

```text
Chess coordinate
      ↓
(row, column)
      ↓
Pygame coordinate
      ↓
(x, y)
```

### Phase complete when

A correct 8×8 chessboard appears and the program knows which chess square corresponds to each screen position.

---

# 8. PHASE 3 — Piece Rendering & GUI Interaction

## 👤 Member 2

This person handles the **visual side**.

### Tasks

* Obtain/create chess piece images
* Load images
* Scale pieces
* Draw pieces on correct squares
* Detect mouse clicks
* Select pieces
* Highlight selected square
* Highlight possible moves
* Display captured pieces
* Create visual feedback

### Important

Member 2 should **not implement the actual chess movement rules**.

Instead:

```text
Movement Engine
      ↓
Possible moves
      ↓
GUI
      ↓
Highlight them
```

### Phase complete when

The starting chess position is visually displayed and pieces can be selected with the mouse.

---

# 9. PHASE 4 — Piece Movement Engine

## 👤 Member 3

This person handles the movement mechanics for **all six pieces**.

Do not split pieces among different members.

### Pawn

* One-square movement
* Two-square first movement
* Diagonal capture

### Rook

* Horizontal
* Vertical

### Knight

* L-shaped movement
* Jumping

### Bishop

* Diagonal movement

### Queen

* Horizontal
* Vertical
* Diagonal

### King

* One-square movement

### General rules

* Board boundaries
* Friendly pieces
* Enemy pieces
* Blocking pieces
* Captures
* Possible move generation

### Important distinction

At this stage:

**Possible move ≠ necessarily legal chess move.**

For example, the engine may determine that the King can physically move to a square, while the Rules Engine later determines that the square is attacked.

### Phase complete when

Every piece can generate its normal possible moves correctly.

---

# 10. PHASE 5 — Chess Rules Engine

## 👤 Member 4

This is the **advanced chess logic**.

### Check

Determine whether a king is attacked.

### Legal Moves

Reject moves that leave the player's own king in check.

### Checkmate

```text
King is in check
+
No legal move exists
=
Checkmate
```

### Stalemate

```text
King is NOT in check
+
No legal move exists
=
Stalemate
```

### Special Moves

Implement:

#### Castling

* Kingside
* Queenside
* Castling restrictions

#### En Passant

* Track previous move
* Determine when available
* Perform capture

#### Pawn Promotion

When a pawn reaches the final rank:

```text
Pawn
 ↓
Queen
Rook
Bishop
Knight
```

### Phase complete when

The game follows official chess legality rather than simply allowing pieces to move according to their basic patterns.

---

# 11. PHASE 6 — Game Controller & Game Flow

## 👤 Member 5

This person connects the different systems.

### Turn Management

* White's turn
* Black's turn
* Change turns after valid moves
* Prevent wrong-player movement

### Game State

Track:

* Current board
* Current player
* Selected piece
* Previous move
* Captured pieces
* Game status

### Game Flow

```text
Start Game
    ↓
White Turn
    ↓
Select Piece
    ↓
Select Destination
    ↓
Validate Move
    ↓
Update Board
    ↓
Black Turn
    ↓
Repeat
```

### UI screens

Member 5 can also manage:

* Main menu
* Start game
* Restart
* Pause
* Game over
* Winner message
* Move history

### Phase complete when

All the individual systems can operate together as an actual playable game.

---

# 12. PHASE 7 — Integration

## 👤 Member 6 — Integration Lead

Member 6 should not simply "wait for everyone else."

They should continuously integrate and test the modules.

### Responsibilities

* Merge branches
* Resolve conflicts
* Test module compatibility
* Identify integration problems
* Maintain test cases
* Track bugs
* Help other members when interfaces need modification

### Integration flow

```text
Board
  ↓
Piece Data
  ↓
Movement
  ↓
Rules
  ↓
Game Controller
  ↓
Pygame GUI
```

### Phase complete when

All major modules communicate correctly.

---

# 13. PHASE 8 — Testing

## 👤 Member 6 — Lead

## 👥 All Members — Support

Testing should happen throughout development, not only at the end.

### Test individual pieces

```text
Pawn
Rook
Knight
Bishop
Queen
King
```

### Test movement

* Normal movement
* Invalid movement
* Blocking
* Capturing
* Board boundaries

### Test chess rules

* Check
* Checkmate
* Stalemate
* Castling
* En passant
* Promotion

### Test unusual positions

```text
King surrounded by pieces
King attacked by multiple pieces
Pinned piece
Piece at board edge
Blocked sliding piece
Multiple captures
Castling while in check
Castling through attacked square
Promotion
En passant
```

---

# 14. PHASE 9 — GUI Polish

## 👤 Member 2 — Lead

## 👤 Member 5 — Support

After the game works, improve the presentation.

### Add

* Better chess pieces
* Better board design
* Move highlighting
* Capture highlighting
* Check highlighting
* Checkmate screen
* Smooth movement
* Animations
* Sound effects
* Background music
* Buttons
* Themes
* Responsive window sizing

### Important

Do not spend most of the project making the game beautiful before the chess logic works.

---

# 15. PHASE 10 — Optional AI

## 👤 Member 6 — Lead

## 👤 Members 3 & 4 — Support

Only begin after the two-player game is working.

### Level 1 — Random AI

Choose a random legal move.

### Level 2 — Simple AI

Prioritize:

* Captures
* Valuable pieces
* King safety

### Level 3 — Minimax

Search possible future moves.

### Level 4 — Alpha-Beta Pruning

Improve Minimax performance.

### AI flow

```text
Current Board
     ↓
Generate Legal Moves
     ↓
Evaluate Moves
     ↓
Select Move
     ↓
Send Move to Game Controller
     ↓
Update Board
```

The AI should use the **same movement and rules system** as the human player.

Do not create a second independent chess engine.

---

# 16. PHASE 11 — Final Testing

## All Members

Play complete games.

### Functional checklist

* [ ] Board works
* [ ] Pieces display correctly
* [ ] Pieces can be selected
* [ ] Movement works
* [ ] Captures work
* [ ] Turns work
* [ ] Check works
* [ ] Checkmate works
* [ ] Stalemate works
* [ ] Castling works
* [ ] En passant works
* [ ] Promotion works
* [ ] Restart works
* [ ] Game-over screen works
* [ ] Move history works

### Performance

Check:

* No unnecessary lag
* Smooth mouse interaction
* No memory issues
* No crashes during normal play

---

# 17. PHASE 12 — Final Project

## All Members

Before submission:

* Clean the code
* Remove unused files
* Add comments where necessary
* Fix naming inconsistencies
* Test the complete application
* Test on another computer
* Check asset paths
* Create requirements file
* Update README
* Add screenshots
* Prepare presentation
* Prepare project demonstration

---

# 18. Git Workflow

Each member works on their own branch.

```text
main
│
├── board
├── gui
├── movement
├── rules
├── game-controller
└── testing-ai
```

### Standard workflow

```text
Pull latest main
       ↓
Work on your branch
       ↓
Test
       ↓
git add .
       ↓
git commit
       ↓
git push
       ↓
Merge / Pull Request
       ↓
Integration testing
```

### Good commit examples

```text
Create 8x8 chess board
Add board coordinate system
Add piece rendering
Implement knight movement
Implement bishop movement
Add check detection
Implement castling
Add game-over screen
Fix pawn promotion
Add move highlighting
```

---

# 19. Team Rules

### Rule 1

**Do not work directly on `main`.**

### Rule 2

Don't modify another member's module unnecessarily.

### Rule 3

If you change a shared data structure, tell everyone.

### Rule 4

Don't commit code that prevents the project from running.

### Rule 5

Commit small, logical changes.

### Rule 6

Test before merging.

### Rule 7

The chess engine and GUI should remain separate.

For example:

```text
BAD:

Movement code
     ↓
Directly draws Pygame graphics
```

Better:

```text
Movement Engine
     ↓
Returns game information
     ↓
GUI
     ↓
Displays it
```

---

# 20. Recommended Development Timeline

## Stage 1 — Foundation

```text
Member 1 → Board
Member 2 → GUI framework
Member 3 → Movement foundation
Member 4 → Rules foundation
Member 5 → Game controller design
Member 6 → Testing framework
```

↓

## Stage 2 — Core Game

```text
Member 1 → Board state
Member 2 → Piece rendering
Member 3 → All piece movement
Member 4 → Check/legal moves
Member 5 → Turns/game flow
Member 6 → Integration testing
```

↓

## Stage 3 — Complete Chess

```text
Member 3 → Movement refinement
Member 4 → Checkmate + special rules
Member 5 → Game-state integration
Member 1 → Board improvements
Member 2 → GUI improvements
Member 6 → Full testing
```

↓

## Stage 4 — Polish

```text
GUI
Animations
Sounds
Move history
Menus
Bug fixing
```

↓

## Stage 5 — Optional AI

```text
AI
 ↓
Testing
 ↓
Difficulty levels
```

↓

## Stage 6 — Final Submission

```text
Complete Game
      ↓
Final Testing
      ↓
Documentation
      ↓
Presentation
      ↓
Demo
```

---

# 21. Final Responsibility Summary

| Member | Primary Module        | Secondary Responsibilities                       |
| ------ | --------------------- | ------------------------------------------------ |
| **1**  | Board System          | Coordinates, board state                         |
| **2**  | Piece Rendering & GUI | Mouse interaction, animations, visual design     |
| **3**  | Movement Engine       | Possible moves, captures, movement testing       |
| **4**  | Chess Rules           | Check, checkmate, special moves                  |
| **5**  | Game Controller       | Turns, game state, menus, move history           |
| **6**  | Integration & Testing | Git integration, testing, debugging, optional AI |

---

# 22. Most Important Dependency

The team should think about the project like this:

```text
                 BOARD
                   │
                   ↓
            PIECE MOVEMENT
                   │
                   ↓
             CHESS RULES
                   │
                   ↓
            GAME CONTROLLER
                   │
                   ↓
              PYGAME GUI
                   │
                   ↓
             USER INPUT
```

But the actual interaction is two-way:

```text
User
 ↓
GUI
 ↓
Game Controller
 ↓
Rules Engine
 ↓
Movement Engine
 ↓
Board State
 ↓
Game Controller
 ↓
GUI
 ↓
User
```

This separation is important because it prevents the project from becoming one huge `main.py` file.

---

# 23. Definition of Done

The project is complete when:

### Board

* [ ] 8×8 board
* [ ] Correct colors
* [ ] Correct coordinates
* [ ] Correct starting position

### Pieces

* [ ] All 12 piece types
* [ ] Correct graphics
* [ ] Correct positions

### Movement

* [ ] Pawn
* [ ] Rook
* [ ] Knight
* [ ] Bishop
* [ ] Queen
* [ ] King
* [ ] Capturing
* [ ] Blocking

### Chess Rules

* [ ] Turns
* [ ] Legal moves
* [ ] Check
* [ ] Checkmate
* [ ] Stalemate
* [ ] Castling
* [ ] En passant
* [ ] Promotion

### GUI

* [ ] Mouse interaction
* [ ] Selection
* [ ] Move highlighting
* [ ] Game status
* [ ] Restart
* [ ] Game-over screen
* [ ] Move history

### Quality

* [ ] Unit testing
* [ ] Integration testing
* [ ] Bug fixing
* [ ] Clean code
* [ ] Git repository organized
* [ ] README completed
* [ ] Presentation prepared

### Optional

* [ ] AI opponent
* [ ] AI difficulty levels
* [ ] Sound
* [ ] Animations
* [ ] Save/load
* [ ] Chess clock

---

# 24. Golden Rule

**Build the game in this order:**

```text
BOARD
  ↓
PIECES
  ↓
MOVEMENT
  ↓
CAPTURES
  ↓
TURNS
  ↓
LEGAL MOVES
  ↓
CHECK
  ↓
CHECKMATE
  ↓
SPECIAL MOVES
  ↓
GUI POLISH
  ↓
AI
```

Do **not** start with AI, animations, or complicated menus.

First make the game **playable and correct**. Then make it **beautiful and advanced**.
