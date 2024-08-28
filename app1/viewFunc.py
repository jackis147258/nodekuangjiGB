from urllib.parse import urlparse ,unquote,quote,parse_qs,urlencode
from app1 import models
from  app1.until import tools,ps1
import json

def url_dict():
          # https://zh.surebet.com/surebets?utf8=✓&selector[order]=profit&selector[outcomes][]=&selector[outcomes][]=2&selector[outcomes][]=3&selector[min_profit]=0.5&selector[max_profit]=&selector[min_roi]=&selector[max_roi]=&selector[settled_in]=86400&selector[bookies_settings]=0:67::;0:105::;4:72::;0:66::;0:76::;0:91::;0:93::;0:182::;0:74::;0:37::;4:148::;0:211::;0:114::;0:260::;0:101::;0:132::;0:42::;0:40::;0:225::;0:126::;0:21::;0:70::;0:263::;0:246::;0:26::;0:139::;0:36::;0:150::;0:202::;0:151::;0:23::;0:204::;0:200::;0:203::;0:0::;0:32::;0:1::;0:65::;0:161::;0:29::;0:10::;0:45::;0:228::;0:34::;0:77::;0:58::;0:253::;0:165::;0:100::;0:95::;0:180::;0:208::;0:48::;0:14::;0:102::;0:197::;0:11::;0:188::;0:38::;0:147::;0:52::;0:198::;0:55::;0:187::;0:33::;0:13::;0:68::;0:176::;0:125::;0:248::;0:236::;0:49::;0:215::;0:62::;0:75::;0:12::;0:193::;0:90::;0:46::;0:229::;0:210::;0:146::;0:117::;0:135::;0:24::;0:92::;0:88::;0:73::;0:258::;0:261::;0:154::;0:129::;0:214::;0:56::;0:104::;0:230::;0:22::;0:145::;0:136::;0:109::;0:257::;0:5::;0:6::;0:60::;0:245::;0:235::;0:175::;0:224::;0:190::;0:4::;0:183::;0:242::;0:213::;0:244::;0:30::;0:15::;0:212::;0:219::;0:128::;0:233::;0:50::;0:9::;0:179::;0:259::;0:178::;0:41::;0:85::;0:84::;0:130::;0:133::;0:247::;0:3::;0:240::;0:8::;0:118::;0:89::;0:166::;0:124::;0:226::;0:209::;0:82::;0:63::;0:83::;0:98::;0:99::;0:61::;0:167::;0:20::;0:19::;0:164::;0:249::;0:39::;0:174::;0:31::;0:54::;0:51::;0:181::;0:2::;0:87::;0:143::;0:7::;0:189::;0:237::;0:156::;0:47::;0:234::;0:251::;0:262::;0:134::;0:218::;0:123::;0:94::;0:254::;0:25::;0:69::;0:140::;0:119::;0:16::;0:207::;0:232::;0:223::;0:163::;0:256::;0:97::;0:173::;0:191::;0:186::;0:192::;0:43::;0:243::;0:199::;0:103::;0:159::;0:184::;0:18::;0:35::;0:59::;0:64::;0:216::;0:86::;0:120::;0:205::;0:149::;0:127::;0:115::;0:17::;0:110::;0:238::;0:239::;0:217::;0:53::;0:155::;0:96::;0:28::;0:220::;0:222::;0:250::;0:252::;0:44::;0:196::;0:227::;0:206::;0:221::;0:71::;0:79::;0:80::;0:78::;0:57::;0:81::;0:27::&selector[exclude_sports_ids_str]=56+57+0+43+32+1+2+3+4+55+60+7+6+5+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+14+27+53+54+58+16+30+13+17+18+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+22+35+24+38+25&selector[extra_filters]=3&commit=筛选&narrow=
    str5="https://zh.surebet.com/surebets?utf8=✓&filter[selected][]=&filter[selected][]=33714663&filter[save]=&filter[current_id]=33714663&selector[order]=profit&selector[outcomes][]=&selector[outcomes][]=2&selector[outcomes][]=3&selector[min_profit]=0.0&selector[max_profit]=&selector[min_roi]=&selector[max_roi]=&selector[settled_in]=86400&selector[bookies_settings]=0:67::;0:72::;0:66::;0:76::;0:182::;0:74::;0:37::;0:148::;0:211::;0:114::;0:260::;0:132::;0:42::;0:40::;0:225::;0:126::;0:21::;0:263::;0:23::;0:246::;0:26::;0:139::;0:36::;0:150::;0:202::;0:151::;0:204::;0:125::;0:200::;0:203::;0:::;0:32::;0:1::;0:65::;0:161::;0:29::;0:10::;0:45::;0:228::;0:34::;0:77::;0:58::;0:253::;0:165::;0:95::;0:180::;0:208::;0:48::;0:14::;0:197::;0:11::;0:188::;0:38::;0:147::;0:52::;0:198::;0:55::;0:187::;0:33::;0:13::;0:176::;0:248::;0:236::;0:215::;0:49::;0:62::;0:75::;0:12::;0:193::;0:90::;0:46::;0:229::;0:210::;0:146::;0:117::;0:135::;0:24::;0:73::;0:258::;0:261::;0:154::;0:129::;0:56::;0:230::;0:22::;0:145::;0:136::;0:30::;0:257::;0:5::;0:6::;0:214::;0:245::;0:235::;0:175::;0:224::;0:190::;0:4::;0:183::;0:242::;0:213::;0:244::;0:15::;0:212::;0:219::;0:128::;0:233::;0:50::;0:9::;0:179::;0:259::;0:178::;0:41::;0:130::;0:133::;0:247::;0:3::;0:240::;0:8::;0:118::;0:89::;0:166::;0:124::;0:226::;0:209::;0:63::;0:61::;0:167::;0:20::;0:164::;0:19::;0:88::;0:249::;0:39::;0:174::;0:31::;0:54::;0:51::;0:181::;0:2::;0:87::;0:143::;0:7::;0:189::;0:237::;0:156::;0:47::;0:234::;0:251::;0:262::;0:134::;0:218::;0:109::;0:123::;0:201::;0:254::;0:25::;0:69::;0:140::;0:119::;0:16::;0:207::;0:232::;0:223::;0:256::;0:163::;0:97::;0:173::;0:191::;0:186::;0:192::;0:43::;0:243::;0:199::;0:159::;0:184::;0:18::;0:35::;0:59::;0:64::;0:216::;0:86::;0:120::;0:205::;0:149::;0:127::;0:115::;0:17::;0:110::;0:53::;0:238::;0:239::;0:217::;0:206::;0:155::;0:28::;0:222::;0:220::;0:250::;0:252::;0:44::;0:196::;0:227::;0:221::;0:27::&selector[exclude_sports_ids_str]=26+23+16+28+11+18+9+17+24+21+27+14+10+56+57+3+8+25+6+5+7+32+29+30+2+43+44+34+39+48+59+47+49+46+45+36+33+40+42+41+37+35+38+63+4+55+60+31+22+0+1+64+20+61+62+51+50+15+53+54+58+19+12+13&selector[extra_filters]=3&narrow="
    query = urlparse(str5).query
    params = parse_qs(query) 
    # print(params)
    # for key,value in params.items():       
    #     print(str(key)+ ':'+str(value))    
    
    return params

def searchStr(userId):
    params=url_dict()
    row_object=models.TcSearch.objects.filter(uid=userId).first()    
    returnOnInvestmentLittle=row_object.returnOnInvestmentLittle  
    returnOnInvestmentBig=row_object.returnOnInvestmentBig
    profitRangeLittle=row_object.profitRangeLittle
    profitRangeBig=row_object.profitRangeBig
    paiXu=row_object.paiXu
    raceTime=row_object.raceTime
    
    tcWebs=row_object.tcWebs.all()
    tcSports=row_object.tcSports.all()
    menOneTwos=row_object.menOneTwos.all()    
    
    # params['utf8']="['✓']"
    # params['filter[selected][]']="['33714663']"
    # params['filter[current_id]']="['33714663']"
    # params['selector[order]']="['profit']"
    # first = True
    # for menOneTwo in menOneTwos:    
    #   if first:
    #     first = False   
    #     menOneTwoStr= menOneTwo.noStr
    #   else:
    #     menOneTwoStr+= ","+menOneTwo.noStr    
    
    # params['selector[outcomes][]'][]="['2', '3']"
    params['selector[min_profit]'][0]=profitRangeLittle
    # params['selector[max_profit]']="["+profitRangeBig+"]"
    # params['selector[max_profit]']="['0.0']"    
    
    params['selector[settled_in]'][0]=str(raceTime)
    
    # Web
    for tcWeb in tcWebs:       
      tcWebStrFind="0:"+tcWeb.noStr+"::"
      # 替换
      tcWebStrReplace="4:"+tcWeb.noStr+"::"      
      
      
      t_str1=params['selector[bookies_settings]'][0]
      
      
      str11Ok = str.replace(t_str1, tcWebStrFind, tcWebStrReplace)
      params['selector[bookies_settings]'][0]=str11Ok
     

    # Sport
    for tcSport in tcSports: 
      tcSportFind=tcSport.noStr
      # 替换
      t_str2=params['selector[exclude_sports_ids_str]'][0]+" " # 加空格
      listS = t_str2.split(" ")
      for listS1 in listS:
        if listS1==tcSportFind:
          listS.remove(listS1)
      str2sportNumOk=" ".join(listS)
      # t_str2+="+"
      # str2sportNumOk = str.replace(t_str2, tcSportFind, tcSportReplace)
      # str2sportNumOk = str2sportNumOk[:-1]      # 去空格
      params['selector[exclude_sports_ids_str]'][0]=str2sportNumOk
      
      
    # # 0:67::
    # tcWebStr=""
    # first = True
    # for tcWeb in tcWebs:  
    #   if first:
    #     first = False    
    #     tcWebStr="0:"+tcWeb.noStr+"::"
    #   else:
    #     tcWebStr+=",0:"+tcWeb.noStr+"::"
    # params['selector[bookies_settings]']=tcWebStr
    
    # tcSportStr=""
    # first = True
    # for tcSport in tcSports:  
    #   if first:
    #     first = False     
    #     tcSportStr=tcSport.noStr   
    #   else:
    #     tcSportStr+="+"+tcSport.noStr
    # params['selector[exclude_sports_ids_str]']=tcSportStr
    # params['selector[exclude_sports_ids_str]']="56+57+0+43+32+1+2+3"    
    params['selector[extra_filters]'][0]='3'
      # 转成 url 转义
    result = urlencode(params)
    # get 出去 得到返回值
    url = "https://zh.surebet.com/surebets?"
    url=url+result    
    # url = "https://zh.surebet.com/surebets?utf8=%E2%9C%93&filter%5Bselected%5D%5B%5D=&filter%5Bselected%5D%5B%5D=33714663&filter%5Bsave%5D=&filter%5Bcurrent_id%5D=33714663&selector%5Border%5D=profit&selector%5Boutcomes%5D%5B%5D=&selector%5Boutcomes%5D%5B%5D=2&selector%5Boutcomes%5D%5B%5D=3&selector%5Bmin_profit%5D=0.0&selector%5Bmax_profit%5D=&selector%5Bmin_roi%5D=&selector%5Bmax_roi%5D=&selector%5Bsettled_in%5D=86400&selector%5Bbookies_settings%5D=0%3A67%3A%3A%3B4%3A72%3A%3A%3B0%3A66%3A%3A%3B0%3A76%3A%3A%3B0%3A182%3A%3A%3B0%3A74%3A%3A%3B0%3A37%3A%3A%3B4%3A148%3A%3A%3B0%3A211%3A%3A%3B0%3A114%3A%3A%3B0%3A260%3A%3A%3B0%3A132%3A%3A%3B0%3A42%3A%3A%3B0%3A40%3A%3A%3B0%3A225%3A%3A%3B0%3A126%3A%3A%3B0%3A21%3A%3A%3B0%3A263%3A%3A%3B0%3A23%3A%3A%3B0%3A246%3A%3A%3B0%3A26%3A%3A%3B0%3A139%3A%3A%3B0%3A36%3A%3A%3B0%3A150%3A%3A%3B0%3A202%3A%3A%3B0%3A151%3A%3A%3B0%3A204%3A%3A%3B0%3A125%3A%3A%3B0%3A200%3A%3A%3B0%3A203%3A%3A%3B0%3A%3A%3A%3B0%3A32%3A%3A%3B0%3A1%3A%3A%3B0%3A65%3A%3A%3B0%3A161%3A%3A%3B0%3A29%3A%3A%3B0%3A10%3A%3A%3B0%3A45%3A%3A%3B0%3A228%3A%3A%3B0%3A34%3A%3A%3B0%3A77%3A%3A%3B0%3A58%3A%3A%3B0%3A253%3A%3A%3B0%3A165%3A%3A%3B0%3A95%3A%3A%3B0%3A180%3A%3A%3B0%3A208%3A%3A%3B0%3A48%3A%3A%3B0%3A14%3A%3A%3B0%3A197%3A%3A%3B0%3A11%3A%3A%3B0%3A188%3A%3A%3B0%3A38%3A%3A%3B0%3A147%3A%3A%3B0%3A52%3A%3A%3B0%3A198%3A%3A%3B0%3A55%3A%3A%3B0%3A187%3A%3A%3B0%3A33%3A%3A%3B0%3A13%3A%3A%3B0%3A176%3A%3A%3B0%3A248%3A%3A%3B0%3A236%3A%3A%3B0%3A215%3A%3A%3B0%3A49%3A%3A%3B0%3A62%3A%3A%3B0%3A75%3A%3A%3B0%3A12%3A%3A%3B0%3A193%3A%3A%3B0%3A90%3A%3A%3B0%3A46%3A%3A%3B0%3A229%3A%3A%3B0%3A210%3A%3A%3B0%3A146%3A%3A%3B0%3A117%3A%3A%3B0%3A135%3A%3A%3B0%3A24%3A%3A%3B0%3A73%3A%3A%3B0%3A258%3A%3A%3B0%3A261%3A%3A%3B0%3A154%3A%3A%3B0%3A129%3A%3A%3B0%3A56%3A%3A%3B0%3A230%3A%3A%3B0%3A22%3A%3A%3B0%3A145%3A%3A%3B0%3A136%3A%3A%3B0%3A30%3A%3A%3B0%3A257%3A%3A%3B0%3A5%3A%3A%3B0%3A6%3A%3A%3B0%3A214%3A%3A%3B0%3A245%3A%3A%3B0%3A235%3A%3A%3B0%3A175%3A%3A%3B0%3A224%3A%3A%3B0%3A190%3A%3A%3B0%3A4%3A%3A%3B0%3A183%3A%3A%3B0%3A242%3A%3A%3B0%3A213%3A%3A%3B0%3A244%3A%3A%3B0%3A15%3A%3A%3B0%3A212%3A%3A%3B0%3A219%3A%3A%3B0%3A128%3A%3A%3B0%3A233%3A%3A%3B0%3A50%3A%3A%3B0%3A9%3A%3A%3B0%3A179%3A%3A%3B0%3A259%3A%3A%3B0%3A178%3A%3A%3B0%3A41%3A%3A%3B0%3A130%3A%3A%3B0%3A133%3A%3A%3B0%3A247%3A%3A%3B0%3A3%3A%3A%3B0%3A240%3A%3A%3B0%3A8%3A%3A%3B0%3A118%3A%3A%3B0%3A89%3A%3A%3B0%3A166%3A%3A%3B0%3A124%3A%3A%3B0%3A226%3A%3A%3B0%3A209%3A%3A%3B0%3A63%3A%3A%3B0%3A61%3A%3A%3B0%3A167%3A%3A%3B0%3A20%3A%3A%3B0%3A164%3A%3A%3B0%3A19%3A%3A%3B0%3A88%3A%3A%3B0%3A249%3A%3A%3B0%3A39%3A%3A%3B0%3A174%3A%3A%3B0%3A31%3A%3A%3B0%3A54%3A%3A%3B0%3A51%3A%3A%3B0%3A181%3A%3A%3B0%3A2%3A%3A%3B0%3A87%3A%3A%3B0%3A143%3A%3A%3B0%3A7%3A%3A%3B0%3A189%3A%3A%3B0%3A237%3A%3A%3B0%3A156%3A%3A%3B0%3A47%3A%3A%3B0%3A234%3A%3A%3B0%3A251%3A%3A%3B0%3A262%3A%3A%3B0%3A134%3A%3A%3B0%3A218%3A%3A%3B0%3A109%3A%3A%3B0%3A123%3A%3A%3B0%3A201%3A%3A%3B0%3A254%3A%3A%3B0%3A25%3A%3A%3B0%3A69%3A%3A%3B0%3A140%3A%3A%3B0%3A119%3A%3A%3B0%3A16%3A%3A%3B0%3A207%3A%3A%3B0%3A232%3A%3A%3B0%3A223%3A%3A%3B0%3A256%3A%3A%3B0%3A163%3A%3A%3B0%3A97%3A%3A%3B0%3A173%3A%3A%3B0%3A191%3A%3A%3B0%3A186%3A%3A%3B0%3A192%3A%3A%3B0%3A43%3A%3A%3B0%3A243%3A%3A%3B0%3A199%3A%3A%3B0%3A159%3A%3A%3B0%3A184%3A%3A%3B0%3A18%3A%3A%3B0%3A35%3A%3A%3B0%3A59%3A%3A%3B0%3A64%3A%3A%3B0%3A216%3A%3A%3B0%3A86%3A%3A%3B0%3A120%3A%3A%3B0%3A205%3A%3A%3B0%3A149%3A%3A%3B0%3A127%3A%3A%3B0%3A115%3A%3A%3B0%3A17%3A%3A%3B0%3A110%3A%3A%3B0%3A53%3A%3A%3B0%3A238%3A%3A%3B0%3A239%3A%3A%3B0%3A217%3A%3A%3B0%3A206%3A%3A%3B0%3A155%3A%3A%3B0%3A28%3A%3A%3B0%3A222%3A%3A%3B0%3A220%3A%3A%3B0%3A250%3A%3A%3B0%3A252%3A%3A%3B0%3A44%3A%3A%3B0%3A196%3A%3A%3B0%3A227%3A%3A%3B0%3A221%3A%3A%3B0%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=56+57+0+43+32+1+2+3+4+55+60+7+6+5+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+14+27+53+54+58+16+30+13+17+18+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+22+35+24+38+25&selector%5Bextra_filters%5D=3&narrow="
    
    html=tools.getUrlList(url,userId)    
    listUrl=ps1.parseHtml(html)
    # html=tools.getLogin()    
    return listUrl

# 处理 vue 不分
def searchNext(userId,cursor):
    # t_seachBody = parse_qs(str(seachBody, encoding='utf-8')) 
    # urlPath=t_seachBody['urlPath']
    # url = "https://zh.surebet.com/surebets?"+urlPath
    
      # 转成 url 转义
    # result = urlencode(cursor)
    # get 出去 得到返回值
    # url = "https://zh.surebet.com/surebets?cursor="
    url = "https://zh.surebet.com"
    url=url+cursor    
    # url = "https://zh.surebet.com/surebets?utf8=%E2%9C%93&filter%5Bselected%5D%5B%5D=&filter%5Bselected%5D%5B%5D=33714663&filter%5Bsave%5D=&filter%5Bcurrent_id%5D=33714663&selector%5Border%5D=profit&selector%5Boutcomes%5D%5B%5D=&selector%5Boutcomes%5D%5B%5D=2&selector%5Boutcomes%5D%5B%5D=3&selector%5Bmin_profit%5D=0.0&selector%5Bmax_profit%5D=&selector%5Bmin_roi%5D=&selector%5Bmax_roi%5D=&selector%5Bsettled_in%5D=86400&selector%5Bbookies_settings%5D=0%3A67%3A%3A%3B4%3A72%3A%3A%3B0%3A66%3A%3A%3B0%3A76%3A%3A%3B0%3A182%3A%3A%3B0%3A74%3A%3A%3B0%3A37%3A%3A%3B4%3A148%3A%3A%3B0%3A211%3A%3A%3B0%3A114%3A%3A%3B0%3A260%3A%3A%3B0%3A132%3A%3A%3B0%3A42%3A%3A%3B0%3A40%3A%3A%3B0%3A225%3A%3A%3B0%3A126%3A%3A%3B0%3A21%3A%3A%3B0%3A263%3A%3A%3B0%3A23%3A%3A%3B0%3A246%3A%3A%3B0%3A26%3A%3A%3B0%3A139%3A%3A%3B0%3A36%3A%3A%3B0%3A150%3A%3A%3B0%3A202%3A%3A%3B0%3A151%3A%3A%3B0%3A204%3A%3A%3B0%3A125%3A%3A%3B0%3A200%3A%3A%3B0%3A203%3A%3A%3B0%3A%3A%3A%3B0%3A32%3A%3A%3B0%3A1%3A%3A%3B0%3A65%3A%3A%3B0%3A161%3A%3A%3B0%3A29%3A%3A%3B0%3A10%3A%3A%3B0%3A45%3A%3A%3B0%3A228%3A%3A%3B0%3A34%3A%3A%3B0%3A77%3A%3A%3B0%3A58%3A%3A%3B0%3A253%3A%3A%3B0%3A165%3A%3A%3B0%3A95%3A%3A%3B0%3A180%3A%3A%3B0%3A208%3A%3A%3B0%3A48%3A%3A%3B0%3A14%3A%3A%3B0%3A197%3A%3A%3B0%3A11%3A%3A%3B0%3A188%3A%3A%3B0%3A38%3A%3A%3B0%3A147%3A%3A%3B0%3A52%3A%3A%3B0%3A198%3A%3A%3B0%3A55%3A%3A%3B0%3A187%3A%3A%3B0%3A33%3A%3A%3B0%3A13%3A%3A%3B0%3A176%3A%3A%3B0%3A248%3A%3A%3B0%3A236%3A%3A%3B0%3A215%3A%3A%3B0%3A49%3A%3A%3B0%3A62%3A%3A%3B0%3A75%3A%3A%3B0%3A12%3A%3A%3B0%3A193%3A%3A%3B0%3A90%3A%3A%3B0%3A46%3A%3A%3B0%3A229%3A%3A%3B0%3A210%3A%3A%3B0%3A146%3A%3A%3B0%3A117%3A%3A%3B0%3A135%3A%3A%3B0%3A24%3A%3A%3B0%3A73%3A%3A%3B0%3A258%3A%3A%3B0%3A261%3A%3A%3B0%3A154%3A%3A%3B0%3A129%3A%3A%3B0%3A56%3A%3A%3B0%3A230%3A%3A%3B0%3A22%3A%3A%3B0%3A145%3A%3A%3B0%3A136%3A%3A%3B0%3A30%3A%3A%3B0%3A257%3A%3A%3B0%3A5%3A%3A%3B0%3A6%3A%3A%3B0%3A214%3A%3A%3B0%3A245%3A%3A%3B0%3A235%3A%3A%3B0%3A175%3A%3A%3B0%3A224%3A%3A%3B0%3A190%3A%3A%3B0%3A4%3A%3A%3B0%3A183%3A%3A%3B0%3A242%3A%3A%3B0%3A213%3A%3A%3B0%3A244%3A%3A%3B0%3A15%3A%3A%3B0%3A212%3A%3A%3B0%3A219%3A%3A%3B0%3A128%3A%3A%3B0%3A233%3A%3A%3B0%3A50%3A%3A%3B0%3A9%3A%3A%3B0%3A179%3A%3A%3B0%3A259%3A%3A%3B0%3A178%3A%3A%3B0%3A41%3A%3A%3B0%3A130%3A%3A%3B0%3A133%3A%3A%3B0%3A247%3A%3A%3B0%3A3%3A%3A%3B0%3A240%3A%3A%3B0%3A8%3A%3A%3B0%3A118%3A%3A%3B0%3A89%3A%3A%3B0%3A166%3A%3A%3B0%3A124%3A%3A%3B0%3A226%3A%3A%3B0%3A209%3A%3A%3B0%3A63%3A%3A%3B0%3A61%3A%3A%3B0%3A167%3A%3A%3B0%3A20%3A%3A%3B0%3A164%3A%3A%3B0%3A19%3A%3A%3B0%3A88%3A%3A%3B0%3A249%3A%3A%3B0%3A39%3A%3A%3B0%3A174%3A%3A%3B0%3A31%3A%3A%3B0%3A54%3A%3A%3B0%3A51%3A%3A%3B0%3A181%3A%3A%3B0%3A2%3A%3A%3B0%3A87%3A%3A%3B0%3A143%3A%3A%3B0%3A7%3A%3A%3B0%3A189%3A%3A%3B0%3A237%3A%3A%3B0%3A156%3A%3A%3B0%3A47%3A%3A%3B0%3A234%3A%3A%3B0%3A251%3A%3A%3B0%3A262%3A%3A%3B0%3A134%3A%3A%3B0%3A218%3A%3A%3B0%3A109%3A%3A%3B0%3A123%3A%3A%3B0%3A201%3A%3A%3B0%3A254%3A%3A%3B0%3A25%3A%3A%3B0%3A69%3A%3A%3B0%3A140%3A%3A%3B0%3A119%3A%3A%3B0%3A16%3A%3A%3B0%3A207%3A%3A%3B0%3A232%3A%3A%3B0%3A223%3A%3A%3B0%3A256%3A%3A%3B0%3A163%3A%3A%3B0%3A97%3A%3A%3B0%3A173%3A%3A%3B0%3A191%3A%3A%3B0%3A186%3A%3A%3B0%3A192%3A%3A%3B0%3A43%3A%3A%3B0%3A243%3A%3A%3B0%3A199%3A%3A%3B0%3A159%3A%3A%3B0%3A184%3A%3A%3B0%3A18%3A%3A%3B0%3A35%3A%3A%3B0%3A59%3A%3A%3B0%3A64%3A%3A%3B0%3A216%3A%3A%3B0%3A86%3A%3A%3B0%3A120%3A%3A%3B0%3A205%3A%3A%3B0%3A149%3A%3A%3B0%3A127%3A%3A%3B0%3A115%3A%3A%3B0%3A17%3A%3A%3B0%3A110%3A%3A%3B0%3A53%3A%3A%3B0%3A238%3A%3A%3B0%3A239%3A%3A%3B0%3A217%3A%3A%3B0%3A206%3A%3A%3B0%3A155%3A%3A%3B0%3A28%3A%3A%3B0%3A222%3A%3A%3B0%3A220%3A%3A%3B0%3A250%3A%3A%3B0%3A252%3A%3A%3B0%3A44%3A%3A%3B0%3A196%3A%3A%3B0%3A227%3A%3A%3B0%3A221%3A%3A%3B0%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=56+57+0+43+32+1+2+3+4+55+60+7+6+5+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+14+27+53+54+58+16+30+13+17+18+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+22+35+24+38+25&selector%5Bextra_filters%5D=3&narrow="
    
    html=tools.getUrlList(url,userId)    
    re =ps1.parseHtml(html)
    # json, nextPageHref, previousHref =ps1.parseHtml(html)
    # html=tools.getLogin()    
    json_str = json.dumps(re)
    return json_str
  
    

    
# 处理 vue 不分
def searchDict(userId,seachBody):
    t_seachBody = parse_qs(str(seachBody, encoding='utf-8')) 
    params=url_dict()    
    t_postData=params
    # params['utf8']="['✓']"
    # params['filter[selected][]']="['33714663']"
    # params['filter[current_id]']="['33714663']"
    # params['selector[order]']="['profit']"
    # first = True
    # for menOneTwo in menOneTwos:    
    #   if first:
    #     first = False   
    #     menOneTwoStr= menOneTwo.noStr
    #   else:
    #     menOneTwoStr+= ","+menOneTwo.noStr    
    
    # params['selector[outcomes][]'][]="['2', '3']"
    params['selector[min_profit]']=t_seachBody['profit']  
    # params['selector[max_profit]']="["+profitRangeBig+"]"
    # params['selector[max_profit]']=t_postData['selector[min_profit]']   
    # params['selector[max_profit]']=t_seachBody['profit']   
    
    # params['selector[settled_in]']=t_seachBody['time'] 
    
    # Web
    # t_webs=t_postData['selector[bookies_settings]']
    # t_webslist = t_webs[0].split(",")
    # t_str1=params['selector[bookies_settings]'][0]    
    # for tcWeb in t_webslist:       
    #   tcWebStrFind="0:"+str(tcWeb)+"::"
    #   # 替换
    #   tcWebStrReplace="4:"+str(tcWeb)+"::" 
    #   t_str1 = str.replace(t_str1, tcWebStrFind, tcWebStrReplace)
      
    # params['selector[bookies_settings]'][0]=t_str1
    
    t_webs=t_seachBody['platform']
    t_webslist = t_webs[0].split(",")
    t_str1=params['selector[bookies_settings]'][0]    
    for tcWeb in t_webslist:       
      tcWebStrFind="0:"+str(tcWeb)+"::"
      # 替换
      tcWebStrReplace="4:"+str(tcWeb)+"::" 
      t_str1 = str.replace(t_str1, tcWebStrFind, tcWebStrReplace)
      
    params['selector[bookies_settings]'][0]=t_str1
     

    # Sport
    # t_tcSport=t_postData['selector[exclude_sports_ids_str]']
    # t_tcSportlist = t_tcSport[0].split(",")
    # t_str2=params['selector[exclude_sports_ids_str]'][0] # 加空格
    # listS = t_str2.split(" ")
    # for tcSport in t_tcSportlist:     
    #   if tcSport in listS:      
    #      listS.remove(tcSport) 
    # str2sportNumOk=" ".join(listS)
    # params['selector[exclude_sports_ids_str]'][0]=str2sportNumOk
    
    t_tcSport=t_seachBody['moveType']
    t_tcSportlist = t_tcSport[0].split(",")
    t_str2=params['selector[exclude_sports_ids_str]'][0] # 加空格
    listS = t_str2.split(" ")
    for tcSport in t_tcSportlist:     
      if tcSport in listS:      
         listS.remove(tcSport) 
    str2sportNumOk=" ".join(listS)
    params['selector[exclude_sports_ids_str]'][0]=str2sportNumOk
      
       
    
    params['selector[extra_filters]'][0]='3'
    
      # 转成 url 转义
    result = urlencode(params)
    # get 出去 得到返回值
    url = "https://zh.surebet.com/surebets?"
    url=url+result    
    # url = "https://zh.surebet.com/surebets?utf8=%E2%9C%93&filter%5Bselected%5D%5B%5D=&filter%5Bselected%5D%5B%5D=33714663&filter%5Bsave%5D=&filter%5Bcurrent_id%5D=33714663&selector%5Border%5D=profit&selector%5Boutcomes%5D%5B%5D=&selector%5Boutcomes%5D%5B%5D=2&selector%5Boutcomes%5D%5B%5D=3&selector%5Bmin_profit%5D=0.0&selector%5Bmax_profit%5D=&selector%5Bmin_roi%5D=&selector%5Bmax_roi%5D=&selector%5Bsettled_in%5D=86400&selector%5Bbookies_settings%5D=0%3A67%3A%3A%3B4%3A72%3A%3A%3B0%3A66%3A%3A%3B0%3A76%3A%3A%3B0%3A182%3A%3A%3B0%3A74%3A%3A%3B0%3A37%3A%3A%3B4%3A148%3A%3A%3B0%3A211%3A%3A%3B0%3A114%3A%3A%3B0%3A260%3A%3A%3B0%3A132%3A%3A%3B0%3A42%3A%3A%3B0%3A40%3A%3A%3B0%3A225%3A%3A%3B0%3A126%3A%3A%3B0%3A21%3A%3A%3B0%3A263%3A%3A%3B0%3A23%3A%3A%3B0%3A246%3A%3A%3B0%3A26%3A%3A%3B0%3A139%3A%3A%3B0%3A36%3A%3A%3B0%3A150%3A%3A%3B0%3A202%3A%3A%3B0%3A151%3A%3A%3B0%3A204%3A%3A%3B0%3A125%3A%3A%3B0%3A200%3A%3A%3B0%3A203%3A%3A%3B0%3A%3A%3A%3B0%3A32%3A%3A%3B0%3A1%3A%3A%3B0%3A65%3A%3A%3B0%3A161%3A%3A%3B0%3A29%3A%3A%3B0%3A10%3A%3A%3B0%3A45%3A%3A%3B0%3A228%3A%3A%3B0%3A34%3A%3A%3B0%3A77%3A%3A%3B0%3A58%3A%3A%3B0%3A253%3A%3A%3B0%3A165%3A%3A%3B0%3A95%3A%3A%3B0%3A180%3A%3A%3B0%3A208%3A%3A%3B0%3A48%3A%3A%3B0%3A14%3A%3A%3B0%3A197%3A%3A%3B0%3A11%3A%3A%3B0%3A188%3A%3A%3B0%3A38%3A%3A%3B0%3A147%3A%3A%3B0%3A52%3A%3A%3B0%3A198%3A%3A%3B0%3A55%3A%3A%3B0%3A187%3A%3A%3B0%3A33%3A%3A%3B0%3A13%3A%3A%3B0%3A176%3A%3A%3B0%3A248%3A%3A%3B0%3A236%3A%3A%3B0%3A215%3A%3A%3B0%3A49%3A%3A%3B0%3A62%3A%3A%3B0%3A75%3A%3A%3B0%3A12%3A%3A%3B0%3A193%3A%3A%3B0%3A90%3A%3A%3B0%3A46%3A%3A%3B0%3A229%3A%3A%3B0%3A210%3A%3A%3B0%3A146%3A%3A%3B0%3A117%3A%3A%3B0%3A135%3A%3A%3B0%3A24%3A%3A%3B0%3A73%3A%3A%3B0%3A258%3A%3A%3B0%3A261%3A%3A%3B0%3A154%3A%3A%3B0%3A129%3A%3A%3B0%3A56%3A%3A%3B0%3A230%3A%3A%3B0%3A22%3A%3A%3B0%3A145%3A%3A%3B0%3A136%3A%3A%3B0%3A30%3A%3A%3B0%3A257%3A%3A%3B0%3A5%3A%3A%3B0%3A6%3A%3A%3B0%3A214%3A%3A%3B0%3A245%3A%3A%3B0%3A235%3A%3A%3B0%3A175%3A%3A%3B0%3A224%3A%3A%3B0%3A190%3A%3A%3B0%3A4%3A%3A%3B0%3A183%3A%3A%3B0%3A242%3A%3A%3B0%3A213%3A%3A%3B0%3A244%3A%3A%3B0%3A15%3A%3A%3B0%3A212%3A%3A%3B0%3A219%3A%3A%3B0%3A128%3A%3A%3B0%3A233%3A%3A%3B0%3A50%3A%3A%3B0%3A9%3A%3A%3B0%3A179%3A%3A%3B0%3A259%3A%3A%3B0%3A178%3A%3A%3B0%3A41%3A%3A%3B0%3A130%3A%3A%3B0%3A133%3A%3A%3B0%3A247%3A%3A%3B0%3A3%3A%3A%3B0%3A240%3A%3A%3B0%3A8%3A%3A%3B0%3A118%3A%3A%3B0%3A89%3A%3A%3B0%3A166%3A%3A%3B0%3A124%3A%3A%3B0%3A226%3A%3A%3B0%3A209%3A%3A%3B0%3A63%3A%3A%3B0%3A61%3A%3A%3B0%3A167%3A%3A%3B0%3A20%3A%3A%3B0%3A164%3A%3A%3B0%3A19%3A%3A%3B0%3A88%3A%3A%3B0%3A249%3A%3A%3B0%3A39%3A%3A%3B0%3A174%3A%3A%3B0%3A31%3A%3A%3B0%3A54%3A%3A%3B0%3A51%3A%3A%3B0%3A181%3A%3A%3B0%3A2%3A%3A%3B0%3A87%3A%3A%3B0%3A143%3A%3A%3B0%3A7%3A%3A%3B0%3A189%3A%3A%3B0%3A237%3A%3A%3B0%3A156%3A%3A%3B0%3A47%3A%3A%3B0%3A234%3A%3A%3B0%3A251%3A%3A%3B0%3A262%3A%3A%3B0%3A134%3A%3A%3B0%3A218%3A%3A%3B0%3A109%3A%3A%3B0%3A123%3A%3A%3B0%3A201%3A%3A%3B0%3A254%3A%3A%3B0%3A25%3A%3A%3B0%3A69%3A%3A%3B0%3A140%3A%3A%3B0%3A119%3A%3A%3B0%3A16%3A%3A%3B0%3A207%3A%3A%3B0%3A232%3A%3A%3B0%3A223%3A%3A%3B0%3A256%3A%3A%3B0%3A163%3A%3A%3B0%3A97%3A%3A%3B0%3A173%3A%3A%3B0%3A191%3A%3A%3B0%3A186%3A%3A%3B0%3A192%3A%3A%3B0%3A43%3A%3A%3B0%3A243%3A%3A%3B0%3A199%3A%3A%3B0%3A159%3A%3A%3B0%3A184%3A%3A%3B0%3A18%3A%3A%3B0%3A35%3A%3A%3B0%3A59%3A%3A%3B0%3A64%3A%3A%3B0%3A216%3A%3A%3B0%3A86%3A%3A%3B0%3A120%3A%3A%3B0%3A205%3A%3A%3B0%3A149%3A%3A%3B0%3A127%3A%3A%3B0%3A115%3A%3A%3B0%3A17%3A%3A%3B0%3A110%3A%3A%3B0%3A53%3A%3A%3B0%3A238%3A%3A%3B0%3A239%3A%3A%3B0%3A217%3A%3A%3B0%3A206%3A%3A%3B0%3A155%3A%3A%3B0%3A28%3A%3A%3B0%3A222%3A%3A%3B0%3A220%3A%3A%3B0%3A250%3A%3A%3B0%3A252%3A%3A%3B0%3A44%3A%3A%3B0%3A196%3A%3A%3B0%3A227%3A%3A%3B0%3A221%3A%3A%3B0%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=56+57+0+43+32+1+2+3+4+55+60+7+6+5+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+14+27+53+54+58+16+30+13+17+18+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+22+35+24+38+25&selector%5Bextra_filters%5D=3&narrow="
    
    html=tools.getUrlList(url,userId)    
    re =ps1.parseHtml(html)
    # json, nextPageHref, previousHref =ps1.parseHtml(html)
    # html=tools.getLogin()    
    json_str = json.dumps(re)
    return json_str
    # return html