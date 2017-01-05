# Web-Monitoring-multi-thread
多线程网站监控python脚本
###介绍
有时候自己的网站挂了却全然不知。总不能一直看刷着自己的网站看吧。所以写了一个自动检测脚本。

多线程网站监控脚本。通过检测网站的状态码。如果不是返回200，就自动发送邮件到多个指定邮箱。

多线程是为了可以同时检测多个站而不堵塞主线程，不用等待一个一个结束。
##用法
修改发件email
```python
sender = 'jeiryc@126.com'
mail_host = 'smtp.126.com'
mail_user = "jeiryc" 
mail_pass = "your email password" 
```

创建线程
```python
try:
  thread.start_new_thread( urlCheck, ("http://www.google.com",60,'receive@email.com',) )
  thread.start_new_thread( urlCheck, ("http://www.facebook.com/",60,'receive@email.com',) )
  #创建了2个线程检测两个网站 第一个值为网址\第二个值为每60秒循环一次\第三个值为出现问题接收提醒邮箱
  jcLog("run")
except:
  print "Error: unable to start thread"
```

##运行方法
可以丢到一个sh文件运行。

1. touch start.sh
2. vi start.sh
3. 粘帖 ``python monitoring.py &``
4. cd 到 对应目录
5. start.sh

然后可以关闭ssh

####或者使用supervisor

Debian / Ubuntu可以直接通过apt安装：
``# apt-get install supervisor``

supervisor就是用Python开发的一套通用的进程管理程序，能将一个普通的命令行进程变为后台daemon，并监控进程状态，异常退出时能自动重启。

详情自行google

win用户可写个cmd，开机运行
