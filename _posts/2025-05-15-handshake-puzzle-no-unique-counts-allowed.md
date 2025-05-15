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

Each of the **25 guests** could have shaken hands with anywhere from:

- **0** other guests (besides you),
- up to **24** others (excluding themselves and you).

So, the possible handshake counts range from **0 to 24**.

That’s **25 possible values**.

---

## Step 2: Apply the Pigeonhole Principle

Suppose—just for contradiction—that **each of the 25 people has a unique handshake count**.

Then their counts must cover **all** the integers from 0 to 24.

But wait: here comes the contradiction.

### Can Someone Have 0 Handshakes?

Yes—someone could’ve refused to shake hands with anyone else.

### Can Someone Have 24 Handshakes?

That would mean they shook hands with **every other person**, including the one who shook **zero hands**—which is impossible!

**You can't have both extremes (0 and 24) in the same room.**

So the assumption that all 25 people have **unique handshake counts** fails.

---

## Conclusion

> At least **two people must share the same handshake count**—by the pigeonhole principle and logical contradiction.

---

## Final Answer

**No matter how the handshakes go, at least two people must have shaken hands with the same number of people.**

# Reference

* [1] [Pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle)
