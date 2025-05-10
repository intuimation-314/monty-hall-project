# 🧠 Monty Hall Simulation (C++)

A terminal-based simulation of the Monty Hall problem — play interactively, simulate thousands of trials, and view win/loss stats. Supports any number of doors!

---

## 🎯 What is the Monty Hall Problem?

> You're shown multiple doors. One hides a **car 🚗**, others hide **goats 🐐**.  
> You pick one. Monty opens all but one goat door. Do you switch?

Statistically, **switching gives you a better chance** of winning.  
This program helps you test and see it yourself!

---

## 🛠 Features

- ✅ Play interactively (3 or more doors)
- ✅ Run simulations (e.g., 1000 trials)
- ✅ Visual door layout in console
- ✅ Game outcomes saved to `game_stats.txt`
- ✅ View full game history

---

## 🗂 File & Function Structure
For a full breakdown of all files and internal functions/classes, see [monty_hall_tree.txt](./monty_hall_tree.txt).

---

## 🚀 How to Compile

```bash
g++ main.cpp monty_hall.cpp -o monty
./monty       # or monty.exe on Windows
