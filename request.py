import requests

url = "http://www.baidu.com"

url2="http://www.4snow.cn/Home/Index/go/op/login"
data ={"login":"xiaogu","pwd":"123456"}
r = requests.get(url2,params=data)
print(r.text)
print(r.encoding)
print(r.json())
add_url="http://www.4snow.cn/Business/Cust/go/op/add"
add_data={}

del_url="http://www.4snow.cn/Business/Cust/go/op/delete"
del_dta={id,}
update_url="http://www.4snow.cn/Business/Cust/go/op/update"
update_data={}

def post_cookie_server(add_url,add_data):
    #第一步 创建session对象
    session = requests.Session()
    #第二步 完成登录操作
    session.post(url,data)
    #第三步 进行新增客户操作
    r = session.post(add_url,add_data)
    #第四步 序列化返回值为json对象
    jsonObj = r.json()
    return jsonObj

