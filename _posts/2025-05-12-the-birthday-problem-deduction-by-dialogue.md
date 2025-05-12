---
layout: post
title: "The Birthday Problem: Deduction by Dialogue"
date: 2025-05-12
category: quantitative interview
---

## The Birthday Problem: Deduction by Dialogue

This logical deduction puzzle, inspired by the famous “Cheryl’s Birthday,” revolves around narrowing down possibilities from a short conversation between two people with partial information.

### The Setup

Your boss A's birthday is one of the following 10 dates:

- **March**: 4, 5, 8  
- **June**: 4, 7  
- **September**: 1, 5  
- **December**: 1, 2, 8

You are told **only the month**, while your colleague C is told **only the day**.

Everyone knows the list of 10 possible dates.

### Step 1: You Say  
> “I don’t know A’s birthday, and I know C doesn’t know it either.”

This tells us your month **cannot** be one with any uniquely identifying days.

Let’s look at the days across months:
- 1 → September, December  
- 2 → December  
- 4 → March, June  
- 5 → March, September  
- 7 → June  
- 8 → March, December

Some days are unique:
- **7** only appears in June  
- **2** only appears in December

If your month were **June** (with day 7) or **December** (with day 2), then C *might* know the birthday right away.

So when you confidently say, “I know C doesn’t know,” it rules out **June** and **December** as your month.

You're left with **March** and **September**.

### Step 2: C Says  
> “At first I didn’t know A’s birthday, but now I do.”

C must have heard a day that was **not unique at first**, but now can be **uniquely associated** with one date, given the month must be March or September.

Let’s filter the list down to March and September dates:

- **March 4, 5, 8**
- **September 1, 5**

So the possible days are: 1, 4, 5, 8

C must have one of these.

Now let’s test which days can identify a unique date from this reduced list:
- 1 → Only in September
- 4 → Only in March
- 5 → Appears in both March and September → **not unique**
- 8 → Only in March

So if C had **5**, they’d still be confused. But if C had **1**, **4**, or **8**, they can now know the date.

Therefore, C must have seen **1**, **4**, or **8**.

### Step 3: You Say  
> “Now I know it, too.”

You must have been told **March** or **September**, and now that C figured it out, you must also be able to.

If your month were **March**, remaining candidates: March 4, 5, 8  
Only **4** and **8** are uniquely identifying after step 2.

If your month were **September**, remaining: September 1, 5  
Only **1** is uniquely identifying.

So, to be sure, your month must be one where only **one** date remains valid after step 2.

- If your month was **March**, and the day was 4 or 8 → still ambiguous
- If your month was **September**, and the day was 1 → unique

Hence, A's birthday is **September 1**.

## Final Answer

**September 1**

# Reference

* [1] [Cheryl’s Birthday Logic Puzzle](https://en.wikipedia.org/wiki/Cheryl%27s_Birthday)