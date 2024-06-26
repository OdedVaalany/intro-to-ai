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

    > we will seperate the answer to 2 sub answers:
    >
    > -   sum heuristic guarantee the optimal solution since the function is
    >     not admissible since the the function sum the levels when each sub
    >     goal were achived. than sometimes the heuristic overestimate the cost
    >     to reach the goal and this leads to unadmissibility. and this leads
    >     that the heuristic not guarantee optimallity
    > -   max heuristic guarantee an optimal solution since the heuristic is
    >     admissible. since the huristic return for an action the number of
    >     graph levels to open until satisfy all the the proposition. and since
    >     the cost of a path is the number of graph levels to open the function
    >     never overestimates the cost to reach the goal

1.  Empirically, what are the lengths of the plans you found for the DWR
    problem (in questions 11 and 12) with each of the heuristics? Include also
    the null heuristic results in your comparison. For each of these - is it an
    optimal plan?

    > Data first:
    >
    > -   **Null**: ran 0.00s and achived plan with 6 actions
    > -   **Max**: ran 0.03s and achived plan with 6 actions
    > -   **Sum**: ran 0.01s and achived plan with 6 actions The planning
    >     problem we recived gose as follow:<br> we have 2 robots r and q and
    >     two containers a and b. <br>The **initial state** is when r free and
    >     in room number 1 and q is free and in room number 2. container a in
    >     room 1 and container b in room 2.<br> we want to end when container a
    >     in room 2 and container b in room 1<br> so one optimal solution
    >     is:<br>
    >
    > 1.  robot r hold container a
    > 1.  robot q hold container b
    > 1.  robot r goes to room 2
    > 1.  robot q goes to room 1
    > 1.  robot r release container a
    > 1.  robot q release container b And therefore we can see that all
    >     huristics achived the optimal solution

1.  Are the theoretical and empirical results consistent with each other? If
    so, explain. If not, explain how this is possible.

    > In terms of the **max heuristic**, both the empirical and theoretical
    > results are consistent. The **max heuristic** is considered an admissible
    > heuristic, which means it will always achieve optimal solutions. This is
    > supported by the empirical results, which also show optimal
    > solutions.<br> However, for the **sum heuristic**, the empirical and
    > theoretical results are not consistent. The theoretical analysis suggests
    > that the **sum heuristic** does not guarantee optimality. However, in
    > this specific planning problem, we happened to obtain an optimal solution
    > using the **sum heuristic**. It's important to note that while optimality
    > is not guaranteed, it doesn't mean that we will always achieve
    > non-optimal solutions. In certain situations, like this one, we may still
    > obtain optimal solutions using the sum heuristic.

### Running Time

1.  Theoretically, can we claim that one of the heuristics is guaranteed to

    > The **max heuristic** is expected to expand more nodes compared to the
    > **sum heuristic** in the general case. This is because the **max
    > heuristic** assigns scores based on the number of levels needed to
    > satisfy all propositions, which may result in multiple actions having the
    > same score. If the A\* algorithm does not prioritize the action that
    > leads to fewer expansions, it may end up expanding unnecessary nodes. On
    > the other hand, the **sum heuristic** considers the sum of achieving
    > levels for each proposition, which allows it to prioritize actions that
    > are more likely to lead to the solution. This probabilistic approach can
    > result in fewer expansions overall.

1.  empirically, how many search nodes were expanded with each one of the
    heuristics? Which heuristic was more efficient in this case?

    > Here are the results:
    >
    > -   The **sum heuristic** expanded 9 search nodes.
    > -   The **max heuristic** expanded 29 search nodes.
    >
    > Therefore, it is evident that the **sum heuristic** was more efficient in
    > this problem.

## Question 14 - set level (3 points) - Understanding Question

In this question we will consider theoretically a heuristic you do not
implement in the exercise - the set level heuristic. Reminder: the set-level
heuristic returns the level at which all the propositions in the goal appear in
the planning graph without mutex between any pair of them. Just like in the
previous question, we will consider the case of using this heuristic to guide
an A\* search.

1. Is the optimality of this heuristic (in the same sense as in the previous
   question) guaranteed?
    > ans
2. What is the relation between this heuristic and the max level heuristic in
   terms of number of nodes expanded?
    > ans
3. Is this heuristic perfect in the sense that it always returns the precise
   distance to the goal?
    > ans
