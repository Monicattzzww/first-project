import random

def greet(name: str) -> str:
    emojis = ["🎉", "✨", "🚀", "💖", "🌟"]
    messages = [
        f"Hello, {name}! 欢迎来到我的第一个 GitHub 项目 {random.choice(emojis)}",
        f"Hi {name}! 今天也要开心写代码 {random.choice(emojis)}",
        f"Hey {name}! 你超棒的，继续加油 {random.choice(emojis)}"
    ]
    return random.choice(messages)

if __name__ == "__main__":
    user_name = input("请输入你的名字：")
    print(greet(user_name))