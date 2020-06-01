# 项目概述
此项目主要目标是 记录sanic的项目框架，如何扩展第三方插件，加入中间件，蓝图管理等等，基本是一个拿来即用便可上线的项目框架

# 项目涉及到的插件
* redis使用sanic-redis包

#### 软件架构
```
|--sanic_frame_demo
    |-- app
    |	 |-- __init__.py
    |    |-- middleware # 中间件(日志中间件)
    |    |-- core # 各种第三方插件 通过 init_app() 注册的方式 都集中此处
    |    |-- utils # 各种工具函数
    |    |    |-- constant.py # 常量
    |    |    |-- exception.py # 异常处理
    |    |    |-- ...
    |    |-- controllers # 路由模块
    |    |    |-- blueprint_api # 某个蓝图模块
    |    |    |-- ...
    |-- config # 项目配置层
    |    |-- __init__.py # 根据环境变量获取具体配置
    |    |-- base.py
    |    |-- local.py # 本地开发配置
    |    |-- develop.py # 测试服配置
    |    |-- product.py # 生产服配置
    |-- start.py # 项目启动文件
    |--	README.md
    |-- requirements.txt
```

# 注意事项
* sanic项目在macos系统中(windows系统忽略此条),如果需要pycharm进行接口内部断点debug,需要设置sanic的auto_reload=False,否则无效

# 项目部署或启动方法
* 环境变量设置
```shell script
export SANIC_ENV='LOCAl'
```
* 使用gunicorn运行,命令如下
```shell script
gunicorn -w 9 -b 0.0.0.0:5000 -t 10 start:app --worker-class sanic.worker.GunicornWorker
```
* 使用内置run()多进程运行,可以指定workers进程数量,看了源代码，好像此方法默认就是使用的uvloop,在sanic.server.py的35,36行
```shell script
python start.py
```
* 使用uvloop运行
```shell script
python start_loop.py
```
# 示例功能描述
* 通过异步redis进行redis list的相关操作
* 实现RSA非对称加密 对参数进行加解密功能 [相关链接](https://www.cnblogs.com/rgcLOVEyaya/p/RGC_LOVE_YAYA_327days.html)

# sanic框架使用注意事项
* 特点:在get请求中，使用request.args获取参数信息，会发现参数值是一个list,使用时必须 list[0]才能获取参数值；如参数名为a,值为1，则获取到的数据为:{'a':[1]}
      这种用法的好处在于 如果用户请求参数为"?key1=value1&key2=value2&key1=value3"时，则key1的值直接为2个值的list=["value1","value3"],不用再处理(不像flask直接省略value3)
* 坑点:在app.run()中的参数如 debug,workers 等需要手动的指定，无法通过app.config设置(和flask不同)
* 注意:在接口中获取此项目配置时，可以通过 request.app.config 获取到配置的dict结构数据(每个请求进入都包含一个app相关信息)，不要通过app.config调用，否则gunicorn启动失败

# 其他备注
* mysql相关: 使用 [tortoise-orm](https://tortoise-orm.readthedocs.io/en/latest/getting_started.html) 进行mysql的orm操作，但是限制python>=3.7
* sanic官方推荐的 [相关拓展](https://github.com/mekicha/awesome-sanic#orm)
* sanic官方文档给出的相关 [框架示例代码](https://github.com/huge-success/sanic/tree/master/examples)

# 总结
* sanic框架的各种第三方包有待完善,特别是mysql相关orm包(渴望出来个sqlalchemy级别的)
* sanic离实际广泛使用仍有很长一段路走!
