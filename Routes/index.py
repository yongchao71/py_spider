from flask import render_template
def index():    
    #return '<h1>Hello World!</h1>'
    aa={"addf":"a首页","BBBB":"B首页","CCCC":"ddddd"}
    return render_template('index.html',name="首页",result=aa)
