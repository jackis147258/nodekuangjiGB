from threading import Thread
from multiprocessing import Process
import os
import requests
import time
from configparser import ConfigParser
import json
import sys 
# import gamePost
import multiprocessing


def game(url,headers,payload):
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

    # print(url,headers,payload)
    # config.payload["record[]"] = "777777";
    # print(payload["record[]"])   

if __name__ == '__main__':
    multiprocessing.freeze_support()
    file_pathConf = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conf.ini")
    cfConf = ConfigParser()
    cfConf.read('conf.ini', encoding='utf-8')

    file_pathData = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.ini")
    cfData = ConfigParser()
    cfData.read('data.ini', encoding='utf-8')
    # print(cf.sections())        # ['mysql', 'redis']
    # print(cf.get('sys_config', 'dataId'))
    dataIdList = json.loads(cfData.get('sys_config', 'dataId'))  
    VarCookie = eval(cfData.get('sys_config', 'cookie'))
    timeSleep = int(cfData.get('sys_config', 'time'))
    # print(timeSleep)
    url = eval(cfConf.get('sys_config', 'url'))    
    headers = eval(cfConf.get('sys_config', 'headers'))
    payload = eval(cfConf.get('sys_config', 'payload')) 
    headers['Cookie']=VarCookie
    # print(headers['Cookie'])
   
    tinydict = {}         
    beiShu=int(float(input("输入倍数: ")))
    # beiShu=timeSleep
    # beiShu=eval(input("输入倍数: "))
    # if isinstance (beiShu,int):
    #     print("请输入数字")
    #     sys.exit()        
    for value in dataIdList:
        payload["record[]"] = value;
        # print(value)
        for i in range(beiShu):            
            # tinydict[i] = Thread(target=game1,args=(url,headers,payload,))    
            tinydict[i] = Process(target=game,args=(url,headers,payload,))    
                # print(i)
        for i in range(beiShu):
            tinydict[i].start()
            # tinydict[i].start()
            # tinydict[i].join()
        # for i in range(beiShu):
        #     if(tinydict[i].is_alive()):                
        #         tinydict[i].terminate()   
        time.sleep(timeSleep)
    
    
    print("结束")
    input('Press Enter to exit…')