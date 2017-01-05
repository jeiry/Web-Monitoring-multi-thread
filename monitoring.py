# coding=utf-8
#!/usr/bin/env python  
import urllib2
import thread
import sys 
import time  
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime
  
# timer_interval=1  
# def delayrun():  
#     print 'running'  

######email
sender = 'jeiryc@126.com'

mail_host = 'smtp.126.com'
mail_user = "jeiryc" 
mail_pass = "your email password" 
smtpObj = smtplib.SMTP()

def jcLog(str):
    today = datetime.datetime.now()
    time1 = today.strftime("%Y%m%d")
    time2 = today.strftime("%Y-%m-%d %H:%M:%S")
    writeresult=file(time1+'.log','a+')  
    str1=writeresult.write(time2+"  "+str+'\n')  
    writeresult.close()
    return True

def sentEmail(url,receiver):
    receivers = [receiver,'250285246@qq.com'] #接收人的邮箱,可设置多个,第一个为设置传入邮箱,后面添加的为固定抄送的邮箱.
    try:
    	content = url+'   进不去' #邮件内容
    	message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = sender
        message['To'] =  receivers[0]
        subject = content
        message['Subject'] = Header(subject, 'utf-8')

        smtpObj.connect(mail_host) 
        smtpObj.login(sender, mail_pass) 
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print "邮件发送成功"
        jcLog("邮件发送成功: "+content)
    except smtplib.SMTPException:
    	print "Error: 无法发送邮件"

dict = {}
#因为偶尔会有掉包,所以会自动尝试3次,3次都无法连接就会发出邮件.如果3次内有一次成功了,就取消记录,继续正常检测.
def urlCheck(value,interval,receiver):
    try:
        code=urllib2.urlopen(value,timeout=25).code
        print value,' url:',code
        jcLog('checked url:'+value)
    	if(code==200):
    		time.sleep(interval)
     	   	urlCheck(value,interval,receiver)
        else:
    		time.sleep(interval)
       		urlCheck(value,interval,receiver)
       	if(dict.has_key(value)):
       		jcLog("试"+bytes(dict[value])+"次 没事了"+value)
       		del dict[value]
    except:
        print value,"timeout"
        jcLog("timeout "+value)
        if(dict.has_key(value)==False):
        	time.sleep(interval)
        	dict[value]=1
        	jcLog("timeout "+bytes(dict[value])+"次 "+value)
        elif dict[value] == 3:
        	sentEmail(value,receiver)
        	jcLog("timeout "+bytes(dict[value])+"次 发邮件"+value)
        	time.sleep(interval+interval+interval+interval+interval)
        	del dict[value]
        else:
        	time.sleep(interval)
        	dict[value]+=1
        	jcLog("timeout "+bytes(dict[value])+"次 "+value)
        	
        print dict
        urlCheck(value,interval,receiver)
    
# 创建多个线程检测
if __name__=='__main__':
	try:
		thread.start_new_thread( urlCheck, ("http://www.google.com",60,'13536621211@163.com',) )
		thread.start_new_thread( urlCheck, ("http://www.facebook.com/",60,'13536621211@163.com',) )
                #创建了2个线程检测两个网站 第一个值为网址\第二个值为每60秒循环一次\第三个值为出现问题接收提醒邮箱
		jcLog("run")
	except:
   		print "Error: unable to start thread"
   		
while 1:
	time.sleep(1)