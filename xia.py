def greet(name: str) -> str:
    return f"Hello, {name}! 欢迎来到我的第一个 GitHub 项目 🎉"

if __name__ == "__main__":
    user_name = input("请输入你的名字：")
    print(greet(user_name))