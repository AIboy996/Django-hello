from django.shortcuts import render,HttpResponse

# Home页面
def hello(request):
    ctx = {}
    ctx['address'] = {}
    ctx['pagename'] = 'Home'
    return render(request, 'index.html', ctx)

# 模版继承，block的重载
def child(request):
    ctx = {}
    ctx['address'] = {'/':'Home'}
    ctx['pagename'] = '模版继承'
    return render(request, 'child.html', ctx)

# 模版语法实践
def text(request):
    from datetime import datetime
    from random import random
    context = {}
    context['hello'] = 'Hello World!'
    context['lst'] = [f'菜鸟教程{i}' for i in range(1,4)]
    context['dic'] = {"a": 1, 'b': 2, 'c': 3}
    context['now'] = datetime.now()
    context['random'] = random()
    context['lst2'] = []
    context['pagename'] = '模版语法实践'
    context['address'] = {'/':'Home'}
    return render(request, 'text.html', context)

# GET请求
def search_form(request):
    ctx = {'pagename': 'GET请求', 'address': {'/': 'Home'}}
    return render(request, 'search_form.html', ctx)

# GET的返回结果
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    ctx = {'pagename': '查询结果', 'address': {
        '/': 'Home', '/search-form/': 'GET请求'}}
    response = render(request, "nav.html", ctx)
    response.write(message)
    return response

# POST请求
def search_post(request):
    ctx ={}
    if request.POST:
        post = request.POST['q']
    try:
        post = float(post)
        ctx['rlt'] = post
        ctx['sq'] = post**.5
    except:
        pass
    ctx['pagename'] = "POST请求"
    ctx['address'] = {'/':'Home'}
    return render(request, "sqrt_post.html", ctx)

# 输出所有的request信息
def info(request):
    ctx = {'pagename':'REQUEST内容', 'address':{'/':'Home'}}
    lst = dir(request)
    s = "<ul>"
    for i in lst:
        j = eval(f"request.{i}")
        s += f"<li>{i}<br>{j}</li>"
    s += "</ul>"
    response = render(request,"nav.html", ctx)
    response.write(s)
    return  response

# 正则匹配
def re_match(request, year, month, day):
    s = f"year:{year}   month:{month}   day:{day}"
    return HttpResponse(s)