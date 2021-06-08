# IA

Let us assume that m vehicles are located in squares (1, 1) through (m, 1) (the
bottom row) of an m × m squared parking. The vehicles must be moved to the
top row, but arranged in reverse order; so vehicle i starting from (i, 1) must end
up in (m − i + 1, m). On each time step, each of the m vehicles is restricted to
move only one square up, down, left, or right, or keep current position (i.e. does
not move); but if a vehicle does not move, one other adjacent vehicle (but not
more than one) can hop over it. Two vehicles cannot occupy the same square.
a. Write a detailed formulation for this search problem.
b. Identify a suitable search algorithm for this task and explain your choice.
