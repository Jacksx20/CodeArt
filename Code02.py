from time import sleep
from colorama import Fore, init
import random

init(autoreset=True)

class CodePoet:
    def __init__(self):
        # 定义一个颜色列表，用于随机选择颜色
        self.palette = [Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.WHITE]
        # 定义一个延迟时间列表，用于随机选择延迟时间
        self.delays = [0.08, 0.12, 0.15]
        self.lines = [
            ("λ 数字游牧人 | 代码炼金师", 0.5),
            ("├─ 解构现实于逻辑晶格", 0.3),
            ("├─ 编织诗意于算法经纬", 0.3),
            ("└─ 在混沌中雕刻秩序的递归之美", 0.6),
            ("", 0.2),
            ("⚙️ 技术圣殿：", 0.4),
            ("  ・Python → 思想的微分方程", 0.3),
            ("  ・JavaScript → 异步宇宙的量子纠缠", 0.3),
            ("  ・Rust → 记忆体炼狱的救赎", 0.3),
            ("", 0.2),
            ("🌌 信仰真言：", 0.4),
            ("  「while(!succeed) { tryAgain() }」", 0.8)
        ]

    # 定义一个函数，用于为文本添加随机颜色
    def chromatic_flow(self, text):
        # 为文本中的每个字符随机添加颜色
        return [random.choice(self.palette) + char for char in text]

    def holographic_print(self):
        for text, pause in self.lines:
            if not text:
                sleep(pause)
                continue
            
            colored_chars = self.chromatic_flow(text)
            for i in range(len(colored_chars)):
                print('\r' + ''.join(colored_chars[:i+1]), end='', flush=True)
                sleep(random.choice(self.delays))
            sleep(pause)
            print()

if __name__ == "__main__":
    poet = CodePoet()
    poet.holographic_print()