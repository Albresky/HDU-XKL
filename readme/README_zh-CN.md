[English](https://github.com/Albresky/XKL) | **中文**

# XKL | 下课啦
`上课啦`系统全接口，主要用于课堂签到和健康打卡

# 注意

**本仓库为技术交流而创建，请不要修改滥用。**

**如果你基于本仓库的代码开发了任何违规、非法的工具，请自行负责。**

# 介绍

本仓库可能有助有获取进入 `上课啦` 系统的若干信息, 包括 `个人信息`，`课堂签到`，`健康打卡`，以及 `课表`等等。

# 如何使用


## 1 依赖requirements的安装

在运行仓库内任何代码之前，请先确保依赖已安装到环境：

```
pip install -r requirements.txt
```

## 2 课堂签到 [`API`]

### 2.1 运行 `demo.py` 文件

`demo.py`
```
myCheck = Check()               # create a `Check` Object
myCheck.getUserinfo()           # get UserInfo
myCheck.getCourse("2022-05-11") # get user's CourseList by date
myCheck.check()                 # class check
```

## 3 自动健康打卡

### 3.1 环境说明

目前未知学校服务器是否有IP检查，故不建议将代码部署到私有云服务器。如果你有长期开机运行的`闲置手机`、`树莓派`、`英伟达 Jetson`，或 `笔记本` 等稳定的硬件设施，那么建议使用cron部署计划任务。

### 3.2 云服务器或本地终端（Android Termux 、Linux）

- 首先用Vim或Nano编辑XKL/src/task.sh：
  - `workdir` 为 `XKL/src` 的完整路径，比如 `/home/ubuntu/XKL/src` 。注意：路径结尾不要有 `/`
  - `thisPython` 为Python解释器的路径，请使用 `Python3` 的路径。Linux系统内可以通过执行 `$which python3` 查看它的路径，比如`/usr/bin/python3`
  - `thisPythonPATH` 为Python依赖包的路径，通常为 `/usr/lib/python3/dist-package`
  
- 然后通过cron创建定时任务：

```
crontab -e

# 从左至右依次表示分、时、日、月、周。示例为每日上午5:20执行任务
20 05 * * * bash /home/XKL/src/task.sh

# 启动服务， Ubuntu系统下cron服务为cron，其他Linux发行版为crond
service cron start

# [附]
# 如果通过crontab -e修改了任务，请重启cron服务
service cron restart

# [附]
# 较新的Linux发行版可能通过systemctl来进行服务管理：
# 启动cron服务
systemctl start cron
# 重启cron服务
systemctl restart cron
```

## 4 附加

首次运行 `demo.py` 会要求输入数字hd的账号密码，后续不再需要输入，且代码会自动更新token。

## 👋 (看这里)

以下文件请 **不要** 手动修改！(如果你只想使用健康打卡功能，那么你可以跳过步骤 `4 附加`，且在执行demo.py前填写好 `User` 节点。)

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
