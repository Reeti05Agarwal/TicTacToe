# TicTacToe

**Representing a Tic-Tac-Toe AI**:

- *S₀*: Initial state (in our case, an empty 3X3 board)
- *Players(s)*: a function that, given a state *s*, returns which player’s turn it is (X or O).
- *Actions(s)*: a function that, given a state *s*, return all the legal moves in this state (what spots are free on the board).
- *Result(s, a)*: a function that, given a state *s* and action *a*, returns a new state. This is the board that resulted from performing the action *a* on state *s* (making a move in the game).
- *Terminal(s)*: a function that, given a state *s*, checks whether this is the last step in the game, i.e. if someone won or there is a tie. Returns *True* if the game has ended, *False* otherwise.
- *Utility(s)*: a function that, given a terminal state *s*, returns the utility value of the state: -1, 0, or 1.

An algorithm determines optimal actions in a game by recursively evaluating potential future states. It starts by considering the current player's turn and predicts whether they will choose actions leading to higher or lower values. By alternating between minimizing and maximizing values, the algorithm assigns values to potential states. This process involves simulating the opponent's optimal moves and recursively evaluating outcomes. Finally, the algorithm selects the action with the highest value for the current player.

- Given a state *s*
    - The maximizing player picks action *a* in *Actions(s)* that produces the highest value of *Min-Value(Result(s, a))*.
    - The minimizing player picks action *a* in *Actions(s)* that produces the lowest value of *Max-Value(Result(s, a))*.
- Function *Max-Value(state)*
    - *v = -∞*
    - if *Terminal(state)*:
        
         return *Utility(state)*
        
    - for *action* in *Actions(state)*:
        
         *v = Max(v, Min-Value(Result(state, action)))*
        
        return *v*
        
- Function *Min-Value(state)*:
    - *v = ∞*
    - if *Terminal(state)*:
        
         return *Utility(state)*
        
    - for *action* in *Actions(state)*:
        
         *v = Min(v, Max-Value(Result(state, action)))*
        
        return *v*
