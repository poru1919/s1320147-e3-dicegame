import random

# ユーザーに名前を尋ねる
name = input("What is your name?\n> ")
print(f"Hello, {name}!")

print("Rolling dice...")

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

print(f"Die 1: {die1}")
print(f"Die 2: {die2}")
print(f"Total value: {total}")

# 勝敗メッセージを追加
if total > 7:
    print("You won")
else:
    print("You lost")