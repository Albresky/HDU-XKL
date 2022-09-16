**English** | [中文](https://github.com/Albresky/XKL/blob/main/readme/README_zh-CN.md)

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

- First, use Vim/Nano to edit `XKL/src/bingo.sh` mannually：
  - `workdir` is the full path of `XKL/src`. e.g. `/home/ubuntu/XKL/src`. ATTENTION: this path doesn't need to be ended up with `/`
  - `thisPython` is the full path of Python interpreter，please use the path of `Python3`. It's full path will be obtained by executing command `$which python3` in Linux systems. The output could be like `/usr/bin/python3`
  - `thisPythonPATH` is the full path of Python's dependencies, and it tends to be `/usr/lin/python3/dist-packages`
  
- Then, create a task with cron:

```
crontab -e

# The first `five` params mean `minute`, `hour`, `day`, `month`, `week`. The example below means execute command at 05:20 on everyday
20 05 * * * bash /home/XKL/src/bingo.sh

# Launch the cron service. In Ubuntu, cron service is `cron`, while in the other Linux distributions, it usually  tends to be `crond`
service cron start

# [Extra]
# Please restart the cron service after modifying the task's content
service cron restart

# [Extra]
# `systemctl` could be used to manage the system services in some lastest Linux releases
# Launch cron service
systemctl start cron
# Restart cron service
systemctl restart cron
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
