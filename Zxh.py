import random


def play_game():
    """
    进行一次猜数字游戏的函数
    """
    # 生成一个1到100之间的随机数作为答案
    answer = random.randint(1, 100)
    # 记录猜测次数
    guess_count = 0
    # 标记是否猜对
    guessed = False
    # 用于存储玩家的历史猜测记录
    guess_history = []

    print("欢迎来到猜数字游戏，我已经想好了一个1到100之间的数字，你来猜猜看哦！")

    while not guessed:
        try:
            # 获取用户输入的猜测数字
            user_guess = int(input("请输入一个1到100之间的整数作为你猜测的数字："))
            # 判断输入数字是否在合理范围
            if user_guess < 1 or user_guess > 100:
                print("你输入的数字超出了1到100这个范围呀，请重新输入哦。")
                continue
            guess_count += 1
            guess_history.append(user_guess)
            if user_guess == answer:
                guessed = True
                print(f"恭喜你，猜对啦！你一共猜了{guess_count}次。")
                print("你的历史猜测记录如下：")
                for index, num in enumerate(guess_history, start=1):
                    print(f"第{index}次猜测：{num}")
            elif user_guess < answer:
                print("猜小了哦，再试试吧。")
            else:
                print("猜大了哦，再猜猜看呀。")
        except ValueError:
            print("请输入有效的整数哦，再试一次吧。")


while True:
    play_game()
    # 询问玩家是否继续游戏
    choice = input("是否想再玩一次游戏呢？（输入yes继续，其他任意内容则退出游戏）")
    if choice.lower()!= "yes":
        print("感谢你玩猜数字游戏，下次再见啦！")
        break
    
