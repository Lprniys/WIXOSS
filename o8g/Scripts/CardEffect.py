# -*- coding: utf-8 -*-  
'''
Created on 2014年7月18日

@author: SynTuner
'''
class CardEffects():
    '''
    to be written
    '''
    def __init__(self):
        self.etype = -2
        
    def WX01_001(self, card, etype, echoice): #太阳之巫女 玉依姬
        mute()
        bounce(card, 1, players[1], -1, 10)
        
    def WX01_002(self, card, etype, echoice): #晓之巫女 玉依姬
        mute()
        reds = []
        whites = []
        getMyLrig()
        if etype == -1:
            mySigni = [s for s in table
                       if isInSigni(s)
                       and s.controller == card.controller]
            for ch in mySigni:
                if ch.properties["颜色"] == "白":
                    whites.append(s)
                if ch.properties["颜色"] == "红":
                    reds.append(s)
            if not reds or not whites:
                updateSigniField()
                #if isInSigni(card):
                for key in SigniField:  #cancel
                    if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                        SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 3000
                        SigniField[key][1].remove(card)
            else:
                if isCurrentLrig(card):
                    for key in SigniField:  #activate
                        if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]:
                            SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] + 3000
                            SigniField[key][1].append(card)
                else:
                    for key in SigniField:  #cancel
                        if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                            SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 3000
                            SigniField[key][1].remove(card)
        elif etype == 1:  #Arrival
            fieldToCrash(1, players[1], -1, 10000, None)
        else:
            fieldToCrash(1, players[1], -1, 99999, None)
        
    def WX01_003(self, card, etype, echoice): #百火缭乱 花代•肆
        mute()
        conditionBan(card, 1, players[1], -1, 10000, -1, 10, None, None)
        
    def WX01_004(self, card, etype, echoice): #轰炎 花代•贰改
        mute()
        updateSigniField()
        getMyLrig()
        if etype == -1:
            if isCurrentLrig(card) and card.controller.isActivePlayer:
                for key in SigniField:
                    if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]:
                        SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] + 5000
                        SigniField[key][1].append(card)
            else:
                for key in SigniField:
                    if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                        SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 5000
                        SigniField[key][1].remove(card)
        else:
            remoteCall(players[1], "setGlobal", [1,0,0])
                    
    def WX01_005(self, card, etype, echoice): #代号 皮璐璐可•Ω
        mute()
        remoteCall(players[1], "randomDiscard", [])
        
    def WX01_006(self, card, etype, echoice): #四式战帝女 绿姬
        mute()
        global phase
        updateSigniField()
        if phase == "mainphase":
            mySigni = [signi for signi in table
                       if isInSigni(signi)
                       and signi.controller == card.controller]
            if not mySigni:
                return False
            s = askCard(mySigni)
            if s == None:
                return
            for key in SigniField.keys():
                if SigniField[key][0] == s:
                    SigniField[key][1].append(card)
                    s.markers[Power] += 10000
                    break
        elif phase == "endphase":
            for key in SigniField.keys():
                if card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] -= 10000
                    SigniField[key][1].remove(card)
        
    def WX01_007(self, card, etype, echoice): #月蚀之巫女 玉依姬
        mute()
        conditionSearch("主卡组", 1, ["SIGNI"], [], -1, 2, -1, 99999, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX01_008(self, card, etype, echoice): #流星之巫女 玉依姬
        mute()
        updateSigniField()
        if isCurrentLrig(card):
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]\
                and SigniField[key][0].properties["颜色"] == card.properties["颜色"]:  #a trick to fulfill color requirement.
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] + 1000
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]\
                and SigniField[key][0].properties["颜色"] == card.properties["颜色"]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 1000
                    SigniField[key][1].remove(card)
        
    def WX01_009(self, card, etype, echoice): #新星之巫女 玉依姬
        mute()
        genDraw(1)
        
    def WX01_010(self, card, etype, echoice): #杰诺之门
        mute()
        conditionSearch("主卡组", 1, ["SIGNI"], ["白"], -1, 10, -1, 99999, [], [], [])
        for signi in searched:
            signi.moveTo(me.hand)
        me.piles["主卡组"].shuffle()
        
    def WX01_011(self, card, etype, echoice): #炽炎舞 花代•叁
        mute()
        conditionBan(card, 1, players[1], -1, 7000, -1, 10, None, None)
        
    def WX01_012(self, card, etype, echoice): #刚炎 花代•贰
        mute()
        updateSigniField()
        if isCurrentLrig(card):
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]\
                and SigniField[key][0].properties["颜色"] == card.properties["颜色"]:  #a trick to fulfill color requirement.
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] + 1000
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]\
                and SigniField[key][0].properties["颜色"] == card.properties["颜色"]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 1000
                    SigniField[key][1].remove(card)
        
    def WX01_013(self, card, etype, echoice): #焰 花代•壹
        mute()
        genDraw(1)
        
    def WX01_014(self, card, etype, echoice): #烈霸一络
        mute()
        conditionBan(card, 1, players[1], -1, 10000, -1, 10, None, None)
        
    def WX01_015(self, card, etype, echoice): #代号 皮璐璐可•Γ
        mute()
        remoteCall(players[1], "chooseDiscard", [])
        
    def WX01_016(self, card, etype, echoice): #代号 皮璐璐可•Β
        mute()
        updateSigniField()
        if isCurrentLrig(card):
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]\
                and SigniField[key][0].properties["颜色"] == card.properties["颜色"]:  #a trick to fulfill color requirement.
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] + 1000
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]\
                and SigniField[key][0].properties["颜色"] == card.properties["颜色"]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 1000
                    SigniField[key][1].remove(card)
        
    def WX01_017(self, card, etype, echoice): #代号 皮璐璐可•Α
        mute()
        genDraw(1)
        
    def WX01_018(self, card, etype, echoice): #魔法反制
        mute()
        
    def WX01_019(self, card, etype, echoice): #四型皇艳娘 绿姬
        mute()
        updateSigniField()
        if isCurrentLrig(card):
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] + 1000
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 1000
                    SigniField[key][1].remove(card)
        
    def WX01_020(self, card, etype, echoice): #三型雌雌娘 绿姬
        mute()
        fromDeckSend("能量区", 1)
        
    def WX01_021(self, card, etype, echoice): #二型斗婚娘 绿姬
        mute()
        updateSigniField()
        if isCurrentLrig(card):
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]\
                and SigniField[key][0].properties["颜色"] == card.properties["颜色"]:  #a trick to fulfill color requirement.
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] + 1000
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]\
                and SigniField[key][0].properties["颜色"] == card.properties["颜色"]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 1000
                    SigniField[key][1].remove(card)
        
    def WX01_022(self, card, etype, echoice): #一型舞斗娘 绿姬
        mute()
        genDraw(1)
        
    def WX01_023(self, card, etype, echoice): #大器晚成
        mute()
        list = [c for c in table
                if isInEnerP(c, players[1])
                or (isInSigni(c) and c.controller == players[1])]
        remoteCall(players[1], "sendToCrashList", [list])
        
    def WX01_024(self, card, etype, echoice): #奇奇怪怪
        mute()
        powerChange(card, 5000, "all")
#        requestInfo(card, etype, echoice)
        
    def WX01_025(self, card, etype, echoice): #营救
        mute()
        getMyLrig()
        colorlist = [myLrig.properties["颜色"]]
        conditionSearch("废弃区", 1, ["SIGNI"], colorlist, -1, 10, -1, 99999, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX01_026(self, card, etype, echoice): #充能
        mute()
        fromDeckSend("能量区", 1)
        
    def WX01_027(self, card, etype, echoice): #原枪 源能枪
        mute()
        if etype == 2:
            if isInSigni(card):
                remoteCall(players[1], "setGlobal", [None, None, 1])
                notify("原枪发动了效果")
            else:
                remoteCall(players[1], "setGlobal", [None, None, 0])
        elif etype == 1:
            chooseUp(1, me)
        elif etype == -3:
            remoteCall(players[1], "setGlobal", [None, None, 0])
        
    def WX01_028(self, card, etype, echoice): #弧光圣气
        mute()
        if etype == 2:
            getMyLrig()
            myLrig.highlight = ArcAura
            notify("{}获得了弧光圣气".format(myLrig))
        
    def WX01_029(self, card, etype, echoice): #罗辉石 金刚珠玉
        mute()
        updateSigniField()
        if etype == -1 and battle_step == "attack effect":
            mute()
        elif etype == 1:
            conditionBan(card, 1, players[1], -1, 7000, -1, 10, None, None)
        elif etype == 2:
            doubleCrash(card, 0, 0)
        elif etype == -3:
            for key in SigniField:
                if card in SigniField[key][1]:  #temporarily will not cause a confusion because double crash is always one-turn effect.
                    card.markers[Power] -= 2000  
                    card.markers[DoubleCrashM] = 0
                    SigniField[key][1].remove(card)
        
    def WX01_030(self, card, etype, echoice): #赎罪之对火
        mute()
        getMyLrig()
        if etype == 2:
            if conditionBan(card, 1, players[1], -1, 12000, -1, 10, None, None):
                doubleCrash(myLrig)
                effectMemo(card, [myLrig])
        elif etype == -3:
            if isCurrentLrig(activatedDict[card][0]):
                cancelDoubleCrash(activatedDict[card][0])
        
    def WX01_031(self, card, etype, echoice): #核心代号 V•A•C
        mute()
        if etype == 1:
            remoteCall(players[1], "chooseDiscard", [])
        if etype == 2:
            conditionSearch("废弃区", 1, ["魔法"], [], None, None, None, None, [], [], [])
            for magic in searched:
                magic.moveTo(card.controller.hand)
        
    def WX01_032(self, card, etype, echoice): #抢夺
        mute()
        remoteCall(players[1], "forcedDiscard", [card, 2])
        rnd(1, 1000)
        #if len(players[1].hand) == 0:
        #    genDraw(1)
        
    def WX01_033(self, card, etype, echoice): #幻兽神 御先狐
        mute()
        if etype == 1:
            conditionSearch("能量区", 1, [], [], None, None, None, None, [], [], [])
            for magic in searched:
                magic.moveTo(card.controller.hand)
        if etype == 2:
            crashed_green = [cg for cg in me.piles["废弃区"]
                             if cg.properties["颜色"] == "绿"]
            for c in crashed_green:
                c.moveTo(me.piles["主卡组"])
            me.piles["主卡组"].shuffle()
        
    def WX01_034(self, card, etype, echoice): #修复
        mute()
        fromDeckSend("生命护甲", 1)
        if zoneNum("能量区", 10, card):
            fromDeckSend("生命护甲", 1)
        
    def WX01_035(self, card, etype, echoice): #祝福女神 雅典娜
        mute()
        bounce(card, 1, players[1], -1, 10)
        
    def WX01_036(self, card, etype, echoice): #巨弓 抛射弓
        mute()
        global exlist
        mySigni = [signi for signi in table
                   if isInSigni(signi)
                   and signi.controller == me]
        excavate(1)
        if exlist[0].properties["类型"] == "SIGNI" and int(exlist[0].properties["等级"]) <= 2 and len(mySigni) == 1:
            askPosition(exlist[0])
        
    def WX01_037(self, card, etype, echoice): #无法忘却的幻想 瓦尔基里
        mute()
        conditionSearch("主卡组", 1, [], [], -1, 3, -1, 99999, [], [], ["无法忘却的幻想 瓦尔基里"])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX01_038(self, card, etype, echoice): #获得但他林
        mute()
        conditionSearch("主卡组", 2, ["SIGNI", "SIGNI"], ["白", "红"], -1, 10, -1, 99999, [], [], [])
        for signi in searched:
            signi.moveTo(me.hand)
        me.piles["主卡组"].shuffle()
        
    def WX01_039(self, card, etype, echoice): #弩炮 加农炮
        mute()
        conditionBan(card, 1, players[1], -1, 10000, -1, 10, None, None)
        
    def WX01_040(self, card, etype, echoice): #罗石 山铜
        mute()
        conditionBan(card, 1, players[1], -1, 7000, -1, 10, None, None)
        
    def WX01_041(self, card, etype, echoice): #轰炮 法典炮
        mute()
        conditionBan(card, 1, players[1], -1, 7000, -1, 10, None, None)
        
    def WX01_042(self, card, etype, echoice): #断罪之轹断
        mute()
        remoteCall(playyers[1], "crash", [1])
        
    def WX01_043(self, card, etype, echoice): #幻水 雅莱娅尔
        mute()
        genDraw(2)
        
    def WX01_044(self, card, etype, echoice): #技艺代号 P•Z•L
        mute()
        askFreeze(card, -1, 3)
        
    def WX01_045(self, card, etype, echoice): #幻水 夏克兰丝
        mute()
        genDraw(1)
        
    def WX01_046(self, card, etype, echoice): #情况糟糕
        mute()
        conditionBan(card, 1, players[1], -1, 99999, -1, 10, None, None)
        
    def WX01_047(self, card, etype, echoice): #罗植 曼茶罗花
        mute()
        conditionSearch("能量区", 1, [], [], -1, 10, -1, 99999, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX01_048(self, card, etype, echoice): #幻兽 雪怪
        mute()
        updateSigniField()
        if etype == 1:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller:  
                    SigniField[key][0].markers[Power] += 2000
                    SigniField[key][1].append(card)
        if etype == -3:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] -= 2000
                    SigniField[key][1].remove(card)
        
    def WX01_049(self, card, etype, echoice): #罗植 植生羊
        mute()
        fromDeckSend("能量区", 1)
        
    def WX01_050(self, card, etype, echoice): #大化
        mute()
        updateSigniField()
        mySigni = [s for s in table
                   if isInSigni(s)
                   and s.controller == me]
        if etype == 2:
            for signi in mySigni:
                signi.markers[Power] += 5000
                SigniField[getKey(signi)][1].append(signi)
        if etype == -3:
            for signi in mySigni:
                if card in SigniField[getKey(signi)][1]:
                    signi.markers[Power] -= 5000
                    SigniField[getKey(signi)][1].remove(signi)
        
    def WX01_051(self, card, etype, echoice): #侍从Q
        mute()
        
    def WX01_052(self, card, etype, echoice): #包括的知识
        mute()
        genDraw(2)
        
    def WX01_053(self, card, etype, echoice): #极剑 噬神剑
        mute()
        
    def WX01_054(self, card, etype, echoice): #极盾 埃奎斯盾
        mute()
        updateSigniField()
        if isInSigni(card) and not card.controller.isActivePlayer:
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +18000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 18000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_055(self, card, etype, echoice): #大盾 镇暴盾
        mute()
        updateSigniField()
        if isInSigni(card) and not card.controller.isActivePlayer:
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +12000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 12000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_056(self, card, etype, echoice): #中盾 方盾
        mute()
        updateSigniField()
        if isInSigni(card) and not card.controller.isActivePlayer:
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +8000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 8000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_057(self, card, etype, echoice): #出弓 炽天弓
        mute()
        global exlist
        mySigni = [signi for signi in table
                   if isInSigni(signi)
                   and signi.controller == me]
        excavate(1)
        if exlist[0].properties["类型"] == "SIGNI" and int(exlist[0].properties["等级"]) <= 2 and len(mySigni) == 1:
            askPosition(exlist[0])
        
    def WX01_058(self, card, etype, echoice): #重新开始的对话 米迦勒
        mute()
        conditionSearch("主卡组", 1, ["SIGNI"], ["白"], -1, 3, -1, 99999, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX01_059(self, card, etype, echoice): #出弓 普弓
        mute()
        global exlist
        mySigni = [signi for signi in table
                   if isInSigni(signi)
                   and signi.controller == me]
        excavate(1)
        if exlist[0].properties["类型"] == "SIGNI" and int(exlist[0].properties["等级"]) <= 1 and len(mySigni) == 1:
            askPosition(exlist[0])
        
    def WX01_060(self, card, etype, echoice): #小盾 圆盾
        mute()
        updateSigniField()
        if isInSigni(card) and not card.controller.isActivePlayer:
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +5000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 5000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_061(self, card, etype, echoice): #探求的思想 汉尼尔
        mute()
        conditionSearch("主卡组", 1, ["SIGNI"], ["白"], -1, 2, -1, 99999, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX01_062(self, card, etype, echoice): #将之开启
        mute()
        excavate(5)
        confirm("请选择要放置到废弃区的卡片。")
        s = card
        tocrash = []
        while s != None:
            s = askCard(exlist)
            if s != None:
                tocrash.append(s)
                exlist.remove(s)
        for c in tocrash:
            c.moveTo(card.controller.piles["废弃区"])
        orderExcavated()
        
    def WX01_063(self, card, etype, echoice): #做好准备
        mute()
        list = [c for c in table
                if c.controller == me
                and isInSigni(c)
                and c.orientation == 1]
        for l in list:
            up(l)
        
    def WX01_064(self, card, etype, echoice): #罗石 金属
        mute()
        
    def WX01_065(self, card, etype, echoice): #罗石 绿宝石
        mute()
        updateSigniField()
        if isInSigni(card) and card.controller.isActivePlayer:
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +18000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 18000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_066(self, card, etype, echoice): #罗石 红宝石
        mute()
        updateSigniField()
        if isInSigni(card) and card.controller.isActivePlayer:
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +12000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 12000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_067(self, card, etype, echoice): #罗石 磷矿石
        mute()
        forcedDiscard(card, 1)
        
    def WX01_068(self, card, etype, echoice): #罗石 琥珀
        mute()
        updateSigniField()
        if isInSigni(card) and card.controller.isActivePlayer:
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +8000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 8000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_069(self, card, etype, echoice): #爆炮 远射炮
        mute()
        conditionBan(card, 1, players[1], -1, 5000, -1, 10, None, None)
        
    def WX01_070(self, card, etype, echoice): #罗石 海人草
        mute()
        forcedDiscard(card, 1)
        
    def WX01_071(self, card, etype, echoice): #罗石 蓝宝石
        mute()
        updateSigniField()
        if isInSigni(card) and card.controller.isActivePlayer:
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +5000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 5000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_072(self, card, etype, echoice): #小炮 德拉古诺夫枪
        mute()
        conditionBan(card, 1, players[1], -1, 2000, -1, 10, None, None)
        
    def WX01_073(self, card, etype, echoice): #落星炎球
        mute()
        conditionBan(card, 1, players[1], -1, 15000, -1, 10, None, None)
        
    def WX01_074(self, card, etype, echoice): #棱晶火柱
        mute()
        conditionBan(card, 1, players[1], -1, 10000, -1, 10, None, None)
        
    def WX01_075(self, card, etype, echoice): #技艺代号 A•S•M
        mute()
        
    def WX01_076(self, card, etype, echoice): #技艺代号 I•D•O•L
        mute()
        if isInSigni(card) and handAdvantage(3, card):
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +18000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 18000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_077(self, card, etype, echoice): #技艺代号 A•D•B
        mute()
        if isInSigni(card) and handAdvantage(2, card):
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +12000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 12000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_078(self, card, etype, echoice): #技艺代号 S•T•G
        mute()
        if isInSigni(card) and handAdvantage(2, card):
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +8000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 8000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_079(self, card, etype, echoice): #技艺代号 W•T•C
        mute()
        askFreeze(card, -1, 2)
        
    def WX01_080(self, card, etype, echoice): #幻水 夏可檀
        mute()
        genDraw(2)
        chooseDiscard()
        
    def WX01_081(self, card, etype, echoice): #技艺代号 T•V
        mute()
        askFreeze(card, 1, 1)
        
    def WX01_082(self, card, etype, echoice): #技艺代号 F•A•N
        mute()
        if isInSigni(card) and handAdvantage(1, card):
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +5000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 5000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_083(self, card, etype, echoice): #幻水 克马诺明
        mute()
        genDraw(1)
        
    def WX01_084(self, card, etype, echoice): #事不过三
        mute()
        genDraw(3)
        chooseDiscard()
        
    def WX01_085(self, card, etype, echoice): #冰封
        mute()
        list = [c for c in table
                if c.controller == players[1]
                and isInSigni(c)]
        for l in list:
            remoteCall(players[1], "down", [l])
            remoteCall(players[1], "freeze", [l, 0, 0])
        
    def WX01_086(self, card, etype, echoice): #幻兽 飞鹰
        mute()
        
    def WX01_087(self, card, etype, echoice): #幻兽 猫妖精
        mute()
        if isInSigni(card) and enerAdvantage(5, card):
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +18000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 18000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_088(self, card, etype, echoice): #幻兽 猫头鹰
        mute()
        
    def WX01_089(self, card, etype, echoice): #幻兽 黑猫
        mute()
        if isInSigni(card) and enerAdvantage(4, card):
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +12000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 12000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_090(self, card, etype, echoice): #幻兽 麻雀
        mute()
        
    def WX01_091(self, card, etype, echoice): #幻兽 树袋熊
        mute()
        powerChange(card, 3000, "me")
        
    def WX01_092(self, card, etype, echoice): #幻兽 白猫
        mute()
        if isInSigni(card) and enerAdvantage(3, card):
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +8000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 8000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_093(self, card, etype, echoice): #罗植 蒲公英
        mute()
        fromDeckSend("能量区", 1)
        
    def WX01_094(self, card, etype, echoice): #幻兽 燕子
        mute()
        
    def WX01_095(self, card, etype, echoice): #幻兽 大熊猫
        mute()
        powerChange(card, 2000, "me")
        
    def WX01_096(self, card, etype, echoice): #幻兽 三色猫
        mute()
        if isInSigni(card) and enerAdvantage(2, card):
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +5000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 5000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX01_097(self, card, etype, echoice): #罗植 鼠尾草
        mute()
        fromDeckSend("能量区", 1)
        
    def WX01_098(self, card, etype, echoice): #芽生
        mute()
        fromDeckSend("能量区", 2)
        
    def WX01_099(self, card, etype, echoice): #逆出
        mute()
        conditionSearch("能量区", 1, ["SIGNI"], [], -1, 10, -1, 99999, [], [], [])
        if searched:
            askPosition(searched[0])
        
    def WX01_100(self, card, etype, echoice): #侍从T
        mute()
        
    def WX01_101(self, card, etype, echoice): #侍从D
        mute()
        
    def WX01_102(self, card, etype, echoice): #侍从O
        mute()
        
    def WX01_103(self, card, etype, echoice): #喷流的知识
        mute()
        genDraw(1)
        
    def WD01_001(self, card, etype, echoice): #满月之巫女 玉依姬
        mute()
        updateSigniField()
        if isCurrentLrig(card) and isThereSigni("甲胄 皇家铠", card.controller):
            for key in SigniField: 
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]:  
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] +2000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 2000
                    SigniField[key][1].remove(card)
    
    def WD01_002(self, card, etype, echoice): #弦月之巫女 玉依姬
        mute()
    
    def WD01_003(self, card, etype, echoice): #半月之巫女 玉依姬
        mute()
    
    def WD01_004(self, card, etype, echoice): #三日月之巫女 玉依姬
        mute()
    
    def WD01_005(self, card, etype, echoice): #新月之巫女 玉依姬
        mute()
    
    def WD01_006(self, card, etype, echoice): #洛可可界线
        mute()
        bounce(card, 2, players[1], -1, 10)
    
    def WD01_007(self, card, etype, echoice): #艾本之书
        mute()
        conditionSearch("主卡组", 2, ["SIGNI", "SIGNI"], ["白", "白"], -1, 10, -1, 99999, [], [], [])
        for signi in searched:
            signi.moveTo(me.hand)
        me.piles["主卡组"].shuffle()
        
    def WD01_008(self, card, etype, echoice): #巴洛克防御
        mute()
        updateSigniField()
        getOppoLrig()
        if etype == 2:
            getOppoLrig()
            list = [c for c in table 
                    if c.controller == players[1]
                    and (isInSigni(c) or c == oppoLrig) 
                    and c.orientation == 0]
            s = askCard(list)
            if s == None:
                return False
            s.markers[attackDisableM] += 1
            if s.properties["类型"] == "SIGNI":
                SigniField[getKey(s)][1].append(card)
        if etype == -3:
            for key in SigniField:
                if card in SigniField[key][1]:
                    SigniField[key][1].remove(card)
                    SigniField[key][1].markers[attackDisableM] -= 1
                if oppoLrig.markers[attackDisableM] != 0:  #it seems like we should also give lrig an effect slot. Wait to see next package.
                    oppoLrig.markers[attackDisableM] -= 1
    
    def WD01_009(self, card, etype, echoice): #甲胄 皇家铠
        mute()
        updateSigniField()
        if isInSigni(card) and not card.controller.isActivePlayer:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] + 1000
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 1000
                    SigniField[key][1].remove(card)
        #updates(0,0,0)
    
    def WD01_010(self, card, etype, echoice): #大剑 石中剑
        mute()
    
    def WD01_011(self, card, etype, echoice): #笼手 铁拳
        mute()
        conditionSearch("主卡组", 1, ["SIGNI"], [], -1, 10, -1, 99999, [], ["甲胄 皇家铠"], [])
        for signi in searched:
            signi.moveTo(me.hand)
        me.piles["主卡组"].shuffle()
    
    def WD01_012(self, card, etype, echoice): #中剑 焰形剑
        mute()
    
    def WD01_013(self, card, etype, echoice): #小剑 库克力弯刀
        mute()
    
    def WD01_014(self, card, etype, echoice): #小弓 箭矢
        mute()
        excavate(3)
        orderExcavated()
    
    def WD01_015(self, card, etype, echoice): #获得圣经
        mute()
        conditionSearch("主卡组", 1, ["SIGNI"], [], -1, 10, -1, 99999, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
    
    def WD02_001(self, card, etype, echoice): #花代•肆
        mute()
        updateSigniField()
        if isCurrentLrig(card) and isThereSigni("罗石 火山石", card.controller) and card.controller.isActivePlayer:
            for key in SigniField: 
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]:  
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] +2000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 2000
                    SigniField[key][1].remove(card)
    
    def WD02_002(self, card, etype, echoice): #花代•叁
        mute()
    
    def WD02_003(self, card, etype, echoice): #花代•贰
        mute()
    
    def WD02_004(self, card, etype, echoice): #花代•壹
        mute()
    
    def WD02_005(self, card, etype, echoice): #花代•零
        mute()
    
    def WD02_006(self, card, etype, echoice): #飞火夏虫
        mute()
        conditionBan(card, 1, players[1], -1, 15000, -1, 10, None, None)
    
    def WD02_007(self, card, etype, echoice): #背炎之阵
        mute()
        mySigni = [msigni for msigni in table
                   if isInSigni(msigni)
                   and msigni.controller == me]
        oppoSigni = [osigni for osigni in table
                     if isInSigni(osigni)
                     and osigni.controller == players[1]]
        banishList(mySigni)
        remoteCall(players[1], "banishList", [oppoSigni])
    
    def WD02_008(self, card, etype, echoice): #烧石炎
        mute()
        conditionBan(card, 1, players[1], -1, 7000, -1, 10, None, None)
    
    def WD02_009(self, card, etype, echoice): #罗石 火山石
        mute()
        conditionBan(card, 1, players[1], -1, 15000, -1, 10, None, None)
    
    def WD02_010(self, card, etype, echoice): #罗石 白银
        mute()
    
    def WD02_011(self, card, etype, echoice): #罗石 石榴石
        mute()
        updateSigniField()
        if etype == 1:
            card.markers[Power] += 8000  #trick, need FAQ
            effectMemo(card, [card])
        if etype == -3:
            if isInSigni(activatedDict[card][0]):
                card.markers[Power] -= 8000
    
    def WD02_012(self, card, etype, echoice): #罗石 铜
        mute()
    
    def WD02_013(self, card, etype, echoice): #罗石 铁
        mute()
    
    def WD02_014(self, card, etype, echoice): #罗石 紫水晶
        mute()
        conditionBan(card, 1, players[1], -1, 1000, -1, 10, None, None)
    
    def WD02_015(self, card, etype, echoice): #轰音火柱
        mute()
        conditionBan(card, 1, players[1], -1, 5000, -1, 10, None, None)
    
    def WD03_001(self, card, etype, echoice): #代号•皮璐璐可•T
        mute()
        updateSigniField()
        if isCurrentLrig(card) and isThereSigni("技艺代号 R•M•N", card.controller) and len(players[1].hand) <= 1:
            for key in SigniField: 
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]:  
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] +2000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 2000
                    SigniField[key][1].remove(card)
    
    def WD03_002(self, card, etype, echoice): #代号•皮璐璐可•G
        mute()
    
    def WD03_003(self, card, etype, echoice): #代号•皮璐璐可•M
        mute()
    
    def WD03_004(self, card, etype, echoice): #代号•皮璐璐可•K
        mute()
    
    def WD03_005(self, card, etype, echoice): #代号•皮璐璐可
        mute()
    
    def WD03_006(self, card, etype, echoice): #窥视分析
        mute()
        i = askInteger("宣言数字？", 1)
        if i == None:
            return False
        remoteCall(players[1], "showHand", [])
        #time.sleep(10)
        #players[1].hand.setVisibility = "all"
        rnd(1,1000)
        opponent_hand = [h for h in players[1].hand]
        s = askCard(opponent_hand)
        list = [c for c in players[1].hand
                if c.properties["等级"] == str(i)]
        remoteCall(players[1], "sendToCrashList", [list])
    
    def WD03_007(self, card, etype, echoice): #不可行动
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
                list.remove(s)
            else: break
        for signi in selected:
            remoteCall(players[1], "down", [signi])
    
    def WD03_008(self, card, etype, echoice): #双重抽卡
        mute()
        genDraw(2)
    
    def WD03_009(self, card, etype, echoice): #技艺代号 R•M•N
        mute()
        remoteCall(players[1], "randomDiscard", [])
    
    def WD03_010(self, card, etype, echoice): #技艺代号 D•R•S
        mute()
    
    def WD03_011(self, card, etype, echoice): #技艺代号 S•M•P
        mute()
        remoteCall(players[1], "showHand", [])
        #time.sleep(10)
        #players[1].hand.setVisibility = "all"
        rnd(1,1000)
        opponent_hand = [h for h in players[1].hand]
        s = card  #to initialize
        while s.properties["等级"] != "1" and s != None:
            s = askCard(opponent_hand)
            if s == None:
                return False
        remoteCall(players[1], "sendToCrash", [s])
        remoteCall(players[1], "hideHand", [])
            
    
    def WD03_012(self, card, etype, echoice): #技艺代号 J•V
        mute()
    
    def WD03_013(self, card, etype, echoice): #技艺代号 S•C
        mute()
    
    def WD03_014(self, card, etype, echoice): #技艺代号 R•F•R
        mute()
        genDraw(1)
        chooseDiscard()
    
    def WD03_015(self, card, etype, echoice): #真可惜
        mute()
        remoteCall(players[1], "randomDiscard", [])

    def PR_017(self, card, etype, echoice): #中枪 古罗马长矛
        mute()
        getMyLrig()
        if isInSigni(card) and myLrig.properties["角色"] == "小玉" and myLrig.properties["等级"] == "4":
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +10000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 10000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
    
    def PR_018(self, card, etype, echoice): #罗石 秘银
        mute()
        if etype == 1:
            forcedDiscard(card, 1)
        if etype == -1:
            updateSigniField()
            if isInSigni(card) and card.controller.isActivePlayer:
                for key in SigniField:
                    if SigniField[key][0]== card and card not in SigniField[key][1]:
                        SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +18000  #need FAQ
                        SigniField[key][1].append(card)
            else:
                for key in SigniField:
                    if SigniField[key][0] == card and card in SigniField[key][1]:
                        SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 18000) +int(card.properties["力量"])
                        SigniField[key][1].remove(card)
    
    def PR_019(self, card, etype, echoice): #珍宝
        mute()
        discard_list = []
        hand_list = [c for c in me.hand]
        s = card
        while s != None:
            s = askCard(hand_list)
            if s != None:
                discard_list.append(s)
                hand_list.remove(s)
        discardList(discard_list)
        genDraw(len(discard_list))
                
    
    def PR_020(self, card, etype, echoice): #增援
        mute()
        if echoice == 1:
            conditionSearch("主卡组", 1, ["SIGNI"], [], -1, 10, -1, 99999, [], [], [])
            if searched:
                searched[0].moveTo(me.hand)
        if echoice == 2:
            fromDeckSend("能量区", 2)
    
    def PR_040(self, card, etype, echoice): #多重
        mute()
        for e in echoice:
            if e == 1:
                getOppoLrig()
                oppoLrig.markers[attackDisableM] = 1
            if e == 2:
                for signi in table:
                    if isInSigni(signi) and signi.controller == players[1]:
                        remoteCall(players[1], "freeze", [signi])  #or freeze directly?
            if e == 3:
                bounce(card, 1, players[1], -1, 10)
            if e == 4:
                genDraw(2)
        
    def WD04_001(self, card, etype, echoice): #四之娘 绿姬
        mute()
        updateSigniField()
        if isCurrentLrig(card) and isThereSigni("幻兽 青龙", card.controller) and zoneNum("能量区", 7, card):
            for key in SigniField: 
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]:  
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] +2000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 2000
                    SigniField[key][1].remove(card)
        
    def WD04_002(self, card, etype, echoice): #三之娘 绿姬
        mute()
        
    def WD04_003(self, card, etype, echoice): #二之娘 绿姬
        mute()
        
    def WD04_004(self, card, etype, echoice): #一之娘 绿姬
        mute()
        
    def WD04_005(self, card, etype, echoice): #斗娘 绿姬
        mute()
        
    def WD04_006(self, card, etype, echoice): #意气扬扬
        mute()
        updateSigniField()
        if etype == 2:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller:  
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] +5000
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 5000
                    SigniField[key][1].remove(card)
        
    def WD04_007(self, card, etype, echoice): #再三再四
        mute()
        list = [c for c in table
                if isInEner(c)]
        selected = []
        for i in range(2):
            s = askCard(list)
            if s == None:
                break
            selected.append(s)
            list.remove(s)
        for l in selected:
            l.moveTo(me.hand)
        
    def WD04_008(self, card, etype, echoice): #付和雷同
        mute()
        conditionBan(card, 1, players[1], 12000, 99999, -1, 10, None, None)
        
    def WD04_009(self, card, etype, echoice): #幻兽 青龙
        mute()
        controllerSigni = [signi for signi in table
                           if signi.controller == card.controller
                           and isInSigni(signi)]
        flag = True
        for s in controllerSigni:
            if s.markers[Power] <15000:
                flag = False
        if len(controllerSigni) < 3:
            flag = False
        if isInSigni(card) and flag:
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[LancerM] += 1
                    SigniField[key][1].append(card)
                if SigniField[key][0]== card and card in SigniField[key][1]:
                    if battle_step == "attack_effect":
                        conditionBan(card, 1, players[1], -1, 99999, -1, 10, None, None)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[LancerM] -= 1
                    SigniField[key][1].remove(card)
                    
    def WD04_010(self, card, etype, echoice): #幻兽 朱雀小姐
        mute()
        if isInSigni(card) and card.markers[Power] >= 10000:
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[LancerM] += 1
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[LancerM] -= 1
                    SigniField[key][1].remove(card)
        
    def WD04_013(self, card, etype, echoice): #幻兽 小玄武
        mute()
        if card.markers[Power] >= 5000 and battle_step == "attack_effect":
            fromDeckSend("能量区", 1)
        
    def WD04_015(self, card, etype, echoice): #幻兽 白虎
        mute()
        if card.markers[Power] >= 3000 and battle_step == "attack_effect":
            fromDeckSend("能量区", 1)
        
    def WD04_016(self, card, etype, echoice): #侍从 Q2
        mute()
        
    def WD04_017(self, card, etype, echoice): #侍从 O2
        mute()
        
    def WD04_018(self, card, etype, echoice): #堕络
        mute()
        if etype == 2:
            if chooseDown(1, me):
                list = [osigni for osigni in table
                        if isInSigni(osigni)
                        and osigni.controller ==players[1]
                        and osigni.markers[Power] < chosen.markers[Power]]
                if not list:
                    return False
                s = askCard(list)
                if s == None:
                    return False
                remoteCall(players[1], "banish", [s])
        
    def WD05_001(self, card, etype, echoice): #狱卒阎魔 乌莉丝
        mute()
        updateSigniField()
        if isCurrentLrig(card) and isThereSigni("堕落炮女 缅茨姆", card.controller) and zoneNum("废弃区", 20, card):
            for key in SigniField: 
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]:  
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] +2000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 2000
                    SigniField[key][1].remove(card)
        
    def WD05_002(self, card, etype, echoice): #阿鼻阎魔 乌莉丝
        mute()
        
    def WD05_003(self, card, etype, echoice): #众合阎魔 乌莉丝
        mute()
        
    def WD05_004(self, card, etype, echoice): #灼热阎魔 乌莉丝
        mute()
        
    def WD05_005(self, card, etype, echoice): #阎魔 乌莉丝
        mute()
        
    def WD05_006(self, card, etype, echoice): #处刑时刻
        mute()
        powerChange(card, -7000, "players[1]")
        
    def WD05_007(self, card, etype, echoice): #永恒处刑
        mute()
        powerChange(card, -15000, "players[1]")
        
    def WD05_008(self, card, etype, echoice): #出墓
        mute()
        list = [c for c in me.piles["废弃区"] 
                if c.properties["类型"] == "SIGNI"]
        selected = []
        for i in range(3):
            s = askCard(list)
            if s == None:
                break
            selected.append(s)
            list.remove(s)
        for l in selected:
            l.moveTo(me.hand)
        
    def WD05_009(self, card, etype, echoice): #堕落炮女 缅茨姆
        mute()
        fromDeckSend("废弃区", 7)
        remoteCall(players[1], "fromDeckSend", ["废弃区", 7])
        
    def WD05_010(self, card, etype, echoice): #废恶象征 别西卜
        mute()
        
    def WD05_011(self, card, etype, echoice): #堕落炮女 卡莉
        mute()
        updateSigniField()
        if isInSigni(card) and zoneNum("废弃区", 10, card):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] += 5000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] -=  5000
                    SigniField[key][1].remove(card)
        
    def WD05_012(self, card, etype, echoice): #背德象征 科思莫
        mute()
        
    def WD05_013(self, card, etype, echoice): #小恶象征 小鬼
        mute()
        
    def WD05_014(self, card, etype, echoice): #堕落炮女 魅魔
        mute()
        fromDeckSend("废弃区", 3)
        
    def WD05_017(self, card, etype, echoice): #完全漆黑
        mute()
        powerChange(card, -4000, "players[1]")
        
    def WD05_018(self, card, etype, echoice): #回想的祝福
        mute()
        conditionSearch("废弃区", 1, ["SIGNI"], [], -1, 10, -1, 99999, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX02_001(self, card, etype, echoice): #金木犀之巫女 玉依姬
        mute()
        if etype == 1:
            conditionSearch("主卡组", 1, ["SIGNI"], [], -1, 10, -1, 99999, [], [], [])
            if searched:
                searched[0].moveTo(me.hand)
        if etype == 2:
            if echoice == 1:
                conditionBan(card, 1, players[1], -1, 7000, -1, 10, None, None)
            if echoice == 2:
                conditionBan(card, 1, players[1], 10000, 99999, -1, 10, None, None)
        
    def WX02_002(self, card, etype, echoice): #火鸟风月 游月·肆
        mute()
        myLife = [life for life in table
                  if isInLife(life)]
        if etype == 1:
            if not myLife:
                return False
            crash(1)
        if etype == 2:
            remoteCall(players[1], "crash", [1])
        
    def WX02_003(self, card, etype, echoice): #艾尔德拉×Ⅳ式
        mute()
        
    def WX02_004(self, card, etype, echoice): #无间阎魔 乌莉丝
        mute()
        powerChange(card, -10000, "players[1]")
        
    def WX02_005(self, card, etype, echoice): #纯白希望
        mute()
        updateSigniField()
#        if not me.isActivePlayer: requestInfo()
#        rnd(1,1000)
        if etype == 2:
            conditionSearch("主卡组", 2, ["SIGNI", "SIGNI"], [], -1, 2, -1, 99999, ["武装", "武装", "武器", "武器"], [], [])
            for s in searched: askPosition(s)
            for c in searched:
                c.markers[WhiteHope] = 1  #currently a workaround
#                if isInSigni(c): SigniField[getKey(s)][1].append(card)
#            sendInfo()
#                    updateSigniField()
#                    SigniField[getKey(s)][1].append(card)
#                    sendInfo()
        if etype == -3: mute()
#                if card in SigniField[key][1] and card.controller == me: 
#                    sendToCrash(SigniField[key][0])
#                elif card in SigniField[key][1] and card.controller != me:
#                    remoteCall(players[1], "sendToCrash", [SigniField[key][0]])
        
    def WX02_006(self, card, etype, echoice): #漆黑野望
        mute()
        if zoneNum("废弃区", 25, card):
            mySigni = [msigni for msigni in table
                       if isInSigni(msigni)
                       and msigni.controller == me]
            oppoSigni = [osigni for osigni in table
                         if isInSigni(osigni)
                         and osigni.controller == players[1]]
            banishList(mySigni)
            remoteCall(players[1], "banishList", [oppoSigni])
        
    def WX02_007(self, card, etype, echoice): #轰罪炎 游月·叁
        mute()
        updateSigniField()
        if etype == 2:
            if echoice == 1:
                conditionBan(card, 1, players[1], -1, 5000, -1, 10, None, None)
            if echoice == 2:
                for key in SigniField:
                    if SigniField[key][0].controller == card.controller:
                        SigniField[key][0].markers[Power] += 5000
                        SigniField[key][1].append(card)
        if etype == -3:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] -= 5000
                    SigniField[key][1].remove(card)
        
    def WX02_008(self, card, etype, echoice): #焰海 游月•贰
        mute()
        
    def WX02_009(self, card, etype, echoice): #焰 游月•壹
        mute()
        
    def WX02_010(self, card, etype, echoice): #艾尔德拉×Ⅲ式
        mute()
        
    def WX02_011(self, card, etype, echoice): #艾尔德拉×Ⅱ式
        mute()
        
    def WX02_012(self, card, etype, echoice): #艾尔德拉×Ⅰ式
        mute()
        
    def WX02_013(self, card, etype, echoice): #叫唤阎魔 乌莉丝
        mute()
        powerChange(card, -7000, "players[1]")
        
    def WX02_014(self, card, etype, echoice): #黑绳阎魔 乌莉丝
        mute()
        updateSigniField()
        if isCurrentLrig(card):
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card not in SigniField[key][1]\
                and SigniField[key][0].properties["颜色"] == card.properties["颜色"]:  #a trick to fulfill color requirement.
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] + 1000
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0].controller == card.controller and card in SigniField[key][1]\
                and SigniField[key][0].properties["颜色"] == card.properties["颜色"]:
                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 1000
                    SigniField[key][1].remove(card)
        
    def WX02_015(self, card, etype, echoice): #等活阎魔 乌莉丝
        mute()
        fromDeckSend("废弃区", 3)
        
    def WX02_016(self, card, etype, echoice): #哥特界限
        mute()
        bounce(card, 1, players[1], -1, 10)
    
    def WX02_017(self, card, etype, echoice): #气炎万丈
        mute()
        crash(1)
        if hasLifeBurst(crashed_to_check):
            list = [c for c in table
                    if isInSigni(c)
                    and c.controller == players[1]
                    and c.markers[Power] <= 10000]
            remoteCall(players[1], "banishList", [list])
        
    def WX02_018(self, card, etype, echoice): #火红柳绿
        mute()
        excavate(1)
        if isMine(exlist[0]) or isDiamond(exlist[0]):
            genDraw(2)
        
    def WX02_019(self, card, etype, echoice): #交织生命护甲
        mute()
        Life = [l for l in table 
                if isInLife(l)]
        if not Life:
            return
        indexlist = []
        for l in Life:
            indexlist.append(l.getIndex)
        o = max(indexlist)
        for l in Life:
            if l.getIndex == o:
                outmost = l
        x = outmost.position[0]
        y = outmost.position[1]
        outmost.moveTo(card.controller.hand)
        Life.remove(outmost)
        s = askCard([c for c in card.controller.hand])
        if s == None:
            return False
        s.moveToTable(x, y, forceFaceDown=True)
        
    def WX02_020(self, card, etype, echoice): #鲜血斩击
        mute()
        if fieldToCrash(1, me, -1, 99999, None):
            conditionBan(card, 1, players[1], -1, 99999, -1, 10, None, None)
        
    def WX02_021(self, card, etype, echoice): #先驱的大天使 大天使该隐
        mute()
        global searched
        if etype == 1:  #Arrival
            conditionSearch("主卡组", 1, ["SIGNI"], [], -1, 10, -1, 99999, ["天使"], [], [])
            if searched != []:
                if not askPosition(searched[0]):  
                    notify("玩家 {} 没有检索成功".format(card.controller))
            else:
                notify("玩家 {} 没有检索成功".format(card.controller))
            notify("玩家 {} 从卡组检索了 {} 到手卡".format(card.controller, card))
        else:  #Continuous--> because Archangel only has two types of effect.(i.e. either etype = -1 or etype = 1)
            updateSigniField()
            if isInSigni(card):  #to activate effect
                for key in SigniField:
                    if SigniField[key][0].controller == card.controller and isAngel(SigniField[key][0]) and card not in SigniField[key][1] :
                        SigniField[key][1].append(card)
            else:  #to cancel effect
                for key in SigniField:
                    if SigniField[key][0].controller == card.controller and isAngel(SigniField[key][0]) and card in SigniField[key][1]:
                        SigniField[key][1].remove(card)
                        notify("{} 的【常】效果不再适用。".format(card))

        
    def WX02_022(self, card, etype, echoice): #弩炮 狙击枪
        mute()
        updateSigniField()
        if etype == 1:
            list = [c for c in table
                    if isInSigni(c)
                    and c.controller == me]
            if not list:
                notify("没有对象")
                return False
            s = askCard(list)
            if s == None:
                return False
            doubleCrash(s, 0, 0)
            effectMemo(card, [card])  #to distinguish double crash from power change.
        if etype == -1:
            myLfie = [c for c in table
                      if isInLifeP(c, card.controller)]
            if isInSigni(card) and len(myLfie) <= 3:
                for key in SigniField:
                    if SigniField[key][0].controller == me and isWeapon(SigniField[key][0]) and card not in SigniField[key][1]:
                        SigniField[key][0].markers[Power] +=2000  #need FAQ
                        SigniField[key][1].append(card)
            else:
                for key in SigniField:
                    if SigniField[key][0] == card and card in SigniField[key][1]:
                        SigniField[key][0].markers[Power] -= 2000
                        SigniField[key][1].remove(card)
        if etype == -3:
            cancelDoubleCrash(card)

                    
    def WX02_023(self, card, etype, echoice): #幻水姬 丝派拉尔•卡米拉
        mute()
        updateSigniField()
        if etype == 1:
            genDraw(1)
        if etype == -1:
            if isInSigni(card) and handAdvantage(2, card):
                for key in SigniField:
                    if SigniField[key][0].controller == me and isWaterBeast(SigniField[key][0]) and card not in SigniField[key][1]:
                        SigniField[key][0].markers[Power] +=2000  #need FAQ
                        SigniField[key][1].append(card)
            else:
                for key in SigniField:
                    if SigniField[key][0] == card and card in SigniField[key][1]:
                        SigniField[key][0].markers[Power] -= 2000
                        SigniField[key][1].remove(card)
        
    def WX02_024(self, card, etype, echoice): #罗植姬 戈休·雅格尼丝
        mute()
        if etype == 1:
            conditionBan(card, 1, players[1], 15000, 99999, -1, 10, None, None)
        if etype == 2:
            fromDeckSend("能量区", 1)
        
    def WX02_025(self, card, etype, echoice): #恶魔姬 安娜•蜃影
        mute()
        if etype == 1:
            forcedToCrash(1, card.controller, -1, 99999, None, None)
        
    def WX02_026(self, card, etype, echoice): #愿望危机
        mute()
        if fieldToCrash(1, me, -1, 99999, "天使"):
            conditionSearch("主卡组", 2, ["SIGNI", "SIGNI"], [], -1, 10, -1, 99999, ["天使", "天使"], [], [])
            for signi in searched:
                askPosition(signi)
        
    def WX02_027(self, card, etype, echoice): #焦土的代价
        mute()
        global magictarget
        flag = False
        for c in magictarget:
            if not isInSigni(c):
                flag = True
        if flag:
            confirm("SIGNI的数量改变了，请重新选择对象")
            getTarget(card)
        for s in magictarget:
            if s.controller == card.controller:
                sendToCrash(s)
            else:
                remoteCall(players[1], "banish", [s])
        magictarget = []
        
    def WX02_028(self, card, etype, echoice): #谜言暗气
        mute()
        if etype == 2:
            getMyLrig()
            myLrig.highlight = EnigmaAura
            notify("{}获得了谜言暗气".format(myLrig))
        
    def WX02_029(self, card, etype, echoice): #宝具 御剑
        mute()
        conditionSearch("主卡组", 1, ["SIGNI"], [], -1, 10, -1, 99999, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX02_030(self, card, etype, echoice): #宝具 御镜
        mute()
        excavate(1)
        if isArmor(exlist[0]):
            exlist[0].moveTo(me.hand)
        
    def WX02_031(self, card, etype, echoice): #使其反跳
        mute()
        bounce(card, 1, players[1], -1, 10)
        
    def WX02_032(self, card, etype, echoice): #罗石 蛋白石
        mute()
        conditionBan(card, 1, None, -1, 7000, -1, 10, None, None)
        
    def WX02_033(self, card, etype, echoice): #罗石 红玉髓
        mute()
        excavate(1)
        if isMine(exlist[0]) or isDiamond(exlist[0]):
            exlist[0].moveTo(me.hand)
        
    def WX02_034(self, card, etype, echoice): #不希望的冲动
        mute()
        if isThereColor("红", card.controller, "能量区") and isThereColor("绿", me, "能量区"):
            conditionBan(card, 1, players[1], -1, 99999, -1, 10, None, None)
        
    def WX02_035(self, card, etype, echoice): #技艺代号 C·P·U
        mute()
        if askFreeze(card, -1, 10):
            genDraw(1)
        
        
    def WX02_036(self, card, etype, echoice): #技艺代号 G•A•B
        mute()
        excavate(1)
        if isElectric(exlist[0]):
            exlist[0].moveTo(me.hand)
        
    def WX02_037(self, card, etype, echoice): #飞溅
        mute()
        if conditionBan(card, 1, me, -1, 99999, -1, 10, "水兽", None):
            genDraw(2)
        
    def WX02_038(self, card, etype, echoice): #幻兽 雉
        mute()
        fromDeckSend("能量区", 2)
        
    def WX02_039(self, card, etype, echoice): #幻兽 八犬
        mute()
        excavate(1)
        if isAirBeast(exlist[0]) or isEarthBeast(exlist[0]):
            exlist[0].moveTo(me.hand)
        
    def WX02_040(self, card, etype, echoice): #着植
        mute()
        updateSigniField()
        if etype == 2:
            for key in SigniField:
                if isAirBeast(SigniField[key][0]) or isEarthBeast(SigniField[key][0]) or isPlant(SigniField[key][0]):
                    if SigniField[key][0].controller == card.controller:
                        SigniField[key][0].markers[LancerM] += 1
                        SigniField[key][1].append(card)
        if etype == -3:
            for key in SigniField:
                if isAirBeast(SigniField[key][0]) or isEarthBeast(SigniField[key][0]) or isPlant(SigniField[key][0]):
                    if SigniField[key][0].controller == card.controller and card in SigniField[key][1]:
                        SigniField[key][0].markers[LancerM] -= 1
                        SigniField[key][1].remove(card)
        
    def WX02_041(self, card, etype, echoice): #大损
        mute()
        conditionBan(card, 1, players[1], 10000, 99999, -1, 10, None, None)
        
    def WX02_042(self, card, etype, echoice): #反制代号 巴勒贝克
        mute()
        if etype == 2:
            conditionSearch("废弃区", 1, ["SIGNI"], [], -1, 10, -1, 99999, [], [], [])
            if searched:
                askPosition(searched[0])
        
    def WX02_043(self, card, etype, echoice): #反制代号 基西拉
        mute()
        excavate(3)
        list = [c for c in exlist
                if isAncientWeapon(c)]
        s = askCard(list)
        if s == None:
            return False
        s.moveTo(me.hand)
        
    def WX02_044(self, card, etype, echoice): #大罪缘由 巴力
        mute()
        excavate(1)
        if isDevil(exlist[0]):
            exlist[0].moveTo(me.hand)
        
    def WX02_045(self, card, etype, echoice): #献祭斩击
        mute()
        if conditionBan(card, 1, me, -1, 99999, -1, 10, None, None):
            conditionBan(card, 1, players[1], -1, 99999, -1, 10, None, None)
        
    def WX02_046(self, card, etype, echoice): #牺牲的微笑 丘雅耶尔
        mute()
        updateSigniField()
        if isInSigni(card) and isThereStype("天使", card.controller):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +12000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 12000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_047(self, card, etype, echoice): #虚构的爱情 希耶尔
        mute()
        updateSigniField()
        if isInSigni(card) and isThereStype("天使", card.controller):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +8000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 8000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_048(self, card, etype, echoice): #宝具 勾玉
        mute()
        excavate(3)
        orderExcavated()
        
    def WX02_049(self, card, etype, echoice): #博爱的聚集 萨尼耶尔
        mute()
        updateSigniField()
        if isInSigni(card) and isThereStype("天使", card.controller):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +5000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 5000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_050(self, card, etype, echoice): #刀剑本领
        mute()
        conditionSearch("主卡组", 2, ["SIGNI", "SIGNI"], [], -1, 10, -1, 99999, ["武装", "天使"], [],[])
        for signi in searched:
            signi.moveTo(me.hand)
        me.piles["主卡组"].shuffle()
        
    def WX02_051(self, card, etype, echoice): #轰炮 远射装置
        mute()
        if isInSigni(card) and isThereStype("武器", card.controller):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +12000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 12000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_052(self, card, etype, echoice): #爆炮 MP5
        mute()
        if isInSigni(card) and isThereStype("武器", card.controller):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +8000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 8000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_053(self, card, etype, echoice): #罗石 翡翠
        mute()
        conditionBan(card, 1, players[1], -1, 2000, -1, 10, None, None)
        
    def WX02_054(self, card, etype, echoice): #小炮 枪匠
        mute()
        if isInSigni(card) and isThereStype("武器", card.controller):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +5000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 5000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_055(self, card, etype, echoice): #光欲宝剑
        mute()
        updateSigniField()
        if etype == 2:
            list = [c for c in table
                    if isInSigni(c)
                    and c.controller == me
                    and (isMine(c) or isDiamond(c) or isWeapon(c))]
            if not list:
                notify("没有对象")
                return False
            s = askCard(list)
            if s == None:
                return False
            doubleCrash(s, 0, 0)
            SigniField[getKey(s)][1].append(card)
        if etype == -3:
            for key in SigniField:
                if card in SigniField[key][1]:
                    cancelDoubleCrash(SigniField[key][0])
                    SigniField[key][1].remove(card)
        
    def WX02_056(self, card, etype, echoice): #幻水 奥科特
        mute()
        updateSigniField()
        if isInSigni(card) and isThereStype("水兽", card.controller):
            for key in SigniField:   #we must write iteration here because of our structure handling Continuous effects.(we need a list to store "eternity")
                if SigniField[key][0]== card and card not in SigniField[key][1]:  #or we can write another function to find the list of a specific card.
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +12000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 12000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_057(self, card, etype, echoice): #幻水 珍珠
        mute()
        if isInSigni(card) and isThereStype("水兽", card.controller):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +8000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 8000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_058(self, card, etype, echoice): #技艺代号 M•M•R
        mute()
        genDraw(1)
        chooseDiscard()
        
    def WX02_059(self, card, etype, echoice): #幻水 科塞梅
        mute()
        if isInSigni(card) and isThereStype("水兽", card.controller):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +5000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 5000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_060(self, card, etype, echoice): #探寻者
        mute()
        conditionSearch("主卡组", 1, ["魔法"], [], None, None, None, None, [], [], [])
        if searched:
            searched[0].moveTo(me.hand)
        
    def WX02_061(self, card, etype, echoice): #蓝色收获
        mute()
        list = [c for c in table
                if isInSigni(c)
                and c.controller == me
                and (isWaterBeast(c) or isElectric(c))]
        genDraw(len(list))
        
    def WX02_062(self, card, etype, echoice): #罗植 葵小姐
        mute()
        if isInSigni(card) and isThereStype("植物", card.controller):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +12000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 12000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_063(self, card, etype, echoice): #罗植 莲
        mute()
        updateSigniField()
        if isInSigni(card) and isThereStype("植物", card.controller):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +8000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 8000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_064(self, card, etype, echoice): #幻兽 猴
        mute()
        fromDeckSend("能量区", 1)
        
    def WX02_065(self, card, etype, echoice): #罗植 虎尾兰
        mute()
        updateSigniField()
        if isInSigni(card) and isThereStype("植物", card.controller):
            for key in SigniField:   
                if SigniField[key][0]== card and card not in SigniField[key][1]: 
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +5000  
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 5000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_066(self, card, etype, echoice): #丰润
        mute()
        list = [c for c in table
                if isInSigni(c)
                and c.controller == me
                and (isAirBeast(c) or isEarthBeast(c) or isPlant(c))]
        fromDeckSend("能量区", len(list))
        
    def WX02_067(self, card, etype, echoice): #恶魔续发 莉莉丝
        mute()
        
    def WX02_068(self, card, etype, echoice): #恶魔勇武 摩莉甘
        mute()
        powerChange(card, -5000, "players[1]")
        
    def WX02_069(self, card, etype, echoice): #反制代号 星云
        mute()
        if etype == 2:
            askPosition(card)
        
    def WX02_070(self, card, etype, echoice): #真实死神 阿尼玛
        mute()
        fromDeckSend("废弃区", 3)
        
    def WX02_071(self, card, etype, echoice): #反制代号 德里
        mute()
        if etype == 2:
            askPosition(card)
        
    def WX02_072(self, card, etype, echoice): #反制代号 马丘比
        mute()
        powerChange(card, -5000, "players[1]")
        
    def WX02_073(self, card, etype, echoice): #反制代号 敌左反魔
        mute()
        #askPosition(card)
        
    def WX02_074(self, card, etype, echoice): #小恶忧郁 格里姆
        mute()
        if isInSigni(card) and zoneNum("废弃区", 2, card):
            for key in SigniField:
                if SigniField[key][0]== card and card not in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - int(card.properties["力量"])) +5000  #need FAQ
                    SigniField[key][1].append(card)
        else:
            for key in SigniField:
                if SigniField[key][0] == card and card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] = (SigniField[key][0].markers[Power] - 5000) +int(card.properties["力量"])
                    SigniField[key][1].remove(card)
        
    def WX02_075(self, card, etype, echoice): #造墓者
        mute()
        fromDeckSend("废弃区", 6)
        
    def WX02_077(self, card, etype, echoice): #侍从 T2
        mute()
        
    def WX02_078(self, card, etype, echoice): #侍从 D2
        mute()
