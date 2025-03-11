import random

memberDict = {
    1: '海因', 
    2: '喬伊', 
    3: '西斯', 
    4: '特麗莎',
    5: '鏈鋸',
    6: '阿札爾', 
    7: '莉安', 
    8: '鳳凰',
    9: '普媽', 
    10: '盾哥',
    11: '卡倫', 
    12: '槍哥', 
    13: '卉子', 
    14 and 15: '雙子', 
    16: '納爾汗', 
    17: '約翰',
    18: '伊利亞',
    19: '蕾琳',
    20: '桃梨',
    21: '羅蘭'
}

random_member = random.choice(list(memberDict.values()))
print(random_member)