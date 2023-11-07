import random

# 题目:
# 给定一个 0-4 随机数生成器 如何生成 0-6 随机数
import random

def rand4():
  return random.randint(0, 4)

def rand6():
  while True:
    num = rand4() * 5 + rand4()
    if num <= 20:
      return num % 7

result = [0] * 7
for i in range(50000):
  r = rand6()
  result[r] += 1

for i in range(len(result)):
  print("num:", i, "times:", result[i])