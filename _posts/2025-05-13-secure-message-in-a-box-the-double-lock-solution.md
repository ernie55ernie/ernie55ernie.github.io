---
layout: post
title: "Secure Message in a Box: The Double-Lock Solution"
date: 2025-05-13
category: quantitative interview
---

A well-known puzzle in secure communication goes as follows:

> You must send a **confidential document** via a courier.  
> The catch? The courier is **untrusted**—if they ever see the box **unlocked** or containing **extra locks**, they will confiscate everything.
>
> - You and your colleague each have a **padlock**, but **only you** know the key to yours, and **only they** know theirs.
> - You **cannot share keys** or meet in person.

**How can you securely send the locked box and its contents?**

## Step-by-Step Solution: The Double-Lock Method

This problem is about using **asymmetric locking** to maintain confidentiality.

### Step 1: You Lock the Box

- Place the document in a box.
- Lock it with **your own padlock**.
- Send the box (locked) to your colleague.

The courier sees a locked box (no loose locks or keys)—safe.

### Step 2: Colleague Adds Their Lock

- Your colleague **cannot open** your lock, so they **add their own padlock** beside yours.
- The box now has **two padlocks** (yours and theirs).
- They send it back to you.

Again, the courier sees a locked box—still secure.

### Step 3: You Remove Your Lock

- You receive the doubly-locked box.
- You **remove your own padlock**, leaving **only your colleague’s lock**.
- Send the box to your colleague once more.

Still locked, and no key was shared.

### Step 4: Colleague Unlocks and Retrieves

- Now your colleague can **unlock their own padlock**.
- They safely access the document inside.

## Why It Works

- The box is **never unlocked in transit**.
- No **keys are exchanged**.
- Both locks are **used sequentially** to ensure only the intended recipient can access the content.

## Final Answer

**Use the double-lock technique**:
1. Lock with your padlock and send.
2. Colleague adds their padlock and returns.
3. You remove your lock and send again.
4. They unlock and retrieve the document.

# Reference

* [1] [Brain Teaser 13: Message Delivery](https://medium.com/@shelvia1039/brain-teaser-13-message-delivery-d54b8d02f73f)
