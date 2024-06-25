# Intro To AI | Ex3

**subnitted by:** Oded Vaalany & Eran Ston

## Question 13 - max level and level sum (3 points) - Understanding Question

In this question we will compare different heuristics we can derive from a
planning graph, theoretically and empirically. We will focus on the max level
and level sum heuristics.<br> **Note**: In this question we talk about the case
where we use forward A\* tree search to solve the planning problem, guided by a
heuristic derived from the planning graph. In particular, here when we talk
about optimality we refer to the question of whether the search algorithm finds
the shortest plan possible.<br> **Note**: In all the questions, if you claim a
property of an heuristic explain why this property holds, even if we stated it
in class. We expect explanations, no formal proofs required.

### Optimality

1.  Theoretically, for each of the heuristics - is its optimality guaranteed?
    > First with sum huristic the optimallity is not guaranteed. if we 2
    > propsitions to achive and 2 actions to check. for the first action one of
    > the proposition achived in level 1 and the other in level 4 so the
    > huristic function will recive score of 5. the other action will achive th
    > first proposition in level 3 and also the sceond proposition, therefore
    > its score is 6. so the A\* algorithem will prefer the action that got 5
    > in the score but do 4 steps for the solution but actually the other
    > action that got 6 will find a solution in 3 steps. all those in the
    > assumption that there is not mutex with both actions.
