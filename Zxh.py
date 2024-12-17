import random

# 生成一个1到100之间的随机数作为答案
answer = random.randint(1, 100)
# 记录猜测次数
guess_count = 0
# 标记是否猜对
guessed = False

print("欢迎来到猜数字游戏，我已经想好了一个1到100之间的数字，你来猜猜看哦！")

while not guessed:
    try:
        # 获取用户输入的猜测数字
        user_guess = int(input("请输入你猜测的数字："))
        guess_count += 1
        if user_guess == answer:
            guessed = True
            print(f"恭喜你，猜对啦！你一共猜了{guess_count}次。")
        elif user_guess < answer:
            print("猜小了哦，再试试吧。")
        else:
            print("猜大了哦，再猜猜看呀。")
    except ValueError:
        print("请输入有效的整数哦，再试一次吧。")