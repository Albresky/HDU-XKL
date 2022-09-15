[中文](https://github.com/Albresky/XKL/blob/main/readme/README_zh-CN.md)

# XKL
Full access to skl, mainly used for class checkin.

# Attention
**This repository is created for technical discussion, any kind of modification is strongly forbidden.**

**IF YOU TRIED TO DEVELOP ANY ILLIEGAL OR UNAUTHORIZED TOOL BASED ON THIS REPOSITORY, PLEASE BE RESPONSIBLE FOR YOUR OWN BEHAVIOR.**

# Introduction
This respository could be helpful to obtain access to `skl` system, including `Personal Info`, `Class Check In`, `Course List`, and etc.

# How to use

## 1 Install modules from `requirements`

Make sure all the modules required are installed before running the code.

Execute the code bellow:

```
pip install -r requirements.txt
```

## 2 Class check in [`API`]

### 2.1 run the `demo.py` file

`demo.py`
```
myCheck = Check()               # create a `Check` Object
myCheck.getUserinfo()           # get UserInfo
myCheck.getCourse("2022-05-11") # get user's CourseList by date
myCheck.check()                 # class check
```

## 3 Daily health check in

### 3.1 Environment advices

Deploying the code to ECS is not recommended, because the IP address could be detected and banned by the school's server.

Creating a cron task on a stable facility using educational network (like dormitory WiFi and i-HDU) is the best choice if you own some devices like `Smart phones`, `Respberry Pi`, `NVIDIA Jetson`, `Laptop` and etc.

### 3.2 ECS or Local Terminal（Android Termux 、Linux）

Install `Cron`, then create a task:

```
crontab -e

# The first `five` params mean `minute`, `hour`, `day`, `month`, `week`. 示例为每日上午5:20执行任务
20 05 * * * /usr/bin/python3 /xxx/xxx/XKL/src/demo.py

# Launch the cron service
service crond start
```

## 4 In addition

Both of your `account` and `password` are required in your first login, and in the next they'll be optional.
 ( Don't worry, the `token` will be updated by code automatically.)


## 👋 (Look at here)

The file below **DO NOT** need to be edited manually. (If you use this repository just for health check in, you could fill in the `User` Node and step over `4 Inaddition`.)

`config.ymal`:
```
User:
  id:       # Your UserID (HDU-CAS)
  pwd:      # Your LoginPassword

params:     # This node is not allowed to edit.
  X-Auth-Token: 
  XAT_updateTime:
```

# ATTENTION

- **DO NOT USE PROXY!**

- **DO NOT USE PROXY!**

- **DO NOT USE PROXY!**

Otherwise, errors could be triggerred like `(Caused by ProxyError('Cannot connect to proxy.', FileNotFoundError(2, 'No such file or directory')))`
