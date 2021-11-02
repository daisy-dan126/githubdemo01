# -*- coding: utf-8 -*-
# author：风变编程--谢丹老师(微信：18589040835)
# 创建于： 2020/9/9 5:24 PM

import random#随机模块
import time


def waiting():
    #制造等待效果
    for i in range(3):
        time.sleep(1)
        print('·')


FORTUNE_POOL = ('','','','','')
waiting()

play = input('抽奖即将开始')
waiting()

print('参与抽奖的同学名字为：')
time.sleep(1)

print(FORTUNE_POOL)
waiting()

print('参与抽奖的总人数为{}'.format(len(FORTUNE_POOL)))
time.sleep(1)

print('现在开始抽奖')
waiting()


def delay_print(content, delay=0.5):
    # 延迟输出
    time.sleep(delay)
    print(content)


# 开头
delay_print('让我们康康丹丹老师抽取的幸运儿')
waiting()


# 抽签过程
delay_print('感谢风变编程让我们相遇', delay=2)
time.sleep(1)
delay_print('让我们倒数3秒')
waiting()

# 抽签
fortune = random.choice(FORTUNE_POOL)

# 抽签结果
delay_print('boom~幸运儿已经诞生!他/她的名字是【{fortune}】。'.format(fortune=fortune))
time.sleep(2)
print('恭喜【{fortune}】同学免费获得领取代码的资格！！'.format(fortune=fortune))
time.sleep(5)