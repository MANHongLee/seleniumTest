import time
import random

"""
获取随机手机号码
"""


def get_mobile_number():
    mobiles = ['130', '131', '132', '133', '134']
    number = str(int(time.time()))[2:]
    mobile = random.choice(mobiles) + number
    return mobile

