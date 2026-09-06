---
layout: post
title: "Light Bulb and Switches: Solving with Heat and Logic"
date: 2025-05-13
category: quantitative interview
---

You face this classic puzzle in deductive reasoning:

> A closed room contains a **light bulb**. Outside the room are **four toggle switches**, all initially off.  
> Exactly **one switch** controls the bulb.  
> You can flip switches however you want, but you're allowed to **enter the room only once** to observe the bulb (its on/off state, and whether it's warm).

**Goal:** Determine exactly **which switch controls the bulb**, using **only one visit** to the room.

---

## Step-by-Step Strategy

You're allowed to **touch** the bulb and check whether it's **on or warm**. This allows you to gain **more information** than just sight.

### Step 1: Create Four Unique States

To distinguish between 4 switches using a single bulb, we need **4 distinct observable states**. We can achieve this by combining **on/off** with **warm/cold**.

Here is the exact procedure:

1. **Turn ON Switch 1 and Switch 2**, and leave them on for about **10 minutes** to let the bulb heat up.
2. **Turn OFF Switch 1**. (Leave Switch 2 on).
3. **Turn ON Switch 3**.
4. **Leave Switch 4 OFF**.
5. **Immediately** enter the room.

### Step 2: Observe and Infer

Once inside, you touch the bulb and observe its state. There are exactly four possible outcomes, each uniquely identifying the correct switch:

- **Bulb is OFF and WARM** → Controlled by **Switch 1** (was on for 10 minutes, but turned off right before entering).
- **Bulb is ON and WARM** → Controlled by **Switch 2** (was on for 10 minutes, and left on).
- **Bulb is ON and COLD** → Controlled by **Switch 3** (was just turned on, so it hasn't had time to heat up).
- **Bulb is OFF and COLD** → Controlled by **Switch 4** (was never turned on).

---

## Final Answer

**You only need to enter the room once.**  
By cleverly combining timing (to create warm/cold states) with switch combinations (on/off states), you can uniquely identify all 4 switches in a single visit!

# Reference

* [1] [Puzzle 7 \| (3 Bulbs and 3 Switches)](https://www.geeksforgeeks.org/puzzle-7-3-bulbs-and-3-switches/)
