# -*- coding: utf-8 -*-  
'''
Created on 2014年7月18日

@author: SynTuner
'''
class CardCost:  #have some problems handling Chinese with regular expressions on OCTGN. All these classes is necessary until we can handle it in a uniform way.
    def __init__(self):
        self.etype = -2
    
    def WX01_001(self, card, etype): #太阳之巫女 玉依姬
        mute()
        global cost
        global echoice
        global specialcost
        notify("done")
        growcost = ["白","白", "白"]
        effectcost2 =  ["白"]
        if etype == -2:
            return False
        elif etype == -1:
            cost == []
        elif etype == 0:  #to grow
            cost = growcost
            for color in cost:
                notify(color)
        elif etype == 1:  #to activate Arrival
            pass
        else:
            cost = effectcost2
            specialcost = {"Discard":{"color": "白", "ctype": "SIGNI", "qty": 1}}
        
    def WX01_002(self, card, etype): #晓之巫女 玉依姬
        mute()
        global cost
        global echoice
        global specialcost
        notify("done")
        growcost = ["白","白", "红","红"]
        effectcost2 =  ["白","白","红"]
        if etype == -2:
            return False
        elif etype == -1:
            cost == []
        elif etype == 0:  #to grow
            cost = growcost
            for color in cost:
                notify(color)
        elif etype == 1:  #to activate Arrival
            pass
        else:
            cost = effectcost2
            specialcost = {"Down":{"target":"self"}}

    def WX01_003(self, card, etype): #百火缭乱 花代•肆
        mute()
        global cost
        global echoice
        global specialcost
        notify("done")
        growcost = ["红", "红","红"]
        effectcost2 =  ["红"]
        
        if etype == -2:
            return False
        elif etype == -1:
            cost == []
        elif etype == 0:  #to grow
            cost = growcost
            for color in cost:
                notify(color)
        elif etype == 1:  #to activate Arrival
            pass
        else:
            cost = effectcost2
            specialcost = {"Discard":{"color": "红", "ctype": "SIGNI", "qty": 1}}
        
    def WX01_004(self, card, etype): #轰炎 花代•贰改
        mute()
        global cost
        global echoice
        global specialcost
        notify("done")
        growcost = ["红", "红"]
        effectcost2 =  ["红", "红", "红"]
        if etype == -2:
            return False
        elif etype == -1:
            cost == []
        elif etype == 0:  #to grow
            cost = growcost
            for color in cost:
                notify(color)
        elif etype == 1:  #to activate Arrival
            pass
        else:
            cost = effectcost2
        
    def WX01_005(self, card, etype): #代号 皮璐璐可•Ω
        mute()
        uniformCost(etype, ["蓝","蓝","蓝"], [], [], [], {"Discard":{"color": "蓝", "ctype": "SIGNI", "qty": 1}}, 2)
        
    def WX01_006(self, card, etype): #四式战帝女 绿姬
        mute()
        global cost
        global echoice
        global specialcost
        notify("done")
        growcost = ["绿","绿","绿"]
        effectcost2 = []
        if etype == -2:
            return False
        elif etype == -1:
            cost == []
        elif etype == 0:  #to grow
            cost = growcost
            for color in cost:
                notify(color)
        elif etype == 1:  #to activate Arrival effect
            pass
        else:  
            cost = effectcost2
            specialcost = {"Discard":{"color": "绿", "ctype": "SIGNI", "qty": 1}}
        
    def WX01_007(self, card, etype): #月蚀之巫女 玉依姬
        mute()
        global cost
        global echoice
        global specialcost
        notify("done")
        growcost = ["白","白"]
        effectcost1 = ["白"]
        if etype == -2:
            return False
        elif etype == -1:
            cost == []
        elif etype == 0:  #to grow
            cost = growcost
            for color in cost:
                notify(color)
        elif etype == 1:  #to activate Arrival effect
            cost = effectcost1
        else:  
            pass
        
    def WX01_008(self, card, etype): #流星之巫女 玉依姬
        mute()
        uniformCost(etype, ["白"], [], [], [], {}, 0)
        
    def WX01_009(self, card, etype): #新星之巫女 玉依姬
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}}, 1)
        
    def WX01_010(self, card, etype): #杰诺之门
        mute()
        uniformCost(etype, [], [], [], ["白"], {}, 0)
        
    def WX01_011(self, card, etype): #炽炎舞 花代•叁
        mute()
        uniformCost(etype, ["红", "红"], [], ["红"], [], {}, 0)
        
    def WX01_012(self, card, etype): #刚炎 花代•贰
        mute()
        uniformCost(etype, ["红"], [], [], [], {}, 0)
        
    def WX01_013(self, card, etype): #焰 花代•壹
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}}, 1)
        
    def WX01_014(self, card, etype): #烈霸一络
        mute()
        uniformCost(etype, [], [], [], ["红", "红", "红"], {}, 0)
        
    def WX01_015(self, card, etype): #代号 皮璐璐可•Γ
        mute()
        uniformCost(etype, ["蓝", "蓝"], [], ["蓝"], [], {}, 0)
        
    def WX01_016(self, card, etype): #代号 皮璐璐可•Β
        mute()
        uniformCost(etype, ["蓝"], [], [], [], {}, 0)
        
    def WX01_017(self, card, etype): #代号 皮璐璐可•Α
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}}, 1)
        
    def WX01_018(self, card, etype): #魔法反制
        mute()
        uniformCost(etype, [], [], ["蓝"], ["蓝", "无"], {}, 0)
        
    def WX01_019(self, card, etype): #四型皇艳娘 绿姬
        mute()
        uniformCost(etype, ["绿", "绿", "绿"], [], [], [], {}, 0)
        
    def WX01_020(self, card, etype): #三型雌雌娘 绿姬
        mute()
        uniformCost(etype, ["绿", "绿"], [], [], [], {}, 0)
        
    def WX01_021(self, card, etype): #二型斗婚娘 绿姬
        mute()
        uniformCost(etype, ["绿"], [], [], [], {}, 0)
        
    def WX01_022(self, card, etype): #一型舞斗娘 绿姬
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}}, 1)
        
    def WX01_023(self, card, etype): #大器晚成
        mute()
        uniformCost(etype, [], [], [], ["绿", "绿", "绿", "绿", "绿", "无", "无", "无", "无", "无", "无", "无"], {}, 0)
        
    def WX01_024(self, card, etype): #奇奇怪怪
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_025(self, card, etype): #营救
        mute()
        uniformCost(etype, [], [], [], ["无"], {}, 0)
        
    def WX01_026(self, card, etype): #充能
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_027(self, card, etype): #原枪 源能枪
        mute()
        uniformCost(etype, [], [], ["白"], ["白", "白"], {}, 0)
        
    def WX01_028(self, card, etype): #弧光圣气
        mute()
        uniformCost(etype, [], [], [], ["白", "白", "白", "白", "白"], {}, 0)
        
    def WX01_029(self, card, etype): #罗辉石 金刚珠玉
        mute()
        uniformCost(etype, [], [], ["红"], ["红", "红"], {}, 0)
        
    def WX01_030(self, card, etype): #赎罪之对火
        mute()
        uniformCost(etype, [], [], [], ["红", "红", "红"], {}, 0)
        
    def WX01_031(self, card, etype): #核心代号 V•A•C
        mute()
        uniformCost(etype, [], [], ["蓝"], ["蓝", "蓝"], {}, 0)
        
    def WX01_032(self, card, etype): #抢夺
        mute()
        uniformCost(etype, [], [], [], ["蓝", "蓝", "无"], {}, 0)
        
    def WX01_033(self, card, etype): #幻兽神 御先狐
        mute()
        uniformCost(etype, [], [], ["绿"], ["绿", "绿"], {}, 0)
        
    def WX01_034(self, card, etype): #修复
        mute()
        uniformCost(etype, [], [], [], ["绿", "绿", "绿"], {}, 0)
        
    def WX01_035(self, card, etype): #祝福女神 雅典娜
        mute()
        uniformCost(etype, [], [], [], ["白"], {"Down":{"target":"self"}}, 2)
        
    def WX01_036(self, card, etype): #巨弓 抛射弓
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_037(self, card, etype): #无法忘却的幻想 瓦尔基里
        mute()
        uniformCost(etype, [], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX01_038(self, card, etype): #获得但他林
        mute()
        uniformCost(etype, [], [], [], ["白", "红"], {}, 0)
        
    def WX01_039(self, card, etype): #弩炮 加农炮
        mute()
        uniformCost(etype, [], [], [], ["红"], {"Down":{"target":"self"}}, 2)
        
    def WX01_040(self, card, etype): #罗石 山铜
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_041(self, card, etype): #轰炮 法典炮
        mute()
        uniformCost(etype, [], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX01_042(self, card, etype): #断罪之轹断
        mute()
        uniformCost(etype, [], [], [], ["红", "红", "红"], {}, 0)
        
    def WX01_043(self, card, etype): #幻水 雅莱娅尔
        mute()
        uniformCost(etype, [], [], [], ["蓝"], {"Down":{"target":"self"}}, 2)
        
    def WX01_044(self, card, etype): #技艺代号 P•Z•L
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_045(self, card, etype): #幻水 夏克兰丝
        mute()
        uniformCost(etype, [], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX01_046(self, card, etype): #情况糟糕
        mute()
        uniformCost(etype, [], [], [], ["蓝"], {}, 0)
        
    def WX01_047(self, card, etype): #罗植 曼茶罗花
        mute()
        uniformCost(etype, [], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX01_048(self, card, etype): #幻兽 雪怪
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_049(self, card, etype): #罗植 植生羊
        mute()
        uniformCost(etype, [], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX01_050(self, card, etype): #大化
        mute()
        uniformCost(etype, [], [], [], ["绿"], {}, 0)
        
    def WX01_051(self, card, etype): #侍从Q
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_052(self, card, etype): #包括的知识
        mute()
        uniformCost(etype, [], [], [], ["无", "无"], {}, 0)
        
    def WX01_053(self, card, etype): #极剑 噬神剑
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_054(self, card, etype): #极盾 埃奎斯盾
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_055(self, card, etype): #大盾 镇暴盾
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_056(self, card, etype): #中盾 方盾
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_057(self, card, etype): #出弓 炽天弓
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_058(self, card, etype): #重新开始的对话 米迦勒
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}, "Down":{"target":"self"}}, 2)
        
    def WX01_059(self, card, etype): #出弓 普弓
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_060(self, card, etype): #小盾 圆盾
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_061(self, card, etype): #探求的思想 汉尼尔
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}, "Down":{"target":"self"}}, 2)
        
    def WX01_062(self, card, etype): #将之开启
        mute()
        uniformCost(etype, [], [], [], ["白"], {}, 0)
        
    def WX01_063(self, card, etype): #做好准备
        mute()
        uniformCost(etype, [], [], [], ["白"], {}, 0)
        
    def WX01_064(self, card, etype): #罗石 金属
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_065(self, card, etype): #罗石 绿宝石
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_066(self, card, etype): #罗石 红宝石
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_067(self, card, etype): #罗石 磷矿石
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_068(self, card, etype): #罗石 琥珀
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_069(self, card, etype): #爆炮 远射炮
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}, "Down":{"target":"self"}}, 2)
        
    def WX01_070(self, card, etype): #罗石 海人草
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_071(self, card, etype): #罗石 蓝宝石
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_072(self, card, etype): #小炮 德拉古诺夫枪
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}, "Down":{"target":"self"}}, 2)
        
    def WX01_073(self, card, etype): #落星炎球
        mute()
        uniformCost(etype, [], [], [], ["红", "红", "红"], {}, 0)
        
    def WX01_074(self, card, etype): #棱晶火柱
        mute()
        uniformCost(etype, [], [], [], ["白", "红"], {}, 0)
        
    def WX01_075(self, card, etype): #技艺代号 A•S•M
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_076(self, card, etype): #技艺代号 I•D•O•L
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_077(self, card, etype): #技艺代号 A•D•B
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_078(self, card, etype): #技艺代号 S•T•G
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_079(self, card, etype): #技艺代号 W•T•C
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_080(self, card, etype): #幻水 夏可檀
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}, "Down":{"target":"self"}}, 2)
        
    def WX01_081(self, card, etype): #技艺代号 T•V
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_082(self, card, etype): #技艺代号 F•A•N
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_083(self, card, etype): #幻水 克马诺明
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}, "Down":{"target":"self"}}, 2)
        
    def WX01_084(self, card, etype): #事不过三
        mute()
        uniformCost(etype, [], [], [], ["蓝"], {}, 0)
        
    def WX01_085(self, card, etype): #冰封
        mute()
        uniformCost(etype, [], [], [], ["蓝"], {}, 0)
        
    def WX01_086(self, card, etype): #幻兽 飞鹰
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_087(self, card, etype): #幻兽 猫妖精
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_088(self, card, etype): #幻兽 猫头鹰
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_089(self, card, etype): #幻兽 黑猫
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_090(self, card, etype): #幻兽 麻雀
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_091(self, card, etype): #幻兽 树袋熊
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_092(self, card, etype): #幻兽 白猫
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_093(self, card, etype): #罗植 蒲公英
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}, "Down":{"target":"self"}}, 2)
        
    def WX01_094(self, card, etype): #幻兽 燕子
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_095(self, card, etype): #幻兽 大熊猫
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_096(self, card, etype): #幻兽 三色猫
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_097(self, card, etype): #罗植 鼠尾草
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}, "Down":{"target":"self"}}, 2)
        
    def WX01_098(self, card, etype): #芽生
        mute()
        uniformCost(etype, [], [], [], ["绿"], {}, 0)
        
    def WX01_099(self, card, etype): #逆出
        mute()
        uniformCost(etype, [], [], [], ["绿"], {}, 0)
        
    def WX01_100(self, card, etype): #侍从T
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_101(self, card, etype): #侍从D
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_102(self, card, etype): #侍从O
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX01_103(self, card, etype): #喷流的知识
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD01_001(self, card, etype): #满月之巫女 玉依姬
        mute()
        uniformCost(etype, ["白","白","白"], [], [], [], {}, 0)
    
    def WD01_002(self, card, etype): #弦月之巫女 玉依姬
        mute()
        uniformCost(etype, ["白","白"], [], [], [], {}, 0)
    
    def WD01_003(self, card, etype): #半月之巫女 玉依姬
        mute()
        uniformCost(etype, ["白"], [], [], [], {}, 0)
    
    def WD01_004(self, card, etype): #三日月之巫女 玉依姬
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD01_005(self, card, etype): #新月之巫女 玉依姬
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD01_006(self, card, etype): #洛可可界线
        mute()
        uniformCost(etype, [], [], [], ["白", "白", "白", "无", "无"], {}, 0)
    
    def WD01_007(self, card, etype): #艾本之书
        mute()
        uniformCost(etype, [], [], [], ["白", "白", "白"], {}, 0)
    
    def WD01_008(self, card, etype): #巴洛克防御
        mute()
        uniformCost(etype, [], [], [], ["白", "白"], {}, 0)
    
    def WD01_009(self, card, etype): #甲胄 皇家铠
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD01_010(self, card, etype): #大剑 石中剑
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD01_011(self, card, etype): #笼手 铁拳
        mute()
        uniformCost(etype, [], [], ["白"], [], {}, 0)
    
    def WD01_012(self, card, etype): #中剑 焰形剑
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD01_013(self, card, etype): #小剑 库克力弯刀
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD01_014(self, card, etype): #小弓 箭矢
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD01_015(self, card, etype): #获得圣经
        mute()
        uniformCost(etype, [], [], [], ["白"], {}, 0)
    
    def WD02_001(self, card, etype): #花代•肆
        mute()
        uniformCost(etype, ["红", "红", "红"], [], [], [], {}, 0)
    
    def WD02_002(self, card, etype): #花代•叁
        mute()
        uniformCost(etype, ["红", "红"], [], [], [], {}, 0)
    
    def WD02_003(self, card, etype): #花代•贰
        mute()
        uniformCost(etype, ["红"], [], [], [], {}, 0)
    
    def WD02_004(self, card, etype): #花代•壹
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD02_005(self, card, etype): #花代•零
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD02_006(self, card, etype): #飞火夏虫
        mute()
        uniformCost(etype, [], [], [], ["红", "红", "红"], {}, 0)
    
    def WD02_007(self, card, etype): #背炎之阵
        mute()
        uniformCost(etype, [], [], [], ["红", "红"], {"Discard":{"qty": 3}}, 2)
    
    def WD02_008(self, card, etype): #烧石炎
        mute()
        uniformCost(etype, [], [], [], ["红", "无"], {}, 0)
    
    def WD02_009(self, card, etype): #罗石 火山石
        mute()
        uniformCost(etype, [], [], ["红", "红", "红"], [], {}, 0)
    
    def WD02_010(self, card, etype): #罗石 白银
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD02_011(self, card, etype): #罗石 石榴石
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD02_012(self, card, etype): #罗石 铜
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD02_013(self, card, etype): #罗石 铁
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD02_014(self, card, etype): #罗石 紫水晶
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD02_015(self, card, etype): #轰音火柱
        mute()
        uniformCost(etype, [], [], [], ["红"], {}, 0)
    
    def WD03_001(self, card, etype): #代号•皮璐璐可•T
        mute()
        uniformCost(etype, ["蓝", "蓝", "蓝"], [], [], [], {}, 0)
    
    def WD03_002(self, card, etype): #代号•皮璐璐可•G
        mute()
        uniformCost(etype, ["蓝", "蓝"], [], [], [], {}, 0)
    
    def WD03_003(self, card, etype): #代号•皮璐璐可•M
        mute()
        uniformCost(etype, ["蓝"], [], [], [], {}, 0)
    
    def WD03_004(self, card, etype): #代号•皮璐璐可•K
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD03_005(self, card, etype): #代号•皮璐璐可
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD03_006(self, card, etype): #窥视分析
        mute()
        uniformCost(etype, [], [], [], ["蓝", "蓝", "蓝"], {}, 0)
    
    def WD03_007(self, card, etype): #不可行动
        mute()
        uniformCost(etype, [], [], [], ["蓝", "蓝", "蓝"], {}, 0)
    
    def WD03_008(self, card, etype): #双重抽卡
        mute()
        uniformCost(etype, [], [], [], ["蓝", "无"], {}, 0)
    
    def WD03_009(self, card, etype): #技艺代号 R•M•N
        mute()
        uniformCost(etype, [], [], ["蓝"], [], {}, 0)
    
    def WD03_010(self, card, etype): #技艺代号 D•R•S
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD03_011(self, card, etype): #技艺代号 S•M•P
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD03_012(self, card, etype): #技艺代号 J•V
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD03_013(self, card, etype): #技艺代号 S•C
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD03_014(self, card, etype): #技艺代号 R•F•R
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def WD03_015(self, card, etype): #真可惜
        mute()
        uniformCost(etype, [], [], [], ["蓝"], {}, 0)

    def PR_017(self, card, etype): #中枪 古罗马长矛
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def PR_018(self, card, etype): #罗石 秘银
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
    
    def PR_019(self, card, etype): #珍宝
        mute()
        uniformCost(etype, [], [], [], ["蓝"], {}, 0)  #special case , we treat TREASURE's special cost as its effect.
    
    def PR_020(self, card, etype): #增援
        mute()
        effectcost2 = ["绿"]
        choiceList = ["「从你的卡组里探寻1张力量10000以上的SIGNI卡，将其公开并加入加入手牌。之后将卡组洗切。」", \
                       "「从你的卡组顶将2张卡放置到能量区」"]
        colorsList = ['#FF0000', '#FF0000'] 
        global cost
        global echoice
        cost = effectcost2
        if etype == 2:
            echoice = askChoice("选择一个效果发动：", choiceList, colorsList)
    
    def PR_040(self, card, etype): #多重
        mute()
        effectcost2 = ["白","白","蓝","蓝"]
        choiceList = ["「对战对手的1只LRIG在这个回合中不能攻击。」", \
                       "「将对战对手的所有SIGNI冻结。」", \
                       "「将对战对手的1只SIGNI返回手牌。」", \
                       "「抽2张卡。」"]
        colorsList = ['#FF0000', '#FF0000', '#FF0000', '#FF0000'] 
        global cost
        global echoice
        cost = effectcost2
        if etype == 2:
            echoice1 = askChoice("选择第一个效果：", choiceList, colorsList)
            del choiceList[echoice1 - 1]
            del colorsList[echoice1 - 1]
            inter = askChoice("选择第二个效果：", choiceList, colorsList)
            if echoice1 <= inter:
                echoice2 = inter + 1
            else:
                echoice2 = inter
            echoice = [echoice1, echoice2]
        
    def WD04_001(self, card, etype): #四之娘 绿姬
        mute()
        uniformCost(etype, ["绿", "绿", "绿"], [], [], [], {}, 0)
        
    def WD04_002(self, card, etype): #三之娘 绿姬
        mute()
        uniformCost(etype, ["绿", "绿"], [], [], [], {}, 0)
        
    def WD04_003(self, card, etype): #二之娘 绿姬
        mute()
        uniformCost(etype, ["绿"], [], [], [], {}, 0)
        
    def WD04_004(self, card, etype): #一之娘 绿姬
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD04_005(self, card, etype): #斗娘 绿姬
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD04_006(self, card, etype): #意气扬扬
        mute()
        uniformCost(etype, [], [], [], ["绿"], {}, 0)
        
    def WD04_007(self, card, etype): #再三再四
        mute()
        uniformCost(etype, [], [], [], ["绿"], {}, 0)
        
    def WD04_008(self, card, etype): #付和雷同
        mute()
        uniformCost(etype, [], [], [], ["绿", "绿", "绿"], {}, 0)
        
    def WD04_009(self, card, etype): #幻兽 青龙
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD04_010(self, card, etype): #幻兽 朱雀小姐
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD04_013(self, card, etype): #幻兽 小玄武
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD04_015(self, card, etype): #幻兽 白虎
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD04_016(self, card, etype): #侍从 Q2
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD04_017(self, card, etype): #侍从 O2
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD04_018(self, card, etype): #堕络
        mute()
        uniformCost(etype, [], [], [], ["绿"], {}, 0)
        
    def WD05_001(self, card, etype): #狱卒阎魔 乌莉丝
        mute()
        uniformCost(etype, ["黑", "黑", "黑"], [], [], [], {}, 0)
        
    def WD05_002(self, card, etype): #阿鼻阎魔 乌莉丝
        mute()
        uniformCost(etype, ["黑", "黑"], [], [], [], {}, 0)
        
    def WD05_003(self, card, etype): #众合阎魔 乌莉丝
        mute()
        uniformCost(etype, ["黑"], [], [], [], {}, 0)
        
    def WD05_004(self, card, etype): #灼热阎魔 乌莉丝
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD05_005(self, card, etype): #阎魔 乌莉丝
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD05_006(self, card, etype): #处刑时刻
        mute()
        uniformCost(etype, [], [], [], ["黑", "黑"], {}, 0)
        
    def WD05_007(self, card, etype): #永恒处刑
        mute()
        uniformCost(etype, [], [], [], ["黑", "黑", "黑"], {}, 0)
        
    def WD05_008(self, card, etype): #出墓
        mute()
        uniformCost(etype, [], [], [], ["黑", "黑", "黑", "黑", "黑"], {}, 0)
        
    def WD05_009(self, card, etype): #堕落炮女 缅茨姆
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD05_010(self, card, etype): #废恶象征 别西卜
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD05_011(self, card, etype): #堕落炮女 卡莉
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD05_012(self, card, etype): #背德象征 科思莫
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD05_013(self, card, etype): #小恶象征 小鬼
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD05_014(self, card, etype): #堕落炮女 魅魔
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WD05_017(self, card, etype): #完全漆黑
        mute()
        uniformCost(etype, [], [], [], ["黑"], {}, 0)
        
    def WD05_018(self, card, etype): #回想的祝福
        mute()
        uniformCost(etype, [], [], [], ["无", "无"], {}, 0)
        
    def WX02_001(self, card, etype): #金木犀之巫女 玉依姬
        mute()
        growcost = ["白","红", "绿"]
        effectcost1 =  ["白"]
        effectcost2 = ["白","红"]
        effectcost3 = ["白","绿","无"]
        choiceList = ["【起】白1+红1：将对战对手的1只力量7000以下的SIGNI驱逐。", "【起】白1+绿1+无1：将对战对手的1只力量10000以上的SIGNI驱逐。"]
        colorsList = ['#FF0000', '#FF0000'] 
        global cost
        global echoice
        if etype == -2:
            return False
        elif etype == -1:
            cost == []
        elif etype == 0:  #to grow
            cost = growcost
            for color in cost:
                notify(color)
        elif etype == 1:  #to activate Arrival
            cost = effectcost1
        else:
            echoice = askChoice("选择一个效果发动：", choiceList, colorsList, customButtons = ["取消"])
            if echoice == 1:
                cost = effectcost2
            elif echoice == 2:
                cost = effectcost3
        
    def WX02_002(self, card, etype): #火鸟风月 游月·肆
        mute()
        uniformCost(etype, ["红", "红", "绿", "绿"], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX02_003(self, card, etype): #艾尔德拉×Ⅳ式
        mute()
        uniformCost(etype, ["蓝", "蓝", "蓝"], [], [], [], {}, 0)
        
    def WX02_004(self, card, etype): #无间阎魔 乌莉丝
        mute()
        uniformCost(etype, ["黑", "黑", "黑"], [], [], ["黑"], {"Discard":{"color": "黑", "ctype": "SIGNI", "qty": 1}}, 0)
        
    def WX02_005(self, card, etype): #纯白希望
        mute()
        uniformCost(etype, [], [], [], ["白", "白", "红"], {}, 0)
        
    def WX02_006(self, card, etype): #漆黑野望
        mute()
        uniformCost(etype, [], [], [], ["黑", "黑", "黑"], {}, 0)
        
    def WX02_007(self, card, etype): #轰罪炎 游月·叁
        mute()
        growcost = ["红", "绿"]
        effectcost2 = ["红"]
        effectcost3 = ["绿"]
        choiceList = ["【起】红1：将对战对手的1只力量5000以下的SIGNI驱逐。", "【起】绿1：直到回合结束时为止，你所有的SIGNI的力量+5000。"]
        colorsList = ['#FF0000', '#FF0000'] 
        global cost
        global echoice
        if etype == -2:
            return False
        elif etype == -1:
            cost == []
        elif etype == 0:  #to grow
            cost = growcost
        elif etype == 1:  #to activate Arrival
            cost = effectcost1
        else:
            echoice = askChoice("选择一个效果发动：", choiceList, colorsList, customButtons = ["取消"])
            if echoice == 1:
                cost = effectcost2
            elif echoice == 2:
                cost = effectcost3
        
    def WX02_008(self, card, etype): #焰海 游月•贰
        mute()
        uniformCost(etype, ["红"], [], [], [], {}, 0)
        
    def WX02_009(self, card, etype): #焰 游月•壹
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_010(self, card, etype): #艾尔德拉×Ⅲ式
        mute()
        uniformCost(etype, ["蓝", "蓝"], [], [], [], {}, 0)
        
    def WX02_011(self, card, etype): #艾尔德拉×Ⅱ式
        mute()
        uniformCost(etype, ["蓝"], [], [], [], {}, 0)
        
    def WX02_012(self, card, etype): #艾尔德拉×Ⅰ式
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_013(self, card, etype): #叫唤阎魔 乌莉丝
        mute()
        uniformCost(etype, ["黑", "黑"], [], [], [], {"Discard":{"qty": 1}}, 1)
        
    def WX02_014(self, card, etype): #黑绳阎魔 乌莉丝
        mute()
        uniformCost(etype, ["黑"], [], [], [], {}, 0)
        
    def WX02_015(self, card, etype): #等活阎魔 乌莉丝
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_016(self, card, etype): #哥特界限
        mute()
        uniformCost(etype, [], [], [], ["白", "无", "无"], {}, 0)
    
    def WX02_017(self, card, etype): #气炎万丈
        mute()
        uniformCost(etype, [], [], [], ["红", "绿"], {}, 0)
        
    def WX02_018(self, card, etype): #火红柳绿
        mute()
        uniformCost(etype, [], [], [], ["红"], {}, 0)
        
    def WX02_019(self, card, etype): #交织生命护甲
        mute()
        uniformCost(etype, [], [], [], ["蓝"], {}, 0)
        
    def WX02_020(self, card, etype): #鲜血斩击
        mute()
        uniformCost(etype, [], [], [], ["黑", "黑"], {}, 0)
        
    def WX02_021(self, card, etype): #先驱的大天使 大天使该隐
        mute()
        global cost
        cost = []
        effectcost =  ["白", "白"]
        if etype == 1:
            cost = effectcost
        else:
            cost =[]
        
    def WX02_022(self, card, etype): #弩炮 狙击枪
        mute()
        uniformCost(etype, [], [], ["红"], [], {}, 0)

    def WX02_023(self, card, etype): #幻水姬 丝派拉尔•卡米拉
        mute()
        uniformCost(etype, [], [], ["蓝"], [], {}, 0)
        
    def WX02_024(self, card, etype): #罗植姬 戈休·雅格尼丝
        mute()
        uniformCost(etype, [], [], ["绿"], [], {"Down":{"target":"植物"}}, 0)
        
    def WX02_025(self, card, etype): #恶魔姬 安娜•蜃影
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_026(self, card, etype): #愿望危机
        mute()
        uniformCost(etype, [], [], [], ["白"], {}, 0)
        
    def WX02_027(self, card, etype): #焦土的代价
        mute()
        uniformCost(etype, [], [], [], ["红", "红"], {}, 0)
        
    def WX02_028(self, card, etype): #谜言暗气
        mute()
        uniformCost(etype, [], [], [], ["黑", "黑"], {}, 0)
        
    def WX02_029(self, card, etype): #宝具 御剑
        mute()
        global cost
        global echoice
        global specialcost
        if etype == -2:
            return False
        elif etype == -1: pass
        elif etype == 0:  pass
        elif etype == 1: 
            specialcost = {"Discard":{"ctype": "SIGNI", "signiclass": ["武装", "武器"], "qty": 1}}
        else: 
            pass
        
    def WX02_030(self, card, etype): #宝具 御镜
        mute()
        uniformCost(etype, [], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX02_031(self, card, etype): #使其反跳
        mute()
        uniformCost(etype, [], [], [], ["白", "白"], {}, 0)
        
    def WX02_032(self, card, etype): #罗石 蛋白石
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"ctype": "SIGNI", "signiclass": ["矿石", "宝石"], "qty": 1}}, 1)
        
    def WX02_033(self, card, etype): #罗石 红玉髓
        mute()
        uniformCost(etype, [], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX02_034(self, card, etype): #不希望的冲动
        mute()
        uniformCost(etype, [], [], [], ["红", "绿"], {}, 0)
        
    def WX02_035(self, card, etype): #技艺代号 C·P·U
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"ctype": "SIGNI", "signiclass": ["电机"], "qty": 1}}, 1)
        
    def WX02_036(self, card, etype): #技艺代号 G•A•B
        mute()
        uniformCost(etype, [], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX02_037(self, card, etype): #飞溅
        mute()
        uniformCost(etype, [], [], [], ["蓝", "无"], {}, 0)
        
    def WX02_038(self, card, etype): #幻兽 雉
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"ctype": "SIGNI", "signiclass": ["空兽", "地兽"], "qty": 1}}, 1)
        
    def WX02_039(self, card, etype): #幻兽 八犬
        mute()
        uniformCost(etype, [], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX02_040(self, card, etype): #着植
        mute()
        uniformCost(etype, [], [], [], ["绿", "绿", "无", "无", "无"], {}, 0)
        
    def WX02_041(self, card, etype): #大损
        mute()
        uniformCost(etype, [], [], [], ["绿", "绿"], {}, 0)
        
    def WX02_042(self, card, etype): #反制代号 巴勒贝克
        mute()
        uniformCost(etype, [], [], [], ["黑"], {"Down":{"target":"self"}}, 2)
        
    def WX02_043(self, card, etype): #反制代号 基西拉
        mute()
        uniformCost(etype, [], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX02_044(self, card, etype): #大罪缘由 巴力
        mute()
        uniformCost(etype, [], [], [], [], {"Down":{"target":"self"}}, 2)
        
    def WX02_045(self, card, etype): #献祭斩击
        mute()
        uniformCost(etype, [], [], [], ["黑", "黑", "黑"], {}, 0)
        
    def WX02_046(self, card, etype): #牺牲的微笑 丘雅耶尔
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_047(self, card, etype): #虚构的爱情 希耶尔
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_048(self, card, etype): #宝具 勾玉
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_049(self, card, etype): #博爱的聚集 萨尼耶尔
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_050(self, card, etype): #刀剑本领
        mute()
        uniformCost(etype, [], [], [], ["白", "白"], {}, 0)
        
    def WX02_051(self, card, etype): #轰炮 远射装置
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_052(self, card, etype): #爆炮 MP5
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_053(self, card, etype): #罗石 翡翠
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_054(self, card, etype): #小炮 枪匠
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_055(self, card, etype): #光欲宝剑
        mute()
        uniformCost(etype, [], [], [], ["红"], {}, 0)
        
    def WX02_056(self, card, etype): #幻水 奥科特
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_057(self, card, etype): #幻水 珍珠
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_058(self, card, etype): #技艺代号 M•M•R
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_059(self, card, etype): #幻水 科塞梅
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_060(self, card, etype): #探寻者
        mute()
        uniformCost(etype, [], [], [], ["无"], {}, 0)
        
    def WX02_061(self, card, etype): #蓝色收获
        mute()
        uniformCost(etype, [], [], [], ["蓝", "无"], {}, 0)
        
    def WX02_062(self, card, etype): #罗植 葵小姐
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_063(self, card, etype): #罗植 莲
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_064(self, card, etype): #幻兽 猴
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_065(self, card, etype): #罗植 虎尾兰
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_066(self, card, etype): #丰润
        mute()
        uniformCost(etype, [], [], [], ["绿"], {}, 0)
        
    def WX02_067(self, card, etype): #恶魔续发 莉莉丝
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_068(self, card, etype): #恶魔勇武 摩莉甘
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"ctype": "SIGNI", "signiclass": ["恶魔"], "qty": 1}}, 1)
        
    def WX02_069(self, card, etype): #反制代号 星云
        mute()
        uniformCost(etype, [], [], [], ["黑", "黑"], {}, 0)
        
    def WX02_070(self, card, etype): #真实死神 阿尼玛
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_071(self, card, etype): #反制代号 德里
        mute()
        uniformCost(etype, [], [], [], ["黑", "无"], {}, 0)
        
    def WX02_072(self, card, etype): #反制代号 马丘比
        mute()
        uniformCost(etype, [], [], [], [], {"Discard":{"qty": 1}, "Down":{"target":"self"}}, 2)
        
    def WX02_073(self, card, etype): #反制代号 敌左反魔
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_074(self, card, etype): #小恶忧郁 格里姆
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_075(self, card, etype): #造墓者
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_077(self, card, etype): #侍从 T2
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)
        
    def WX02_078(self, card, etype): #侍从 D2
        mute()
        uniformCost(etype, [], [], [], [], {}, 0)