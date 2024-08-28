import requests
import ssl


def getUrlList(url):
  ssl._create_default_https_context = ssl._create_unverified_context

  # url = "https://zh.surebet.com/surebets?utf8=%E2%9C%93&filter%5Bselected%5D%5B%5D=&filter%5Bselected%5D%5B%5D=33714663&filter%5Bsave%5D=&filter%5Bcurrent_id%5D=33714663&selector%5Border%5D=profit&selector%5Boutcomes%5D%5B%5D=&selector%5Boutcomes%5D%5B%5D=2&selector%5Boutcomes%5D%5B%5D=3&selector%5Bmin_profit%5D=0.0&selector%5Bmax_profit%5D=&selector%5Bmin_roi%5D=&selector%5Bmax_roi%5D=&selector%5Bsettled_in%5D=86400&selector%5Bbookies_settings%5D=0%3A67%3A%3A%3B4%3A72%3A%3A%3B0%3A66%3A%3A%3B0%3A76%3A%3A%3B0%3A182%3A%3A%3B0%3A74%3A%3A%3B0%3A37%3A%3A%3B4%3A148%3A%3A%3B0%3A211%3A%3A%3B0%3A114%3A%3A%3B0%3A260%3A%3A%3B0%3A132%3A%3A%3B0%3A42%3A%3A%3B0%3A40%3A%3A%3B0%3A225%3A%3A%3B0%3A126%3A%3A%3B0%3A21%3A%3A%3B0%3A263%3A%3A%3B0%3A23%3A%3A%3B0%3A246%3A%3A%3B0%3A26%3A%3A%3B0%3A139%3A%3A%3B0%3A36%3A%3A%3B0%3A150%3A%3A%3B0%3A202%3A%3A%3B0%3A151%3A%3A%3B0%3A204%3A%3A%3B0%3A125%3A%3A%3B0%3A200%3A%3A%3B0%3A203%3A%3A%3B0%3A%3A%3A%3B0%3A32%3A%3A%3B0%3A1%3A%3A%3B0%3A65%3A%3A%3B0%3A161%3A%3A%3B0%3A29%3A%3A%3B0%3A10%3A%3A%3B0%3A45%3A%3A%3B0%3A228%3A%3A%3B0%3A34%3A%3A%3B0%3A77%3A%3A%3B0%3A58%3A%3A%3B0%3A253%3A%3A%3B0%3A165%3A%3A%3B0%3A95%3A%3A%3B0%3A180%3A%3A%3B0%3A208%3A%3A%3B0%3A48%3A%3A%3B0%3A14%3A%3A%3B0%3A197%3A%3A%3B0%3A11%3A%3A%3B0%3A188%3A%3A%3B0%3A38%3A%3A%3B0%3A147%3A%3A%3B0%3A52%3A%3A%3B0%3A198%3A%3A%3B0%3A55%3A%3A%3B0%3A187%3A%3A%3B0%3A33%3A%3A%3B0%3A13%3A%3A%3B0%3A176%3A%3A%3B0%3A248%3A%3A%3B0%3A236%3A%3A%3B0%3A215%3A%3A%3B0%3A49%3A%3A%3B0%3A62%3A%3A%3B0%3A75%3A%3A%3B0%3A12%3A%3A%3B0%3A193%3A%3A%3B0%3A90%3A%3A%3B0%3A46%3A%3A%3B0%3A229%3A%3A%3B0%3A210%3A%3A%3B0%3A146%3A%3A%3B0%3A117%3A%3A%3B0%3A135%3A%3A%3B0%3A24%3A%3A%3B0%3A73%3A%3A%3B0%3A258%3A%3A%3B0%3A261%3A%3A%3B0%3A154%3A%3A%3B0%3A129%3A%3A%3B0%3A56%3A%3A%3B0%3A230%3A%3A%3B0%3A22%3A%3A%3B0%3A145%3A%3A%3B0%3A136%3A%3A%3B0%3A30%3A%3A%3B0%3A257%3A%3A%3B0%3A5%3A%3A%3B0%3A6%3A%3A%3B0%3A214%3A%3A%3B0%3A245%3A%3A%3B0%3A235%3A%3A%3B0%3A175%3A%3A%3B0%3A224%3A%3A%3B0%3A190%3A%3A%3B0%3A4%3A%3A%3B0%3A183%3A%3A%3B0%3A242%3A%3A%3B0%3A213%3A%3A%3B0%3A244%3A%3A%3B0%3A15%3A%3A%3B0%3A212%3A%3A%3B0%3A219%3A%3A%3B0%3A128%3A%3A%3B0%3A233%3A%3A%3B0%3A50%3A%3A%3B0%3A9%3A%3A%3B0%3A179%3A%3A%3B0%3A259%3A%3A%3B0%3A178%3A%3A%3B0%3A41%3A%3A%3B0%3A130%3A%3A%3B0%3A133%3A%3A%3B0%3A247%3A%3A%3B0%3A3%3A%3A%3B0%3A240%3A%3A%3B0%3A8%3A%3A%3B0%3A118%3A%3A%3B0%3A89%3A%3A%3B0%3A166%3A%3A%3B0%3A124%3A%3A%3B0%3A226%3A%3A%3B0%3A209%3A%3A%3B0%3A63%3A%3A%3B0%3A61%3A%3A%3B0%3A167%3A%3A%3B0%3A20%3A%3A%3B0%3A164%3A%3A%3B0%3A19%3A%3A%3B0%3A88%3A%3A%3B0%3A249%3A%3A%3B0%3A39%3A%3A%3B0%3A174%3A%3A%3B0%3A31%3A%3A%3B0%3A54%3A%3A%3B0%3A51%3A%3A%3B0%3A181%3A%3A%3B0%3A2%3A%3A%3B0%3A87%3A%3A%3B0%3A143%3A%3A%3B0%3A7%3A%3A%3B0%3A189%3A%3A%3B0%3A237%3A%3A%3B0%3A156%3A%3A%3B0%3A47%3A%3A%3B0%3A234%3A%3A%3B0%3A251%3A%3A%3B0%3A262%3A%3A%3B0%3A134%3A%3A%3B0%3A218%3A%3A%3B0%3A109%3A%3A%3B0%3A123%3A%3A%3B0%3A201%3A%3A%3B0%3A254%3A%3A%3B0%3A25%3A%3A%3B0%3A69%3A%3A%3B0%3A140%3A%3A%3B0%3A119%3A%3A%3B0%3A16%3A%3A%3B0%3A207%3A%3A%3B0%3A232%3A%3A%3B0%3A223%3A%3A%3B0%3A256%3A%3A%3B0%3A163%3A%3A%3B0%3A97%3A%3A%3B0%3A173%3A%3A%3B0%3A191%3A%3A%3B0%3A186%3A%3A%3B0%3A192%3A%3A%3B0%3A43%3A%3A%3B0%3A243%3A%3A%3B0%3A199%3A%3A%3B0%3A159%3A%3A%3B0%3A184%3A%3A%3B0%3A18%3A%3A%3B0%3A35%3A%3A%3B0%3A59%3A%3A%3B0%3A64%3A%3A%3B0%3A216%3A%3A%3B0%3A86%3A%3A%3B0%3A120%3A%3A%3B0%3A205%3A%3A%3B0%3A149%3A%3A%3B0%3A127%3A%3A%3B0%3A115%3A%3A%3B0%3A17%3A%3A%3B0%3A110%3A%3A%3B0%3A53%3A%3A%3B0%3A238%3A%3A%3B0%3A239%3A%3A%3B0%3A217%3A%3A%3B0%3A206%3A%3A%3B0%3A155%3A%3A%3B0%3A28%3A%3A%3B0%3A222%3A%3A%3B0%3A220%3A%3A%3B0%3A250%3A%3A%3B0%3A252%3A%3A%3B0%3A44%3A%3A%3B0%3A196%3A%3A%3B0%3A227%3A%3A%3B0%3A221%3A%3A%3B0%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=56+57+0+43+32+1+2+3+4+55+60+7+6+5+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+14+27+53+54+58+16+30+13+17+18+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+22+35+24+38+25&selector%5Bextra_filters%5D=3&narrow="
  # url = "https://zh.surebet.com/surebets?utf8=%E2%9C%93&selector%5Border%5D=profit&selector%5Boutcomes%5D%5B%5D=&selector%5Boutcomes%5D%5B%5D=2&selector%5Boutcomes%5D%5B%5D=3&selector%5Bmin_profit%5D=&selector%5Bmax_profit%5D=&selector%5Bmin_roi%5D=&selector%5Bmax_roi%5D=&selector%5Bsettled_in%5D=0&selector%5Bbookies_settings%5D=4%3A67%3A%3A%3B4%3A72%3A%3A%3B0%3A66%3A%3A%3B4%3A76%3A%3A%3B0%3A182%3A%3A%3B4%3A74%3A%3A%3B4%3A37%3A%3A%3B4%3A148%3A%3A%3B4%3A211%3A%3A%3B4%3A114%3A%3A%3B4%3A260%3A%3A%3B4%3A132%3A%3A%3B4%3A42%3A%3A%3B4%3A40%3A%3A%3B4%3A225%3A%3A%3B4%3A126%3A%3A%3B4%3A21%3A%3A%3B4%3A263%3A%3A%3B4%3A23%3A%3A%3B4%3A246%3A%3A%3B4%3A26%3A%3A%3B4%3A139%3A%3A%3B4%3A36%3A%3A%3B4%3A150%3A%3A%3B4%3A202%3A%3A%3B4%3A151%3A%3A%3B4%3A204%3A%3A%3B4%3A125%3A%3A%3B4%3A200%3A%3A%3B4%3A203%3A%3A%3B4%3A%3A%3A%3B4%3A32%3A%3A%3B4%3A1%3A%3A%3B4%3A65%3A%3A%3B4%3A161%3A%3A%3B4%3A29%3A%3A%3B4%3A10%3A%3A%3B4%3A45%3A%3A%3B4%3A228%3A%3A%3B4%3A34%3A%3A%3B4%3A77%3A%3A%3B4%3A58%3A%3A%3B4%3A253%3A%3A%3B4%3A165%3A%3A%3B4%3A95%3A%3A%3B4%3A180%3A%3A%3B4%3A208%3A%3A%3B4%3A48%3A%3A%3B4%3A14%3A%3A%3B4%3A197%3A%3A%3B4%3A11%3A%3A%3B4%3A188%3A%3A%3B4%3A38%3A%3A%3B4%3A147%3A%3A%3B4%3A52%3A%3A%3B4%3A198%3A%3A%3B4%3A55%3A%3A%3B4%3A187%3A%3A%3B4%3A33%3A%3A%3B4%3A13%3A%3A%3B4%3A176%3A%3A%3B4%3A248%3A%3A%3B4%3A236%3A%3A%3B4%3A215%3A%3A%3B4%3A49%3A%3A%3B4%3A62%3A%3A%3B4%3A75%3A%3A%3B4%3A12%3A%3A%3B4%3A193%3A%3A%3B4%3A90%3A%3A%3B4%3A46%3A%3A%3B4%3A229%3A%3A%3B4%3A210%3A%3A%3B4%3A146%3A%3A%3B4%3A117%3A%3A%3B4%3A135%3A%3A%3B4%3A24%3A%3A%3B4%3A88%3A%3A%3B4%3A73%3A%3A%3B4%3A258%3A%3A%3B4%3A261%3A%3A%3B4%3A154%3A%3A%3B4%3A129%3A%3A%3B4%3A56%3A%3A%3B4%3A230%3A%3A%3B4%3A22%3A%3A%3B4%3A145%3A%3A%3B4%3A136%3A%3A%3B4%3A30%3A%3A%3B4%3A257%3A%3A%3B4%3A5%3A%3A%3B4%3A6%3A%3A%3B4%3A214%3A%3A%3B4%3A245%3A%3A%3B4%3A235%3A%3A%3B4%3A175%3A%3A%3B4%3A224%3A%3A%3B4%3A190%3A%3A%3B4%3A4%3A%3A%3B4%3A183%3A%3A%3B4%3A242%3A%3A%3B4%3A213%3A%3A%3B4%3A244%3A%3A%3B4%3A15%3A%3A%3B4%3A212%3A%3A%3B4%3A219%3A%3A%3B4%3A128%3A%3A%3B4%3A233%3A%3A%3B4%3A50%3A%3A%3B4%3A9%3A%3A%3B4%3A179%3A%3A%3B4%3A259%3A%3A%3B4%3A178%3A%3A%3B4%3A41%3A%3A%3B4%3A130%3A%3A%3B4%3A133%3A%3A%3B4%3A247%3A%3A%3B4%3A3%3A%3A%3B4%3A240%3A%3A%3B4%3A8%3A%3A%3B4%3A118%3A%3A%3B4%3A89%3A%3A%3B4%3A166%3A%3A%3B4%3A124%3A%3A%3B4%3A226%3A%3A%3B4%3A209%3A%3A%3B4%3A63%3A%3A%3B4%3A61%3A%3A%3B4%3A167%3A%3A%3B4%3A20%3A%3A%3B4%3A164%3A%3A%3B4%3A19%3A%3A%3B4%3A249%3A%3A%3B4%3A39%3A%3A%3B4%3A174%3A%3A%3B4%3A31%3A%3A%3B4%3A54%3A%3A%3B4%3A51%3A%3A%3B4%3A181%3A%3A%3B4%3A2%3A%3A%3B4%3A87%3A%3A%3B4%3A143%3A%3A%3B4%3A7%3A%3A%3B4%3A189%3A%3A%3B4%3A237%3A%3A%3B4%3A156%3A%3A%3B4%3A47%3A%3A%3B4%3A234%3A%3A%3B4%3A251%3A%3A%3B4%3A262%3A%3A%3B4%3A134%3A%3A%3B4%3A218%3A%3A%3B4%3A109%3A%3A%3B4%3A123%3A%3A%3B4%3A201%3A%3A%3B4%3A254%3A%3A%3B4%3A25%3A%3A%3B4%3A69%3A%3A%3B4%3A140%3A%3A%3B4%3A119%3A%3A%3B4%3A16%3A%3A%3B4%3A207%3A%3A%3B4%3A232%3A%3A%3B4%3A223%3A%3A%3B4%3A256%3A%3A%3B4%3A163%3A%3A%3B4%3A97%3A%3A%3B4%3A173%3A%3A%3B4%3A191%3A%3A%3B4%3A186%3A%3A%3B4%3A192%3A%3A%3B4%3A43%3A%3A%3B4%3A243%3A%3A%3B4%3A199%3A%3A%3B4%3A159%3A%3A%3B4%3A184%3A%3A%3B4%3A18%3A%3A%3B4%3A35%3A%3A%3B4%3A59%3A%3A%3B4%3A64%3A%3A%3B4%3A216%3A%3A%3B4%3A86%3A%3A%3B4%3A120%3A%3A%3B4%3A205%3A%3A%3B4%3A149%3A%3A%3B4%3A127%3A%3A%3B4%3A115%3A%3A%3B4%3A17%3A%3A%3B4%3A110%3A%3A%3B4%3A53%3A%3A%3B4%3A238%3A%3A%3B4%3A239%3A%3A%3B4%3A217%3A%3A%3B4%3A206%3A%3A%3B4%3A155%3A%3A%3B4%3A28%3A%3A%3B4%3A222%3A%3A%3B4%3A220%3A%3A%3B4%3A250%3A%3A%3B4%3A252%3A%3A%3B4%3A44%3A%3A%3B4%3A196%3A%3A%3B4%3A227%3A%3A%3B4%3A221%3A%3A%3B4%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=56+57+0+43+32+3+55+60+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+53+54+58+30+13+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+35+38&selector%5Bextra_filters%5D=&narrow="

  payload={}
  headers = {
    'Cookie': '_sp5=azErMXR1KzJ0bUxPVzg5bXlMWmh5R3RDcFpRcFBWTDVvZ0haL1JZYW5Ham5OekczYmJJank3RVVpOExDSnBEZ3c2aERDTmhJSFBjd05vd28yZnRNZ1p1bDhFT3ZXSFVRQkJnTTFFRXUreUNtTFhSK2g2eDRvK2JyanhuaDZ3TEYrS08xQXlFTW9sMWc2MnM1VE9PWGtDNU9FdUppZDVmUkV6UkRaSkF5aVNaZTQ5V1FnNFdOMEc4WDJHS0hwdDhSLS00eVA4bTN1RHlWVHVHWGtva21pRmlBPT0%3D--fe9258d26d8dff2bd8d1594a0d2434f66851f6fc; ab=732; order_surebets_index=profit; ref=b0lTN1B5MHVVd0wxMG9tSFBDZFhoOWljUHpQK3hwTVBoSEFOQTNiWUptaHRqeURwS2djS3crbkw2cHdvK244SGNkZ040amFTdU1QdkJKVnRrQVZRUHh6REVmSW1pSUs0YktuekduNmJhTEo1eTlEa3QwYWM0NkRoeEtwWFNvUm4tLXBxQlJ2V0p0Q29RazYyWGliQ1FZYVE9PQ%3D%3D--97b7ab2017f313373c20fab7c971e26608c1785d; sel%3Asurebets=72b49d023af1686c0475fa4545c93009; uu=dae08a21-1c38-4d70-b955-fd5e639368c2'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  a=response.text
  return a;

def game():
  ssl._create_default_https_context = ssl._create_unverified_context

  # url = "https://zh.surebet.com/surebets?utf8=%E2%9C%93&filter%5Bselected%5D%5B%5D=&filter%5Bselected%5D%5B%5D=33714663&filter%5Bsave%5D=&filter%5Bcurrent_id%5D=33714663&selector%5Border%5D=profit&selector%5Boutcomes%5D%5B%5D=&selector%5Boutcomes%5D%5B%5D=2&selector%5Boutcomes%5D%5B%5D=3&selector%5Bmin_profit%5D=0.0&selector%5Bmax_profit%5D=&selector%5Bmin_roi%5D=&selector%5Bmax_roi%5D=&selector%5Bsettled_in%5D=86400&selector%5Bbookies_settings%5D=0%3A67%3A%3A%3B4%3A72%3A%3A%3B0%3A66%3A%3A%3B0%3A76%3A%3A%3B0%3A182%3A%3A%3B0%3A74%3A%3A%3B0%3A37%3A%3A%3B4%3A148%3A%3A%3B0%3A211%3A%3A%3B0%3A114%3A%3A%3B0%3A260%3A%3A%3B0%3A132%3A%3A%3B0%3A42%3A%3A%3B0%3A40%3A%3A%3B0%3A225%3A%3A%3B0%3A126%3A%3A%3B0%3A21%3A%3A%3B0%3A263%3A%3A%3B0%3A23%3A%3A%3B0%3A246%3A%3A%3B0%3A26%3A%3A%3B0%3A139%3A%3A%3B0%3A36%3A%3A%3B0%3A150%3A%3A%3B0%3A202%3A%3A%3B0%3A151%3A%3A%3B0%3A204%3A%3A%3B0%3A125%3A%3A%3B0%3A200%3A%3A%3B0%3A203%3A%3A%3B0%3A%3A%3A%3B0%3A32%3A%3A%3B0%3A1%3A%3A%3B0%3A65%3A%3A%3B0%3A161%3A%3A%3B0%3A29%3A%3A%3B0%3A10%3A%3A%3B0%3A45%3A%3A%3B0%3A228%3A%3A%3B0%3A34%3A%3A%3B0%3A77%3A%3A%3B0%3A58%3A%3A%3B0%3A253%3A%3A%3B0%3A165%3A%3A%3B0%3A95%3A%3A%3B0%3A180%3A%3A%3B0%3A208%3A%3A%3B0%3A48%3A%3A%3B0%3A14%3A%3A%3B0%3A197%3A%3A%3B0%3A11%3A%3A%3B0%3A188%3A%3A%3B0%3A38%3A%3A%3B0%3A147%3A%3A%3B0%3A52%3A%3A%3B0%3A198%3A%3A%3B0%3A55%3A%3A%3B0%3A187%3A%3A%3B0%3A33%3A%3A%3B0%3A13%3A%3A%3B0%3A176%3A%3A%3B0%3A248%3A%3A%3B0%3A236%3A%3A%3B0%3A215%3A%3A%3B0%3A49%3A%3A%3B0%3A62%3A%3A%3B0%3A75%3A%3A%3B0%3A12%3A%3A%3B0%3A193%3A%3A%3B0%3A90%3A%3A%3B0%3A46%3A%3A%3B0%3A229%3A%3A%3B0%3A210%3A%3A%3B0%3A146%3A%3A%3B0%3A117%3A%3A%3B0%3A135%3A%3A%3B0%3A24%3A%3A%3B0%3A73%3A%3A%3B0%3A258%3A%3A%3B0%3A261%3A%3A%3B0%3A154%3A%3A%3B0%3A129%3A%3A%3B0%3A56%3A%3A%3B0%3A230%3A%3A%3B0%3A22%3A%3A%3B0%3A145%3A%3A%3B0%3A136%3A%3A%3B0%3A30%3A%3A%3B0%3A257%3A%3A%3B0%3A5%3A%3A%3B0%3A6%3A%3A%3B0%3A214%3A%3A%3B0%3A245%3A%3A%3B0%3A235%3A%3A%3B0%3A175%3A%3A%3B0%3A224%3A%3A%3B0%3A190%3A%3A%3B0%3A4%3A%3A%3B0%3A183%3A%3A%3B0%3A242%3A%3A%3B0%3A213%3A%3A%3B0%3A244%3A%3A%3B0%3A15%3A%3A%3B0%3A212%3A%3A%3B0%3A219%3A%3A%3B0%3A128%3A%3A%3B0%3A233%3A%3A%3B0%3A50%3A%3A%3B0%3A9%3A%3A%3B0%3A179%3A%3A%3B0%3A259%3A%3A%3B0%3A178%3A%3A%3B0%3A41%3A%3A%3B0%3A130%3A%3A%3B0%3A133%3A%3A%3B0%3A247%3A%3A%3B0%3A3%3A%3A%3B0%3A240%3A%3A%3B0%3A8%3A%3A%3B0%3A118%3A%3A%3B0%3A89%3A%3A%3B0%3A166%3A%3A%3B0%3A124%3A%3A%3B0%3A226%3A%3A%3B0%3A209%3A%3A%3B0%3A63%3A%3A%3B0%3A61%3A%3A%3B0%3A167%3A%3A%3B0%3A20%3A%3A%3B0%3A164%3A%3A%3B0%3A19%3A%3A%3B0%3A88%3A%3A%3B0%3A249%3A%3A%3B0%3A39%3A%3A%3B0%3A174%3A%3A%3B0%3A31%3A%3A%3B0%3A54%3A%3A%3B0%3A51%3A%3A%3B0%3A181%3A%3A%3B0%3A2%3A%3A%3B0%3A87%3A%3A%3B0%3A143%3A%3A%3B0%3A7%3A%3A%3B0%3A189%3A%3A%3B0%3A237%3A%3A%3B0%3A156%3A%3A%3B0%3A47%3A%3A%3B0%3A234%3A%3A%3B0%3A251%3A%3A%3B0%3A262%3A%3A%3B0%3A134%3A%3A%3B0%3A218%3A%3A%3B0%3A109%3A%3A%3B0%3A123%3A%3A%3B0%3A201%3A%3A%3B0%3A254%3A%3A%3B0%3A25%3A%3A%3B0%3A69%3A%3A%3B0%3A140%3A%3A%3B0%3A119%3A%3A%3B0%3A16%3A%3A%3B0%3A207%3A%3A%3B0%3A232%3A%3A%3B0%3A223%3A%3A%3B0%3A256%3A%3A%3B0%3A163%3A%3A%3B0%3A97%3A%3A%3B0%3A173%3A%3A%3B0%3A191%3A%3A%3B0%3A186%3A%3A%3B0%3A192%3A%3A%3B0%3A43%3A%3A%3B0%3A243%3A%3A%3B0%3A199%3A%3A%3B0%3A159%3A%3A%3B0%3A184%3A%3A%3B0%3A18%3A%3A%3B0%3A35%3A%3A%3B0%3A59%3A%3A%3B0%3A64%3A%3A%3B0%3A216%3A%3A%3B0%3A86%3A%3A%3B0%3A120%3A%3A%3B0%3A205%3A%3A%3B0%3A149%3A%3A%3B0%3A127%3A%3A%3B0%3A115%3A%3A%3B0%3A17%3A%3A%3B0%3A110%3A%3A%3B0%3A53%3A%3A%3B0%3A238%3A%3A%3B0%3A239%3A%3A%3B0%3A217%3A%3A%3B0%3A206%3A%3A%3B0%3A155%3A%3A%3B0%3A28%3A%3A%3B0%3A222%3A%3A%3B0%3A220%3A%3A%3B0%3A250%3A%3A%3B0%3A252%3A%3A%3B0%3A44%3A%3A%3B0%3A196%3A%3A%3B0%3A227%3A%3A%3B0%3A221%3A%3A%3B0%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=56+57+0+43+32+1+2+3+4+55+60+7+6+5+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+14+27+53+54+58+16+30+13+17+18+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+22+35+24+38+25&selector%5Bextra_filters%5D=3&narrow="
  url = "https://zh.surebet.com/surebets?utf8=%E2%9C%93&selector%5Border%5D=profit&selector%5Boutcomes%5D%5B%5D=&selector%5Boutcomes%5D%5B%5D=2&selector%5Boutcomes%5D%5B%5D=3&selector%5Bmin_profit%5D=&selector%5Bmax_profit%5D=&selector%5Bmin_roi%5D=&selector%5Bmax_roi%5D=&selector%5Bsettled_in%5D=0&selector%5Bbookies_settings%5D=4%3A67%3A%3A%3B4%3A72%3A%3A%3B0%3A66%3A%3A%3B4%3A76%3A%3A%3B0%3A182%3A%3A%3B4%3A74%3A%3A%3B4%3A37%3A%3A%3B4%3A148%3A%3A%3B4%3A211%3A%3A%3B4%3A114%3A%3A%3B4%3A260%3A%3A%3B4%3A132%3A%3A%3B4%3A42%3A%3A%3B4%3A40%3A%3A%3B4%3A225%3A%3A%3B4%3A126%3A%3A%3B4%3A21%3A%3A%3B4%3A263%3A%3A%3B4%3A23%3A%3A%3B4%3A246%3A%3A%3B4%3A26%3A%3A%3B4%3A139%3A%3A%3B4%3A36%3A%3A%3B4%3A150%3A%3A%3B4%3A202%3A%3A%3B4%3A151%3A%3A%3B4%3A204%3A%3A%3B4%3A125%3A%3A%3B4%3A200%3A%3A%3B4%3A203%3A%3A%3B4%3A%3A%3A%3B4%3A32%3A%3A%3B4%3A1%3A%3A%3B4%3A65%3A%3A%3B4%3A161%3A%3A%3B4%3A29%3A%3A%3B4%3A10%3A%3A%3B4%3A45%3A%3A%3B4%3A228%3A%3A%3B4%3A34%3A%3A%3B4%3A77%3A%3A%3B4%3A58%3A%3A%3B4%3A253%3A%3A%3B4%3A165%3A%3A%3B4%3A95%3A%3A%3B4%3A180%3A%3A%3B4%3A208%3A%3A%3B4%3A48%3A%3A%3B4%3A14%3A%3A%3B4%3A197%3A%3A%3B4%3A11%3A%3A%3B4%3A188%3A%3A%3B4%3A38%3A%3A%3B4%3A147%3A%3A%3B4%3A52%3A%3A%3B4%3A198%3A%3A%3B4%3A55%3A%3A%3B4%3A187%3A%3A%3B4%3A33%3A%3A%3B4%3A13%3A%3A%3B4%3A176%3A%3A%3B4%3A248%3A%3A%3B4%3A236%3A%3A%3B4%3A215%3A%3A%3B4%3A49%3A%3A%3B4%3A62%3A%3A%3B4%3A75%3A%3A%3B4%3A12%3A%3A%3B4%3A193%3A%3A%3B4%3A90%3A%3A%3B4%3A46%3A%3A%3B4%3A229%3A%3A%3B4%3A210%3A%3A%3B4%3A146%3A%3A%3B4%3A117%3A%3A%3B4%3A135%3A%3A%3B4%3A24%3A%3A%3B4%3A88%3A%3A%3B4%3A73%3A%3A%3B4%3A258%3A%3A%3B4%3A261%3A%3A%3B4%3A154%3A%3A%3B4%3A129%3A%3A%3B4%3A56%3A%3A%3B4%3A230%3A%3A%3B4%3A22%3A%3A%3B4%3A145%3A%3A%3B4%3A136%3A%3A%3B4%3A30%3A%3A%3B4%3A257%3A%3A%3B4%3A5%3A%3A%3B4%3A6%3A%3A%3B4%3A214%3A%3A%3B4%3A245%3A%3A%3B4%3A235%3A%3A%3B4%3A175%3A%3A%3B4%3A224%3A%3A%3B4%3A190%3A%3A%3B4%3A4%3A%3A%3B4%3A183%3A%3A%3B4%3A242%3A%3A%3B4%3A213%3A%3A%3B4%3A244%3A%3A%3B4%3A15%3A%3A%3B4%3A212%3A%3A%3B4%3A219%3A%3A%3B4%3A128%3A%3A%3B4%3A233%3A%3A%3B4%3A50%3A%3A%3B4%3A9%3A%3A%3B4%3A179%3A%3A%3B4%3A259%3A%3A%3B4%3A178%3A%3A%3B4%3A41%3A%3A%3B4%3A130%3A%3A%3B4%3A133%3A%3A%3B4%3A247%3A%3A%3B4%3A3%3A%3A%3B4%3A240%3A%3A%3B4%3A8%3A%3A%3B4%3A118%3A%3A%3B4%3A89%3A%3A%3B4%3A166%3A%3A%3B4%3A124%3A%3A%3B4%3A226%3A%3A%3B4%3A209%3A%3A%3B4%3A63%3A%3A%3B4%3A61%3A%3A%3B4%3A167%3A%3A%3B4%3A20%3A%3A%3B4%3A164%3A%3A%3B4%3A19%3A%3A%3B4%3A249%3A%3A%3B4%3A39%3A%3A%3B4%3A174%3A%3A%3B4%3A31%3A%3A%3B4%3A54%3A%3A%3B4%3A51%3A%3A%3B4%3A181%3A%3A%3B4%3A2%3A%3A%3B4%3A87%3A%3A%3B4%3A143%3A%3A%3B4%3A7%3A%3A%3B4%3A189%3A%3A%3B4%3A237%3A%3A%3B4%3A156%3A%3A%3B4%3A47%3A%3A%3B4%3A234%3A%3A%3B4%3A251%3A%3A%3B4%3A262%3A%3A%3B4%3A134%3A%3A%3B4%3A218%3A%3A%3B4%3A109%3A%3A%3B4%3A123%3A%3A%3B4%3A201%3A%3A%3B4%3A254%3A%3A%3B4%3A25%3A%3A%3B4%3A69%3A%3A%3B4%3A140%3A%3A%3B4%3A119%3A%3A%3B4%3A16%3A%3A%3B4%3A207%3A%3A%3B4%3A232%3A%3A%3B4%3A223%3A%3A%3B4%3A256%3A%3A%3B4%3A163%3A%3A%3B4%3A97%3A%3A%3B4%3A173%3A%3A%3B4%3A191%3A%3A%3B4%3A186%3A%3A%3B4%3A192%3A%3A%3B4%3A43%3A%3A%3B4%3A243%3A%3A%3B4%3A199%3A%3A%3B4%3A159%3A%3A%3B4%3A184%3A%3A%3B4%3A18%3A%3A%3B4%3A35%3A%3A%3B4%3A59%3A%3A%3B4%3A64%3A%3A%3B4%3A216%3A%3A%3B4%3A86%3A%3A%3B4%3A120%3A%3A%3B4%3A205%3A%3A%3B4%3A149%3A%3A%3B4%3A127%3A%3A%3B4%3A115%3A%3A%3B4%3A17%3A%3A%3B4%3A110%3A%3A%3B4%3A53%3A%3A%3B4%3A238%3A%3A%3B4%3A239%3A%3A%3B4%3A217%3A%3A%3B4%3A206%3A%3A%3B4%3A155%3A%3A%3B4%3A28%3A%3A%3B4%3A222%3A%3A%3B4%3A220%3A%3A%3B4%3A250%3A%3A%3B4%3A252%3A%3A%3B4%3A44%3A%3A%3B4%3A196%3A%3A%3B4%3A227%3A%3A%3B4%3A221%3A%3A%3B4%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=56+57+0+43+32+3+55+60+28+8+44+9+26+34+10+11+12+39+47+46+48+49+59+53+54+58+30+13+29+45+19+36+33+31+40+64+42+41+20+62+61+50+51+63+21+37+23+35+38&selector%5Bextra_filters%5D=&narrow="


  payload = {
    'utf8': '✓',
    'user[email]': '731772412@qq.com',
    'user[password]': 'dnjsrl0620',    
    'user[remember_me]': '1',
    'commit': '登录',    
    'authenticity_token': 'aFsAakxX2LNr4cHK-13RQJxX7zVeheMtZMJTbBRnIKgn9rPzm3wPrwIBJvs1On_JhEAg8IysQeW0KDBKSM-erw'    
    } 
  
  headers = {
    'Cookie': '_sp5=azErMXR1KzJ0bUxPVzg5bXlMWmh5R3RDcFpRcFBWTDVvZ0haL1JZYW5Ham5OekczYmJJank3RVVpOExDSnBEZ3c2aERDTmhJSFBjd05vd28yZnRNZ1p1bDhFT3ZXSFVRQkJnTTFFRXUreUNtTFhSK2g2eDRvK2JyanhuaDZ3TEYrS08xQXlFTW9sMWc2MnM1VE9PWGtDNU9FdUppZDVmUkV6UkRaSkF5aVNaZTQ5V1FnNFdOMEc4WDJHS0hwdDhSLS00eVA4bTN1RHlWVHVHWGtva21pRmlBPT0%3D--fe9258d26d8dff2bd8d1594a0d2434f66851f6fc; ab=732; order_surebets_index=profit; ref=b0lTN1B5MHVVd0wxMG9tSFBDZFhoOWljUHpQK3hwTVBoSEFOQTNiWUptaHRqeURwS2djS3crbkw2cHdvK244SGNkZ040amFTdU1QdkJKVnRrQVZRUHh6REVmSW1pSUs0YktuekduNmJhTEo1eTlEa3QwYWM0NkRoeEtwWFNvUm4tLXBxQlJ2V0p0Q29RazYyWGliQ1FZYVE9PQ%3D%3D--97b7ab2017f313373c20fab7c971e26608c1785d; sel%3Asurebets=72b49d023af1686c0475fa4545c93009; uu=dae08a21-1c38-4d70-b955-fd5e639368c2'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  a=response.text
  return a;


b=game()
print(b)
