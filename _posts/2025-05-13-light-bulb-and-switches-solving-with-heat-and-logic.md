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

### Step 1: Divide and Conquer with Time

1. **Turn on Switch 1** — leave it on for **a few minutes** (say 5).
2. **Turn off Switch 1**, then **turn on Switch 2**.
3. Leave Switches 3 and 4 **off**.
4. **Immediately** enter the room.

### Step 2: Observe and Infer

Once inside, observe the bulb:

- **Bulb is ON** → Controlled by **Switch 2**
- **Bulb is OFF but warm** → Controlled by **Switch 1**
- **Bulb is OFF and cold** → Controlled by **Switch 3 or 4**

Now, you've narrowed it down to:

- If warm → Switch 1
- If on → Switch 2
- If off and cold → Must be either Switch 3 or 4

### Step 3: Handling 3 or 4

Now you only need to distinguish between **Switch 3 and 4**. This requires just **one more experiment**. Repeat the process but only for the two remaining candidates.

However, the puzzle specifically asks for the **minimum number of room entries** to **guarantee** the answer.

---

## Final Answer

**You only need to enter the room once**  
With clever timing and heat detection, you can determine exactly which switch controls the bulb.

# Reference

* [1] [Puzzle 7 \| (3 Bulbs and 3 Switches)](https://www.geeksforgeeks.org/puzzle-7-3-bulbs-and-3-switches/)
