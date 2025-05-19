---
layout: post
title: "Russian Roulette: Optimal Strategies Across Four Variants"
date: 2025-05-19
category: quantitative interview
---

Russian roulette presents various strategic decisions depending on the game's rules. Let's analyze four distinct scenarios to determine the optimal choice in each.

---

### Variant 1: One Bullet, No Re-Spin

**Setup**: A single bullet is placed in a six-chamber revolver. The cylinder is spun once at the start and then remains fixed. Players take turns pulling the trigger.

**Question**: Should you go first or second?

**Analysis**:

- The bullet's position is fixed after the initial spin.
- Each chamber has an equal probability of containing the bullet.
- The sequence of trigger pulls corresponds to the sequence of chambers.

**Conclusion**:

- Each player has an equal chance of encountering the bullet.
- Therefore, it doesn't matter whether you go first or second; the probability of being shot is equal for both players.

---

### Variant 2: One Bullet, Re-Spin Each Turn

**Setup**: A single bullet is placed in a six-chamber revolver. The cylinder is spun before each trigger pull. Players take turns pulling the trigger.

**Question**: Should you go first or second?

**Analysis**:

- Each trigger pull is independent due to the re-spin.
- The probability of being shot on any given turn is \\( \frac{1}{6} \\).
- However, the first player has a \\( \frac{1}{6} \\) chance of being shot immediately.
- The second player's chance of being shot is \\( \frac{5}{6} \times \frac{1}{6} = \frac{5}{36} \\), assuming the first player survives.

**Conclusion**:

- The second player has a lower initial risk.
- Therefore, it's better to go second to minimize the chance of being shot.

---

### Variant 3: Two Bullets in Random Chambers

**Setup**: Two bullets are placed randomly in the six chambers. After the first player survives, you must decide whether to spin the cylinder before your turn.

**Question**: Should you spin the cylinder?

**Analysis**:

- **If you spin**: Each chamber has an equal chance of containing a bullet. With two bullets, the probability of being shot is \\( \frac{2}{6} = \frac{1}{3} \\).
- **If you don't spin**: The first player survived, so their chamber was empty. There are now five chambers left with two bullets. The probability of being shot is \\( \frac{2}{5} = 0.4 \\).

**Conclusion**:

- Spinning reduces the probability of being shot from 0.4 to approximately 0.333.
- Therefore, you should spin the cylinder before your turn.

---

### Variant 4: Two Bullets in Consecutive Chambers

**Setup**: Two bullets are placed in adjacent chambers. After the first player survives, you must decide whether to spin the cylinder before your turn.

**Question**: Should you spin the cylinder?

**Analysis**:

- **If you spin**: The probability of being shot is \\( \frac{2}{6} = \frac{1}{3} \\).
- **If you don't spin**: Given the bullets are adjacent and the first player survived, there's a \\( \frac{1}{4} \\) chance of being shot.

**Conclusion**:

- Not spinning reduces the probability of being shot from approximately 0.333 to 0.25.
- Therefore, you should not spin the cylinder before your turn.

---

## Summary

| Variant                                      | Optimal Choice | Probability of Being Shot |
|----------------------------------------------|----------------|---------------------------|
| One Bullet, No Re-Spin                       | Either         | Equal for both players    |
| One Bullet, Re-Spin Each Turn                | Go Second      | Lower for second player   |
| Two Bullets in Random Chambers               | Spin           | \\( \frac{1}{3} \\)         |
| Two Bullets in Consecutive Chambers          | Don't Spin     | \\( \frac{1}{4} \\)         |

## Reference

* [1] [In Russian roulette, is it best to go first?](https://math.stackexchange.com/questions/96331)
