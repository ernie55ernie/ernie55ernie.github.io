---
layout: post
title: "Airplane Seating Puzzle: The Drunk Passenger Paradox"
date: 2025-05-18
category: quantitative interview
---

You’re on a full flight with a peculiar boarding process:

> - There are **100 passengers**, each with a **ticketed seat** numbered 1 to 100.  
> - The **first passenger** is drunk and picks a seat **at random**.  
> - Each subsequent passenger:
>   - Takes their **own seat** if it's available.  
>   - If it's **taken**, they choose a **random available** seat.

**Question:** What is the probability that the **last passenger (100)** ends up in their **own seat**?

---

## Step 1: Analyze the Chaos

At first glance, this looks complicated—the drunk passenger disrupts the entire seating process.

But there’s a surprising **pattern** hiding beneath the randomness.

Let’s define \\(P_n\\) as the probability that passenger \\(n\\) finds seat \\(n\\) unoccupied when they board.

We want \\(P_{100}\\).

---

## Step 2: Insight from Simpler Cases

### Case \\(n = 2\\):

- Passenger 1 (drunk) picks randomly: seat 1 or seat 2
  - If they pick seat 1 → passenger 2 gets their seat.
  - If they pick seat 2 → passenger 2 gets a random one.

So:
- \\(P_2 = \frac{1}{2}\\)

### Case \\(n = 3\\):

Carefully working through possibilities, you find:

- \\(P_3 = \frac{1}{2}\\)

And for \\(n = 4, 5, \ldots, 100\\), simulations and theory confirm:

\\[
P_{100} = \frac{1}{2}
\\]

---

## Step 3: General Pattern and Intuition

Key realization:

- The first passenger creates the only randomness.
- The process preserves a surprising symmetry:
  - Whenever the first passenger chooses seat 1 → everyone else sits normally.
  - If they choose seat 100 → passenger 100 loses their seat.
  - Any other choice just "reshuffles" the issue among the remaining passengers.

The only time passenger 100 **definitely loses** is if passenger 1 **chooses seat 100**.

There are two equally likely endpoints:
- Seat 1 is taken first → passenger 100 wins.
- Seat 100 is taken first → passenger 100 loses.

---

## Final Answer

> The probability that the last passenger gets their assigned seat is:
>
> \\[
> \boxed{\frac{1}{2}}
> \\]

# Reference

* [1] [Taking Seats on a Plane](https://math.stackexchange.com/questions/5595/taking-seats-on-a-plane)