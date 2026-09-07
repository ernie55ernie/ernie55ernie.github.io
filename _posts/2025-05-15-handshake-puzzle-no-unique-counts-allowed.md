---
layout: post
title: "Handshake Puzzle: No Unique Counts Allowed"
date: 2025-05-15
category: quantitative interview
---

You're at a party with **25 other guests** (26 people total).  
Each guest shakes hands with whomever they like—**except** themselves.

You shake hands with **each of the 25**.  
But the others may or may not shake hands among themselves.

> **Question:** Show that **at least two people** (among the 25 others) must have shaken hands with the **same number** of people.

---

## Step 1: What Are the Possible Handshake Counts?

Let's look at the **total number of handshakes** for each of the 25 other guests.

Since you shook hands with **everyone**, every guest has at least **1** handshake.  
The maximum number of handshakes a guest could have is **25** (you + the 24 other guests).

So, the possible total handshake counts range from **1 to 25**.

That’s exactly **25 possible values**.

---

## Step 2: Apply the Pigeonhole Principle

Suppose—just for contradiction—that **each of the 25 guests has a unique handshake count**.

Then their counts must perfectly cover **all** the integers from 1 to 25.

But wait: here comes the contradiction.

### The Guest with 1 Handshake
This guest shook hands with exactly one person. Since you shook hands with everyone, their single handshake **must have been with you**. They shook hands with **no other guests**.

### The Guest with 25 Handshakes
This guest shook hands with **every single person** in the room. This includes you, and crucially, it includes the guest who only had 1 handshake!

**You can't have both extremes in the same room.** The guest with 25 handshakes must have shaken hands with the guest with 1 handshake, but the guest with 1 handshake *only* shook hands with you. This is impossible!

So the assumption that all 25 people have **unique handshake counts** fails.

---

## Conclusion

> At least **two people must share the same handshake count**—by the pigeonhole principle and logical contradiction.

---

## Final Answer

**No matter how the handshakes go, at least two people must have shaken hands with the same number of people.**

# Reference

* [1] [Pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle)
