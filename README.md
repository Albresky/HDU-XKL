# XKL
Full access to skl, mainly used for class checkin.

# Attention
**This repository is created for technical discussion, all kinds of illegal modification are strongly forbidden !**

**IF YOU TRIED TO DEVELOP ANY ILLIEGAL OR UNAUTHORIZED TOOL BASED ON THIS REPOSITORY, PLEASE BE RESPONSIBLE FOR YOUR OWN BEHAVIOR.**

# Introduction
This respository could be helpful to obtain access to `skl` system, including `Personal Info`, `Class Checkin`, and `Course List`, etc.

# How to use

## run the `demo.py` file

`demo.py`
```
myCheck = Check()               # create a `Check` Object
myCheck.getUserinfo()           # get UserInfo
myCheck.getCourse("2022-05-11") # get user's CourseList by date
myCheck.check()                 # class check
```

## (Look at here)

The `config.ymal` DO NOT need to be edited manually.

`config.ymal`
```
User:
  id:       # Your UserID
  pwd:      # Your LoginPassword

params:     # This node is not allowed to edit.
  X-Auth-Token: 
  XAT_updateTime:
```

