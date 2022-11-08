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
    ctx = {'pagename':'数据查询','address':{
        '/':'Home',
        '/model':'模型',
    }}
    response = render(request, "nav.html", ctx)
    response.write(f"{s}</table><br><a href='../add/'>添加数据</a>")
    return response

# 更多查询
def more_query(request):
    # 在网页https://docs.djangoproject.com/en/4.1/ref/models/querysets/
    # 可以查看全部的api
    ctx = {'pagename':'更多数据查询','address':{
        '/':'Home',
        '/model':'模型',
    }}
    try:
        method = request.GET['method']
        arg = request.GET['arg'].split(',')
    except Exception as e:
        method = 'None'
        arg = 'None'
        query = ''
        print(repr(e))
    match method:
        case "None":
            pass
        case "all":
            arg = ''
            query = Test.objects.all()
            query = list(query.values())
        case "filter":
            arg = 'loc="上海"'
            query = Test.objects.filter(loc='上海')
            query = list(query.values())
            # filter传入的参数还可以这样写
            ## filter(loc__contains='海')
            ## 等等，还有很多花样
        case "exclude":
            arg = 'loc="上海"'
            query = Test.objects.exclude(loc="上海")
            query = list(query.values())
        case "get":
            # 这个函数有些特别，他返回的值是一个模型对象，也就是Test对象
            # 并且如果满足筛选条件的对象有多个会抛出错误
            arg = 'loc="浙江"'
            query = Test.objects.get(loc='浙江')
        case "order_by":
            query = Test.objects.order_by(*arg)
            query = list(query.values())
        case "reverse":
            arg = '按照名字正序之后再反转'
            query = Test.objects.order_by('name').reverse()
            query = list(query.values())
        case "count":
            arg = ''
            query = Test.objects.count()
        case "first":
            # 返回的是Test对象
            arg = ''
            query = Test.objects.first()
        case "last":
            # 返回的是Test对象
            arg = ''
            query = Test.objects.last()
        case "exists":
            arg = ''
            query = Test.objects.exists()
        case "values":
            query = Test.objects.values(*arg)
            query = list(query)
        case "values_list":
            query = Test.objects.values_list(*arg)
            query = list(query)
        case "distinct":
            arg = ''
            query = Test.objects.values_list('loc').distinct()
            query = list(query)
        
    response = render(request, "nav.html", ctx)
    response.write("""<h2>QuerySet常用的api：</h2>
    Methods that return new QuerySet：<ul>
    filter()
    exclude()
    annotate()
    alias()
    order_by()
    reverse()
    distinct()
    values()
    values_list()
    dates()
    datetimes()
    none()
    all()
    union()
    intersection()
    difference()
    select_related()
    prefetch_related()
    extra()
    defer()
    only()
    using()
    select_for_update()
    raw()
    </ul>
    Operators that return new QuerySet
    <ul>
    AND (&)
    OR (|)
    XOR (^)
    </ul>
    Methods that do not return QuerySet
    <ul>
    get()
    create()
    get_or_create()
    update_or_create()
    bulk_create()
    bulk_update()
    count()
    in_bulk()
    iterator()
    latest()
    earliest()
    first()
    last()
    aggregate()
    exists()
    contains()
    update()
    delete()
    as_manager()
    explain()
    </ul><br>
    查询示例：
    <br>
    <a href='../more_query?method=values_list&arg=loc'>查询所有的loc（结果不去重）</a>
    <br>
    <a href='../more_query?method=all&arg='>查询所有的数据</a>
    <br>
    <a href='../more_query?method=get&arg='>查询loc='浙江'的数据</a>
    """)
    response.write(f"<h3>Test.objects.{method}({arg})</h3><br>")
    response.write(query)
    return response

# 更新数据
def update(request):
    ctx = {'pagename':'更新数据','address':{
        '/':'Home',
        '/model':'模型',
    }}
    try:
        flt = request.GET['filter'].split(',')
        update = request.GET['update'].split(',')
        query = f"query = Test.objects.filter({flt[0]}='{flt[1]}').update({update[0]}='{update[1]}')"
        exec(query)
    except Exception as e:
        print(repr(e))
    response = render(request, "nav.html", ctx)
    response.write("传入参数filter和update，例如\
        <br>update?filter=name,zy&update=loc,US\
        <br>可以把所有name=zy的对象的loc属性改为US<br><br>")
    response.write(list(Test.objects.values()))
    return response

# 删除数据
def delete(request):
    ctx = {'pagename':'删除数据','address':{
        '/':'Home',
        '/model':'模型',
    }}
    try:
        flt = request.GET['filter'].split(',')
        query = f"query = Test.objects.filter({flt[0]}='{flt[1]}').delete()"
        exec(query)
    except Exception as e:
        print(repr(e))
    response = render(request, "nav.html", ctx)
    response.write("传入参数filter例如\
        <br>delete?filter=name,zy\
        <br>可以把所有name=zy的对象删除<br><br>")
    response.write(list(Test.objects.values()))
    return response