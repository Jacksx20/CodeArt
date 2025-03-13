from time import sleep
from colorama import Fore, Style, init
import random

init(autoreset=True)

class StellarCartographer:
    def __init__(self):
        self.star_palette = [Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
        self.nova_speed = [0.06, 0.12, 0.18]
        self.celestial_manifest = [
            (f"{Style.BRIGHT}◈ 二进制星云的漫游者", 0.8),
            ("│", 0.2),
            ("├ 用变量编织星座图谱", 0.4),
            ("├ 在内存深渊打捞失落的情感", 0.4),
            ("└ 将递归函数锻造成时空罗盘", 0.6),
            ("", 0.3),
            (f"{Style.DIM}🜨 技术星域：", 0.5),
            ("  ∞ Python —— 星辰的语法糖", 0.3),
            ("  ∞ TypeScript —— 类型论的占星术", 0.3),
            ("  ∞ Rust —— 超新星纪元的内存契约", 0.3),
            ("", 0.3),
            (f"{Style.BRIGHT}♅ 灵魂终端：", 0.5),
            ("  while(existence):", 0.4),
            ("      explore(universe)", 0.8)
        ]
        self.epilogue = [
            "我是一名穿梭于0和1之间的旅者，",
            "在代码的宇宙里探索未知的星辰。",
            "像一个孤独的诗人，用变量谱写情感的诗篇，",
            "每一个函数都是一段精心雕琢的故事，",
            "每一行注释都是内心深处的旁白。",
            "我，用逻辑构建梦想的城堡，",
            "用算法解开生活的谜题。"
        ]

    def quasar_typewriter(self, text):
        return [random.choice(self.star_palette) + char for char in text]

    def event_horizon_effect(self):
        for line, pause in self.celestial_manifest:
            if not line:
                sleep(pause)
                print()
                continue
            
            stardust = self.quasar_typewriter(line)
            for i in range(len(stardust)):
                print('\r' + ''.join(stardust[:i+1]), end='', flush=True)
                sleep(self.nova_speed[i%3] * random.uniform(0.8, 1.2))
            sleep(pause)
            print()
        
        print(f"\n{Fore.YELLOW}{Style.DIM}※ 星间絮语 ※")
        for verse in self.epilogue:
            print(f"{Fore.WHITE}{verse}")
            sleep(0.5)

if __name__ == "__main__":
    voyager = StellarCartographer()
    voyager.event_horizon_effect()