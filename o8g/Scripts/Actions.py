# -*- coding: utf-8 -*-  

#This is a Python script for trading card game Wixoss based on OCTGN platform. We wrote
#it for learning certain skills and game rules. Please do not use it for commercial purpose 
#without permission.
#
#Scripts Copyright (C) 2014  Minchao Wu
#
#Created by SynTuner 2014.07.05 
#
#Revised by SynTuner 2014.08.13
#
#Cards data processing: 指尖上的青蛙 bunlion
#
#Pictures of cards: たいほう  藤宫游月  絕對絕望·すみつき
#
#Translation: THE一灭寂组  Wixoss卡图中文化小组
#
#Testing: SynTuner  无限汉堡包
#
#A version of script with no automation and which is based on OCTGN2 was created by 
#海落樱·坦格里安 2014.05.19 , revised by SynTuner 2014.05.23, and 咲·saki was responsible for 
#cards data processing.
#
#**海落樱·坦格里安 and 咲·saki are no longer the members of this project after 30 May 2014. 
#   We show full respect for their previous work.
#

#Permission is granted to anyone to use this script for noncommercial purpose, subject to the following restrictions:
#
#   1. The origin of this script must not be misrepresented; you
#      must not claim that you wrote the original script. If you use
#      this script in a product, an acknowledgment in the product
#      documentation would be appreciated but is not required.
#
#   2. Altered source versions must be plainly marked as such, and
#      must not be misrepresented as being the original script.
#
#   3. This notice may not be removed or altered from any source
#      distribution.

import re
import copy
import time

Gold = ("Gold", "01ecf94f-c408-4e43-8984-211fbdc25001")
Power = ("Power", "00000000-0000-0000-0000-000000000001")
freezeMarker = ("冻结", "00000000-0000-0000-0000-000000000002")
DoubleCrashM = ("双重击溃","00000000-0000-0000-0000-000000000004")
LancerM = ("枪兵","00000000-0000-0000-0000-000000000005")
attackDisableM = ("不能攻击","00000000-0000-0000-0000-000000000003")
WhiteHope = ("纯白希望", "00000000-0000-0000-0000-000000000001")

#---------------------------------------------------------------------------
# Constants
#---------------------------------------------------------------------------

ArcAura = "#ffffff" #white
EnigmaAura = "#000000"  #black
LancerColor  = "#3cb371"  #SpringGreen

AleftS = (-150,50) 
AmiddleS = (-30,50)
ArightS = (90,50)
Alrig = (-30,160) 

BleftS = (90,-140)
BmiddleS = (-30,-140)
BrightS = (-150,-140)
Blrig = (-30,-250) 

#EnerRangeA = [-600, -270, 40, 150]
EnerRangeA = [-1000, -270, 40, 150]  #low bound is expanded in case of green's energy overcharge.
#EnerRangeB = [210, 540, -240, -130]
EnerRangeB = [210, 940, -240, -130]  #the same reason.
LifeRangeA = [180, 160]
LifeRangeB = [-240, -250]

CheckZoneA = (-150, 160)
CheckZoneB = (90, -250)

#---------------------------------------------------------------------------
# Global Variables
#---------------------------------------------------------------------------
SigniField = {}
OSigniField = {}

LrigZone = (0,0)

phase = ""
battle_step = ""  #currently we have "attack_effect"
timing = ""
lock = 0

cost = []
specialcost = {}
echoice = 0

myLrig = None
oppoLrig = None
chosen = None

magictarget = []

hanayolv2 = 0  #花代
cainContinuous =0  #该隐
gensouRed2 = 0  #原枪
plant = 0  #着植

activatedDict = {}
exlist = []
searched = []
hammer = []  # to handle Texas Hammer.
crashed_to_check = None

arrival_limit = 0

lrig_attacked_flag = 0

#---------------------------------------------------------------------------
# Phase
#---------------------------------------------------------------------------

def helloworld():
    mute()
    notify("夢限少女 {}: Open!".format(me))
    
def setTurn():
    players[1].setActivePlayer()

def decide(group, x, y ):
    mute()
    if turnNumber() >= 1: return
    if not me.hasInvertedTable():
        n = rnd(1, 2)
        if n == 1:
            notify("玩家 {} 先攻，玩家 {} 后攻。".format(me, players[1]))
            remoteCall(players[1], "setTurn", [])
        else:
            notify("玩家 {} 先攻，玩家 {} 后攻。".format(players[1], me))
            setTurn()

def standPhase(group, x = 0, y = 0):
    mute()
    global phase
    global plant
    phase = "standphase"
    updateSigniField()
    notify("--------对战对手请注意--------：\n 玩家 {} 宣告：进入【竖置阶段】".format(me))
    for card in table:
        if card.markers[freezeMarker] == 0 and card.controller == me and isInEner(card) == False:
            card.orientation = 0
        else:
            card.markers[freezeMarker] = 0
        if plant == 1 and isInSigni(card) and card.controller == me:
            card.markers[LancerM] += 1
    notify("玩家 {} 竖置了其所有可竖置卡".format(me))

def drawPhase(group, x = 0, y = 0):
    mute()
    global phase
    phase = "drawphase"
    updateSigniField()
    notify("--------对战对手请注意--------\n 玩家 {} 宣告：进入【抽卡阶段】".format(me))
    if turnNumber() == 1: genDraw(1)
    else: genDraw(2)

def chargePhase(group, x = 0, y = 0):
    mute()
    global phase
    phase = "chargephase"
    updateSigniField()
    notify("--------对战对手请注意--------\n 玩家 {} 宣告：进入【充能阶段】".format(me))
    charge()
    updateSigniField()

def growPhase(group, x = 0, y = 0):
    mute()
    global phase
    phase = "growphase"
    updateSigniField()
    getMyLrig()
    if myLrig.name == "轰炎 花代•贰改":
        notify("由于轰炎 花代•贰改的效果，成长阶段被跳过。")
        pass
    else:
        notify("--------对战对手请注意--------\n 玩家 {} 宣告：进入【成长阶段】".format(me))
        getMyLrig()
        choice = confirm("要成长吗？")
        if choice:
            list = [card for card in me.piles["Lrig卡组"]
                    if card.properties["类型"] == "LRIG"
                    and int(card.properties["等级"]) <= int(myLrig.properties["等级"]) + 1
                    and card.name != myLrig.name
                    and (reg(myLrig.properties["角色"], card.properties["角色"]) or reg(card.properties["角色"], myLrig.properties["角色"]))]
            s = askCard(list)
            if s != None:
                if payCost(s, 0): s.moveToTable(LrigZone[0], LrigZone[1])
                else: notify("没有成长")
        getMyLrig()
        mySigni = [c for c in table
                   if isInSigni(c)
                   and c.controller == me]
        for signi in mySigni:
            if int(signi.properties["等级"]) > int(myLrig.properties["等级"]):
                notify("{} 的等级超过 {} 的等级，送去废弃区。".format(signi, myLrig))
                sendToCrash(signi)
                mySigni.remove(signi)
        sum = 0
        for r in mySigni:
            sum = sum + int(r.properties["等级"])
        tocrash = None
        while sum > int(myLrig.properties["界限"]):
            whisper("场上SIGNI等级合计将超过 {} 的界限，请选择送去废弃区的SIGNI。".format(myLrig))
            while tocrash == None:
                tocrash = askCard(mySigni)
                if tocrash != None:
                    sendToCrash(tocrash)
                    mySigni.remove(tocrash)
            sum = 0
            for r in mySigni:
                sum = sum + int(r.properties["等级"])

def mainPhase(group, x = 0, y = 0):
    mute()
    global phase
    phase = "mainphase"
    updateSigniField()
    notify("--------对战对手请注意--------\n 玩家 {} 宣告：进入【主要阶段】".format(me))

def artsPhase(group, x = 0, y = 0):
    mute()
    if lock == 1:
        confirm("请等待对方响应")
        return
    if turnNumber() == 1:
        notify("第一回合没有攻击阶段")
        return
    notify("--------对战对手请注意--------\n 玩家 {} 宣告：进入【攻击阶段：技艺使用步骤】".format(me))
    global phase
    phase = "artsphase"
    updateSigniField()
    remoteCall(players[1], "setPhase", [phase])
    castArt()
    
def attackPhase(group, x = 0, y = 0):
    mute()
    if turnNumber() == 1:
        notify("第一回合没有攻击阶段")
        return
    notify("--------对战对手请注意--------\n 玩家 {} 宣告：进入【攻击阶段：SIGNI攻击步骤】".format(me))
    global phase
    phase = "attackphase"
    updateSigniField()
    
def endPhase(group, x = 0, y = 0):
    mute()
    global phase
    global plant
    global lrig_attacked_flag
    getMyLrig()
    getOppoLrig()
    tocancel =[]
    phase = "endphase"
    for card in table:
        card.arrow(card, False)
        card.highlight = None
    notify("--------对战对手请注意--------\n 玩家 {} 宣告：【回合结束】".format(me))
    updateSigniField()
    for key in SigniField.keys():  #now we may always try to call activatedDict rather than add cards to effect slot except for Continuous effects.
        if key in SigniField:
            if plant == 1 and SigniField[key][0].markers[LancerM] > 0:  #to cancel plant
                SigniField[key][0].markers[LancerM] -= 1
            l = len(SigniField[key][1])
            for i in range(l):
                if isOneTurn(SigniField[key][1][i]): tocancel.append(SigniField[key][1][i])
            for t in tocancel: execEffect(t, -3, 0)  #to cancel its effect
    for ac in activatedDict: execEffect(ac, -3, 0)
    activatedDict.clear()
    for key in SigniField:  # in fact we do not need key due to the workaround
        if SigniField[key][0].markers[WhiteHope] != 0 and SigniField[key][0].controller == me:
            sendToCrash(SigniField[key][0])
        elif SigniField[key][0].markers[WhiteHope] != 0 and SigniField[key][0].controller != me:
            remoteCall(players[1], "sendToCrash", [SigniField[key][0]])
    oppoLrig.markers[attackDisableM] = 0  #workaround
    myLrig.markers[attackDisableM] = 0
    updateSigniField()
    plant = 0
    lrig_attacked_flag = 0
    sendInfo()
    while len(me.hand) > 6:
        confirm("手牌超过6张上限，舍弃手牌")
        s = askCard([h for h in me.hand])
        if s != None: sendToCrash(s)
    players[1].setActivePlayer()
    update()
    notify("{} passes the turn to {}.".format(me, players[1]))
    #for key in SigniField:  #to check Continuous effect
    #    if isContinuous(SigniField[key][0]) and SigniField[key][0].controller == me:
    #        activateContinuous(SigniField[key][0])
    #        notify("{} 的【常】效果适用。".format(SigniField[key][0]))
    
def setPhase(p):
    global phase
    phase = p
        
#---------------------------------------------------------------------------
# Costs and effects
#---------------------------------------------------------------------------

def getCost(card, etype):
    global cost
    global specialcost
    cost = []
    specialcost = {}
    getattr(CardCost(), card.properties["编号"])(card, etype)
    updateSigniField()
    if card.properties["颜色"] == "蓝" and card.properties["类型"] == "魔法":
        for key in SigniField:
            if SigniField[key][0].name =="核心代号 V•A•C" and "无" in cost:
                cost.remove("无")
                
def payCost(card, etype):
    getCost(card, etype)
    if etype == -2:  #failed to activate. 0 means growing, 1 means Arrival, 2 means activated, -1 means Continuous effect.
        return False
    ener = [e for e in table
            if isInEner(e)]
    selected = []
    for color in cost:
        confirm("请支付{}色费用！".format(color))
        if color != "无":
            list = [e for e in ener
                    if e.properties["颜色"] == color
                    or isOmni(e)]
            if list == []:
                confirm("没有{}色能量！".format(color))
            s = askCard(list)
            if s == None:
                notify("没有完成费用支付")
                return False
        else:
            list = [e for e in ener]
            if list == []:
                confirm("没有足够能量！")
            s = askCard(list)
            if s == None:
                notify("没有完成费用支付")
                return False
        ener.remove(s)
        selected.append(s)
    if paySpecialCost(card, etype):
        #if len(selected) == len(cost):  # is this necessary?
        for scard in selected:
            scard.moveTo(me.piles["废弃区"])
        return True
        #else:  #impossible,because if unequal, the function must have already returned false.
          #  return False
    else: return False
    
def paySpecialCost(card, etype):
    #getCost(card, etype)
    got = []
    for key in specialcost.keys():
        notify(key)
    if specialcost.has_key("Discard"):
        list = [c for c in me.hand]
        wait = []
        if specialcost["Discard"].has_key("color"):
            list = [c for c in list
                    if c.properties["颜色"] == specialcost["Discard"]["color"]]
            if not list: return False
        if specialcost["Discard"].has_key("ctype"):
            list = [c for c in list
                    if c.properties["类型"] == specialcost["Discard"]["ctype"]]
            if not list: return False
        if specialcost["Discard"].has_key("signiclass"):
            for w in list:  #w:card to be checked
                for t in specialcost["Discard"]["signiclass"]:  #t:class needed
                    if reg(t, w.properties["类别"]):
                        wait.append(w)
            if not wait: return False  #no card satisfied to be cost.
        if wait != []:  #which means that cards of specific classes must be discarded
            for i in range(specialcost["Discard"]["qty"]):
                s = askCard(wait)
                if s != None:
                    got.append(s)
                    wait.remove(s)
                else:
                    return False
            #discardList(selected)
            #return True
        else:
            for i in range(specialcost["Discard"]["qty"]):
                s = askCard(list)
                if s != None:
                    got.append(s)
                    list.remove(s)
                else:
                    return False
            #discardList(selected)
            #return True
    if specialcost.has_key("Down"):
        if specialcost["Down"].has_key("target"):  #need more examples and packages.
            if specialcost["Down"]["target"] == "self":
                down_target = card
            elif specialcost["Down"]["target"] == "植物":
                down_list = [signi for signi in table
                             if isInSigni(signi)
                             and isPlant(signi)
                             and signi.controller == me
                             and signi.orientation == 0]
                s = askCard(down_list)
                if s == None:
                    return False
                down_target = s
        if down(down_target):
            if discardList:
                discardList(got)
                return True
        else:
            notify("无法横置")
            return False
    discardList(got)
    return True

def execEffect(card, etype, echoice):
    getattr(CardEffects(), card.properties["编号"])(card, etype, echoice)
    if not card.controller.piles["主卡组"]:
        rebuild()
    if not players[1].piles["主卡组"]:
        remoteCall(players[1], "rebuild", [])
    if me.isActivePlayer:
        updateSigniField()
        sendInfo()     
    
def execLB(card):
    getattr(LifeBurst(), card.properties["编号"])(card)
    
def menuActivate(card, x=0, y=0):
    if phase != "mainphase":
        whisper("不是主阶段，不能发动【起】效果")
        return
    activate(card, x = 0, y = 0)

def activate(card, x = 0, y = 0):
    mute()
    if card.properties["类型"] == "SIGNI" and phase != "mainphase":
        whisper("不是主阶段，不能发动【起】效果")
        return False
    if card.properties["类型"] == "SIGNI" and not isActivated(card):
        whisper("{} 没有【起】效果，不能发动".format(card))
        return False
    if me.hasInvertedTable() == False:
        checkzone = CheckZoneA
    else:
        checkzone = CheckZoneB
    global echoice
    echoice = 0
    if payCost(card, 2):  #now we've got echoice.
      #  if card.properties["类型"] == "魔法":
      #      card.moveToTable(checkzone[0],checkzone[1])
      #      execEffect(card, 2, echoice)
      #      time.sleep(2)
      #      card.moveTo(me.piles["废弃区"])
        if card.properties["类型"] == "技艺":
            me.piles["Lrig卡组"].setVisibility("None")  #if visibility == me, python could not recognize properties.
            card.isFaceUp = True
            rnd(1,1000)
            notify("{} 发动了技艺 {}".format(me, card))
            card.moveToTable(checkzone[0],checkzone[1])
            execEffect(card, 2, echoice)
            time.sleep(2)
            card.moveTo(me.piles["Lrig废弃区"])
            me.piles["Lrig卡组"].setVisibility("me")
        else:
            notify("{} 发动了 {} 的【起】效果".format(me, card))
            execEffect(card, 2, echoice)
        return True
    else: return False
    #echoice = 0
    tracePower(card)
    
def fromCrashActivate(group, x=0, y=0):
    if lock == 1:
        confirm("请等待对方响应")
        return
    if phase != "mainphase":
        whisper("不是主阶段，不能发动")
        return False
    list = [c for c in me.piles["废弃区"]
            if isCrashEffect(c)]
    if list:
        s = askCard(list)
        if s == None: return
        activate(s, 2, 0)
    
def activateContinuous(card):
    mute()
    global echoice
    echoice = 0
    payCost(card, -1)
    execEffect(card, -1, echoice)
    tracePower(card)
    
def activateArrival(card):
    mute()
    global echoice
    echoice = 0
    if payCost(card, 1):
        execEffect(card, 1, echoice)
    tracePower(card)
    
def activateLB():
    mute()
    if me.hasInvertedTable() == False:
        checkzone = CheckZoneA
    else:
        checkzone = CheckZoneB
    wait = []
    lb = []
    for card in table:
        if card.position == checkzone and card.properties["类型"] != "技艺":
            wait.append(card)
    for w in wait:
        if hasLifeBurst(w): lb.append(w)
    if lb !=[]:
        l = len(lb)
        for i in range(l):
            confirm("请选择使用生命迸发效果的卡，不发请关闭选卡界面。")
            s = askCard(lb)
            if s != None:
                if isThereLrig("火鸟风月 游月·肆", me):
                    fromDeckSend("能量区", 1)
                execLB(s)
                notify("{} 的生命迸发发动".format(s))
                sendToEner(s)
                lb.remove(s)
                wait.remove(s)
            else: pass
    for r in wait: sendToEner(r)
    tracePower(card)
    
#---------------------------------------------------------------------------
# Hand Actions
#---------------------------------------------------------------------------
    
#def cast(card, x=0, y=0):
#    if lock != 1:
#        if card.properties["类型"] == "SIGNI":
#            askPosition(card)
    
def cast(card, x = 0, y = 0):
    if lock != 1:  #to prevent players from using any command while they are waiting for another player's response. INCOMPLETE.
        if card.properties["类型"] == "SIGNI":
            askPosition(card)
        elif card.properties["类型"] == "魔法" and card.name != "情况糟糕":
            magicStep1(card)
        elif card.name == "情况糟糕":
            if len(players[1].hand) > 0: whisper("对方手牌不为0，不能发动。")
            else: magicStep1(card)
            
def castMagic(card, x = 0, y = 0):
    if lock != 1:
        if card.properties["类型"] == "魔法" and card.name != "情况糟糕":
            activate(card, 0, 0)
        elif card.name == "情况糟糕":
            if len(players[1].hand) > 0: whisper("对方手牌不为0，不能发动。")
            else: activate(card, 0, 0)
        else: whisper("{} 不是魔法！".format(card))
            
def mainArt(group, x, y):
    if lock == 1:
        confirm("请等待对方响应")
        return
    castArt()
            
def castArt():
    global phase
    if phase == "mainphase":
        mainArt = [card for card in me.piles["Lrig卡组"]
                if card.properties["类型"] == "技艺"
                and isMainArt(card)]
        if mainArt == []: whisper("没有能发动的技艺卡。")
        else:
            a = askCard(mainArt)
            if a != None: activate(a, 2)
    elif phase == "artsphase":
        choice = confirm("要使用技艺吗？")
        if not choice:
            if me.isActivePlayer == True:
                notify("{} 放弃了使用技艺，等待 {} 使用技艺".format(me, players[1]))
                remoteCall(players[1], "castArt", [])
        while choice:
            list = [card for card in me.piles["Lrig卡组"]
                    if card.properties["类型"] == "技艺"
                    and isAttackArt(card)]
            if list == []:
                whisper("没有能发动的技艺卡。")
                if me.isActivePlayer == True:
                    notify("{} 放弃了使用技艺，等待 {} 使用技艺".format(me, players[1]))
                    remoteCall(players[1], "castArt", [])
                break
            else:
                s = askCard(list)
                if s != None:
                    activate(s, 2)
                    choice = confirm("要继续使用技艺吗？")
                    if not choice and me.isActivePlayer: ###
                        remoteCall(players[1], "castArt", [])
                else:
                    if me.isActivePlayer == True:
                        notify("{} 放弃了使用技艺，等待 {} 使用技艺".format(me, players[1]))
                        remoteCall(players[1], "castArt", [])
                    break
        if me.isActivePlayer == False:
            notify("技艺使用步骤结束，回合玩家进入SIGNI攻击步骤。")
            remoteCall(players[1], "attackPhase", [table, 0, 0])
    else: pass
    
#def askCutIn(target):
#    toask = []
#    for arts in me.piles["Lrig卡组"]:
#        if isCutIn(arts): toask.append(arts)
#    if not toask:
#        remoteCall(players[1],"magicStep2",[])
#        return False
#    s = askCard(toask)
#    if s != None: activate(s,2)
#    remoteCall(player[1],"magicStep2",[])
    
def leftS(card, x = 0, y = 0):
    mute()
    if lock == 0:
        if me.hasInvertedTable() == False:
            position = AleftS
        else:
            position = BleftS
        card.moveToTable(position[0], position[1])
        notify("玩家 {} 将SIGNI 【{}】 出场到其左域 ".format(me, card))

def middleS(card, x = 0, y = 0):
    mute()
    if me.hasInvertedTable() == False:
        position = AmiddleS
    else:
        position = BmiddleS
    card.moveToTable(position[0], position[1])
    notify("玩家 {} 将SIGNI 【{}】 出场到其中央 ".format(me, card))

def rightS(card, x = 0, y = 0):
    mute()
    if me.hasInvertedTable() == False:
        position = ArightS
    else:
        position = BrightS
    card.moveToTable(position[0], position[1])
    notify("玩家 {} 将SIGNI 【{}】 出场到其右域 ".format(me, card))
    
def askPosition(card):
    updateSigniField()
    getMyLrig()
    mySigni = [c for c in table
               if isInSigni(c)
               and c.controller == me]
    sum = 0
    total = 0
    if int(card.properties["等级"]) > int(myLrig.properties["等级"]):
        whisper("{} 的等级超过 {} 的等级，不能出场。".format(card, myLrig))
        return
    for s in mySigni:
        sum = sum + int(s.properties["等级"])
    total = sum + int(card.properties["等级"])
    if total > int(myLrig.properties["界限"]):
        whisper("场上SIGNI等级合计将超过 {} 的界限，不能出场。".format(myLrig))
        return
    if not limitCondition(card): return
    choiceList = []
    colorsList = []
    if me.hasInvertedTable() == False:
        ask = ["AleftS","AmiddleS","ArightS"]
    else:
        ask = ["BleftS","BmiddleS","BrightS"]
    for loc in ask:
        if not SigniField.has_key(loc):
            if reg("left", loc):
                choiceList.append("左区")
                colorsList.append("#FFFAFA")  #snow
            if reg("middle", loc):
                choiceList.append("中区")
                colorsList.append("#FFFAFA")
            if reg("right", loc):
                choiceList.append("右区")
                colorsList.append("#FFFAFA")
    if choiceList == []:
        confirm("没有空位！")
        return False
    else:
        choice = askChoice("请选择出场区域：", choiceList, colorsList)
        if choice == 0:
            return False
        if reg("左区",choiceList[choice - 1]):
            leftS(card, 0, 0)
            return True
        elif reg("中区",choiceList[choice - 1]):
            middleS(card, 0, 0)
            return True
        elif reg("右区",choiceList[choice - 1]):
            rightS(card, 0, 0)
            return True
        else: pass
    
#---------------------------------------------------------------------------
# Preparation
#---------------------------------------------------------------------------

def checkDeck():
    mute()
    me.piles["主卡组"].setVisibility("me")
    deck = [card for card in me.piles["主卡组"]]
    lb = []
    check = []
    if len(deck) != 40:
        notify("玩家 {} 主卡组数量不满足条件".format(me))
        confirm("主卡组数量不满足条件，请重新构筑卡组")
        return
    for c in deck:
        if c.properties["生命迸发标记"] == "1":
            lb.append(c)
    if len(lb) != 20:
        notify("玩家 {} 生命迸发数量为 {} ，不满足条件".format(me, str(len(lb))))
        confirm("生命迸发数量不满足条件，请重新构筑卡组")
        return
    for d in deck:
        i = 0
        while i < 40:
            if d.name == deck[i].name:  #we do not know the order of cards in deck.
                #notify(d.name)
                check.append(deck[i])
            i = i +1
        #notify(str(len(check)))
        #return
        if len(check) > 4:
            notify("{} 的数量超过4张。".format(check[0]))
            return
        else: check = []
    notify("卡组符合要求")
    me.piles["主卡组"].setVisibility("none")

def prepare():
    mute()
    if me.hasInvertedTable() == False:
        initX = 180
        variation = 30
        LrigX = -30
        LrigY = 160
    else:
        initX = -240
        variation = -30
        LrigX = -30
        LrigY = -250
    notify("--------玩家 {} 开始游戏准备--------".format(me))
    me.piles['主卡组'].shuffle()
    count = 0
    countlb = 0
    for card in me.hand:
        card.moveToTable(LrigX, LrigY, forceFaceDown=False) 
    for card in me.piles['主卡组'].top(5):
        card.moveTo(me.hand)
    adjust()
    for card in me.piles['主卡组'].top(7):
        card.moveToTable(initX, LrigY, forceFaceDown=True) 
        initX = initX+variation
    notify("玩家 {} 的【初始Lrig】已就位;".format(me))
    notify("玩家 {} 的【初始手卡】已补充;".format(me))
    notify("玩家 {} 的【生命护甲】已装填;".format(me))
    notify("---------玩家 {} 准备已完成--------- ".format(me))
    
def adjust():
    choice = confirm("要调整手卡吗？")
    if choice == True:
        goselect = confirm("请选择要调整的卡牌，选择否或关闭选卡界面结束选择。")
        if goselect == True:
            list = [c for c in me.hand]
            selected = []
            for card in me.hand:
                s = askCard(list)
                if s != None:
                    selected.append(s)
                    list.remove(s)
                else:
                    notify("结束选择。")
                    break
            for card in selected:
                card.moveToBottom(me.piles['主卡组'])
            me.piles['主卡组'].shuffle()
            me.piles['主卡组'].shuffle()
            genDraw(len(selected))
    
#------------------------------------------------------------------------------
# Pile Actions
#------------------------------------------------------------------------------

def draw(group, x = 0, y = 0):
    if len(group) == 0: return
    mute()
    group[0].moveTo(me.hand)
    notify("{} 抽了一张卡.".format(me))

def shuffle(group):
    group.shuffle()
    group.shuffle()

def rebuild():
    mute()
    for card in me.piles["废弃区"]:
        card.moveToBottom(me.piles['主卡组'])
        me.piles['主卡组'].shuffle()
        me.piles['主卡组'].shuffle()
    Life = [c for c in table
            if isInLife(c)]
    if not Life: return
    list = []
    for c in Life: list.append(c.getIndex)
    o = max(list)
    for c in Life:
        if c.getIndex == o: c.moveTo(me.piles["废弃区"])
        
#---------------------------------------------------------------------------
# Event Actions
#---------------------------------------------------------------------------

def moveTrigger(player,card,fromGroup,toGroup,oldIndex,index,oldX,oldY,x,y,isScriptMove):
    mute()
    #notify("{}".format(player))
    if isScriptMove and fromGroup == table and (oldX <= -270 or oldX >= 210) and card.isFaceUp:
        return
    if player == me and isScriptMove:
        #notify("{}".format(player))
        global arrival_limit
        global plant
        update()
        updateSigniField()
        getMyLrig()
        getOppoLrig()
        if isScriptMove and toGroup == table and card.properties["类型"] == "SIGNI":
            card.markers[Power] = int(card.properties["力量"])
            if plant == 1 and isInSigni(card): lancer(card, 0, 0)
            for key in SigniField:  #check Continuous effect
                if isContinuous(SigniField[key][0]): activateContinuous(SigniField[key][0])
                    #notify("{} 的【常】效果适用。".format(SigniField[key][0]))
            if isContinuous(myLrig): activateContinuous(myLrig)
                #notify("{} 的【常】效果适用。".format(myLrig))
            if isContinuous(oppoLrig): activateContinuous(oppoLrig)
                #notify("{} 的【常】效果适用。".format(oppoLrig))
            if isArrival(card) and (isInSigni(card) or isCurrentLrig(card))  and card.controller == me and arrival_limit == 0:  #check Arrival effect
                getCost(card, 1)
                if cost != [] or specialcost != {}:
                    #for a in cost: notify(a)
                    choice = confirm("要发动【出】的能力吗？")
                    if choice: activateArrival(card)
                    else: notify("{} 没有发动 {} 的【出】能力。".format(me, card))
                else:
                    notify("{} 的【出】效果强制发动。".format(card))
                    activateArrival(card)  #Signis with 0-cost Arrival effect are forced to be activated.
            sendInfo()
            arrival_limit = 0
        if isScriptMove and toGroup == table and card.properties["类型"] == "LRIG" and card.controller == me:
            for key in SigniField:  #to check Continuous effect
                if isContinuous(SigniField[key][0]): activateContinuous(SigniField[key][0])
                    #notify("{} 的【常】效果适用。".format(SigniField[key][0]))
            alllrig = [lrig for lrig in table
                       if isInLrig(lrig)]  #notice that function isInLrig()  knows controller.
            for lr in alllrig:
                if isContinuous(lr) and lr != card:
                    activateContinuous(lr)  #in fact, to cancel the previous lrig's Continuous effect.
                    #notify("{} 的【常】效果不再适用。".format(lr))
            if isContinuous(myLrig):  #to activate current lrig's Continuous effect.
                activateContinuous(myLrig)
                #notify("{} 的【常】效果适用。".format(myLrig))
            if isContinuous(oppoLrig):
                activateContinuous(oppoLrig)
                #notify("{} 的【常】效果适用。".format(oppoLrig))
            if isArrival(card) and not isInEner(card) and not isInCheck(card):  #check Arrival effect
                getCost(card, 1)
                if cost != [] or specialcost != {}:
                    #for a in cost: notify(a)
                    choice = confirm("要发动 {} 的【出】效果吗？".format(card.name))
                    if choice: activateArrival(card)
                    else: notify("{} 没有发动 {} 的【出】效果。".format(me, card))
                else:
                    notify("{} 的【出】效果强制发动。".format(card))
                    activateArrival(card)
            sendInfo()
        if isScriptMove and  (fromGroup == table or toGroup == me.hand or toGroup == me.piles["废弃区"]) and me.isActivePlayer:
            tracePower(card)
            sendInfo()
        #if fromGroup == me.hand and toGroup == me.hand:
        #    card.markers[Power] = int(card.properties["力量"])
        #if fromGroup == me.piles['主卡组'] and toGroup ==me.hand and card.properties["类型"] == "SIGNI":
        #    card.markers[Power] = int(card.properties["力量"])
        if toGroup != me.piles['主卡组'] and card.position != Alrig and card.position != Blrig and card.isFaceUp :
            #update()
            updateSigniField()
            #getSigniField()
            #for key in SigniField:
            #    notify(SigniField[key][0].name)
        #if toGroup == me.piles['废弃区'] and fromGroup == card.controller.piles['主卡组'] and card.name == "反制代号 敌左反魔":
        #    askPosition(card)
    summary()
    
def onCardClick(card, mouseButton, keysDown):
    if lock == 1:
        confirm("请等待对方响应")
        
def protectPower(card, markerName, oldValue, newValue, isScriptChange):
    mute()
#    if me.isActivePlayer and not isScriptChange:
#        card.markers[markerName] = oldValue
#        notify("start tracing")
#        notify("{}".format(markerName))
#        if markerName != ('Power', '00000000-0000-0000-0000-000000000001'):
#            notify("not power")
#        else:
#            notify("get")
#            return
#        if not isScriptChange:
#            card.markers[Power] = oldValue
#            notify("not script")
#            return
#        if card.properties["颜色"] != "绿": 
#            notify("not green")
#            return
#        updateSigniField()
#        for key in SigniField:  #check Continuous effect
#            if isContinuous(SigniField[key][0]): activateContinuous(SigniField[key][0])
      
def onTurn(player, turnNumber):
    mute()
    updateSigniField()
    if me.isActivePlayer:
        for key in SigniField:  #to check Continuous effect
            if isContinuous(SigniField[key][0]):
                activateContinuous(SigniField[key][0])
                notify("{} 的【常】效果适用（回合开始）。".format(SigniField[key][0]))
    if turnNumber == 1: prepare()
    if me.isActivePlayer:
        getMyLrig()
        standPhase(0,0,0)
        drawPhase(0,0,0)
        chargePhase(0,0,0)
        if myLrig.name == "轰炎 花代•贰改":
            mainPhase(0,0,0)
        else:
            growPhase(0,0,0)
            mainPhase(0,0,0)
        
def onLoadDeck(player, groups):
    mute()
    if player ==me:
        checkDeck()
    
#---------------------------------------------------------------------------
# Debugging
#---------------------------------------------------------------------------

def position(card,x = 0, y = 0):
    mute()
    position = card.position
    x = str(card.position[0])
    y = str(card.position[1])
    notify("x坐标:{}，y坐标:{}".format(x, y))

def kneel(card, x = 0, y = 0):
    mute()
    card.orientation ^= Rot90
    if card.orientation & Rot90 == Rot90:
        notify('{} 横置了 【{}】'.format(me, card))
    else:
        notify('{} 竖置了 【{}】'.format(me, card))
        
def addMarkers(card, x = 0, y = 0):
    mute()
    choice = confirm("请添加力量标记，+1000/白色标记，-1000/黑色标记。选择“是”后会弹出对话框，在Custom markers栏选择白色或黑色，Quantity中填入希望添加的数量，Name可以不填，之后按Add确认")
    if choice == True:
        marker, qty = askMarker()
        card.markers[marker] += qty
        notify("{} 为 【{}】 添加了{}个力量标记，+1000/白色标记，-1000/黑色标记".format(me, card, qty))

def flipcard(card, x = 0, y = 0):
    mute()
    if card.isFaceUp:
        notify("{} 将 【{}】 翻至反面朝上.".format(me, card))
        card.isFaceUp = False
    else:
        card.isFaceUp = True
        notify("{} 将 【{}】 翻至正面朝上.".format(me, card))
        
def debugLifeBurst(card, x=0, y=0):
    execLB(card)
    
def test(card, x=0, y=0):
    adjust()
    
def test2(group, x = 0, y = 0):
    getOppoLrig()
    notify("{}".format(oppoLrig))
    #charge()
    
def ask():
    s = confirm("received？")
        
def test3(group, x = 0, y = 0):
    mute()
    #summary()
    #remoteCall(players[1], "Tadjust" , [])
    global lock
    lock = 0
        
def setLock():
    global lock
    lock = 1
    #notify("done")
    
def unlock():
    global lock
    lock = 0
    #notify("done")
    
def test4(card, x=0, y=0):
    attack(card)
    #send(card)
    #payCost(card, 0)
    
def updates(group, x = 0, y = 0):
#    if not me.isActivePlayer: requestInfo()
    rnd(1,1000)
    updateSigniField()
    for key in SigniField:
        if SigniField[key][1] != []:
            for e in SigniField[key][1]:
                notify("在 {} 中的SIGNI为 {} ，正受到 {} 的效果影响。".format(key, SigniField[key][0], e))
        else:
            notify("在 {} 中的SIGNI为 {} 。".format(key, SigniField[key][0]))
