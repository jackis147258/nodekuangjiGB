
from bs4 import BeautifulSoup
from urllib.parse import urlparse ,unquote,quote,parse_qs,urlencode
import ssl
import pandas as pd
import csv
import requests
from app1 import  models
import json

def get_one_page(i):
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        
        cookie=models.dengLuInfo.objects.get(uid=1).cookie

        url = "https://zh.surebet.com/surebets?utf8=%E2%9C%93&filter%5Bselected%5D%5B%5D=&filter%5Bselected%5D%5B%5D=33714663&filter%5Bsave%5D=&filter%5Bcurrent_id%5D=33714663&selector%5Border%5D=profit&selector%5Boutcomes%5D%5B%5D=&selector%5Boutcomes%5D%5B%5D=2&selector%5Boutcomes%5D%5B%5D=3&selector%5Bmin_profit%5D=0.0&selector%5Bmax_profit%5D=&selector%5Bmin_roi%5D=&selector%5Bmax_roi%5D=&selector%5Bsettled_in%5D=86400&selector%5Bbookies_settings%5D=0%3A67%3A%3A%3B4%3A72%3A%3A%3B0%3A66%3A%3A%3B0%3A76%3A%3A%3B0%3A182%3A%3A%3B0%3A74%3A%3A%3B0%3A37%3A%3A%3B4%3A148%3A%3A%3B0%3A211%3A%3A%3B0%3A114%3A%3A%3B0%3A260%3A%3A%3B0%3A132%3A%3A%3B0%3A42%3A%3A%3B0%3A40%3A%3A%3B0%3A225%3A%3A%3B0%3A126%3A%3A%3B0%3A21%3A%3A%3B0%3A263%3A%3A%3B0%3A23%3A%3A%3B0%3A246%3A%3A%3B0%3A26%3A%3A%3B0%3A139%3A%3A%3B0%3A36%3A%3A%3B0%3A150%3A%3A%3B0%3A202%3A%3A%3B0%3A151%3A%3A%3B0%3A204%3A%3A%3B0%3A125%3A%3A%3B0%3A200%3A%3A%3B0%3A203%3A%3A%3B0%3A%3A%3A%3B0%3A32%3A%3A%3B0%3A1%3A%3A%3B0%3A65%3A%3A%3B0%3A161%3A%3A%3B0%3A29%3A%3A%3B0%3A10%3A%3A%3B0%3A45%3A%3A%3B0%3A228%3A%3A%3B0%3A34%3A%3A%3B0%3A77%3A%3A%3B0%3A58%3A%3A%3B0%3A253%3A%3A%3B0%3A165%3A%3A%3B0%3A95%3A%3A%3B0%3A180%3A%3A%3B0%3A208%3A%3A%3B0%3A48%3A%3A%3B0%3A14%3A%3A%3B0%3A197%3A%3A%3B0%3A11%3A%3A%3B0%3A188%3A%3A%3B0%3A38%3A%3A%3B0%3A147%3A%3A%3B0%3A52%3A%3A%3B0%3A198%3A%3A%3B0%3A55%3A%3A%3B0%3A187%3A%3A%3B0%3A33%3A%3A%3B0%3A13%3A%3A%3B0%3A176%3A%3A%3B0%3A248%3A%3A%3B0%3A236%3A%3A%3B0%3A215%3A%3A%3B0%3A49%3A%3A%3B0%3A62%3A%3A%3B0%3A75%3A%3A%3B0%3A12%3A%3A%3B0%3A193%3A%3A%3B0%3A90%3A%3A%3B0%3A46%3A%3A%3B0%3A229%3A%3A%3B0%3A210%3A%3A%3B0%3A146%3A%3A%3B0%3A117%3A%3A%3B0%3A135%3A%3A%3B0%3A24%3A%3A%3B0%3A73%3A%3A%3B0%3A258%3A%3A%3B0%3A261%3A%3A%3B0%3A154%3A%3A%3B0%3A129%3A%3A%3B0%3A56%3A%3A%3B0%3A230%3A%3A%3B0%3A22%3A%3A%3B0%3A145%3A%3A%3B0%3A136%3A%3A%3B0%3A30%3A%3A%3B0%3A257%3A%3A%3B0%3A5%3A%3A%3B0%3A6%3A%3A%3B0%3A214%3A%3A%3B0%3A245%3A%3A%3B0%3A235%3A%3A%3B0%3A175%3A%3A%3B0%3A224%3A%3A%3B0%3A190%3A%3A%3B0%3A4%3A%3A%3B0%3A183%3A%3A%3B0%3A242%3A%3A%3B0%3A213%3A%3A%3B0%3A244%3A%3A%3B0%3A15%3A%3A%3B0%3A212%3A%3A%3B0%3A219%3A%3A%3B0%3A128%3A%3A%3B0%3A233%3A%3A%3B0%3A50%3A%3A%3B0%3A9%3A%3A%3B0%3A179%3A%3A%3B0%3A259%3A%3A%3B0%3A178%3A%3A%3B0%3A41%3A%3A%3B0%3A130%3A%3A%3B0%3A133%3A%3A%3B0%3A247%3A%3A%3B0%3A3%3A%3A%3B0%3A240%3A%3A%3B0%3A8%3A%3A%3B0%3A118%3A%3A%3B0%3A89%3A%3A%3B0%3A166%3A%3A%3B0%3A124%3A%3A%3B0%3A226%3A%3A%3B0%3A209%3A%3A%3B0%3A63%3A%3A%3B0%3A61%3A%3A%3B0%3A167%3A%3A%3B0%3A20%3A%3A%3B0%3A164%3A%3A%3B0%3A19%3A%3A%3B0%3A88%3A%3A%3B0%3A249%3A%3A%3B0%3A39%3A%3A%3B0%3A174%3A%3A%3B0%3A31%3A%3A%3B0%3A54%3A%3A%3B0%3A51%3A%3A%3B0%3A181%3A%3A%3B0%3A2%3A%3A%3B0%3A87%3A%3A%3B0%3A143%3A%3A%3B0%3A7%3A%3A%3B0%3A189%3A%3A%3B0%3A237%3A%3A%3B0%3A156%3A%3A%3B0%3A47%3A%3A%3B0%3A234%3A%3A%3B0%3A251%3A%3A%3B0%3A262%3A%3A%3B0%3A134%3A%3A%3B0%3A218%3A%3A%3B0%3A109%3A%3A%3B0%3A123%3A%3A%3B0%3A201%3A%3A%3B0%3A254%3A%3A%3B0%3A25%3A%3A%3B0%3A69%3A%3A%3B0%3A140%3A%3A%3B0%3A119%3A%3A%3B0%3A16%3A%3A%3B0%3A207%3A%3A%3B0%3A232%3A%3A%3B0%3A223%3A%3A%3B0%3A256%3A%3A%3B0%3A163%3A%3A%3B0%3A97%3A%3A%3B0%3A173%3A%3A%3B0%3A191%3A%3A%3B0%3A186%3A%3A%3B0%3A192%3A%3A%3B0%3A43%3A%3A%3B0%3A243%3A%3A%3B0%3A199%3A%3A%3B0%3A159%3A%3A%3B0%3A184%3A%3A%3B0%3A18%3A%3A%3B0%3A35%3A%3A%3B0%3A59%3A%3A%3B0%3A64%3A%3A%3B0%3A216%3A%3A%3B0%3A86%3A%3A%3B0%3A120%3A%3A%3B0%3A205%3A%3A%3B0%3A149%3A%3A%3B0%3A127%3A%3A%3B0%3A115%3A%3A%3B0%3A17%3A%3A%3B0%3A110%3A%3A%3B0%3A53%3A%3A%3B0%3A238%3A%3A%3B0%3A239%3A%3A%3B0%3A217%3A%3A%3B0%3A206%3A%3A%3B0%3A155%3A%3A%3B0%3A28%3A%3A%3B0%3A222%3A%3A%3B0%3A220%3A%3A%3B0%3A250%3A%3A%3B0%3A252%3A%3A%3B0%3A44%3A%3A%3B0%3A196%3A%3A%3B0%3A227%3A%3A%3B0%3A221%3A%3A%3B0%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=56+57+0+43+32+1+2+3+4+55+60+7+6+5+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+14+27+53+54+58+16+30+13+17+18+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+22+35+24+38+25&selector%5Bextra_filters%5D=3&narrow="
    # url = "https://zh.surebet.com/surebets?utf8=%E2%9C%93&selector%5Border%5D=profit&selector%5Boutcomes%5D%5B%5D=&selector%5Boutcomes%5D%5B%5D=2&selector%5Boutcomes%5D%5B%5D=3&selector%5Bmin_profit%5D=&selector%5Bmax_profit%5D=&selector%5Bmin_roi%5D=&selector%5Bmax_roi%5D=&selector%5Bsettled_in%5D=0&selector%5Bbookies_settings%5D=4%3A67%3A%3A%3B4%3A72%3A%3A%3B0%3A66%3A%3A%3B4%3A76%3A%3A%3B0%3A182%3A%3A%3B4%3A74%3A%3A%3B4%3A37%3A%3A%3B4%3A148%3A%3A%3B4%3A211%3A%3A%3B4%3A114%3A%3A%3B4%3A260%3A%3A%3B4%3A132%3A%3A%3B4%3A42%3A%3A%3B4%3A40%3A%3A%3B4%3A225%3A%3A%3B4%3A126%3A%3A%3B4%3A21%3A%3A%3B4%3A263%3A%3A%3B4%3A23%3A%3A%3B4%3A246%3A%3A%3B4%3A26%3A%3A%3B4%3A139%3A%3A%3B4%3A36%3A%3A%3B4%3A150%3A%3A%3B4%3A202%3A%3A%3B4%3A151%3A%3A%3B4%3A204%3A%3A%3B4%3A125%3A%3A%3B4%3A200%3A%3A%3B4%3A203%3A%3A%3B4%3A%3A%3A%3B4%3A32%3A%3A%3B4%3A1%3A%3A%3B4%3A65%3A%3A%3B4%3A161%3A%3A%3B4%3A29%3A%3A%3B4%3A10%3A%3A%3B4%3A45%3A%3A%3B4%3A228%3A%3A%3B4%3A34%3A%3A%3B4%3A77%3A%3A%3B4%3A58%3A%3A%3B4%3A253%3A%3A%3B4%3A165%3A%3A%3B4%3A95%3A%3A%3B4%3A180%3A%3A%3B4%3A208%3A%3A%3B4%3A48%3A%3A%3B4%3A14%3A%3A%3B4%3A197%3A%3A%3B4%3A11%3A%3A%3B4%3A188%3A%3A%3B4%3A38%3A%3A%3B4%3A147%3A%3A%3B4%3A52%3A%3A%3B4%3A198%3A%3A%3B4%3A55%3A%3A%3B4%3A187%3A%3A%3B4%3A33%3A%3A%3B4%3A13%3A%3A%3B4%3A176%3A%3A%3B4%3A248%3A%3A%3B4%3A236%3A%3A%3B4%3A215%3A%3A%3B4%3A49%3A%3A%3B4%3A62%3A%3A%3B4%3A75%3A%3A%3B4%3A12%3A%3A%3B4%3A193%3A%3A%3B4%3A90%3A%3A%3B4%3A46%3A%3A%3B4%3A229%3A%3A%3B4%3A210%3A%3A%3B4%3A146%3A%3A%3B4%3A117%3A%3A%3B4%3A135%3A%3A%3B4%3A24%3A%3A%3B4%3A88%3A%3A%3B4%3A73%3A%3A%3B4%3A258%3A%3A%3B4%3A261%3A%3A%3B4%3A154%3A%3A%3B4%3A129%3A%3A%3B4%3A56%3A%3A%3B4%3A230%3A%3A%3B4%3A22%3A%3A%3B4%3A145%3A%3A%3B4%3A136%3A%3A%3B4%3A30%3A%3A%3B4%3A257%3A%3A%3B4%3A5%3A%3A%3B4%3A6%3A%3A%3B4%3A214%3A%3A%3B4%3A245%3A%3A%3B4%3A235%3A%3A%3B4%3A175%3A%3A%3B4%3A224%3A%3A%3B4%3A190%3A%3A%3B4%3A4%3A%3A%3B4%3A183%3A%3A%3B4%3A242%3A%3A%3B4%3A213%3A%3A%3B4%3A244%3A%3A%3B4%3A15%3A%3A%3B4%3A212%3A%3A%3B4%3A219%3A%3A%3B4%3A128%3A%3A%3B4%3A233%3A%3A%3B4%3A50%3A%3A%3B4%3A9%3A%3A%3B4%3A179%3A%3A%3B4%3A259%3A%3A%3B4%3A178%3A%3A%3B4%3A41%3A%3A%3B4%3A130%3A%3A%3B4%3A133%3A%3A%3B4%3A247%3A%3A%3B4%3A3%3A%3A%3B4%3A240%3A%3A%3B4%3A8%3A%3A%3B4%3A118%3A%3A%3B4%3A89%3A%3A%3B4%3A166%3A%3A%3B4%3A124%3A%3A%3B4%3A226%3A%3A%3B4%3A209%3A%3A%3B4%3A63%3A%3A%3B4%3A61%3A%3A%3B4%3A167%3A%3A%3B4%3A20%3A%3A%3B4%3A164%3A%3A%3B4%3A19%3A%3A%3B4%3A249%3A%3A%3B4%3A39%3A%3A%3B4%3A174%3A%3A%3B4%3A31%3A%3A%3B4%3A54%3A%3A%3B4%3A51%3A%3A%3B4%3A181%3A%3A%3B4%3A2%3A%3A%3B4%3A87%3A%3A%3B4%3A143%3A%3A%3B4%3A7%3A%3A%3B4%3A189%3A%3A%3B4%3A237%3A%3A%3B4%3A156%3A%3A%3B4%3A47%3A%3A%3B4%3A234%3A%3A%3B4%3A251%3A%3A%3B4%3A262%3A%3A%3B4%3A134%3A%3A%3B4%3A218%3A%3A%3B4%3A109%3A%3A%3B4%3A123%3A%3A%3B4%3A201%3A%3A%3B4%3A254%3A%3A%3B4%3A25%3A%3A%3B4%3A69%3A%3A%3B4%3A140%3A%3A%3B4%3A119%3A%3A%3B4%3A16%3A%3A%3B4%3A207%3A%3A%3B4%3A232%3A%3A%3B4%3A223%3A%3A%3B4%3A256%3A%3A%3B4%3A163%3A%3A%3B4%3A97%3A%3A%3B4%3A173%3A%3A%3B4%3A191%3A%3A%3B4%3A186%3A%3A%3B4%3A192%3A%3A%3B4%3A43%3A%3A%3B4%3A243%3A%3A%3B4%3A199%3A%3A%3B4%3A159%3A%3A%3B4%3A184%3A%3A%3B4%3A18%3A%3A%3B4%3A35%3A%3A%3B4%3A59%3A%3A%3B4%3A64%3A%3A%3B4%3A216%3A%3A%3B4%3A86%3A%3A%3B4%3A120%3A%3A%3B4%3A205%3A%3A%3B4%3A149%3A%3A%3B4%3A127%3A%3A%3B4%3A115%3A%3A%3B4%3A17%3A%3A%3B4%3A110%3A%3A%3B4%3A53%3A%3A%3B4%3A238%3A%3A%3B4%3A239%3A%3A%3B4%3A217%3A%3A%3B4%3A206%3A%3A%3B4%3A155%3A%3A%3B4%3A28%3A%3A%3B4%3A222%3A%3A%3B4%3A220%3A%3A%3B4%3A250%3A%3A%3B4%3A252%3A%3A%3B4%3A44%3A%3A%3B4%3A196%3A%3A%3B4%3A227%3A%3A%3B4%3A221%3A%3A%3B4%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=56+57+0+43+32+3+55+60+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+53+54+58+30+13+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+35+38&selector%5Bextra_filters%5D=&narrow="

        payload={}
        headers = {
            # 'Cookie': '_sp5=azErMXR1KzJ0bUxPVzg5bXlMWmh5R3RDcFpRcFBWTDVvZ0haL1JZYW5Ham5OekczYmJJank3RVVpOExDSnBEZ3c2aERDTmhJSFBjd05vd28yZnRNZ1p1bDhFT3ZXSFVRQkJnTTFFRXUreUNtTFhSK2g2eDRvK2JyanhuaDZ3TEYrS08xQXlFTW9sMWc2MnM1VE9PWGtDNU9FdUppZDVmUkV6UkRaSkF5aVNaZTQ5V1FnNFdOMEc4WDJHS0hwdDhSLS00eVA4bTN1RHlWVHVHWGtva21pRmlBPT0%3D--fe9258d26d8dff2bd8d1594a0d2434f66851f6fc; ab=732; order_surebets_index=profit; ref=b0lTN1B5MHVVd0wxMG9tSFBDZFhoOWljUHpQK3hwTVBoSEFOQTNiWUptaHRqeURwS2djS3crbkw2cHdvK244SGNkZ040amFTdU1QdkJKVnRrQVZRUHh6REVmSW1pSUs0YktuekduNmJhTEo1eTlEa3QwYWM0NkRoeEtwWFNvUm4tLXBxQlJ2V0p0Q29RazYyWGliQ1FZYVE9PQ%3D%3D--97b7ab2017f313373c20fab7c971e26608c1785d; sel%3Asurebets=72b49d023af1686c0475fa4545c93009; uu=dae08a21-1c38-4d70-b955-fd5e639368c2'
            'Cookie': cookie
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        a=response.text
        return a;

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        paras = {
            'reportTime': '2019-12-31',   
		#可以改报告日期，比如2018-6-30获得的就是该季度的信息
		'pageNum': i   #页码
		}
        # url = 'http://s.askci.com/stock/a/?' + urlencode(paras)
        url="'https://zh.surebet.com/surebets?utf8=✓&filter[selected][]=&filter[selected][]=33714663&filter[save]=&filter[current_id]=33714663&selector[order]=profit&selector[outcomes][]=&selector[outcomes][]=2&selector[outcomes][]=3&selector[min_profit]=0.0&selector[max_profit]=&selector[min_roi]=&selector[max_roi]=&selector[settled_in]=86400&selector[bookies_settings]=0:67::;4:72::;0:66::;0:76::;0:182::;0:74::;0:37::;4:148::;0:211::;0:114::;0:260::;0:132::;0:42::;0:40::;0:225::;0:126::;0:21::;0:263::;0:23::;0:246::;0:26::;0:139::;0:36::;0:150::;0:202::;0:151::;0:204::;0:125::;0:200::;0:203::;0:::;0:32::;0:1::;0:65::;0:161::;0:29::;0:10::;0:45::;0:228::;0:34::;0:77::;0:58::;0:253::;0:165::;0:95::;0:180::;0:208::;0:48::;0:14::;0:197::;0:11::;0:188::;0:38::;0:147::;0:52::;0:198::;0:55::;0:187::;0:33::;0:13::;0:176::;0:248::;0:236::;0:215::;0:49::;0:62::;0:75::;0:12::;0:193::;0:90::;0:46::;0:229::;0:210::;0:146::;0:117::;0:135::;0:24::;0:73::;0:258::;0:261::;0:154::;0:129::;0:56::;0:230::;0:22::;0:145::;0:136::;0:30::;0:257::;0:5::;0:6::;0:214::;0:245::;0:235::;0:175::;0:224::;0:190::;0:4::;0:183::;0:242::;0:213::;0:244::;0:15::;0:212::;0:219::;0:128::;0:233::;0:50::;0:9::;0:179::;0:259::;0:178::;0:41::;0:130::;0:133::;0:247::;0:3::;0:240::;0:8::;0:118::;0:89::;0:166::;0:124::;0:226::;0:209::;0:63::;0:61::;0:167::;0:20::;0:164::;0:19::;0:88::;0:249::;0:39::;0:174::;0:31::;0:54::;0:51::;0:181::;0:2::;0:87::;0:143::;0:7::;0:189::;0:237::;0:156::;0:47::;0:234::;0:251::;0:262::;0:134::;0:218::;0:109::;0:123::;0:201::;0:254::;0:25::;0:69::;0:140::;0:119::;0:16::;0:207::;0:232::;0:223::;0:256::;0:163::;0:97::;0:173::;0:191::;0:186::;0:192::;0:43::;0:243::;0:199::;0:159::;0:184::;0:18::;0:35::;0:59::;0:64::;0:216::;0:86::;0:120::;0:205::;0:149::;0:127::;0:115::;0:17::;0:110::;0:53::;0:238::;0:239::;0:217::;0:206::;0:155::;0:28::;0:222::;0:220::;0:250::;0:252::;0:44::;0:196::;0:227::;0:221::;0:27::&selector[exclude_sports_ids_str]=56+57+0+43+32+1+2+3+4+55+60+7+6+5+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+14+27+53+54+58+16+30+13+17+18+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+22+35+24+38+25&selector[extra_filters]=3&narrow="

        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except:
        print('爬取失败')

# beatutiful soup解析然后提取表格
def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    content = soup.select('#surebets-table')[0] #[0]将返回的list改为bs4类型
    print(content)
    tbl = pd.read_html(content.prettify(),header = 0)[0]
    # prettify()优化代码,[0]从pd.read_html返回的list中提取出DataFrame
	
    tbl.rename(columns = {'序号':'serial_number', '股票代码':'stock_code', '股票简称':'stock_abbre', '公司名称':'company_name', '省份':'province', '城市':'city', '主营业务收入(201712)':'main_bussiness_income', '净利润(201712)':'net_profit', '员工人数':'employees', '上市日期':'listing_date', '招股书':'zhaogushu', '公司财报':'financial_report', '行业分类':'industry_classification', '产品类型':'industry_type', '主营业务':'main_business'},inplace = True)
	
    # print(tbl)
	# return tbl
	# rename将表格15列的中文名改为英文名，便于存储到mysql及后期进行数据分析
	# tbl = pd.DataFrame(tbl,dtype = 'object') #dtype可统一修改列格式为文本
    tbl.to_csv(r'd:\dk\ticai\3.csv', mode='a',encoding='utf_8_sig', header=1, index=0)

def parseHtml(html):
    soup = BeautifulSoup(html,'lxml')
    msg=""
    jsonTable=''
    nextPageHref=''
    previousHref=''
    if soup.select('#surebets-table')!=[]:
        content = soup.select('#surebets-table')[0] #将返回的list改为bs4类型
    
    
# tables = soup.findAll('table')
# tab = tables[0]
        listTable=[]
        # tableTr={'profitText':'','ageText':'','td':listTd}
        # tabletd={'booker':'','bookerspanText':'','time':'','event':'','coeff':'','value':'' }
        
        for tbody in content.findAll('tbody'):
            listTd=[]
            tableTr={'profitText':'','ageText':'','td': listTd}
           
            for tr in tbody.findAll('tr'):
                tabletd={'booker':'','bookerspanText':'','time':'','eventA':'','eventSpan':'','coeff':'','value':'' }
                for td in tr.findAll('td'):
                    # profitbox = td.get('.profit-box')
                    if td["class"][0]=='profit-box':
                        profitText = td.find("span", class_="profit").getText()
                        ageText = td.find("span", class_="age").getText()
                        tableTr['profitText']=profitText
                        tableTr['ageText']=ageText
                    
                    if td["class"][0]=='booker':
                        bookerText = td.find("a").getText()
                        bookerspanText = td.find("span", class_="minor").getText()
                        tabletd['booker']=bookerText
                        tabletd['bookerspanText']=bookerspanText
                    
                    if td["class"][0]=='time':
                        timeText = td.getText()
                        tabletd['time']=timeText
                      
                    if td["class"][0]=='event':
                        # eventText = td.getText()
                        eventText = td.find("a").getText()
                        eventspanText = td.find("span", class_="minor").getText()
                        tabletd['eventA']=eventText
                        tabletd['eventSpan']=eventspanText
                       
                    if td["class"][0]=='coeff':
                        coeffText = td.getText()
                        tabletd['coeff']=coeffText
                        
                    if td["class"][0]=='value':
                        valueText = td.find("a").getText()
                        tabletd['value']=valueText
                listTd.append(tabletd)   
            tableTr['td']=listTd   
            listTable.append(tableTr)      
                    # if td["class"][0]=='generative':
                    #     bookerText = td.find("a", rel_="noopener").getText()
                    #     bookerText = td.find("span", class_="minor").getText()
                        

 

        # 获得 上一页 下一页    
        nextPageHref=""
        previousHref=""
        if soup.select('.next_page')!=[]:    
            nextPage = soup.select('.next_page')[0] #将返回的list改为bs4类型            
            nextPageHref = nextPage.get('href')
        
        if soup.select('.previous_page')!=[]:    
            previousPage = soup.select('.previous_page')[0] #将返回的list改为bs4类型            
            previousHref = previousPage.get('href')
        
      
        
        # tbl = pd.read_html(content.prettify(),header = 0)[0]       
        # t_dict1= tbl.to_dict(orient='records') # 横排列
        # jsonTable = json.dumps(t_dict1)
        

 
        # jsonTable = json.dumps(listTable)
        
    return listTable,nextPageHref,previousHref
 
    # return msg

# listUrl=get.getUrlList(url)

# html=get_one_page(1)

# parse_one_page(html)


