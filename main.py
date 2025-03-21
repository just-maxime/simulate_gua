# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 12:12:09 2024

@author: maxim
"""
import random

# 定义卦辞
qian_gua = "乾卦：元亨利贞。"                        # 1
kun_gua = "坤卦：元亨，利牝马之贞。"                 # 2
zhun_gua = "屯卦：元亨，利贞。勿用，有攸往，利建侯。"
meng_gua = "蒙卦："
xu_gua = "需卦"
song_gua = "讼卦"
shi_gua = "师卦"
bi_gua = "比卦"
xiaoxu_gua = "小畜卦"
lv_gua = "履卦"
tai_gua = "泰卦"
pi_gua = "否卦"
tongren_gua = "同人卦"
dayou_gua = "大有卦"
qian_gua = "谦卦"
yu_gua = "豫卦"
sui_gua = "随卦"
gu_gua = "蛊卦"
lin_gua = "临卦"
guan_gua = "观卦"
shike_gua = "噬磕卦"
bi_gua = "贲卦"
bo_gua = "剥卦"
fu_gua = "复卦"
wuwang_gua = "无妄卦"
dachu_gua = "大畜卦"
yi_gua = "颐卦"
daguo_gua = "大过卦"
kan_gua = "坎卦"
li_gua = "离卦"
xian_gua = "咸卦"
heng_gua = "恒卦"
dun_gua = "遁卦"
dazhuang_gua = "大壮卦"
jin_gua = "晋卦"
mingyi_gua = "明夷卦"
jiaren_gua = "家人卦"
kui_gua = "睽卦"
jian_gua = "蹇卦"
jie_gua = "解卦"
sun_gua = "损卦"
yi_gua = "益卦"
guai_gua = "夬卦"
gou_gua = "姤卦"
cui_gua = "萃卦"
sheng_gua = "升卦"
kun_gua = "困卦"
jing_gua = "井卦"
ge_gua = "革卦"
ding_gua = "鼎卦"
zhen_gua = "震卦"
gen_gua = "艮卦"
jian_gua = "渐卦"
guimei_gua = "归妹卦"
feng_gua = "丰卦"
lv_gua = "旅卦"
xun_gua = "巽卦"
dui_gua = "兑卦"
huan_gua = "涣卦"
jie_gua = "节卦"
zhongfu_gua = "中孚卦"
xiaoguo_gua = "小过卦"
jiji_gua = "既济卦"
weiji_gua = "未济卦"

def generate_gua():
    """
    模拟蓍草起卦，返回剩原始卦象和变卦的结果

    Returns:
      list: original_gua, bian_gua
    """
    # 初始化卦象
    original_gua_num = []
    bian_gua_num = []
    original_gua = [] # 原始卦象
    bian_gua = []     # 变卦
    

    for _ in range(6): #六变生卦
        num = 49 # 初始化蓍草的数量
        for __ in range(3): # 三变生爻
            # 变
            num1 = random.randint(1, num) # num1∈[1, num]
            num2 = num - num1 - 1
            
            remainder1 = num1 % 4
            if remainder1 == 0:
                num1 = num1 - 4
            else:
                num1 = num1 - remainder1
                
            remainder2 = num2 % 4
            if remainder2 == 0:
                num2 = num2 - 4
            else:
                num2 = num2 - remainder2
                
            num = num1 + num2

        original_gua_num.append(num/4)
        
        if (num/4) == 6.0: # 变卦
            bian_gua_num.append(7.0)
        elif (num/4) == 9.0:
            bian_gua_num.append(8.0)
        else:
            bian_gua_num.append(num/4)
            
    for i in original_gua_num: # 0: 阴爻； 1：阳爻
        if i == 6.0:
            original_gua.append(0)
        elif i == 7.0:
            original_gua.append(1)
        elif i == 8.0:
            original_gua.append(0)
        elif i == 9.0:
            original_gua.append(1)
        else:
            print('error')
    
    for i in bian_gua_num: # 0: 阴爻； 1：阳爻
        if i == 7.0:
            bian_gua.append(1)
        elif i == 8.0:
            bian_gua.append(0)
        else:
            print('error')
            
    return original_gua[::-1], bian_gua[::-1]

# 定义函数：根据卦象查找卦辞
def find_gua_ci(gua):
    """
    根据卦象查找卦辞

    Args:
      gua: 卦象，一个包含六个爻的列表

    Returns:
      str: 对应的卦辞
    """
    # 此处需要根据实际的卦象和卦辞进行匹配
    if gua == [1,1,1,1,1,1]:
        return qian_gua
    elif gua == [0,0,0,0,0,0]:
        return kun_gua
    elif gua == [0,1,0,0,0,1]:
        return zhun_gua 
    elif gua == [1,0,0,0,1,0]:
        return meng_gua 
    elif gua == [0,1,0,1,1,1]:
        return xu_gua 
    elif gua == [1,1,1,0,1,0]:
        return song_gua 
    elif gua == [0,0,0,0,1,0]:
        return shi_gua 
    elif gua == [0,1,0,0,0,0]:
        return bi_gua 
    elif gua == [1,1,0,1,1,1]:
        return xiaoxu_gua 
    elif gua == [1,1,1,0,1,1]:
        return lv_gua 
    elif gua == [0,0,0,1,1,1]:
        return tai_gua 
    elif gua == [1,1,1,0,0,0]:
        return pi_gua 
    elif gua == [1,1,1,1,0,1]:
        return tongren_gua 
    elif gua == [1,0,1,1,1,1]:
        return dayou_gua 
    elif gua == [0,0,0,1,0,0]:
        return qian_gua 
    elif gua == [0,0,1,0,0,0]:
        return yu_gua 
    elif gua == [0,1,1,0,0,1]:
        return sui_gua 
    elif gua == [1,0,0,1,1,0]:
        return gu_gua 
    elif gua == [0,0,0,0,1,1]:
        return lin_gua 
    elif gua == [1,1,0,0,0,0]:
        return guan_gua 
    elif gua == [1,0,1,0,0,1]:
        return shike_gua 
    elif gua == [1,0,0,1,0,1]:
        return bi_gua 
    elif gua == [1,0,0,0,0,0]:
        return bo_gua 
    elif gua == [0,0,0,0,0,1]:
        return fu_gua 
    elif gua == [1,1,1,0,0,1]:
        return wuwang_gua 
    elif gua == [1,0,0,1,1,1]:
        return dachu_gua 
    elif gua == [1,0,0,0,0,1]:
        return yi_gua 
    elif gua == [0,1,1,1,1,0]:
        return daguo_gua 
    elif gua == [0,1,0,0,1,0]:
        return kan_gua 
    elif gua == [1,0,1,1,0,1]:
        return li_gua 
    elif gua == [0,1,1,1,0,0]:
        return xian_gua 
    elif gua == [0,0,1,1,1,0]:
        return heng_gua 
    elif gua == [1,1,1,1,0,0]:
        return dun_gua 
    elif gua == [1,1,0,0,0,0]:
        return dazhuang_gua 
    elif gua == [1,0,1,0,0,0]:
        return jin_gua 
    elif gua == [0,0,0,1,0,1]:
        return mingyi_gua 
    elif gua == [1,1,0,1,0,1]:
        return jiaren_gua 
    elif gua == [1,0,1,0,1,1]:
        return kui_gua 
    elif gua == [0,1,0,1,0,0]:
        return jian_gua 
    elif gua == [0,0,1,0,1,0]:
        return jie_gua 
    elif gua == [1,0,0,0,1,1]:
        return sun_gua 
    elif gua == [1,1,0,0,0,1]:
        return yi_gua 
    elif gua == [0,1,1,1,1,1]:
        return guai_gua 
    elif gua == [1,1,1,1,1,0]:
        return gou_gua 
    elif gua == [0,1,1,0,0,0]:
        return cui_gua 
    elif gua == [0,0,0,1,1,0]:
        return sheng_gua 
    elif gua == [0,1,1,0,1,0]:
        return kun_gua 
    elif gua == [0,1,0,1,1,0]:
        return jing_gua 
    elif gua == [0,1,1,1,0,1]:
        return ge_gua 
    elif gua == [1,0,1,1,1,0]:
        return ding_gua 
    elif gua == [0,0,1,0,0,1]:
        return zhen_gua 
    elif gua == [1,0,0,1,0,0]:
        return gen_gua 
    elif gua == [1,1,0,1,0,0]:
        return jian_gua 
    elif gua == [0,0,1,0,1,1]:
        return guimei_gua 
    elif gua == [0,0,1,1,0,1]:
        return feng_gua 
    elif gua == [1,0,1,1,0,0]:
        return lv_gua 
    elif gua == [1,1,0,1,1,0]:
        return xun_gua 
    elif gua == [0,1,1,0,1,1]:
        return dui_gua 
    elif gua == [1,1,0,0,1,0]:
        return huan_gua 
    elif gua == [0,1,0,0,1,1]:
        return jie_gua 
    elif gua == [1,1,0,0,1,1]:
        return zhongfu_gua 
    elif gua == [0,0,1,1,0,0]:
        return xiaoguo_gua 
    elif gua == [0,1,0,0,1,0]:
        return jiji_gua 
    elif gua == [1,0,1,1,0,1]:
        return weiji_gua 
    else:
      return "error"
  

def print_gua(gua):
    for i in gua:
        if i == 1:
            print('---')
        elif i ==0:
            print('- -')
        else:
            print('error')



if __name__ == "__main__":
    print("开始起卦...")
    original_gua, bian_gua = generate_gua()
    
    print("原始卦象：")
    print_gua(original_gua)
    print("原始卦词：")
    print(find_gua_ci(original_gua))


    print("\n变卦卦象：")
    print_gua(bian_gua)
    print("变卦卦词：")
    print(find_gua_ci(bian_gua))