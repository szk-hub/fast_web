def judge(black_list, white_list):
    
    # 数值颜色分离
    black_number = []
    black_color = []
    white_number = []
    white_color = []
    for i in black_list:
        a = list(i)
        black_number.append(a[0])
        black_color.append(a[1])
    for j in white_list:
        b = list(j)
        white_number.append(b[0])
        white_color.append(b[1])

    # 替换数字字符为数字10,11....
    rep = {'T':'10','J':'11','Q':'12','K':'13','A':'14'}
    temp1 = [rep[i] if i in rep else i for i in black_number]
    temp2 = [rep[j] if j in rep else j for j in white_number]
    black_number = [int(i) for i in temp1]
    white_number = [int(j) for j in temp2]
    black_number.sort()
    white_number.sort()

    blnu_com = {}
    whnu_com = {}
    wt = bt = 0
    wd = bd = 0
    bs = ws = 0 
    bt = wt = 0
    wsp = bsp = 0
    wsp_flag = bsp_flag = wdz_flag = bdz_flag = wsz_flag = bsz_flag = 0
    wtz_flag = btz_flag = whl_flag = bhl_flag = wth_flag = bth_flag = 0
    wld_flag = bld_flag = wsp_flag = bsp_flag = wst_flag = bst_flag = 0
    # 条件判断
    # 统计相同数值情况
    for i in black_number:
        if black_number.count(i) >= 2:
            blnu_com[i] = black_number.count(i)
        else:
            bsp += 1
    for j in white_number:
        if white_number.count(j) >= 2:
            whnu_com[j] = white_number.count(j)
        else:
            wsp += 1 
    for i in blnu_com:
        if i == 2:
            bd += 1
        if i == 3:
            bs += 1
        if i == 4:
            bt += 1
    for j in whnu_com:
        if j == 2:
            wd += 1
        if j == 3:
            ws += 1
        if j == 4:
            wt = 1 
    # 顺子
    if wsp == 5 and bsp == 5:  
        if (black_number[4] - black_number[0]) == 4:
            bsz_flag = 1
        else: bsp_flag = 1
        if (white_number[4] - white_number[0]) == 4:
            wsz_flag = 1
        else: wsp_flag = 1

    # 同花
    for i in black_color:
        if black_color.count(i) == 5:
            bt += 1
    for j in white_color:
        if white_color.count(j) == 5:
            wt += 1
    if bt == 5:
        bth_flag = 1
    if wt == 5:
        wth_flag = 1

    # 对子            
    if bd == 2 and bs != 3:
        bdz_flag = 1      
    if wd == 2 and ws != 3:
        wdz_flag = 1

    # 两对
    if bd == 4:
        bld_flag = 1
    if wd == 4:
        wld_flag = 1
 
    # 三条  葫芦  三条+对子。 比较三张大小一样的牌的牌点数。
    if bs == 3:
        if bd == 2:    
            bhl_flag =1
        else:
            bst_flag = 1      
    if ws == 3:
        if wd == 2:
            whl_flag = 1
        else:
            wst_flag = 1

    # 铁支  有四张同样大小的牌片。 比较四张大小一样的牌的牌点数。
    if bt == 4:
        btz_flag = 1
    if wt == 4:
        wtz_flag = 1
    
    # 散牌大小
    if bth_flag != 1 and wth_flag != 1:
        if bsp_flag == 1 and wsp_flag == 1:
            if black_number[4] > white_number[4]:
                return "Black Wins"
            elif black_number[4] == white_number[4]:
                if black_number[3] > white_number[3]:
                    return "Black Wins"
                elif black_number[3] == white_number[3]:
                    if black_number[2] > white_number[2]:
                        return "Black Wins"
                    elif black_number[2] == white_number[2]:
                        if black_number[1] > white_number[1]:
                            return "Black Wins"
                        elif black_number[1] == white_number[1]:
                            return "Tie" 
                        else: return "White Wins"
                    else: return "White Wins"
                else: return "White Wins"
            else: return "White Wins"              
        
    #同花散排 同花顺大小
    if bth_flag == 1 and wth_flag == 1:
        if bsz_flag == 1 and wsz_flag == 1:
            if black_number[4] > white_number[4]:
                return "Black Wins"
            elif black_number[4] == white_number[4]:
                return "Tie" 
            else:
                return "White Wins"
        if bsp_flag == 1 and wsp_flag == 1:
            if black_number[4] > white_number[4]:
                return "Black Wins"
            elif black_number[4] == white_number[4]:
                if black_number[3] > white_number[3]:
                    return "Black Wins"
                elif black_number[3] == white_number[3]:
                    if black_number[2] > white_number[2]:
                        return "Black Wins"
                    elif black_number[2] == white_number[2]:
                        if black_number[1] > white_number[1]:
                            return "Black Wins"
                        elif black_number[1] == white_number[1]:
                            return "Tie" 
                        else: return "White Wins"
                    else: return "White Wins"
                else: return "White Wins"
            else: return "White Wins"           

    # 铁支大小
    if btz_flag == 1 and wtz_flag == 1:
        if get_keys(blnu_com, 4) > get_keys(whnu_com, 4):
            return "Black Wins"
        elif get_keys(blnu_com, 4) == get_keys(whnu_com, 4):
            return "Tie"
        else:
            return "White Wins"
    
    # 三条 葫芦大小 都只看三条
    if bst_flag == 1 and wst_flag == 1:
        #if bdz_flag == 1 and wdz_flag == 1:
        if get_keys(blnu_com, 3) > get_keys(whnu_com, 3):
            return "Black Wins"
        elif get_keys(blnu_com, 3) == get_keys(whnu_com, 3):
            return "Tie"
        else:
            return "White Win"

    # 对子 大小
    if bdz_flag  == 1 and wdz_flag == 1 and wst_flag != 1 and bst_flag != 1:
        if get_keys(blnu_com, 2) > get_keys(whnu_com, 2):
            return "Black Wins"
        elif get_keys(blnu_com, 2) == get_keys(whnu_com, 2):
            return "Tie"
        else:
            return "White Win"
    # 两对 大小       
    if bld_flag == 1 and wld_flag == 1:
        if get_keys(blnu_com, 2)[1] > get_keys(whnu_com, 2)[1]:
            return "Black Wins"
        elif get_keys(blnu_com, 2)[1] == get_keys(whnu_com, 2)[1]:
            if get_keys(blnu_com, 2)[0] > get_keys(whnu_com, 2)[0]:
                return "Black Wins"
            elif get_keys(blnu_com, 2)[0] == get_keys(whnu_com, 2)[0]:
                return "Tie"
            else: return "White Wins"
        else: return "White Wins"
        

    # 同花顺与其他
    if (bth_flag + bsz_flag) == 2 and (wth_flag + wsz_flag != 2):
        return "Black Wins"
    if (bth_flag + bsz_flag) != 2 and (wth_flag + wsz_flag == 2):
        return "White Wins"

    # 铁支与其他(除同花顺)
    if (bth_flag + bsz_flag) != 2 and (wth_flag + wsz_flag) != 2:
        if btz_flag == 1 and wtz_flag != 1:
            return "Black Wins"
        if btz_flag != 1 and wtz_flag == 1:
            return "White Wins"
        if btz_flag != 1 and wtz_flag != 1:
                if bhl_flag == 1 and whl_flag != 1:
                    return "Black Wins"
                if bhl_flag != 1 and whl_flag == 1:
                    return "White Wins"
                if bhl_flag != 1 and whl_flag != 1:
                    if bth_flag == 1 and wth_flag != 1:
                        return "Black Wins"
                    if bth_flag != 1 and wth_flag == 1:
                        return "White Wins"
                    if bth_flag != 1 and wth_flag != 1:
                        if bsz_flag == 1 and wsz_flag != 1:
                            return "Black Wins"
                        if bsz_flag != 1 and wsz_flag == 1:
                            return "White Wins"
                        if bsz_flag != 1 and wsz_flag != 1:
                            if bst_flag == 1 and wst_flag != 1:
                                return "Black Wins"
                            if bst_flag != 1 and wst_flag == 1:
                                return "White Wins"
                            if bst_flag != 1 and wst_flag != 1:
                                if bld_flag == 1 and wld_flag != 1:
                                    return "Black Wins" 
                                if bld_flag != 1 and wld_flag == 1:
                                    return "White Wins" 
                                if bld_flag != 1 and wld_flag != 1:
                                    if bdz_flag == 1 and wdz_flag != 1:
                                        return "Black Wins"
                                    if bdz_flag != 1 and wdz_flag == 1:
                                        return "White Wins"

# 获取key
def get_keys(count, value):

    return [k for k,v in count.items() if v == value]

if __name__ == '__main__':

    black_list = []
    white_list = []
    for i in range(0,5):
        print("输入black方手牌")
        black_list.append(input())
    for j in range(0,5):
        print("输入white方手牌")
        white_list.append(input())

    print(judge(black_list, white_list))
    