# Py Rainbow Fart

#### Rainbow Fart Python版本，随手一写的小玩意。

#### 原版的Rainbow Fart是通过Vscode API搞定的。然而我太菜了，没认真研究。就考虑了用Hook抓取，Vsocde窗口下的键盘记录。之后在通过一些过滤，即可搞定。

#### 安装起来比较麻烦，第一，pyhook3的安装。推荐通过whl方式进行安装。github搜索pyhook3，就能找到对应的whl版本。下载安装即可。第二，playsound的大坑。playsound占用资源问题，其实在playsound的源代码那边加个exit就好，具体百度方法有。好久之前做另外一个项目的时候改的。所以也不清楚本项目，是否会产生影响。

#### 项目仅仅是个娱乐项目，如果大家体验的话，就是食用已经打包好的exe。win10 64位。

#### 使用pyinstaller打包，打开后，没有任何界面弹出，是正常情况。关闭方法，打开任务管理器，找到Py Rainbow Fart进程终结即可。

#### 这就是所谓的简约吧，简约到不需要任何界面233333.

#### 配音资源仅可本项目使用，配音资源是找身边学播音专业的妹子配的。请大家不要拿去商用。

#### 配置修改Config文件即可，前4行不用动，从第6-第17行是指，对应输入的字符如果是xxx,就会播放对应的Rainbow Fart.项目注释没怎么写。如果感兴趣的同学可以加我QQ：619443458.其实百度一下原理都就出来啦。

####　6.23更新：

#### 新增了更多关键词，与音效。

#### 新增了萝莉音与御姐音

####　食用方式：在config sound_conf=luoyi_sound_voice.conf 食用萝莉音效

#### 在config sound_conf=yujie_sound_voice.conf 食用御姐音效