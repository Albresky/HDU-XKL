# XKL | 下课啦
`上课啦`系统全接口，主要用于课堂签到和健康打卡

# 注意

**本仓库为技术交流而创建，请不要修改滥用。**

**如果你基于本仓库的代码开发了任何违规、非法的工具，请自行负责。**

# 介绍

本仓库可能有助有获取进入 `上课啦` 系统的若干信息, 包括 `个人信息`, `课堂签到`, `健康打卡`,以及 `课表`等等。

# 如何使用


## 1 依赖requirements的安装

在运行仓库内任何代码之前，请先确保依赖已安装到环境：

```
pip install -r requirements.txt
```

## 2 课堂签到

### 2.1 运行 `demo.py` 文件

`demo.py`
```
myCheck = Check()               # create a `Check` Object
myCheck.getUserinfo()           # get UserInfo
myCheck.getCourse("2022-05-11") # get user's CourseList by date
myCheck.check()                 # class check
```

## 3 课堂签到

### 3.1 环境说明

目前未知学校服务器是否有IP检查，故不建议将代码部署到私有云服务器。如果你有长期开机运行的`闲置手机`、`树莓派`、`Jetson`，或`笔记本`等稳定的硬件设施，那么建议使用cron部署计划任务。

### 3.2 云服务器或本地终端（Android Termux 、Linux）

安装Cron，然后创建定时任务：

```
crontab -e

# 从左至右依次表示分、时、日、月、周。示例为每日上午5:20执行任务
20 05 * * * /usr/bin/python3 /xxx/xxx/XKL/src/demo.py

# 启动服务
service crond start
```

## 4 附加

首次运行`demo.py`会要求输入数字hd的账号密码，后续不再需要输入，且代码会自动更新token。

## 👋 (看这里)

以下文件请 **不要** 手动修改！(如果你只想使用健康打卡功能，那么你可以跳过步骤` 4 附加`，且在执行demo.py前填写好`User`节点。)

`config.ymal`:
```
User:
  id:       # Your UserID (HDU-CAS)
  pwd:      # Your LoginPassword

params:     # This node is not allowed to edit.
  X-Auth-Token: 
  XAT_updateTime:
```

# 注意

`在IDE内运行，请`
- **不要使用代理！**

- **不要使用代理！**

- **不要使用代理！**

否则可能触发异常： `(Caused by ProxyError('Cannot connect to proxy.', FileNotFoundError(2, 'No such file or directory')))`