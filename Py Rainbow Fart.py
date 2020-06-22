#coding=utf-8
import re
import random
import PyHook3
import datetime
import pythoncom
import threading
from playsound import playsound

_config={
    'key_list_length' : '', #值越大数量，速度越慢，但效果更好
    'sound_conf' : '', #声音文件定义
    'Pool_core':'', #多进程 最大为8 默认为2
    'good_count':'',
    'window_name':'',
    'hello_world':'',#你好世界。  (嘿嘿，你好呀，世界)
    'Good_sound_1':'', #表现好的声音  (哇，宝贝，你真的好厉害鸭)
    'Good_sound_2':'', #表现好的声音 (嘿嘿，我家宝贝最棒)
    'Good_sound_3':'', #表现好的声音 (你的代码写的也太优美了吧，像诗一样。)
    'import_sound':'', #导入包的声音 (biu~恭喜你你成功导入~真棒~)
    'def_sound':'', #定义函数的声音 (啊，你定义了一个方法)
    'print_sound':'', #打印 声音 (叮咚，你正在输出。)
    'fuck_sound':'', #当气急败坏的声音 （怎么啦，不开心了嘛？没有关系的啦，你是最棒的哇。）
    'overtime_sound':'', #当加班时的声音 （呜呜，你怎么又在写代码鸭，这都天黑了，你也不陪陪我嘛。）
    'need_rest_sound':'',# 当需要休息时的声音 （滴滴，宝贝，你该休息啦~注意身体健康呀）
    'annotation':'',# 注释的声音 (咦~你在干嘛鸭~哦！原来在备注。)
    'annotation2':'',# 注释的声音 (咦~你在干嘛鸭~哦！原来在备注。)
}

_sounds={
    'hello_world':'',#你好世界。  (嘿嘿，你好呀，世界)
    'Good_sound_1':'', #表现好的声音  (哇，宝贝，你真的好厉害鸭)
    'Good_sound_2':'', #表现好的声音 (嘿嘿，我家宝贝最棒)
    'Good_sound_3':'', #表现好的声音 (你的代码写的也太优美了吧，像诗一样。)
    'import_sound':'', #导入包的声音 (biu~恭喜你你成功导入~真棒~)
    'def_sound':'', #定义函数的声音 (啊，你定义了一个方法)
    'print_sound':'', #打印 声音 (叮咚，你正在输出。)
    'fuck_sound':'', #当气急败坏的声音 （怎么啦，不开心了嘛？没有关系的啦，你是最棒的哇。）
    'overtime_sound':'', #当加班时的声音 （呜呜，你怎么又在写代码鸭，这都天黑了，你也不陪陪我嘛。）
    'need_rest_sound':'',# 当需要休息时的声音 （滴滴，宝贝，你该休息啦~注意身体健康呀）
    'annotation':'',# 注释的声音 (咦~你在干嘛鸭~哦！原来在备注。)
}

key_list=[]
count_change=0
count_time_rist = 0
start_time=datetime.datetime.now()

def get_config():
    with open('config','r',encoding='utf-8') as f:
        configs_tmp=f.readlines()
    f.close()
    for config_tmp in configs_tmp:
        config_tmp = config_tmp.strip('\n').split('=')
        _config[config_tmp[0]]=config_tmp[1]

    with open(_config['sound_conf'],'r',encoding='utf-8') as f:
        sounds_configs=f.readlines()
    f.close()

    for sounds_config in sounds_configs:
        sounds_config = sounds_config.strip('\n').split(':')
        _sounds[sounds_config[0]]=sounds_config[1]
    
    # print(_config)

def add_key_list(key_value):      
    key_list.append(key_value)
    if len(key_list) >= int(_config['key_list_length']):
        for i in range(0,len(key_list)-1):
            key_list[i]=key_list[i+1]
        key_list.pop()
    
    return key_list


def remove_value(str_text):
    tmp_list=[]
    for i in range(0,len(key_list)):
        tmp_list.append(key_list[i])
    pre_text = str_text[0]
    pos_pre_text = 0
    while len(tmp_list) == len(key_list) :
        pos_pre_text = key_list.index(pre_text,pos_pre_text,len(key_list))
        del_flag=0
        for i in range(1,len(str_text)):
            if str_text[i] == key_list[pos_pre_text+i] :
                del_flag = 1
            else :
                del_flag = 0
        if del_flag == 1:
            for i in range(0,len(str_text)):
                key_list.remove(str_text[i])
        pos_pre_text += 1

def happy_coding(key_value):
    global count_change
    global count_time_rist
    count_change += 1
    tmp_str=""
    for i in range(0,len(key_value)):
        tmp_str+=key_value[i]
    # print(count_change)
    sound_p=[]
    if  count_change % int(_config['good_count']) == 0:
        count_change=0
        case_num = random.randint(1,3)
        if case_num == 1:
            thead_one = threading.Thread(target=playsound, args=(_sounds['Good_sound_1'],))
            sound_p.append(thead_one)
            for n in sound_p:
                n.start()
        if case_num == 2:
            thead_one = threading.Thread(target=playsound, args=(_sounds['Good_sound_2'],))
            sound_p.append(thead_one)
            for n in sound_p:
                n.start()
        if case_num == 3:
            thead_one = threading.Thread(target=playsound, args=(_sounds['Good_sound_3'],))
            sound_p.append(thead_one)
            for n in sound_p:
                n.start()

    if _config['hello_world'] in tmp_str:
        thead_one = threading.Thread(target=playsound, args=(_sounds['hello_world'],))
        sound_p.append(thead_one)
        remove_value(_config['hello_world'])
        for n in sound_p:
            n.start()
    
    if _config['import_sound'] in tmp_str:
        thead_one = threading.Thread(target=playsound, args=(_sounds['import_sound'],))
        sound_p.append(thead_one)
        remove_value(_config['import_sound'])
        for n in sound_p:
            n.start()

    if _config['def_sound'] in tmp_str:
        thead_one = threading.Thread(target=playsound, args=(_sounds['def_sound'],))
        sound_p.append(thead_one)
        remove_value(_config['def_sound'])
        for n in sound_p:
            n.start()
    
    if _config['print_sound'] in tmp_str:
        thead_one = threading.Thread(target=playsound, args=(_sounds['print_sound'],))
        sound_p.append(thead_one)
        remove_value(_config['print_sound'])
        for n in sound_p:
            n.start()

    if _config['fuck_sound'] in tmp_str:
        thead_one = threading.Thread(target=playsound, args=(_sounds['fuck_sound'],))
        sound_p.append(thead_one)
        remove_value(_config['fuck_sound'])
        for n in sound_p:
            n.start()
    
    # if _config['annotation'] in tmp_str:
    #     thead_one = threading.Thread(target=playsound, args=(_sounds['annotation'],))
    #     sound_p.append(thead_one)
    #     remove_value(_config['annotation'])
    #     for n in sound_p:
    #         n.start()
        

    if _config['annotation2'] in tmp_str:
        thead_one = threading.Thread(target=playsound, args=(_sounds['annotation2'],))
        sound_p.append(thead_one)
        remove_value(_config['annotation2'])
        for n in sound_p:
            n.start()
        

    try:
        pa=re.search(_config['overtime_sound'],tmp_str).span()
        pa_str=""
        for i in range(pa[0],pa[1]):
            pa_str+=tmp_str[i]
        # print("ok")
        thead_one = threading.Thread(target=playsound, args=(_sounds['overtime_sound'],))
        sound_p.append(thead_one)
        remove_value(pa_str)
        for n in sound_p:
            n.start()
    except:
        pass
    
    zhong_time = datetime.datetime.now()
    if int((zhong_time-start_time).seconds / 3600) == 1:
        if count_time_rist <= 3 :
            thead_one = threading.Thread(target=playsound, args=(_sounds['need_rest_sound'],))
            sound_p.append(thead_one)
            for n in sound_p:
                n.start()
    
    if int((zhong_time-start_time).seconds / 3600) == 2:
        count_time_rist += 1
        if count_time_rist <= 3 :
            thead_one = threading.Thread(target=playsound, args=(_sounds['need_rest_sound'],))
            sound_p.append(thead_one)
            for n in sound_p:
                n.start()
    
        count_time_rist+=1
        

# 键盘事件处理函数ddprinthellowohelloworlddpython
def OnKeyboardEvent(event):
    key_value=event.Ascii
    #判断输入的值为Ascii值
    #并且过滤 空格 TAB 换行 BACK
    if key_value > 0 and _config['window_name'] in event.WindowName:
        if key_value == 9 or key_value == 13 or key_value == 32 or key_value ==8:
            pass
        else:
            key_value = str(chr(key_value))
            tmp_key=add_key_list(key_value)
            happy_coding(tmp_key)
    # print(key_list)
    return True

def main():
    get_config()
    hm = PyHook3.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    

if __name__ == "__main__":
    main()