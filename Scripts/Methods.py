# -*- coding: utf-8 -*-  

'''
Created on 2014年8月13日

@author: SynTuner
'''

#---------------------------------------------------------------------------
# Flow & Status
#---------------------------------------------------------------------------

def tracePower(card):
    updateSigniField()
    for key in SigniField:
        if isContinuous(SigniField[key][0]): execEffect(SigniField[key][0], -1, 0)
        
def getEner():
    mute()
    EnerCards = [card for card in table 
                 if isInEner(card) == True 
                 and card.controller == me]
    #notify("玩家 {} 的能量数量为 {}".format(me, str(len(EnerCards))))
    me.counters['Energy'].value = len(EnerCards)
    
def getLife():
    mute()
    LifeCards = [card for card in table 
                 if isInLife(card) == True 
                 and card.controller == me]
    #notify("玩家 {} 的生命数量为 {}".format(me, str(len(LifeCards))))
    me.counters['Life'].value = len(LifeCards)
    
def getKey(card):
    updateSigniField()
    for k in SigniField:
        if SigniField[k][0] == card:
            return k
    return None
    
def getMyLrig():
    global myLrig
    list = [card for card in table
            if isInLrig(card)]
    index = []
    for card in list:
        index.append(card.getIndex)
    o = max(index)
    for card in list:
        if card.getIndex == o:
            myLrig = card
            
def getOppoLrig():
    global oppoLrig
    list = [card for card in table
            if card.properties["类型"] == "LRIG"
            and card.controller != me]
    index = []
    for card in list:
        index.append(card.getIndex)
    o = max(index)
    for card in list:
        if card.getIndex == o:
            oppoLrig = card
    #notify("{}".format(oppoLrig))
    
def summary():
    mute()
    getEner()
    getLife()
    EnerCards = [card for card in table
       if isInEner(card) == True
       and card.controller == me]
    #sum = dict.fromkeys(["白","黑","红","蓝","绿","无"],[])   #fatal: if list.append is used, python will pass the same value to each key.
    sum = {"白":[],"黑":[],"红":[],"蓝":[],"绿":[],"无":[]}  
    #notify(str(len(sum["白"])))  #debug
    for card in EnerCards:
        if card.properties["颜色"] == "白":
            sum["白"].append(card)
            #notify("1")
        elif card.properties["颜色"] == "黑":
            sum["黑"].append(card)
            #notify("2")
        elif card.properties["颜色"] =="红":
            sum["红"].append(card)
            #notify("3")
        elif card.properties["颜色"] == "蓝":
            sum["蓝"].append(card)
            #notify("4")
            #notify(str(len(sum["白"])))
        elif card.properties["颜色"] == "绿":
            sum["绿"].append(card)
            #notify("5")
        elif card.properties["颜色"] == "无":
            sum["无"].append(card)
            #notify("6")
        else: pass
    for key in sum:
        me.counters[key].value = len(sum[key])
        
#def refreshSigniField():
#    SigniField.clear()
#    getSigniField()
    
def getSigniField():  #[card object in the related signi field, [list of card objects which have effect on this card]]
    #global SigniField
    for card in table:
        if card.position == AleftS:
            SigniField["AleftS"] = [card, []]
        elif card.position == AmiddleS:
            SigniField["AmiddleS"] = [card, []]
        elif card.position == ArightS:
            SigniField["ArightS"] = [card, []]
        elif card.position == BleftS:
            SigniField["BleftS"] = [card, []]
        elif card.position == BmiddleS:
            SigniField["BmiddleS"] = [card, []]
        elif card.position == BrightS:
            SigniField["BrightS"] = [card, []]
            
def backSigniField():
    global OSigniField
    OSigniField = copy.deepcopy(SigniField)
                
#tested that same named cards on table are treated differently by OCTGN
def filterSigniField():  
    for key in OSigniField.keys():   #to prevent dictionary size from changing during iteration
        if OSigniField[key][0].group != table or OSigniField[key][0].position != eval(key):
            del OSigniField[key]

def updateSigniField():
    backSigniField()
    filterSigniField()
    SigniField.clear()
    getSigniField()
    SigniField.update(OSigniField)
    #if me.isActivePlayer:
    #    list = []
    #    for key in SigniField:
    #        list.append(SigniField[key][1])
    #    if list != []:
    #        send(list)
        
def receive(info):  #to receive the latest SigniField information from opponent.
    updateSigniField()
#    i = 0
    for key in SigniField:  #iteration is necessary, because OC cannot pass a dictionary with a mixture of card object and list(even we use setGlobalVariable()). If do so ,we get an error.
        for i in info:
            if key == i[0][0]:
                SigniField[key][1] = i[1]  #now we try to only pass the list, because the remote player is able to get cards information by his local function.
#    notify("收到了信息")
#        SigniField[key][1] = info[i] 
#        i = i + 1 
#    #notify("{}".format(info[0][0]))
    
def send(info):  #to pass the latest SigniField information to opponent.
    remoteCall(players[1], "receive", [info])
    
def sendInfo():
    list = []
    updateSigniField() ################
#    for key in SigniField:
#        list.append(SigniField[key][1])
    for key in SigniField:
        list.append([[key], SigniField[key][1]])  #must be [key]
    if list != []:
        send(list)
        
#def requestInfo(card, etype, echoice):
#    remoteCall(players[1], "replyAndExecute", [card, etype, echoice])
    
#def replyAndExecute(card, etype, echoice):
#    global INFO_REJECT
#    sendInfo()
#    INFO_REJECT = 1
#    functionName = card.properties["编号"] + "Handler"
#    remoteCall(players[1], functionName, [card])
    
#def WX01_024Handler(card):
#    powerChange(card, 5000, "all")
#    sendInfo()
#    remoteCall(players[1], "reconnect", [])
    
#def reconnect():
#    global INFO_REJECT
#    INFO_REJECT = 0
        
def setGlobal(hanayo, cain, gensou):  #these effects change the game rules.
    global hanayolv2
    global cainContinuous
    global gensouRed2
    if hanayo != None:
        hanayolv2 = hanayo
    if cain != None:
        cainContinuous = cain
    if gensou != None:
        gensouRed2 = gensou
        notify("受到了原枪效果的影响")
        
def effectMemo(card, targetlist):
    mute()
    global activatedDict
    activatedDict = {}
    activatedDict[card] = targetlist
        
def charge():
    mute()
    choice = confirm("要充能吗？")
    if choice:
        list = [card for card in table
            if card.properties["类型"] != "LRIG" 
            and card.controller ==me and not isInEner(card) and not isInLife(card)]
        h = [c for c in me.hand]
        for card in h:  #.extend failed.
            list.append(card)
        s = askCard(list)
        if s != None:
            if me.hasInvertedTable() == False:
                s.moveToTable(-290, 60)
            else:
                s.moveToTable(230, -150)
        tidy()  #notice that this command will trigger the event of onMoveCard
        
def attack(card):  #notice that we should not write "for card in table".
    mute()
    updateSigniField()
    global lrig_attacked_flag
    if phase != "attackphase":
        whisper("请先进入SIGNI攻击步骤")
        return False
    oppoLife = [life for life in table
                if isInLifeP(life, players[1])]
    global battle_step
    if card.markers[attackDisableM] != 0:
        notify("不能攻击")
        return False
    if lrig_attacked_flag == 1 and card.properties["类型"] == "SIGNI":
        whisper("LRIG已经攻击，不能再用SIGNI攻击")
        return False
    if not down(card): return False
    if card.properties["类型"] == "LRIG":
        lrig_attacked_flag = 1
        notify("{} 攻击".format(card))
    battle_step = "attack_effect"
    if card.highlight == ArcAura:
        choice = confirm("要把一只SIGNI放置到废弃区吗？")
        if choice:
            if fieldToCrash(1, me, -1, 99999, None):
                up(card)
    if card.highlight == EnigmaAura:
        choice = confirm("要把SIGNI放置到废弃区吗？")
        if choice: enigmaAuraHandler(card)
    if isAttackEffect(card): execEffect(card, -1, 0)
    if card.properties["颜色"] == "红" and isThereSigni("罗辉石 金刚珠玉", me):
        for key in SigniField:
            if SigniField[key][0].name == "罗辉石 金刚珠玉" and SigniField[key][0].controller == me:
                card.markers[Power] += 2000
                SigniField[getKey(card)][1].append(SigniField[key][0])
    battle_step = "attack"
    getOppoLrig()
    l = oppoLrig
    if card.properties["类型"] == "SIGNI":  #here
        for key in SigniField.keys():
            if SigniField[key][0] == card:
                loc = key
        if reg("left", loc):
            if reg("A",  loc):
                target = re.sub("Aleft","Bright",loc)
            else:
                target = re.sub("Bleft","Aright",loc)
        elif not reg('middle',loc):
            if reg('A',  loc):
                target = re.sub("Aright","Bleft",loc)
            else:
                target = re.sub("Bright","Aleft",loc)
        else:
            if reg('A',  loc):
                target = re.sub("A","B",loc)
            else:
                target = re.sub("B","A",loc)
#       notify(target)  #to here
        if SigniField.has_key(target):
            targetcard = SigniField[target][0]
            card.arrow(targetcard, True)
            notify("{} 攻击 {}".format(card, targetcard))
            if card.markers[Power] >= targetcard.markers[Power]:
                remoteCall(players[1], "banish",[targetcard])
                if card.markers[LancerM] != 0:
                    notify("{} 的枪兵效果发动。".format(card))
                    remoteCall(players[1], "crash",[1])
            else: pass
        else:
            card.arrow(l, True)
            notify("{} 直接攻击".format(card))
            if not oppoLife:
                notify("{} 获得了胜利。".format(me))
                return 
            if card.markers[DoubleCrashM] != 0:
                remoteCall(players[1], "crash",[2])
            else:
                remoteCall(players[1], "crash",[1])
    else:
        card.arrow(l, True)  #lrig's attack
        notify("{} 请等待对方选择防御。".format(me))
        remoteCall(players[1], "chooseGuard",[card])
        
def chooseGuard(lrig):
    mute()
    global hanayolv2
    if hanayolv2 == 1:
        list = [card for card in me.hand
            if isGuard(card) and int(card.properties["等级"]) > 2]
    else:
        list = [card for card in me.hand
                if isGuard(card)]
        myLife = [l for l in table
                  if isInLife(l)]
    if list == []:
        confirm("没有防御怪兽！")
        notify("{} 没有防御".format(me))
        if not myLife:
            notify("{} 获得了胜利".format(players[1]))
            return
        if lrig.markers[DoubleCrashM] != 0:
            crash(2)
        else:
            crash(1)
        remoteCall(players[1], "unlock", [])
    else:
        s = askCard(list)
        if s != None:  #7.23 1:17
            sendToCrash(s)
            remoteCall(players[1], "guardReply", [me, s])
        else:
            notify("{} 没有防御".format(me))
            if not myLife:
                notify("{} 获得了胜利".format(players[1]))
                return
            if lrig.markers[DoubleCrashM] != 0 :
                crash(2)
            else:
                crash(1)
        remoteCall(players[1], "unlock", [])
        
def guardReply(player, card):
    confirm("{} 使用了 {} 进行防御".format(player, card.name))
    
def magicStep1(card): #to pay cost
    mute()
    if me.hasInvertedTable() == False:
        checkzone = CheckZoneA
    else:
        checkzone = CheckZoneB
    global magictarget
    if payCost(card, 2):  #now we've got echoice.
        #if card.properties["类型"] == "魔法":
        card.moveToTable(checkzone[0],checkzone[1])
        card.isFaceUp = True
        rnd(1,1000)
        notify("{} 发动了魔法 {}，等待 {} 确认魔法切入".format(me, card, players[1]))
        magictarget = []
        getTarget(card)
        updateSigniField()
        if card.properties["颜色"] == "绿" and card.properties["类型"] == "魔法":
            for key in SigniField:
                if SigniField[key][0].name =="幻兽神 御先狐" and SigniField[key][0].controller == me:
                    fromDeckSend("能量区", 1)
        remoteCall(players[1], "askCutIn", [card, magictarget])
        setLock()
        
def getTarget(card):
    mute()
    global magictarget
    if card.name == "焦土的代价":
        oppoSigni = [osigni for osigni in table
                   if isInSigni(osigni)
                   and osigni.controller == players[1]
                   and affect(card, osigni)]
        mySigni = [msigni for msigni in table
                   if isInSigni(msigni)
                   and msigni.controller == me
                   and (isArmor(msigni) or isWeapon(msigni))]
        s = card
        os = None
        mselected = []
        oselected = []
        for i in range(len(oppoSigni)):
            confirm("选择要放置到废弃区的SIGNI")
            s = askCard(mySigni)
            if s != None:
                mselected.append(s)
                mySigni.remove(s)
            else: break
        for j in range(len(mselected)):
            confirm("选择要驱逐的SIGNI")
            while os == None and oppoSigni:
                os = askCard(oppoSigni)
                if os != None:
                    oselected.append(os)
                    oppoSigni.remove(os)
                else:
                    confirm("必须选择一只")
        magictarget = [m for m in table
                       if m in mselected
                       or m in oselected]
        for t in magictarget:
            notify("{} 选择了 {} 为对象。".format(card.controller, t))
            
def magicStep2(card, isAnti):  #to execute effect
    mute()
    unlock()
    if isAnti:
        notify("{} 被魔法反制，不处理效果".format(card))
        card.moveTo(me.piles["废弃区"])
        return False
    execEffect(card, 2, echoice)
    time.sleep(2)
    card.moveTo(me.piles["废弃区"])

def askCutIn(card, magictarget):
    mute()
    choice = confirm("要发动魔法切入的技艺吗？")
    if not choice:
        notify("{} 放弃了切入".format(me))
        remoteCall(players[1], "magicStep2", [card, False])
        return
    s = card  #to initialize
    arts = [art for art in me.piles["Lrig卡组"]
            if art.properties["类型"] == "技艺"
            and isCutIn(art)]
    s = askCard(arts)
    if s == None:
        remoteCall(players[1], "magicStep2", [card, False])
        return
    if activate(s, 2):
        if s.name == "魔法反制":
            remoteCall(players[1], "magicStep2", [card, True])
        else:
            remoteCall(players[1], "magicStep2", [card, False])
    else:
        remoteCall(players[1], "magicStep2", [card, False])

def tidy():
    mute()
    tidy_free = 1
    if me.hasInvertedTable() == False:    
        x = -290
        for card in table:
            if isInEner(card):
                card.orientation = 0
                card.moveToTable(x, 60) 
                x = x - 30
    else:
        x = 230
        for card in table:
            if isInEner(card):
                card.orientation = 0
                card.moveToTable(x, -150) 
                x = x + 30

#---------------------------------------------------------------------------
# Condition Judgment
#---------------------------------------------------------------------------

def reg(pat, sample):
    if pat == None:
        return True
    s = sample
    p = pat
    np = "got"
    news=re.sub(p,np,s)
    if news != s:
        return True
    else:
        return False    

def isInEner(card):
    mute()
    if me.hasInvertedTable() == False:
        Uboundx = EnerRangeA[1]
        Lboundx = EnerRangeA[0]
        Uboundy = EnerRangeA[3]
        Lboundy = EnerRangeA[2]
    else:
        Uboundx = EnerRangeB[1]
        Lboundx = EnerRangeB[0]
        Uboundy = EnerRangeB[3]
        Lboundy = EnerRangeB[2]
    if card.position[0] < Uboundx and card.position[0] > Lboundx and card.position[1]  < Uboundy and card.position[1]  > Lboundy:
        return True
    else:
        return False
    
def isInEnerP(card, player):  
    mute()
    if player.hasInvertedTable() == False:
        Uboundx = EnerRangeA[1]
        Lboundx = EnerRangeA[0]
        Uboundy = EnerRangeA[3]
        Lboundy = EnerRangeA[2]
    else:
        Uboundx = EnerRangeB[1]
        Lboundx = EnerRangeB[0]
        Uboundy = EnerRangeB[3]
        Lboundy = EnerRangeB[2]
    if card.position[0] < Uboundx and card.position[0] > Lboundx and card.position[1]  < Uboundy and card.position[1]  > Lboundy:
        return True
    else:
        return False
    
def isInLife(card):
    if me.hasInvertedTable() == False:
        if card.position[0] >= LifeRangeA[0]  and card.position[1] == LifeRangeA[1]:
            return True
        else:
            return False
    else:
        if card.position[0] <= LifeRangeB[0]  and card.position[1] == LifeRangeB[1]:
            return True
        else:
            return False
        
def isInLifeP(card, player):
    if player.hasInvertedTable() == False:
        if card.position[0] >= LifeRangeA[0]  and card.position[1] == LifeRangeA[1]:
            return True
        else:
            return False
    else:
        if card.position[0] <= LifeRangeB[0]  and card.position[1] == LifeRangeB[1]:
            return True
        else:
            return False
        
def isInSigni(card):
    updateSigniField()
    for key in SigniField:
        if SigniField[key][0] == card:
            return True
        else: pass
    return False
        
def isInCheck(card):
    #if me.hasInvertedTable() == False:
    #    checkzone = CheckZoneA
    #else:
    #    checkzone = CheckZoneB
    if card.position == CheckZoneA or card.position == CheckZoneB:
        return True
    else:
        return False

def isInLrig(card):
    global LrigZone
    if me.hasInvertedTable() == False:
        LrigZone = Alrig
    else:
        LrigZone = Blrig
    if card.position == LrigZone:
        return True
    else:
        return False
    
def isCurrentLrig(card):
    getMyLrig()
    getOppoLrig()
    if card == myLrig or card == oppoLrig:
        return True
    else:
        return False
    
def isThereStype(stype, player):  
    updateSigniField()
    cache = []
    for key in SigniField:
        if SigniField[key][0].controller== player and reg(stype, SigniField[key][0].properties["类别"]):
            cache.append(SigniField[key][0])
    if len(cache) >= 2:
        return True
    else:
        return False
    
def isThereStype1(stype, player):  
    updateSigniField()
    cache = []
    for key in SigniField:
        if SigniField[key][0].controller== player and reg(stype, SigniField[key][0].properties["类别"]):
            cache.append(SigniField[key][0])
    if len(cache) >= 1:
        return True
    else:
        return False
    
def isThereSigni(sname, player):  
    updateSigniField()
    cache = []
    for key in SigniField:
        if SigniField[key][0].controller== player and reg(sname, SigniField[key][0].name):
            cache.append(SigniField[key][0])
    if len(cache) >= 1:
        return True
    else:
        return False
    
def isThereLrig(lname, player):  #player may be dummy.
    getMyLrig()
    if myLrig.name == lname:
        return True
    else:
        return False
    
def isThereColor(color, player, zname):
    if zname == "能量区":
        cache = []
        myEner = [e for e in table
                      if isInEner(e)]
        for e in myEner:
            if e.properties["颜色"] == color:
                cache.append(e)
        if cache:
            return True
        else:
            return False
        
def limitCondition(card):  #bool
    getMyLrig()
    if card.properties["限定条件"] == "":
        return True
    if reg(myLrig.properties["角色"], card.properties["限定条件"]):
        return True
    elif myLrig.properties["角色"] =="花代/游月" and \
    (card.properties["限定条件"] == "花代限定" or card.properties["限定条件"] == "游月限定"):  #need a function to handle regular expressions with Chinese.
        return True
    else:
        return False
                
def isOmni(card):  #need to write a function to handle regular expression uniformly.
    sample = card.properties["技能"]
    pat = "【万花色】"
    newpat = "有"
    news=re.sub(pat,newpat,sample)
    if (news != sample or isThereSigni("原枪 源能枪", card.controller)) and card.name != "原枪 源能枪":
        return True
    else:
        return False
    
def isArrival(card):
    sample = card.properties["技能"]
    pat = "【出】"
    newpat = "有"
    news=re.sub(pat,newpat,sample)
    if news != sample:
        return True
    else:
        return False
    
def isContinuous(card):
    sample = card.properties["技能"]
    pat = "【常】"
    newpat = "有"
    news=re.sub(pat,newpat,sample)
    if news != sample:
        return True
    else:
        return False    
    
def isActivated(card):
    if reg("【起】", card.properties["技能"]):
        return True
    else:
        return False
    
def isCrashEffect(card):
    if reg("这只SIGNI存在于废弃区的场合才可以使用", card.properties["技能"]):
        return True
    else:
        return False
    
def isOneTurn(card):
    if reg("直到回合结束时为止", card.properties["技能"]) \
    or reg("这个回合中", card.properties["技能"]) \
    or reg("直到回合结束前", card.properties["技能"]) \
    or reg("直到回合结束为止", card.properties["技能"]) \
    or card.name == "纯白希望":
        return True
    else:
        return False
    
def isGuard(card):
    if card.properties["防御标记"] == "1":
        return True
    else:
        return False
    
def hasLifeBurst(card):
    if card.properties["生命迸发标记"] == "1" or isThereLrig("火鸟风月 游月·肆", card.controller):
        return True
    else:
        return False
    
def isAttackArt(card):
    if reg("【攻击阶段】", card.properties["技能"]):
        return True
    else:
        return False

def isAttackEffect(card):
    if reg("这只SIGNI攻击时", card.properties["技能"]):
        return True
    else:
        return False
    
def isMainArt(card):
    if reg("【主要阶段】", card.properties["技能"]):
        return True
    else:
        return False
    
def isCutIn(card):
    if reg("【魔法切入】", card.properties["技能"]):
        return True
    else:
        return False
    
def isAngel(card):
    if reg("天使", card.properties["类别"]):
        return True
    else:
        return False
    
def isDevil(card):
    if reg("恶魔", card.properties["类别"]):
        return True
    else:
        return False
    
def isAncientWeapon(card):
    if reg("古代兵器", card.properties["类别"]):
        return True
    else:
        return False
    
def isAirBeast(card):
    if reg("空兽", card.properties["类别"]):
        return True
    else:
        return False
    
def isEarthBeast(card):
    if reg("地兽", card.properties["类别"]):
        return True
    else:
        return False
    
def isWaterBeast(card):
    if reg("水兽", card.properties["类别"]):
        return True
    else:
        return False
    
def isElectric(card):
    if reg("电机", card.properties["类别"]):
        return True
    else:
        return False
    
def isPlant(card):
    if reg("植物", card.properties["类别"]):
        return True
    else:
        return False
    
def isMine(card):
    if reg("矿石", card.properties["类别"]):
        return True
    else:
        return False
    
def isDiamond(card):
    if reg("宝石", card.properties["类别"]):
        return True
    else:
        return False
    
def isWeapon(card):
    if reg("武器", card.properties["类别"]):
        return True
    else:
        return False
    
def isArmor(card):
    if reg("武装", card.properties["类别"]):
        return True
    else:
        return False
    
def handAdvantage(num, signi):
#    if signi.controller.isActivePlayer == False:
#        if len(signi.controller.hand) - num >= len(players[0].hand):
#            return True
#        else:
#            return False
#    else:
#        if len(signi.controller.hand) - num >= len(players[1].hand):
#            return True
#        else:
#            return False
    if signi.controller == me:  #make it consistent with the change of moveTrigger
        if len(signi.controller.hand) - num >= len(players[1].hand):
            return True
        else:
            return False
    else:
        if len(signi.controller.hand) - num >= len(players[0].hand):
            return True
        else:
            return False
        
def enerAdvantage(num, signi):
    controllerEner = [c for c in table 
                      if isInEnerP(c, signi.controller)]
#    if signi.controller.isActivePlayer == False:
#        oppoEner = [oc for oc in table
#                    if isInEnerP(oc, players[0])]
#    else:
#        oppoEner = [oc for oc in table
#                    if isInEnerP(oc, players[1])]
#    if len(controllerEner) - num >= len(oppoEner):
#        return True
#    else:
#        return False
    if signi.controller == me:
        oppoEner = [oc for oc in table
                    if isInEnerP(oc, players[1])]
    else:
        oppoEner = [oc for oc in table
                    if isInEnerP(oc, players[0])]
    if len(controllerEner) - num >= len(oppoEner):
        return True
    else:
        return False
    
def zoneNum(zname, num, card):
    cache = []
    if zname == "能量区":
        controllerEner = [c for c in table
                          if isInEnerP(c, card.controller)]
        if len(controllerEner) >= num:
            return True
        else:
            return False
    else:
        cache = [c for c in card.controller.piles[zname]]
        if len(cache) >= num:
            return True
        else:
            return False
  
#---------------------------------------------------------------------------
# Methods
#---------------------------------------------------------------------------

def down(card):
    mute()
    if card.orientation != 1:
        card.orientation = 1
        return True
    else: return False
    
def up(card):
    mute()
    if card.orientation != 0:
        card.orientation = 0
        return True
    else: return False

def genDraw(num):
    mute()
    if len(me.piles['主卡组']) == 0: return
    mute()
    cards = me.piles['主卡组'].top(num)
    for c in cards: c.moveTo(me.hand)
    notify("{} 抽了{}张卡.".format(me,num))

def randomDiscard():
    mute()
    card = me.hand.random()
    if card == None: return
    notify("{} 随机弃除了一张手卡.".format(me))
    card.moveTo(me.piles['废弃区'])

def discardList(list):
    mute()
    for card in list:
        card.moveTo(me.piles['废弃区'])
        notify("{} 弃除了 {}.".format(me, card))
        
def chooseDiscard():
    mute()
    handlist = [c for c in me.hand]
    s = None
    while s == None and handlist:
        s = askCard(handlist)
    if s == None: return False
    s.moveTo(me.piles['废弃区'])
    notify("{} 弃除了一张手卡.".format(me))
    
def forcedDiscard(card, num):
    mute()
    handlist = [c for c in me.hand]
    s = None
    selected = []
    for i in range(num):
        s = None
        while s == None and handlist:
            s = askCard(handlist)
        if s != None:  #in case of empty handlist.
            selected.append(s)
            handlist.remove(s)
    for c in selected: c.moveTo(me.piles['废弃区'])
    notify("{} 弃除了{}张手卡.".format(me, str(len(selected))))
    if len(me.hand) == 0 and card.name == "抢夺":
        remoteCall(card.controller, "genDraw", [1])
    if len(selected) < num: return False

def fromDeckSend(zname, num):
    global hammer
    hammer = []
    list = me.piles["主卡组"].top(num)
    if zname == "废弃区":
        for c in list:
            c.moveTo(me.piles['废弃区'])
            hammer.append(c)
        hammerHelper()
    elif zname == "能量区":
        for c in list: sendToEner(c)
    elif zname == "生命护甲":
        Life = [l for l in table 
                if isInLife(l)]
        indexlist = []
        i = 1
        for l in Life: indexlist.append(l.getIndex)
        o = max(indexlist)
        for l in Life:
            if l.getIndex == o:
                outmost = l
        for c in list:
            if not me.hasInvertedTable():
                c.moveToTable(outmost.position[0] + 30*i, outmost.position[1], forceFaceDown=True)
            else:
                c.moveToTable(outmost.position[0] - 30*i, outmost.position[1], forceFaceDown=True)
            i += 1
            
def hammerHelper():  #to handle Texas hammer's effect.
    global timing
    timing = "toCrash"
    for crashed in hammer:
        if crashed.properties["编号"] == "WX02_073":
            notify("{} 的常效果被触发".format(crashed))
            askPosition(crashed)
    timing = ""

def freeze(card, x = 0, y = 0):
    mute()
    card.markers[freezeMarker] += 1
    notify('{} 的 {} 被冻结，在下个竖置阶段不能竖置，效果持续至下个竖置阶段结束'.format(me, card))
        
def cancelFreeze(card):
    if card.markers[freezeMarker] != 0:
        card.markers[freezeMarker] -= 1
    if phase == "standphase":
        card.markers[freezeMarker] = 0

def askFreeze(card, llevel, ulevel):
    oppoSigni = [signi for signi in table
                 if isInSigni(signi)
                 and signi.controller == players[1]
                 and int(signi.properties["等级"]) >= llevel
                 and int(signi.properties["等级"]) <= ulevel]
    s = askCard(oppoSigni)
    if s == None:
        notify("没有满足条件的SIGNI！")
        return False
    freeze(s, 0, 0)

def doubleCrash(card, x = 0, y = 0):
    mute()
    card.markers[DoubleCrashM] += 1
    notify('{} 的 {} 获得双重击溃能力，一次直接攻击命中可将对手的2张生命护甲同时击溃'.format(me, card))

def cancelDoubleCrash(card):
    mute()
    card.markers[DoubleCrashM] -= 1
    notify('{} 的 {} 失去了双重击溃能力'.format(me, card))

def lancer(card, x = 0, y = 0):
    mute()
    card.markers[LancerM] += 1
    notify('{} 的【{}】获得枪兵能力，通过战斗将对手的SIGNI驱逐时，同时将对手的1张生命护甲击溃。'.format(me, card))

def cancelLancer(card):
    card.markers[LancerM] -= 1
    notify('{} 的 {} 失去了枪兵能力'.format(me, card))
    
def mainPhaseSend(card, x=0, y=0):
    global phase
    if card.properties["类型"] != "SIGNI":
        whisper("不是SIGNI，不能送入废弃区")
        return
    if phase == "mainphase":
        sendToCrash(card)
    else:
        whisper("不是主阶段，不能送入废弃区")
    
def sendToCrash(card):
    mute()
    card.moveTo(me.piles["废弃区"])
    notify("{} 被送入废弃区".format(card))
    
def sendToCrashList(list):
    mute()
    for card in list:
        sendToCrash(card)
    
def fieldToCrash(num, player, lbound, ubound, stype):
    mute()
    updateSigniField()
    list = [c for c in table
            if isInSigni(c)
            and c.controller == player
            and reg(stype, c.properties["类别"])
            and c.markers[Power] <= ubound
            and c.markers[Power] >= lbound]
    if len(list) < num:
        notify("没有足够满足条件的卡")
        return False
    selected = []
    for i in range(num):
        s = askCard(list)
        if s != None:
            selected.append(s)
            list.remove(s)
    if not selected: return False
    if player == me:
        sendToCrashList(selected)
        return True
    else:
        remoteCall(players[1], "sendToCrashList", [selected])
        
def enigmaAuraHandler(card):
    updateSigniField()
    list = [c for c in table
            if isInSigni(c)
            and c.controller == card.controller]
    selected = []
    s = []  #initialize
    while s != None and list:
        s = askCard(list)
        if s != None:
            selected.append(s)
            list.remove(s)
    sendToCrashList(selected)
    fromDeckSend("生命护甲", len(selected))

def forcedToCrash(num, player, lbound, ubound, stype, state):
    updateSigniField()
    list = [c for c in table
            if isInSigni(c)
            and c.controller == player
            and reg(stype, c.properties["类别"])
            and c.markers[Power] <= ubound
            and c.markers[Power] >= lbound
            and (state == None or c.markers[state] >= 1)]
    if len(list) < num:
        notify("没有足够满足条件的卡")
        return False
    selected = []
    for i in range(num):
        s = askCard(list)
        while s == None:
            confirm("必须选择一张")
            s = askCard(list)
        selected.append(s)
        list.remove(s)
    if player == me:
        sendToCrashList(selected)
    else:
        remoteCall(players[1], "sendToCrashList", [selected])

def decktoCrash(num):
    mute()
    if len(me.piles['主卡组']) == 0: return
    mute()
    cards = me.piles['主卡组'].top(num)
    for c in cards:
        c.moveTo(me.piles['废弃区'])
    notify("{} 从卡组顶将{}张卡放置到废弃区.".format(me,num))
    
def bounce(card, num, player, llevel, ulevel):
    updateSigniField()
    list = [c for c in table
            if isInSigni(c)
            and c.controller == player
            and int(c.properties["等级"]) >= llevel
            and int(c.properties["等级"]) <= ulevel
            and affect(card, c)]
    selected = []
    if not list:
        notify("没有满足条件的卡")
        return False
    for i in range(num):
        s = askCard(list)
        if s != None:
            selected.append(s)
            list.remove(s)
        else: break
    if player == me:
        fieldToHand(selected)
    else:
        remoteCall(players[1], "fieldToHand", [selected])
        
def search(num):
    mute()
    me.piles["主卡组"].setVisibility("me")
    global searched
    searched[:] = []
    for i in range(num):
        s = askCard([c for c in me.piles["主卡组"]])
        searched.append(s)
    for card in searched:  #to make sure Python could recognize properties.
        card.isFaceUp = True
    me.piles["主卡组"].setVisibility("None")
    me.piles["主卡组"].shuffle()
    #for card in selected:
      #  card.moveTo(me.hand)
        #notify("玩家 {} 从卡组检索了 {} 到手卡".format(me, card))
        #card.isFaceUp = False
        
def conditionSearch(zname, num, ctypelist, colorlist, llevel, ulevel, lbound, ubound, stypelist, snamelist, exclusion):  #don't forget to make order
    mute()
    flag = False
    if zname == "主卡组":
        me.piles[zname].setVisibility("me")
    global searched
    searched[:] = []
    while flag == False:
        searched[:] = []
        flag = True
        confirm("请选择符合条件的卡牌")
        ctype_copy = [ctype for ctype in ctypelist]
        color_copy = [color for color in colorlist]
        stype_copy = [stype for stype in stypelist]
        sname_copy = [sname for sname in snamelist]
        if zname != "能量区":
            pilecard = [c for c in me.piles[zname]]
        else:
            pilecard = [c for c in table
                        if isInEner(c)]
        for i in range(num):
            s = askCard(pilecard)
            if s != None:
                searched.append(s)
                pilecard.remove(s)
        for card in searched:  
            card.isFaceUp = True  #to make sure Python could recognize properties.
            update()
            #if len(searched) != num:
              #  flag = False
            if colorlist and card.properties["颜色"] not in color_copy:
                flag = False
                whisper("颜色不正确")
            elif colorlist and card.properties["颜色"] in color_copy:
                color_copy.remove(card.properties["颜色"])
                whisper("颜色通过")
            if ctypelist and card.properties["类型"] not in ctype_copy:
                flag = False
                whisper("类型不正确")
            elif ctypelist and card.properties["类型"] in ctype_copy:
                ctype_copy.remove(card.properties["类型"])
                whisper("类型通过")
            #if stypelist and card.properties["类别"] not in stype_copy:
            if stypelist:
                for t in stype_copy:
                    flag = False
                    if reg(t, card.properties["类别"]):
                        flag = True
                        stype_copy.remove(t)
                        break
                if not flag: whisper("类别不正确")
            #elif stypelist and card.properties["类别"] in stype_copy:
            #    stype_copy.remove(card.properties["类别"])
            #    notify("32")
            if llevel != None and (card.properties["等级"] == "" or int(card.properties["等级"]) < llevel):  #to handle magic card
                flag = False
                whisper("等级不正确（低）")
            if ulevel != None and (card.properties["等级"] == "" or int(card.properties["等级"]) > ulevel):
                flag = False
                whisper("等级不正确（高）")
            if lbound != None and (card.properties["力量"] == "" or int(card.properties["力量"]) < lbound):  #to handle magic card
                flag = False
                whisper("力量不正确（低）")
            if ubound != None and (card.properties["力量"] == "" or int(card.properties["力量"]) > ubound):
                flag = False
                whisper("等级不正确（高）")
            if snamelist and card.name not in sname_copy:
                flag = False
                whisper("卡名不正确")
            elif snamelist and card.name in sname_copy:
                sname_copy.remove(card.name)
                whisper("卡名通过")
            if exclusion and card.name in exclusion:
                flag = False
                whisper("除外条件不正确")
            if not flag: break  #to quit for
    if zname == "主卡组":
        me.piles[zname].setVisibility("None")            
        me.piles[zname].shuffle()
    for a in searched:
        a.isFaceUp = True
        rnd(1,1000)
        notify("{} 检索了 {}".format(a.controller, a))
        
def sendToEner(card):
    if me.hasInvertedTable() == False:
        card.moveToTable(-290, 60)
    else:
        card.moveToTable(230, -150)
    tidy()
    
def sendToEnerList(list):
    for card in list:
        if me.hasInvertedTable() == False:
            card.moveToTable(-290, 60)
        else:
            card.moveToTable(230, -150)
    
def fieldToHand(list):
    if me.hasInvertedTable() == False:
        checkzone = CheckZoneA
    else:
        checkzone = CheckZoneB
    for card in list:
        card.moveToTable(checkzone[0], checkzone[1])
        notify("{} 被返回了手牌".format(card))
        time.sleep(2)  #to force OC to wait until onCardMove event is executed. 
        card.moveTo(me.hand)
    
def crashLife():
    mute()
    getMyLrig()
    global crashed_to_check
    crashed_to_check = None
    if me.hasInvertedTable() == False:
        checkzone = CheckZoneA
    else:
        checkzone = CheckZoneB
    Life = [card for card in table
            if isInLife(card)]
    if not Life: return
    list = []
    for card in Life:
        list.append(card.getIndex)
    o = max(list)
    for card in Life:
        if card.getIndex == o:
            card.moveToTable(checkzone[0], checkzone[1])
            card.isFaceUp = True
            crashed_to_check = card
            if myLrig.name == "艾尔德拉×Ⅳ式":
                genDraw(1)

def banish(card):
    mute()
    global gensouRed2
    if gensouRed2 == 1:
        sendToCrash(card)
    else:
        sendToEner(card)
    if (isDevil(card) and isThereSigni("恶魔姬 安娜•蜃影", card.controller)) or card.name == "恶魔姬 安娜•蜃影":  #though I think it muse be the controller calls this function.
        remoteCall(players[1], "forcedBan", [card, 1, players[1], -1, 99999, None, None])
    #card.arrow(card, active = False)
    notify("{} 被驱逐".format(card))
    
def banishList(list):
    for card in list:
        banish(card)
        
def conditionBan(card, num, player, lbound, ubound, llevel, ulevel, stype, state):
    mute()
    updateSigniField()
    if player != None:
        list = [c for c in table
                if isInSigni(c)
                and c.controller == player
                and reg(stype, c.properties["类别"])
                and c.markers[Power] <= ubound
                and c.markers[Power] >= lbound
                and int(c.properties["等级"]) >= llevel
                and int(c.properties["等级"]) <= ulevel
                and (state == None or c.markers[state] >= 1)
                and affect(card, c)]
    else:
        list = [c for c in table
                if isInSigni(c)
                and reg(stype, c.properties["类别"])
                and c.markers[Power] <= ubound
                and c.markers[Power] >= lbound
                and int(c.properties["等级"]) >= llevel
                and int(c.properties["等级"]) <= ulevel
                and (state == None or c.markers[state] >= 1)
                and affect(card, c)]
    if len(list) < num:
        notify("没有足够满足条件的卡")
        return False
    selected = []
    for i in range(num):
        s = askCard(list)
        if s != None:
            selected.append(s)
            list.remove(s)
        #else:
        #    notify("{} 没有发动驱逐的效果。".format(me))
    for f in selected:  #filter
        if affect(card, f): pass
        else: selected.remove(f)
    for ff in selected:
        notify("{} 选择了 {}".format(me, ff))
    for fs in selected:
        if fs.controller == me: banish(fs)
        else: remoteCall(players[1], "banish", [fs])
    return True
        
def forcedBan(card, num, player, lbound, ubound, stype, state):
    mute()
    updateSigniField()
    list = [c for c in table
            if isInSigni(c)
            and c.controller == player
            and reg(stype, c.properties["类别"])
            and c.markers[Power] <= ubound
            and c.markers[Power] >= lbound
            and (state == None or c.markers[state] >= 1)]  #whether archangel can be targeted is a big question.
    if len(list) < num:
        notify("没有足够满足条件的卡")
        return False
    selected = []
    for i in range(num):
        s = askCard(list)
        while s == None:
            confirm("必须选择一张")
            s = askCard(list)
        selected.append(s)
        list.remove(s)
    for ff in selected:
        notify("{} 选择了 {}".format(me, ff))
    for f in selected:  #filter
        if affect(card, f): pass
        else: selected.remove(f)
    if player == me: banishList(selected)
    else: remoteCall(players[1], "banishList", [selected])
                
def crash(num):
    mute()
    if num == 1:
        crashLife()
        activateLB()
    elif num == 2:
        crashLife()
        crashLife()
        activateLB()
        
def effectCrashLife():
    mute()
    getMyLrig()
    global crashed_to_check
    crashed_to_check = None
    if me.hasInvertedTable() == False:
        checkzone = CheckZoneA
    else:
        checkzone = CheckZoneB
    Life = [card for card in table
            if isInLife(card)]
    list = []
    for card in Life:
        list.append(card.getIndex)
    o = max(list)
    for card in Life:
        if card.getIndex == o:
            card.moveToTable(checkzone[0], checkzone[1])
            card.isFaceUp = True
            crashed_to_check = card
            if myLrig.name == "艾尔德拉×Ⅳ式":
                genDraw(1)
    
def effectCrash(num):
    mute()
    if num == 1:
        effectCrashLife()
        activateLB()
    elif num == 2:
        effectCrashLife()
        effectCrashLife()
        activateLB()
    
#def conditionPowChange(concolor, constype, color, stype):
#    mySigni = [s for s in table
#                       if isInSigni(s)
#                       and s.controller == me]
#    colorlist = []
#    for ch in mySigni:  #check
#        if ch.properties["颜色"] == concolor:
#            colorlist.append(s)
#        #if ch.properties["颜色"] == "红":
#        #    reds.append(s)
#    if not colorlist:
#        updateSigniField()
#        #if isInSigni(card):
#        for key in SigniField:  #cancel
#            if SigniField[key][0].controller == me and card in SigniField[key][1]and \
#                (SigniField[key][0].properties["颜色"] == color or color ==None):
#                SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 3000
#                SigniField[key][1].remove(card)
#    else:
#        if card == myLrig:
#            for key in SigniField:  #activate
#                if SigniField[key][0].controller == me and card not in SigniField[key][1] and \
#                (SigniField[key][0].properties["颜色"] == color or color ==None):
#                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] + 3000
#                    SigniField[key][1].append(card)
#        else:
#            for key in SigniField:  #cancel
#                if SigniField[key][0].controller == me and card in SigniField[key][1] and \
#                (SigniField[key][0].properties["颜色"] == color or color ==None):
#                    SigniField[key][0].markers[Power] = SigniField[key][0].markers[Power] - 3000
#                    SigniField[key][1].remove(card)
        
def excavate(num):
    global exlist
    inter = me.piles["主卡组"].top(num)
    exlist = [e for e in inter]
    for c in exlist:
        c.isFaceUp = True
        rnd(1,1000)
        notify("{} 展示了 {}。".format(me, c))
        
def orderExcavated():
    global exlist
    confirm("请以从下往上的顺序选择卡片放回卡组。")
    list = []
    cache = [c for c in exlist]
    for i in exlist:
        s = askCard(cache)
        if s == None:
            exlist.reverse()
            for r in exlist:
                r.moveTo(me.piles["主卡组"])
                r.isFaceUp = False
                update()
            return False
        cache.remove(s)
        list.append(s)
    for l in list:
        l.moveTo(me.piles["主卡组"])
        l.isFaceUp = False
        update()
    notify("放回了卡组")
    
def powerChange(card, value, player):
        mute()
        global phase
        updateSigniField()
        if phase == "mainphase" or phase == "growphase" or phase == "attackphase" or phase == "artsphase":
            oppoSigni = [osigni for osigni in table
                       if isInSigni(osigni)
                       and osigni.controller == players[1]
                       and affect(card, osigni)]
            mySigni = [msigni for msigni in table
                       if isInSigni(msigni)
                       and msigni.controller == me]
            if player == "me":
                wait = mySigni
            elif player == "players[1]":
                wait = oppoSigni
            elif player == "all":
                wait = [signi for signi in table 
                        if isInSigni(signi)]
            if not wait:
                return False
            s = askCard(wait)
            if s == None: return
            if affect(card, s): pass  #filter
            else: return False
            for key in SigniField.keys():
                if SigniField[key][0] == s:
                    SigniField[key][1].append(card)
                    s.markers[Power] += value
                    break
        elif phase == "endphase":
            for key in SigniField.keys():
                if card in SigniField[key][1]:
                    SigniField[key][0].markers[Power] -= value
                    SigniField[key][1].remove(card)
        updateSigniField()
        for key in SigniField.keys():
            if SigniField[key][0].markers[Power] <= 0 and SigniField[key][0].controller == me:
                banish(SigniField[key][0])
            if SigniField[key][0].markers[Power] <= 0 and SigniField[key][0].controller == players[1]:
                remoteCall(players[1], "banish", [SigniField[key][0]])
            
def showHand():
    mute()
    me.hand.setVisibility("all")
    #me.hand.setController(players[1])
    update()
    
def hideHand():
    mute()
    me.hand.setVisibility("me")
    update()
    
def chooseDown(num, player):
    mute()
    global chosen
    chosen = None
    selected = []
    signilist = [signi for signi in table
               if isInSigni(signi)
               and signi.controller == player
               and signi.orientation != 1]
    if not signilist: return False
    confirm("选择要横置的SIGNI")
    for i in range(num):
        s = askCard(signilist)
        if s == None: break
        selected.append(s)
        signilist.remove(s)
    if not selected: return False
    if player == me:
        down(s)
        chosen = s
    else:
        remoteCall(players[1], "down", [s])
        chosen = s
    return True
        
def chooseUp(num, player):
    mute()
    global chosen
    chosen = None
    selected = []
    signilist = [signi for signi in table
               if isInSigni(signi)
               and signi.controller == player
               and signi.orientation != 0]
    if not signilist:
        return False
    confirm("选择要竖置的SIGNI")
    for i in range(num):
        s = askCard(signilist)
        if s == None: break
        selected.append(s)
        signilist.remove(s)
    if not selected: return False
    if player == me:
        up(s)
        chosen = s
    else:
        remoteCall(players[1], "up", [s])
        chosen = s
        
def affect(card, target):
    updateSigniField()
    if card.properties["类型"] == "LRIG":
        return True
    flag = False
    for c in SigniField[getKey(target)][1]:
        if c.name == "先驱的大天使 大天使该隐" and (c.controller != me or c.controller != card.controller):  #e.g. forcedBan()
            flag = True
            acard = c
            break
    if flag:
        notify("{} 因 {} 的效果不受影响。".format(target, acard))
        return False
    else:
        return True
    
def disaffect(card, target):
    updateSigniField()
    for key in SigniField:
        if card in SigniField[getKey(target)][1]:
            SigniField[getKey(target)][1].remove(card)
            
def uniformCost(etype, grow, Continuous, Arrival, activated, special, where_is_special):
        mute()
        global cost
        global echoice
        global specialcost
        #notify("done")
        growcost = grow
        if etype == -2:
            return False
        elif etype == -1:
            cost == Continuous
        elif etype == 0:  #to grow
            cost = grow
        elif etype == 1:  #to activate Arrival effect
            cost = Arrival
            if where_is_special == 1: specialcost = special
        elif etype == 2:
            cost = activated
            if where_is_special == 2: specialcost = special
    
#---------------------------------------------------------------------------
# To be announced
#---------------------------------------------------------------------------
        
def openFAQ(group, x=0, y=0):
    openUrl('http://www.takaratomy.co.jp/products/wixoss/card/index.php')
    
def viewProperties(card, x=0, y=0):
    confirm("{} 的类别为 {} \n限定条件为 {} \n效果为 {} \n生命迸发为 {}".format(card.name, card.properties["类别"], card.properties["限定条件"], card.properties["技能"], card.properties["生命迸发能力"]))
    
def powerHandler(card, target, value, way_of_change):  #next version.  Aims to uniformly handle SIGNI's power change.
    mute()
#---------------------------------------------------------------------------
# Card effect
#---------------------------------------------------------------------------