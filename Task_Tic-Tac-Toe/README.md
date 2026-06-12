# Tic-Tac-Toe AI using Minimax Algorithm

---

## What This Project Does

This is a terminal-based Tic-Tac-Toe game where you play against a computer.
The computer is not random — it uses a real AI algorithm called **Minimax** to
think through every possible move and always pick the best one.

- **You** play as `X`
- **Computer** plays as `O`
- The board has 9 spots, numbered 1 to 9
- Type a number to place your X
- The AI will respond with its best move
- First to get 3 in a row wins — or it ends in a draw!

---

## Requirements

- Python 3 (any version — 3.6 or above works fine)
- No extra libraries needed. Everything used here comes built into Python.

---

## How to Run the Game

**Step 1:** Make sure Python is installed. Check by running:
```
python3 --version
```

**Step 2:** Save the file `tic_tac_toe.py` somewhere on your computer.

**Step 3:** Open a terminal, go to the folder where you saved the file, and run:
```
python3 tic_tac_toe.py
```

That's it! The game will start right in your terminal.

---

## How the Board Works

When the game starts, you will see this:

```
  1 | 2 | 3
 -----------
  4 | 5 | 6
 -----------
  7 | 8 | 9
```

Each number is a spot on the board. You type that number to place your X there.

For example, if you type `5`, your X goes in the middle. After a few moves it
might look like this:

```
  X | 2 | 3
 -----------
  4 | O | 6
 -----------
  7 | 8 | X
```

---

## Project Structure

There is only one file in this project:

```
tic_tac_toe.py
```

Everything is inside that single file — no imports, no extra setup needed.

---

## How the Code Is Organized (Step by Step)

The code is split into 9 clearly labelled steps. Here is what each one does:

---

### Step 1 — `create_board()`

Creates the board as a Python list with 9 items: `["1", "2", ..., "9"]`.

Each item starts as a number string. As the game goes on, numbers get replaced
by `"X"` or `"O"` depending on who plays there.

```python
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
```

Think of it like 9 boxes in a row. The positions map to the grid like this:

```
index:  0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
```

---

### Step 2 — `show_board(board)`

Prints the board in a grid format using f-strings.

It reads from the board list and displays index 0–2 as the top row,
3–5 as the middle row, and 6–8 as the bottom row.

---

### Step 3 — `player_move(board)`

Asks the player to type a number between 1 and 9.

Before placing `X`, it checks three things:
1. Did the player actually type a number (not letters)?
2. Is the number between 1 and 9?
3. Is that spot still empty (not already taken)?

If any check fails, it prints a message and asks again using a `while True` loop.

Once all checks pass, it places `"X"` on the board.

One thing to note: the player types `1–9` but the list uses indexes `0–8`,
so the code does `index = move - 1` to convert.

---

### Step 4 — `check_winner(board, player)`

Checks if a given player (`"X"` or `"O"`) has won.

A player wins by getting 3 in a row — across a row, down a column, or diagonally.

The function checks all 8 possible winning combinations one by one:
- Row 1: indexes 0, 1, 2
- Row 2: indexes 3, 4, 5
- Row 3: indexes 6, 7, 8
- Column 1: indexes 0, 3, 6
- Column 2: indexes 1, 4, 7
- Column 3: indexes 2, 5, 8
- Diagonal ↘: indexes 0, 4, 8
- Diagonal ↙: indexes 2, 4, 6

Returns `True` if that player has won, `False` otherwise.

---

### Step 5 — `check_draw(board)`

Checks if the board is completely full with no winner.

It loops through all 9 spots. If even one spot still has a number in it
(meaning it's empty), the game is not a draw yet.

If all 9 spots have `"X"` or `"O"`, returns `True` (it's a draw).

---

### Step 6 — `minimax(board, is_ai_turn)`

This is the most important function — the AI's brain.

**What is Minimax?**

Minimax is a decision-making algorithm. It works by simulating every single
possible game that could happen from the current board position, all the way
to the end. Then it scores each outcome:

| Outcome     | Score |
|-------------|-------|
| AI (O) wins | +1    |
| Human wins  | -1    |
| Draw        |  0    |

The AI tries to **maximize** its score (pick moves leading to +1).
The human is assumed to **minimize** the AI's score (pick moves leading to -1).

**How does it work in code?**

The function calls itself recursively. Each call simulates one more move,
alternating between AI and human, until the game ends. Then it returns the
score back up the chain.

This is what makes the AI unbeatable — it has already seen every possible
future before it makes a single move.

---

### Step 7 — `best_ai_move(board)`

Calls `minimax()` for every empty spot on the board and compares the scores.

Whichever empty spot returns the highest score is the one the AI plays.
It then places `"O"` in that spot for real.

---

### Step 8 — `play_game()`

The main game loop. This is where everything connects together.

It keeps looping until the game is over:
1. Human picks a spot → board updates → check if human won or drew
2. AI picks a spot → board updates → check if AI won or drew
3. Repeat

---

### Step 9 — `if __name__ == "__main__"`

This is standard Python practice. It means: only run `play_game()` when this
file is executed directly. If someone imports this file into another project,
the game won't accidentally start on its own.

---

## Full Flow Diagram

```
START
  |
  v
create_board()          <-- makes the 9-spot list
  |
  v
show_board()            <-- prints the grid
  |
  v
[ GAME LOOP ]
  |
  +---> player_move()   <-- human picks a spot (with validation)
  |         |
  |         v
  |     show_board()
  |         |
  |         v
  |     check_winner("X") --> win? --> print result, END
  |         |
  |         v
  |     check_draw()    --> draw? --> print result, END
  |         |
  |         v
  +---> best_ai_move()  <-- AI uses minimax to pick best spot
  |         |
  |         v
  |     show_board()
  |         |
  |         v
  |     check_winner("O") --> win? --> print result, END
  |         |
  |         v
  |     check_draw()    --> draw? --> print result, END
  |         |
  +---------+           <-- loop again
```

---

## Key Python Concepts Used

| Concept | Where It's Used |
|---|---|
| Lists | The board is stored as a list of 9 items |
| f-strings | Used to display the board nicely |
| while True loop | Keeps asking for input until it's valid |
| Functions | Each step is its own function |
| if / elif / else | Checking winner, draw, valid input |
| Recursion | Minimax calls itself to simulate future moves |
| Boolean (True/False) | check_winner and check_draw return these |

---

## Sample Game Output

```
===================================
   Welcome to Tic-Tac-Toe!
   You are X  |  Computer is O
===================================

  The board positions are:
   1 | 2 | 3
  -----------
   4 | 5 | 6
  -----------
   7 | 8 | 9

  1 | 2 | 3
 -----------
  4 | 5 | 6
 -----------
  7 | 8 | 9

Your turn! Pick a spot (1-9): 1

  X | 2 | 3
 -----------
  4 | 5 | 6
 -----------
  7 | 8 | 9

  Computer is thinking...
  Computer placed O on spot 5

  X | 2 | 3
 -----------
  4 | O | 6
 -----------
  7 | 8 | 9
```

---

## Can You Beat the AI?

No — and that is actually the point! Minimax with a complete game tree (like
Tic-Tac-Toe) will always find the perfect move. The best result you can get
against it is a draw, if you also play perfectly.

This is what makes it a great algorithm to learn — it is simple enough to
understand, but powerful enough to never lose.

---

## What I Learned Building This

- How to represent a game board as a Python list
- How to validate user input properly using loops
- How to check win conditions by looking at specific index combinations
- What recursion is and how it works in practice
- How the Minimax algorithm thinks ahead and evaluates moves
- How to connect multiple functions together into one working program

## Author
Made by Kalal Sohana

LinkedIn: [https://lnkd.in/g3aakZvn]

GitHub: [https://github.com/sohanakalal-ux/CODSOFT/tree/main/Task_Tic-Tac-Toe]

