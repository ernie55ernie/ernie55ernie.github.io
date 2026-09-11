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

## Step 3: The Symmetry Argument

To solve this elegantly, notice what happens when *any* displaced passenger is forced to pick a random seat:

- If they pick **Seat 1**: The chain of displacement ends immediately. Every remaining passenger will find their assigned seat empty, including Passenger 100.
- If they pick **Seat 100**: Passenger 100's seat is gone, and they will definitely lose.
- If they pick **Seat \\(k\\)** (some other seat): The problem is simply deferred to Passenger \\(k\\), who will later find their seat taken and have to pick a random seat themselves.

Here is the magic symmetry: Whenever a passenger makes a random choice, **Seat 1 and Seat 100 are always both available**. Since they are picking randomly from the remaining pool, they are exactly equally likely to pick Seat 1 as they are to pick Seat 100. 

The cycle of displacement bounces around until someone finally picks either Seat 1 or Seat 100. Because those two specific seats are perfectly symmetric in every random draw, there is exactly a **50/50 chance** of which one gets picked first.

---

## Final Answer

> The probability that the last passenger gets their assigned seat is:
>
> \\[
> \boxed{\frac{1}{2}}
> \\]

# Reference

* [1] [Taking Seats on a Plane](https://math.stackexchange.com/questions/5595/taking-seats-on-a-plane)