#import src.Routes.order as order
import Routes as routes;
from flask import Flask;
from Common.Config import Config;

app = Flask(__name__)

@app.route('/') #@app.route('/user/<name>')
def home():    
    aa={"addf":"home页","BBBB":"B首页","CCCC":"SSS"}
    
    print("dddddddd")
    return "<h1>这是home</h1><h2>%s</h2>" % aa

app.add_url_rule('/index',view_func=routes.index)
app.add_url_rule('/order/list',view_func=routes.orderlist,methods=['POST','GET'])
app.add_url_rule('/order/item',view_func=routes.orderitem)
app.add_url_rule('/order/add',view_func=routes.orderadd,methods=['GET'])
app.add_url_rule('/order/del',view_func=routes.orderdel,methods=['POST'])

app.add_url_rule('/order/mmmmm',view_func=routes.mmmmm,methods=['GET'])
app.add_url_rule('/order/wtest',view_func=routes.wanghuan,methods=['GET'])
app.add_url_rule('/order/test',view_func=routes.u_test,methods=['GET'])
app.add_url_rule('/distribution/list',view_func=routes.distributionlist,methods=['POST','GET'])
app.add_url_rule('/distribution/item',view_func=routes.distributionitem)
app.add_url_rule('/distribution/add',view_func=routes.distributionadd)


if __name__ == '__main__':  
    print('开始执行--')
    app.run(host='127.0.0.1',port=9990,debug=False)
# app.run()
print('执行结束')



