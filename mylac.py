from LAC import LAC
def mylac(cache_title_list):
    for i in cache_title_list:
        i = i.encode("unicode_escape")
    # print(cache_title_list)


    # 装载LAC模型
    lac = LAC(mode='lac')

    # 批量样本输入, 输入为多个句子组成的list，平均速率更快

    lac_result = lac.run(cache_title_list)
    # print(lac_result)

    org = []
    loc = []
    per = []
    n = []

    print("机构相关关键词：")
    for i in lac_result:
        for j in i[1]:
            if j == 'ORG':
                org.append(i[0][i[1].index(j)] + "\n")
    neworg = set(org)
    print(neworg)

    print("地点相关关键词：")
    for i in lac_result:
        for j in i[1]:
            if j == 'LOC':
                loc.append(i[0][i[1].index(j)] + "\n")
    newloc = set(loc)
    print(newloc)

    print("人物相关关键词：")
    for i in lac_result:
        for j in i[1]:
            if j == 'PER':
                per.append(i[0][i[1].index(j)] + "\n")
    newper = set(per)
    print(newper)

    print("相关名词：")
    for i in lac_result:
        for j in i[1]:
            if j == 'n':
                n.append(i[0][i[1].index(j)] + "\n")
    newn = set(n)
    print(newn)
    text = "机构相关关键词：\n"+str(neworg)+"\n"+"地点相关关键词：\n"+str(newloc)+"\n"+"人物相关关键词：\n"+str(newper)+"\n"+"相关名词：\n"+str(newn)
    return text