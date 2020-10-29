# 사업자등록상태조회
# Python version : 3.10.0a1
# ex) python .\company_nm_cheack.py 220-81-62517 220-81-83676 206-85-26551
# 사업자등록상태 조회 : https://teht.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/ab/a/a/UTEABAAA13.xml
# 사업자 조회 : http://www.ftc.go.kr/bizCommPop.do?wrkr_no=2068526551

import sys
import requests
import xml.etree.ElementTree as ET

POST_URL = "https://teht.hometax.go.kr/wqAction.do?actionId=ATTABZAA001R08&screenId=UTEABAAA13&popupYn=false&realScreenId="
XML_RAW = "<map id=\"ATTABZAA001R08\"><pubcUserNo/><mobYn>N</mobYn><inqrTrgtClCd>1</inqrTrgtClCd><txprDscmNo>\{txprDscmNo\}</txprDscmNo><dongCode>15</dongCode><psbSearch>Y</psbSearch><map id=\"userReqInfoVO\"/></map>"

# 사업자 조회
def call(txprDscmNo):
    res = requests.post(POST_URL, data=XML_RAW.replace("\{txprDscmNo\}", txprDscmNo), headers={'Content-Type': 'application/xml'})

    # xml 결과값 리턴
    return res

if (len(sys.argv) < 2):
    print("사업자등록번호를 입력하세요.")
    exit()

for idx, value in enumerate(sys.argv):
    # print("idx : {0}, trtCntn : {1}".format(idx, value))
    if(idx == 0): continue

    # call(value) 값을 전달 받아 파싱
    root = call(value.replace("-",""))
    # print(root.text)

    # 등록유무 확인 내용 smpcBmanTrtCntn
    smpcBmanTrtCntn = ET.fromstring(root.text).find("smpcBmanTrtCntn").text.strip()

    # 사업 현황 내용 trtCntn
    trtCntn = ET.fromstring(root.text).find("trtCntn").text.strip()

    # result = crn + "\t" + xml.replace("\n","").replace("\t", " ") + "\n"
    print("사업자등록번호 : {0}, 등록유무 : {1}\t 사업현황 : {2}".format(value, smpcBmanTrtCntn, trtCntn))
    # result += call(value)

# result = result.strip()
# print(result)