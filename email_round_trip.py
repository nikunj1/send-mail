import smtplib
import imaplib
import email
import time


# Send Mail Function
def send_message(addr, to, msg,sendTime):
	try:
		server = smtplib.SMTP('smtp.gmail.com',587)
    		server.ehlo()
    		server.starttls()
    		server.ehlo()
    		server.login('nikunj.svens@gmail.com','nikunj@1')
		
		server.sendmail(addr, to, msg)

		print 'message has been send'
		
    	except smtplib.SMTPAuthenticationError:
    		return 'login_err'
	
	finally:
		server.quit()

			
# get Inboxsubject function
def getLastInbox_subject():
	print 'Trying to read message:'
  	mailbox = imaplib.IMAP4_SSL('imap.gmail.com')
  	mailbox.login('ramoli013@gmail.com', '96019493')
  	selected = mailbox.select('INBOX')
  	result, data = mailbox.search(None, "ALL")
  	ids = data[0]
  	id_list = ids.split()
  	latest_email_id = id_list[-1]
  	result, data = mailbox.fetch(latest_email_id, '(RFC822)')
  	raw_email = data[0][1]
  	email_message = email.message_from_string(raw_email)
  	sub = email_message['subject']
  	return sub
    
  	mailbox.logout()



if __name__ == '__main__':
	
	fromAddr = 'nikunj.sevens@gmail.com'
	toAddr='ramoliya2013@gmail.com'
	sub = 'Hello' 
	

	msg = ("From:%s\r\nTo:%s \r\nSubject:%s" % (fromAddr,toAddr,sub))
	print 'Trying to send message : '
	print msg
	print time.ctime()
	sendTime = time.time()
	success = send_message(fromAddr,toAddr,msg, sendTime)
	
	if success=='login_err':
	    print '''Error logging in 
		     check your email_id or password.	
		'''
	else:
		time.sleep(5)
		temp_subject = getLastInbox_subject()
		
		if temp_subject == sub:
			print 'successfully read message'
			send_message(fromAddr,'nikunj.sevens@gmail.com','mail has been successfuly send ', sendTime)
			print '''	
				___________________________
				
				successfully receive send mail notification in inbox
				'''
		else:	
			while(True):
				time.sleep(5)
				current_time = time.time()
				if current_time - sendTime > 5*60:
					break
				else:
					send_message(fromAddr,'nikunj.sevens@gmail.com','sending mail has been failed', sendTime)
					print '''	
						___________________________
				
						successfully receive fail mail notification in inbox
						'''
					break	

	
	
	


	                                     	
		
		

