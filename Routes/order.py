from flask import redirect,request,render_template,abort
from DbData.orderdata import OrderData

def orderlist():
    orderlist=OrderData().order_list()
    aa={"addf":"eeee","BBBB":"这是结果","CCCC":"ddddd"}
    #return "这是订单列表页面"
    return render_template('order/orderlist.html',name="人员信息",result=orderlist)

def u_test():
    orderlist=OrderData().order_list()
    aa={"addf":"eeee","BBBB":"这是结果","CCCC":"ddddd"}
    #return "这是订单列表页面"
    return render_template('order/newTest.html',test="人员信息",result=orderlist)

def mmmmm():
    aa={"addf":"eeee","BBBB":"这是结果","CCCC":"ddddd"}
    #return "这是订单列表页面"
    return render_template('order/mmmm.html',name="人员信息")


def wanghuan():
    aa={"addf":"eeee","BBBB":"这是结果","CCCC":"ddddd"}
    #return "这是订单列表页面"
    return render_template('order/wtest.html',name="wanghuan",ds=aa)


def orderitem(orderid='-1'):
    print(request.args.get('name'))
    if orderid == '-1':
        return redirect('http://www.baidu.com')
    elif orderid == 'NO':
        return abort(404)

    return '<h1> 订单详情页，订单id是：%s</h1>' % (orderid)
    #uname=request.form['uname']
def orderadd(id='-1'):
    itemid=request.args.get('name')
 
    print(itemid)
    orderlist=OrderData().order_add_item()
    #if orderid == '-1':
    #    return redirect('http://www.baidu.com')
    #elif orderid == 'NO':
    #   return abort(404)
    return "%s" % orderlist
def orderdel():
    itemid=request.form["id"]
    if itemid=="":
        return "FALSE"
    print(itemid)
    orderdel=OrderData().order_item_del(itemid)
    return "%s" % orderdel
    