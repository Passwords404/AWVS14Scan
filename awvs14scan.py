import requests
import urllib3
import multiprocessing
urllib3.disable_warnings()

awvs_url = "https://localhost:3443"
apikey ="1986ad8c0a5b3df4d7028d5f3c06e936c38211c213f4b491384f28da29e550ad8"
headers = {
    "Cookie": "ui_session="+apikey,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Auth": apikey,
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "close"
}

def addscan():
    addurl = awvs_url+"/api/v1/targets/add"
    urls = []
    targetids = []
    with open('url.txt','r') as f:
        for i in f.readlines():
            urls.append(i.strip())
    for x in urls:
        #print(x)
        data = '{"targets":[{"address":"%s","description":""}]}' %(x)
        #print(data)
        add = requests.post(url = addurl,data = data,headers=headers,verify=False,timeout=10)
        data_json = add.json()
        items = data_json.get("targets", [])
        for y in items:
            targetid = y.get("target_id")
        scanurl = awvs_url+"/api/v1/scans"
        data2 = '{"profile_id":"11111111-1111-1111-1111-111111111111","incremental":false,"schedule":{"disable":false,"start_date":null,"time_sensitive":false},"target_id":"%s"}' % targetid
        scan = requests.post(url = scanurl,data = data2,headers=headers,verify=False,timeout=10)
        print(x,"添加成功")
def delscan():
    url = awvs_url+"/api/v1/scans"
    id = requests.get(url = url,headers=headers,verify=False,timeout=10)
    data_json = id.json()
    items = data_json.get("scans", [])
    xxxurl = awvs_url + "/api/v1/scans?l=20"
    xxxget = requests.get(url=xxxurl, headers=headers, verify=False, timeout=10)
    for y in items:
        targetid = y.get("target_id")
        #print(targetid)
        delurl = awvs_url+"/api/v1/scans/"+targetid
        delrep = requests.delete(url = delurl,headers=headers,verify=False,timeout=10)
        #print(delrep.text)


if __name__ == '__main__':
    print("作者：最菜的Mat Blog:https://www.cnblogs.com/matsec")
    print("\n配置说明：目标请放在url.txt文件中，请在awvs_url中配置awvs地址，apikey中填写key")
    model = (input("\n添加扫描目标请输入1，删除扫描目标请输入2："))
    if model == "1":
        p = multiprocessing.Process(target=addscan)
        p.start()
    if model == "2":
        delscan()
