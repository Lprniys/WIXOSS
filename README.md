## TCG Wixoss based on OCTGN ##

**WIXOSS** is a trading card game for two players with their LRIGs. Beat down opponent's LRIG and you will be mugen uncle.

This is a repository for the game definition and scripts for OCTGN platform.The scripts make game highly automated and allow the game to play faster with less mistakes.

An english version of this file may be available if required.

### OCTGN平台教程 ###

- 下载最新版OCTGN3: [Online Card and Tabletop Gaming Network (OCTGN)](http://www.octgn.net/Home/GetOctgn)

- 打开OCTGN，切换到Games Manager选项卡，点击Add Game Feed，在Name里填 Wixoss 或任何你喜欢的名字，在Feed Url里填：
    `https://www.myget.org/F/wixoss-project/`
  ，username 和 password 不填。

- 加载完feed后点击左边下拉菜单，选择刚才填的名字，选中Wixoss The Card Game，点击Install。

- 选中Wixoss The Card Game，点击Add Image Packes，选择[WX image packages.o8c](http://pan.baidu.com/s/1dD3pSXV)安装。

- 下载[Pyhton的标准库(Lib.rar)](http://pan.baidu.com/s/1dD3pSXV)，解压到Documents\OCTGN\OCTGN\Scripting\Lib下并覆盖。

- **非中国大陆地区可跳过这一步**：找到\Documents\OCTGN\OCTGN\OCTGN.exe.config文件，右键选择记事本打开，将第13行
`<add key="WebsitePath" value="https://www.octgn.net/"/>`
改为
`<add key="WebsitePath" value="http://www.octgn.net/"/>`

- 重新打开OCTGN，切换到Play or Spectate选项卡，Start创建游戏，Game选择Wixoss The Card Game。联网对战需要hamachi等工具，非主机玩家选择Join Unlisted，填上IP和端口，可以开始游戏。单机测试需要双开OCTGN客户端，主机点start，非主机点Join。

### 游戏教程 ###

- 双方都进入游戏后会在左下角记录框中看到双方宣言Open的提示，表明网络连接正常，脚本开始运行。

- 此时双方可以点击左上角Game选项，选择Load Deck。双方卡组都载入完毕后，由**主机玩家**右击桌面任何区域，选择**决定先攻玩家**。

- 此后只需根据程序提示和游戏规则操作，所有流程和卡牌效果均为自动处理，但**不要手动拖动**桌面上的任何卡牌，以免造成不可预知的结果。

- 游戏制作的人力有限，BUG在所难免，如果在游戏运行过程中，左下角记录框出现红字报错，或者场上的效果处理出现不符合双方玩家预期的情况，可以截图并在贴吧的相关帖子下回帖，简单说明当时的操作，BUG会尽可能在下一次更新中修复。

- 正常游戏中请勿使用右键菜单中的debug选项或单卡debug选项，如果因网络状况造成卡牌力量变化没有更新等情况，可以将那张SIGNI拖回手牌重新出场，在多数情况下程序会自动更新那张SIGNI的当前力量。

- 如果不适应自动处理，双方也可以全程手动游戏！:)。

- Game Documents 选项中可以查看Wixoss游戏的入门指南。

### 卡包 ###

- 涵盖了截至2014.08.13官方正式发售的卡包内的所有卡牌。


### Screenshots ###

蓝色 VS 绿色

![截图1](http://fc05.deviantart.net/fs70/i/2014/225/a/6/qq______20140814011423_by_recoracle-d7v00sa.png)

冻结 & 卡图

![截图1](http://fc02.deviantart.net/fs71/i/2014/225/3/8/qq20140814011550_by_recoracle-d7v01gq.png)

出场选择 & 效果选择

![截图1](http://fc06.deviantart.net/fs70/i/2014/225/5/d/qq______20140814013916_by_recoracle-d7v035u.png)

![截图1](http://fc05.deviantart.net/fs71/i/2014/225/3/0/qq20140814014107_by_recoracle-d7v03me.png)
