进口要求
进口urllib3
进口多重处理
urllib3。禁用_警告()

awvs_url =" https://localhost:3443 "
apikey =" 1986 ad 8 c 0 a 5 B3 df 4d 7028d 5 F3 c 06 e 936 c 6 C4 a 625946534489 A8 ea 478 e 2 b 166 ADC "
标题={
    "饼干": " ui_session= "+apikey，
    "用户代理": “Mozilla/5.0(Windows NT 10.0；Win64x64) AppleWebKit/537.36 (KHTML，像壁虎一样)Chrome/98 . 0 . 4758 . 102 Safari/537.36 ",
    "内容类型": "应用程序/json ",
    "接受": "应用程序/json，文本/普通，*/* ",
    " X-Auth ":apikey，
    "接受编码": gzip，放气,
    "接受-语言": “zh-CN，zh；q=0.9英寸,
    “连接”: "关闭"
}

极好的 添加扫描():
addurl = awvs_url+"/api/v1/targets/add "
urls =[]
targetids =[]
    随着 打开(' url.txt ',r ') 如同女:
        为 i 在f.阅读行():
网址。附加(爱达荷（Idaho的缩写）剥夺())
    为 x 在URL:
数据={"targets":[{"address":"%s "，" description":""}]} ' %(x)
添加=请求。邮政(url=addurl，data=data，headers=headers，verify=错误的，超时=10)
data_json = add。json()
items = data_json。得到("目标", [])
        为 y 在项目:
targetid = y。得到("目标标识")
targetids。附加(targetid)  # 将每次迭代得到的targetid添加到列表中
scanurl = awvs_url+"/api/v1/scans "
        为targetid在目标id:# 针对列表中的每个targetid进行扫描
数据2 ={ " profile _ id ":" 11111111-1111-1111-1111-1111 "，" incremental":false，" schedule":{"disable":false，" start_date":null，" time_sensitive":false}，" target_id":"%s"} '% targetid
扫描=请求。邮政(url=scanurl，data=data2，headers=headers，verify=错误的，超时=10)
            打印(x，"添加成功")
极好的 德尔斯坎():
url = awvs_url+"/api/v1/scans "
id =请求。得到(url = url，头=头，验证=错误的，超时=10)
data_json = id。json()
items = data_json。得到("扫描", [])
xxxurl = awvs_url +“/api/v1/scans？l=20英寸
xxxget =请求。得到(url=xxxurl，头=头，验证=错误的，超时=10)
    为 y 在项目:
targetid = y。得到("目标标识")
        #打印(目标id)
delurl = awvs_url+"/api/v1/scans/"+targetid
delrep =请求。删除(url = delurl，headers=headers，verify=错误的，超时=10)
        #打印(delrep.text)


如果__name__ ==__main__ ':
    打印("作者：最菜的mat Blog:https://www . cn blogs . com/matsec ")
    打印(" \n配置说明：目标请放在url.txt文件中,请在awvs_url中配置awv地址，apikey中填写关键")
型号=(投入(" \n添加扫描目标请输入1,删除扫描目标请输入2:"))
    如果模型=="1":
p =多重处理。过程(target=addscan)
页（page的缩写）开始()
    如果模型=="2":
        德尔斯坎()
