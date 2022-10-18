# -*- coding: utf-8 -*-
from urllib import response
from django.shortcuts import render
from TestModel.models import Test

# 模型
def model(request):
    ctx = {'pagename':'模型', 'address':{'/':'Home'}}
    return render(request, 'model.html', ctx)

# 增加数据
def adddata(request):
    ctx = {'pagename':'增加数据', 'address':{'/':'Home','/model/':"模型"}}
    if request.POST:
        name = request.POST['name']
        loc = request.POST['loc']
        test2 = Test(name=name, loc=loc)
        test2.save()
        ctx['dic'] = {'name':name,'loc':loc}
        print(ctx)
    return render(request, "add_data_post.html", ctx)

# 查询数据
def query(request):
    s = "<br><table border=1><tr><th>name</th><th>location</th></tr>"
    lst = Test.objects.all()
    # 输出所有数据
    for var in lst:
        s += f"<tr><td>{var.name}</td><td>{var.loc}</td></tr>"
    ctx = {'pagename':'数据查询结果','address':{
        '/':'Home',
        '/model':'模型',
    }}
    response = render(request, "nav.html", ctx)
    response.write(f"{s}</table><br><a href='../add/'>添加数据</a>")
    return response

# 更新数据
def update(request):
    ctx = {'pagename':'更新数据','address':{
        '/':'Home',
        '/model':'模型',
    }}
    response = render(request, "nav.html", ctx)
    return response
# 删除数据
def delete(request):
    ctx = {'pagename':'删除数据','address':{
        '/':'Home',
        '/model':'模型',
    }}
    response = render(request, "nav.html", ctx)
    return response