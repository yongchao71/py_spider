from flask import redirect,request,render_template,escape
def distributionlist():
    aa={"addf":"eeee","BBBB":"这是结果","CCCC":"ddddd"}
    #return "这是分配列表页面"
    return render_template('distribution/distributionlist.html',name="分配列表",result=aa)

def distributionitem():
    return "这是分配详情页"
def distributionadd():
    return "这是分配添加页面"