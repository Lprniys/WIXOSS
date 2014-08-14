# -*- coding: utf-8 -*-  

'''
Created on 2014年7月19日

@author: SynTuner
'''

class LifeBurst():
    def __init__(self):
        self.name = "LB"
    
    def WX01_001(self, card): #太阳之巫女 玉依姬
        mute()
        
    def WX01_002(self, card): #晓之巫女 玉依姬
        mute()
        
    def WX01_003(self, card): #百火缭乱 花代•肆
        mute()
        
    def WX01_004(self, card): #轰炎 花代•贰改
        mute()
        
    def WX01_005(self, card): #代号 皮璐璐可•Ω
        mute()
        
    def WX01_006(self, card): #四式战帝女 绿姬
        mute()
        
    def WX01_007(self, card): #月蚀之巫女 玉依姬
        mute()
        
    def WX01_008(self, card): #流星之巫女 玉依姬
        mute()
        
    def WX01_009(self, card): #新星之巫女 玉依姬
        mute()
        
    def WX01_010(self, card): #杰诺之门
        mute()
        
    def WX01_011(self, card): #炽炎舞 花代•叁
        mute()
        
    def WX01_012(self, card): #刚炎 花代•贰
        mute()
        
    def WX01_013(self, card): #焰 花代•壹
        mute()
        
    def WX01_014(self, card): #烈霸一络
        mute()
        
    def WX01_015(self, card): #代号 皮璐璐可•Γ
        mute()
        
    def WX01_016(self, card): #代号 皮璐璐可•Β
        mute()
        
    def WX01_017(self, card): #代号 皮璐璐可•Α
        mute()
        
    def WX01_018(self, card): #魔法反制
        mute()
        
    def WX01_019(self, card): #四型皇艳娘 绿姬
        mute()
        
    def WX01_020(self, card): #三型雌雌娘 绿姬
        mute()
        
    def WX01_021(self, card): #二型斗婚娘 绿姬
        mute()
        
    def WX01_022(self, card): #一型舞斗娘 绿姬
        mute()
        
    def WX01_023(self, card): #大器晚成
        mute()
        
    def WX01_024(self, card): #奇奇怪怪
        mute()
        
    def WX01_025(self, card): #营救
        mute()
        
    def WX01_026(self, card): #充能
        mute()
        
    def WX01_027(self, card): #原枪 源能枪
        mute()
        conditionSearch("主卡组", 1, [], ["白"], None, None, None, None, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX01_028(self, card): #弧光圣气
        mute()
        getOppoLrig()
        list = [c for c in table 
                if c.controller == players[1]
                and (isInSigni(c) or c == oppoLrig) 
                and c.orientation == 0]
        for l in list:
            remoteCall(players[1], "down", [l])
        
    def WX01_029(self, card): #罗辉石 金刚珠玉
        mute()
        conditionBan(card, 1, players[1], -1, 10000, -1, 10, None, None)
        
    def WX01_030(self, card): #赎罪之对火
        mute()
        Life = [l for l in table 
                if isInLife(l)]
        if not Life:
            return False
        indexlist = []
        for l in Life:
            indexlist.append(l.getIndex)
        o = max(indexlist)
        for l in Life:
            if l.getIndex == o:
                outmost = l
        outmost.moveTo(me.piles["废弃区"])
        remoteCall(players[1], "crash", [1])
        
    def WX01_031(self, card): #核心代号 V•A•C
        mute()
        remoteCall(players[1], "chooseDiscard", [])
        
    def WX01_032(self, card): #抢夺
        mute()
        remoteCall(players[1], "randomDiscard", [])
        
    def WX01_033(self, card): #幻兽神 御先狐
        mute()
        fromDeckSend("能量区", 2)
        
    def WX01_034(self, card): #修复
        mute()
        fromDeckSend("生命护甲", 1)
        
    def WX01_035(self, card): #祝福女神 雅典娜
        mute()
        
    def WX01_036(self, card): #巨弓 抛射弓
        mute()
        conditionSearch("主卡组", 1, ["SIGNI"], [], 4, 4, -1, 99999, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX01_037(self, card): #无法忘却的幻想 瓦尔基里
        mute()
        
    def WX01_038(self, card): #获得但他林
        mute()
        
    def WX01_039(self, card): #弩炮 加农炮
        mute()
        
    def WX01_040(self, card): #罗石 山铜
        mute()
        conditionBan(card, 1, players[1], -1, 5000, -1, 10, None, None)
        
    def WX01_041(self, card): #轰炮 法典炮
        mute()
        
    def WX01_042(self, card): #断罪之轹断
        mute()
        
    def WX01_043(self, card): #幻水 雅莱娅尔
        mute()
        
    def WX01_044(self, card): #技艺代号 P•Z•L
        mute()
        
    def WX01_045(self, card): #幻水 夏克兰丝
        mute()
        
    def WX01_046(self, card): #情况糟糕
        mute()
        
    def WX01_047(self, card): #罗植 曼茶罗花
        mute()
        
    def WX01_048(self, card): #幻兽 雪怪
        mute()
        fromDeckSend("能量区", 1)
        
    def WX01_049(self, card): #罗植 植生羊
        mute()
        
    def WX01_050(self, card): #大化
        mute()
        
    def WX01_051(self, card): #侍从Q
        mute()
        fromDeckSend("能量区", 1)
        
    def WX01_052(self, card): #包括的知识
        mute()
        fromDeckSend("能量区", 1)
        
    def WX01_053(self, card): #极剑 噬神剑
        mute()
        
    def WX01_054(self, card): #极盾 埃奎斯盾
        mute()
        
    def WX01_055(self, card): #大盾 镇暴盾
        mute()
        
    def WX01_056(self, card): #中盾 方盾
        mute()
        
    def WX01_057(self, card): #出弓 炽天弓
        mute()
        genDraw(1)
        
    def WX01_058(self, card): #重新开始的对话 米迦勒
        mute()
        
    def WX01_059(self, card): #出弓 普弓
        mute()
        genDraw(1)
        
    def WX01_060(self, card): #小盾 圆盾
        mute()
        
    def WX01_061(self, card): #探求的思想 汉尼尔
        mute()
        
    def WX01_062(self, card): #将之开启
        mute()
        
    def WX01_063(self, card): #做好准备
        mute()
        conditionSearch("主卡组", 1, ["SIGNI"], [], -1, 10, -1, 99999, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX01_064(self, card): #罗石 金属
        mute()
        
    def WX01_065(self, card): #罗石 绿宝石
        mute()
        
    def WX01_066(self, card): #罗石 红宝石
        mute()
        
    def WX01_067(self, card): #罗石 磷矿石
        mute()
        genDraw(1)
        
    def WX01_068(self, card): #罗石 琥珀
        mute()
        
    def WX01_069(self, card): #爆炮 远射炮
        mute()
        
    def WX01_070(self, card): #罗石 海人草
        mute()
        genDraw(1)
        
    def WX01_071(self, card): #罗石 蓝宝石
        mute()
        
    def WX01_072(self, card): #小炮 德拉古诺夫枪
        mute()
        
    def WX01_073(self, card): #落星炎球
        mute()
        conditionBan(card, 1, players[1], -1, 10000, -1, 10, None, None)
        
    def WX01_074(self, card): #棱晶火柱
        mute()
        
    def WX01_075(self, card): #技艺代号 A•S•M
        mute()
        
    def WX01_076(self, card): #技艺代号 I•D•O•L
        mute()
        
    def WX01_077(self, card): #技艺代号 A•D•B
        mute()
        
    def WX01_078(self, card): #技艺代号 S•T•G
        mute()
        
    def WX01_079(self, card): #技艺代号 W•T•C
        mute()
        genDraw(1)
        
    def WX01_080(self, card): #幻水 夏可檀
        mute()
        
    def WX01_081(self, card): #技艺代号 T•V
        mute()
        genDraw(1)
        
    def WX01_082(self, card): #技艺代号 F•A•N
        mute()
        
    def WX01_083(self, card): #幻水 克马诺明
        mute()
        
    def WX01_084(self, card): #事不过三
        mute()
        
    def WX01_085(self, card): #冰封
        mute()
        list = [c for c in table
                if c.controller == players[1]
                and isInSigni(c)]
        s = card
        selected = []
        for i in range(2):
            s = askCard(list)
            if s != None:
                selected.append(s)
            else:
                break
        for signi in selected:
            remoteCall(players[1], "down", [signi])
            remoteCall(players[1], "freeze", [signi, 0, 0])
            
        
    def WX01_086(self, card): #幻兽 飞鹰
        mute()
        
    def WX01_087(self, card): #幻兽 猫妖精
        mute()
        
    def WX01_088(self, card): #幻兽 猫头鹰
        mute()
        
    def WX01_089(self, card): #幻兽 黑猫
        mute()
        
    def WX01_090(self, card): #幻兽 麻雀
        mute()
        
    def WX01_091(self, card): #幻兽 树袋熊
        mute()
        genDraw(1)
        
    def WX01_092(self, card): #幻兽 白猫
        mute()
        
    def WX01_093(self, card): #罗植 蒲公英
        mute()
        
    def WX01_094(self, card): #幻兽 燕子
        mute()
        
    def WX01_095(self, card): #幻兽 大熊猫
        mute()
        genDraw(1)
        
    def WX01_096(self, card): #幻兽 三色猫
        mute()
        
    def WX01_097(self, card): #罗植 鼠尾草
        mute()
        
    def WX01_098(self, card): #芽生
        mute()
        
    def WX01_099(self, card): #逆出
        mute()
        list = [c for c in table
                if isInEner(c)]
        s = askCard(list)
        if s == None:
            return False
        s.moveTo(me.hand)
        
    def WX01_100(self, card): #侍从T
        mute()
        fromDeckSend("能量区", 1)
        
    def WX01_101(self, card): #侍从D
        mute()
        fromDeckSend("能量区", 1)
        
    def WX01_102(self, card): #侍从O
        mute()
        fromDeckSend("能量区", 1)
        
    def WX01_103(self, card): #喷流的知识
        mute()
        fromDeckSend("能量区", 1)
        
    def WD01_001(self, card): #满月之巫女 玉依姬
        mute()
    
    def WD01_002(self, card): #弦月之巫女 玉依姬
        mute()
    
    def WD01_003(self, card): #半月之巫女 玉依姬
        mute()
    
    def WD01_004(self, card): #三日月之巫女 玉依姬
        mute()
    
    def WD01_005(self, card): #新月之巫女 玉依姬
        mute()
    
    def WD01_006(self, card): #洛可可界线
        mute()
    
    def WD01_007(self, card): #艾本之书
        mute()
    
    def WD01_008(self, card): #巴洛克防御
        mute()
    
    def WD01_009(self, card): #甲胄 皇家铠
        mute()
        bounce(card, 1, players[1], -1, 10)
    
    def WD01_010(self, card): #大剑 石中剑
        mute()
    
    def WD01_011(self, card): #笼手 铁拳
        mute()
        genDraw(1)
    
    def WD01_012(self, card): #中剑 焰形剑
        mute()
    
    def WD01_013(self, card): #小剑 库克力弯刀
        mute()
    
    def WD01_014(self, card): #小弓 箭矢
        mute()
    
    def WD01_015(self, card): #获得圣经
        mute()
    
    def WD02_001(self, card): #花代•肆
        mute()
    
    def WD02_002(self, card): #花代•叁
        mute()
    
    def WD02_003(self, card): #花代•贰
        mute()
    
    def WD02_004(self, card): #花代•壹
        mute()
    
    def WD02_005(self, card): #花代•零
        mute()
    
    def WD02_006(self, card): #飞火夏虫
        mute()
    
    def WD02_007(self, card): #背炎之阵
        mute()
    
    def WD02_008(self, card): #烧石炎
        mute()
    
    def WD02_009(self, card): #罗石 火山石
        mute()
        conditionBan(card, 1, players[1], -1, 7000, -1, 10, None, None)
    
    def WD02_010(self, card): #罗石 白银
        mute()
    
    def WD02_011(self, card): #罗石 石榴石
        mute()
        genDraw(1)
    
    def WD02_012(self, card): #罗石 铜
        mute()
    
    def WD02_013(self, card): #罗石 铁
        mute()
    
    def WD02_014(self, card): #罗石 紫水晶
        mute()
    
    def WD02_015(self, card): #轰音火柱
        mute()
    
    def WD03_001(self, card): #代号•皮璐璐可•T
        mute()
    
    def WD03_002(self, card): #代号•皮璐璐可•G
        mute()
    
    def WD03_003(self, card): #代号•皮璐璐可•M
        mute()
    
    def WD03_004(self, card): #代号•皮璐璐可•K
        mute()
    
    def WD03_005(self, card): #代号•皮璐璐可
        mute()
    
    def WD03_006(self, card): #窥视分析
        mute()
    
    def WD03_007(self, card): #不可行动
        mute()
    
    def WD03_008(self, card): #双重抽卡
        mute()
    
    def WD03_009(self, card): #技艺代号 R•M•N
        mute()
        remoteCall(players[1], "chooseDiscard", [])
    
    def WD03_010(self, card): #技艺代号 D•R•S
        mute()
    
    def WD03_011(self, card): #技艺代号 S•M•P
        mute()
        genDraw(1)
    
    def WD03_012(self, card): #技艺代号 J•V
        mute()
    
    def WD03_013(self, card): #技艺代号 S•C
        mute()
    
    def WD03_014(self, card): #技艺代号 R•F•R
        mute()
    
    def WD03_015(self, card): #真可惜
        mute()

    def PR_017(self, card): #中枪 古罗马长矛
        mute()
    
    def PR_018(self, card): #罗石 秘银
        mute()
        genDraw(1)
    
    def PR_019(self, card): #珍宝
        mute()
        handlist = [c for c in me.hand]
        s = None
        selected = []
        for i in range(2):
            while s == None and handlist:
                s = askCard(handlist)
            selected.append(s)
            handlist.remove(s)
        for c in selected:
            c.moveTo(me.piles['废弃区'])
        notify("{} 弃除了{}张手卡.".format(me, str(num)))
        if len(selected) == 2:
            genDraw(3)
    
    def PR_020(self, card): #增援
        mute()
    
    def PR_040(self, card): #多重
        mute()
        
    def WD04_001(self, card): #四之娘 绿姬
        mute()
        
    def WD04_002(self, card): #三之娘 绿姬
        mute()
        
    def WD04_003(self, card): #二之娘 绿姬
        mute()
        
    def WD04_004(self, card): #一之娘 绿姬
        mute()
        
    def WD04_005(self, card): #斗娘 绿姬
        mute()
        
    def WD04_006(self, card): #意气扬扬
        mute()
        
    def WD04_007(self, card): #再三再四
        mute()
        
    def WD04_008(self, card): #付和雷同
        mute()
        
    def WD04_009(self, card): #幻兽 青龙
        mute()
        conditionBan(card, 1, players[1], 10000, 99999, -1, 10, None, None)
        
    def WD04_010(self, card): #幻兽 朱雀小姐
        mute()
        conditionBan(card, 1, players[1], 12000, 99999, -1, 10, None, None)
        
    def WD04_013(self, card): #幻兽 小玄武
        mute()
        
    def WD04_015(self, card): #幻兽 白虎
        mute()
        
    def WD04_016(self, card): #侍从 Q2
        mute()
        
    def WD04_017(self, card): #侍从 O2
        mute()
        
    def WD04_018(self, card): #堕络
        mute()
        
    def WD05_001(self, card): #狱卒阎魔 乌莉丝
        mute()
        
    def WD05_002(self, card): #阿鼻阎魔 乌莉丝
        mute()
        
    def WD05_003(self, card): #众合阎魔 乌莉丝
        mute()
        
    def WD05_004(self, card): #灼热阎魔 乌莉丝
        mute()
        
    def WD05_005(self, card): #阎魔 乌莉丝
        mute()
        
    def WD05_006(self, card): #处刑时刻
        mute()
        
    def WD05_007(self, card): #永恒处刑
        mute()
        
    def WD05_008(self, card): #出墓
        mute()
        
    def WD05_009(self, card): #堕落炮女 缅茨姆
        mute()
        list = [c for c in me.piles["废弃区"]]
        s = askCard(list)
        if s != None:
            s.moveTo(me.hand)
        
    def WD05_010(self, card): #废恶象征 别西卜
        mute()
        
    def WD05_011(self, card): #堕落炮女 卡莉
        mute()
        genDraw(1)
        
    def WD05_012(self, card): #背德象征 科思莫
        mute()
        
    def WD05_013(self, card): #小恶象征 小鬼
        mute()
        
    def WD05_014(self, card): #堕落炮女 魅魔
        mute()
        
    def WD05_017(self, card): #完全漆黑
        mute()
        
    def WD05_018(self, card): #回想的祝福
        mute()
        list = [c for c in me.piles["废弃区"]
                if c.properties["类型"] == "SIGNI"]
        s = askCard(list)
        if s != None:
            s.moveTo(me.hand)
        
        
    def WX02_001(self, card): #金木犀之巫女 玉依姬
        mute()
        
    def WX02_002(self, card): #火鸟风月 游月·肆
        mute()
        
    def WX02_003(self, card): #艾尔德拉×Ⅳ式
        mute()
        
    def WX02_004(self, card): #无间阎魔 乌莉丝
        mute()
        
    def WX02_005(self, card): #纯白希望
        mute()
        
    def WX02_006(self, card): #漆黑野望
        mute()
        
    def WX02_007(self, card): #轰罪炎 游月·叁
        mute()
        
    def WX02_008(self, card): #焰海 游月•贰
        mute()
        
    def WX02_009(self, card): #焰 游月•壹
        mute()
        
    def WX02_010(self, card): #艾尔德拉×Ⅲ式
        mute()
        
    def WX02_011(self, card): #艾尔德拉×Ⅱ式
        mute()
        
    def WX02_012(self, card): #艾尔德拉×Ⅰ式
        mute()
        
    def WX02_013(self, card): #叫唤阎魔 乌莉丝
        mute()
        
    def WX02_014(self, card): #黑绳阎魔 乌莉丝
        mute()
        
    def WX02_015(self, card): #等活阎魔 乌莉丝
        mute()
        
    def WX02_016(self, card): #哥特界限
        mute()
    
    def WX02_017(self, card): #气炎万丈
        mute()
        
    def WX02_018(self, card): #火红柳绿
        mute()
        
    def WX02_019(self, card): #交织生命护甲
        mute()
        
    def WX02_020(self, card): #鲜血斩击
        mute()
        
    def WX02_021(self, card): #先驱的大天使 大天使该隐
        mute()
        conditionSearch("主卡组", 1, ["SIGNI"], [], -1, 10, -1, 99999, ["天使"], [], [])
        if searched:
            searched[0].moveTo(me.hand)
            getOppoLrig()
            list = [c for c in table 
                    if c.controller == players[1]
                    and (isInSigni(c) or c == oppoLrig) 
                    and c.orientation == 0]
            confirm("选择要横置的卡")
            s = askCard(list)
            if s == None:
                return
            remoteCall(players[1], "down", [s])
        
    def WX02_022(self, card): #弩炮 狙击枪
        mute()
        list = [c for c in table
                if c.controller == players[1]
                and isInSigni(c)
                and c.markers[Power] <= 8000]
        s = card
        selected = []
        sum = 0
        if not list:
            notify("没有满足条件的卡")
            return False
        while s != None and list:
            s = askCard(list)
            if s != None:
                selected.append(s)
                list.remove(s)
                sum += s.markers[Power]
                list = [c for c in list 
                        if (c.markers[Power] + sum) <= 8000]
        remoteCall(players[1], "banishList", [selected])

    def WX02_023(self, card): #幻水姬 丝派拉尔•卡米拉
        mute()
        choiceList = ["「抽1张卡。」", "「不查看对战对手的手牌而选择1张，并将它舍弃。」"]
        colorsList = ['#FF0000', '#FF0000'] 
        echoice = askChoice("选择一个效果发动：", choiceList, colorsList, customButtons = ["取消"])
        if echoice == 1:
            genDraw(1)
        elif echoice == 2:
            remoteCall(players[1], "randomDiscard", [])
        
    def WX02_024(self, card): #罗植姬 戈休·雅格尼丝
        mute()
        choiceList = ["「将对战对手的1只力量10000以上的SIGNI驱逐。」", "「将你卡组顶的1张卡放置到能量区。」"]
        colorsList = ['#FF0000', '#FF0000'] 
        echoice = askChoice("选择一个效果发动：", choiceList, colorsList, customButtons = ["取消"])
        if echoice == 1:
            conditionBan(card, 1, players[1], 10000, 99999, -1, 10, None, None)
        elif echoice == 2:
            fromDeckSend("能量区", 1)
        
    def WX02_025(self, card): #恶魔姬 安娜•蜃影
        mute()
        excavate(5)
        list = [c for c in exlist
                if isDevil(c)]
        s = askCard(list)
        if s == None:
            for e in exlist:
                e.moveTo(me.piles["废弃区"])
            return False
        s.moveTo(me.hand)
        exlist.remove(s)
        for r in exlist:
            r.moveTo(me.piles["废弃区"])
        
    def WX02_026(self, card): #愿望危机
        mute()
        global arrival_limit
        conditionSearch("主卡组", 1, ["SIGNI"], [], -1, 10, -1, 99999, ["天使"], [], [])
        if searched:
            arrival_limit = 1
            if not askPosition(searched[0]):
                arrival_limit = 0
        
    def WX02_027(self, card): #焦土的代价
        mute()
        if conditionBan(card, 1, players[1], -1, 99999, -1, 10, None, None):
            genDraw(1)
        
    def WX02_028(self, card): #谜言暗气
        mute()
        global arrival_limit
        list = [c for c in me.piles["废弃区"]
                if c.properties["类型"] == "SIGNI"
                and c.properties["颜色"] == "黑"]
        s = askCard(list)
        if s != None:
            arrival_limit = 1
            if not askPosition(s):
                arrival_limit = 0
        
    def WX02_029(self, card): #宝具 御剑
        mute()
        fromDeckSend("能量区", 1)
        
    def WX02_030(self, card): #宝具 御镜
        mute()
        genDraw(1)
        
    def WX02_031(self, card): #使其反跳
        mute()
        
    def WX02_032(self, card): #罗石 蛋白石
        mute()
        fromDeckSend("能量区", 1)
        
    def WX02_033(self, card): #罗石 红玉髓
        mute()
        genDraw(1)
        
    def WX02_034(self, card): #不希望的冲动
        mute()
        if isThereColor("红", me, "能量区") and isThereColor("绿", me, "能量区"):
            conditionBan(card, 1, players[1], -1, 99999, -1, 10, None, None)
        
    def WX02_035(self, card): #技艺代号 C·P·U
        mute()
        
    def WX02_036(self, card): #技艺代号 G•A•B
        mute()
        genDraw(1)
        
    def WX02_037(self, card): #飞溅
        mute()
        genDraw(1)
        if isThereStype1("水兽", card.controller):
            genDraw(1)
        
    def WX02_038(self, card): #幻兽 雉
        mute()
        fromDeckSend("能量区", 1)
        
    def WX02_039(self, card): #幻兽 八犬
        mute()
        genDraw(1)
        
    def WX02_040(self, card): #着植
        mute()
        global plant
        plant = 1
        notify("着植效果适用。")
        
    def WX02_041(self, card): #大损
        mute()
        conditionBan(card, 1, players[1], 12000, 99999, -1, 10, None, None)
        
    def WX02_042(self, card): #反制代号 巴勒贝克
        mute()
        
    def WX02_043(self, card): #反制代号 基西拉
        mute()
        
    def WX02_044(self, card): #大罪缘由 巴力
        mute()
        genDraw(1)
        
    def WX02_045(self, card): #献祭斩击
        mute()
        conditionBan(card, 1, players[1], -1, 99999, -1, 10, None, None)
        
    def WX02_046(self, card): #牺牲的微笑 丘雅耶尔
        mute()
        
    def WX02_047(self, card): #虚构的爱情 希耶尔
        mute()
        
    def WX02_048(self, card): #宝具 勾玉
        mute()
        
    def WX02_049(self, card): #博爱的聚集 萨尼耶尔
        mute()
        
    def WX02_050(self, card): #刀剑本领
        mute()
        
    def WX02_051(self, card): #轰炮 远射装置
        mute()
        
    def WX02_052(self, card): #爆炮 MP5
        mute()
        
    def WX02_053(self, card): #罗石 翡翠
        mute()
        
    def WX02_054(self, card): #小炮 枪匠
        mute()
        
    def WX02_055(self, card): #光欲宝剑
        mute()
        
    def WX02_056(self, card): #幻水 奥科特
        mute()
        
    def WX02_057(self, card): #幻水 珍珠
        mute()
        
    def WX02_058(self, card): #技艺代号 M•M•R
        mute()
        chooseDiscard()
        remoteCall(players[1], "chooseDiscard", [])
        
    def WX02_059(self, card): #幻水 科塞梅
        mute()
        
    def WX02_060(self, card): #探寻者
        mute()
        conditionSearch("主卡组", 1, ["魔法"], [], None, None, None, None, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX02_061(self, card): #蓝色收获
        mute()
        
    def WX02_062(self, card): #罗植 葵小姐
        mute()
        
    def WX02_063(self, card): #罗植 莲
        mute()
        
    def WX02_064(self, card): #幻兽 猴
        mute()
        
    def WX02_065(self, card): #罗植 虎尾兰
        mute()
        
    def WX02_066(self, card): #丰润
        mute()
        
    def WX02_067(self, card): #恶魔续发 莉莉丝
        mute()
        
    def WX02_068(self, card): #恶魔勇武 摩莉甘
        mute()
        
    def WX02_069(self, card): #反制代号 星云
        mute()
        
    def WX02_070(self, card): #真实死神 阿尼玛
        mute()
        
    def WX02_071(self, card): #反制代号 德里
        mute()
        
    def WX02_072(self, card): #反制代号 马丘比
        mute()
        
    def WX02_073(self, card): #反制代号 敌左反魔
        mute()
        genDraw(1)
        
    def WX02_074(self, card): #小恶忧郁 格里姆
        mute()
        
    def WX02_075(self, card): #造墓者
        mute()
        
    def WX02_077(self, card): #侍从 T2
        mute()
        
    def WX02_078(self, card): #侍从 D2
        mute()
