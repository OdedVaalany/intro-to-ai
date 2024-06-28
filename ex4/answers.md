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
    > -   **sum heuristic** not guarantee the optimal solution, The function is
    >     not admissible since the the function sum the levels when each sub
    >     goal were achived. than sometimes the heuristic overestimate the cost
    >     to reach the goal and this leads to unadmissibility. and since
    >     consistentsy lead to admissibility therefore we can conclude that it
    >     isn't a consistent heuristic
    > -   **max heuristic** guarantee an optimal solution since the heuristic
    >     is consistent. The huristic return for an action the number of graph
    >     levels to open until satisfy all the the proposition. We have
    >     $e=(v_1,v_2)$ ,the value of $h(v_1)$ will be the number of levels
    >     until satisfy all the propositions, and also for > $v_2$ now since
    >     $v_2$ comes after $v_1$ so $h(v_1)-h(v_2) \leq 1$ cause if $e$ cause
    >     forward us to the goal so therefore
    >     $h(v_1)-h(v_2) = 1 $ and if it
    >     didn't so $h(v_1)-h(v_2) = 0 $ and now we know that $c(e) = 1$
    >     and we can write
    >     $h(v_1)-h(v_2) \leq 1 = c(e) \iff h(v_1) \leq c(e) + h(v_2)$ and this
    >     is the definition of consistent heuristic.

1.  Empirically, what are the lengths of the plans you found for the DWR
    problem (in questions 11 and 12) with each of the heuristics? Include also
    the null heuristic results in your comparison. For each of these - is it an
    optimal plan?

    > Data first:
    >
    > -   **Null**: ran 0.00s and achived plan with 6 actions
    > -   **Max**: ran 0.03s and achived plan with 6 actions
    > -   **Sum**: ran 0.01s and achived plan with 6 actions The planning
    >
    > The planning problem we recived as follow:<br> we have 2 robots r and q
    > and two containers a and b. <br>The **initial state** is when r free and
    > in room number 1 and q is free and in room number 2. container a in room
    > 1 and container b in room 2.<br> we want to end when container a in room
    > 2 and container b in room 1<br> so one optimal solution is:<br>
    >
    > 1.  robot r hold container a
    > 1.  robot q hold container b
    > 1.  robot r goes to room 2
    > 1.  robot q goes to room 1
    > 1.  robot r release container a
    > 1.  robot q release container b
    >
    > And therefore we can see that all huristics achived the optimal solution

1.  Are the theoretical and empirical results consistent with each other? If
    so, explain. If not, explain how this is possible.

    > In terms of the **max heuristic**, both the empirical and theoretical
    > results are consistent. The **max heuristic** is considered an consistent
    > heuristic, which means it will always achieve optimal solutions. This is
    > supported by the empirical results, which also show optimal
    > solutions.<br> However, for the **sum heuristic**, the empirical and
    > theoretical results are not consistent. The theoretical analysis suggests
    > that the **sum heuristic** does not guarantee optimality. However, in
    > this specific planning problem, we happened to obtain an optimal solution
    > using the **sum heuristic**. It's important to note that while optimality
    > is not guaranteed, it doesn't mean that we will always achieve
    > non-optimal solutions. In certain situations, like this one, we may still
    > obtain optimal solutions using the **sum heuristic**.

### Running Time

1.  Theoretically, can we claim that one of the heuristics is guaranteed to
    expand less-or-equal nodes than the other heuristic (in the general case)?

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

    > Yes, this heuristic also consistent since it return the level when all
    > the propositional are satisfied and there is no mutex between them. lets
    > assume that $e=(v_1,v_2)$, the cost of $e$ is 1 becuase we count the
    > number of actions(level). lets assume that $h(v_1) - h(v_2) > 1 = c(e)$ ,
    > that means that if the heuristic says that from $v_2$ achives all
    > propsitions at level X with no mutexs , than $h(v_1) \leq  X + 1$
    > (becuase path from v_1 to goal going throw v_2 is at most X +1), so
    > $h(v_1) - h(v_2) \leq 1$ in contradiction to our assumption.

2. What is the relation between this heuristic and the max level heuristic in
   terms of number of nodes expanded?
    > the number of expanded nodes for the set heurisitc will be smaller than
    > the number of expanded nodes for the max heuristic. all the paths that
    > the set heuristic prefer is sub group of the pathes that the max
    > heuristic will be prefere becuase the set heuristic is max heuristic with
    > more constraints. if there is 2 pathes one get to goal with no mutex at
    > level X and one get to goal with mutex at level X+1 the max heuristic
    > will go to the one at level and only after to the level X+1 , while the
    > set heuristic will go to the one at level X+1 and wont expand the path to
    > the path at level X.
3. Is this heuristic perfect in the sense that it always returns the precise
   distance to the goal?
    > No , because it isnt taking in considiration the mutex on the actions.
    > There are levels that all goals propresitions will be and there will be
    > no mutexs between them but the actions that got us there are with mutexes
    > so the path to this level will be not valid.
