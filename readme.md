# Django Hello World
本项目是[菜鸟教程](https://www.runoob.com/django/django-tutorial.html)的复刻，也是本人在校数据库课程的上机作业。

- 为了方便调试，添加了站点导航以及每个页面的导航。

- 为了方便mysql的配置，使用**docker-compose**搭建了mysql+django的容器组合，clone本项目后在根目录运行：

```bash
docker-compose up -d --build
```

即可一键运行服务（web服务映射在本机的8000端口）：

![image-20221201032834970](assets/image-20221201032834970.png)

## 预览

### 首页
![image-20221201032202901](assets/image-20221201032202901.png)
### Django模版语法实践
![](assets/16661126497112.jpg)
### 模型
![image-20221201032241926](assets/image-20221201032241926.png)

#### 添加数据（利用POST请求实现

![image-20221201032416543](assets/image-20221201032416543.png)

#### 查询数据

![image-20221201032437002](assets/image-20221201032437002.png)

#### 更多查询数据（利用GET请求实现

![image-20221201032520675](assets/image-20221201032520675.png)

#### 更新数据（利用GET请求实现

![image-20221201032600902](assets/image-20221201032600902.png)

#### 删除数据（利用GET请求实现

![image-20221201032615193](assets/image-20221201032615193.png)

### GET请求

![image-20221201032651960](assets/image-20221201032651960.png)

### POST请求

![image-20221201032707561](assets/image-20221201032707561.png)
