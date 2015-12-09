import smtplib
import imaplib
import email
from datetime import date


def getLastInbox(count = 4):
  mailbox = imaplib.IMAP4_SSL('imap.gmail.com')
  mailbox.login('nikunj.sevens@gmail.com', 'nikunj@123')
  selected = mailbox.select('INBOX')
  result, data = mailbox.search(None, "ALL")
  ids = data[0]
  id_list = ids.split()
  latest_email_id = id_list[-1]
  result, data = mailbox.fetch(latest_email_id, '(RFC822)')
  raw_email = data[0][1]
  email_message = email.message_from_string(raw_email)
  print email_message['subject']
  return True
    
  mailbox.logout()

def send_message(addr, to, msg):
	try:
		server = smtplib.SMTP('smtp.gmail.com',587)
    		server.ehlo()
    		server.starttls()
    		server.ehlo()
    		server.login('nikunj.sevens@gmail.com','nikunj@123')
		server.sendmail(addr, to, msg)
		print 'message has been send'
		
		
    	except smtplib.SMTPAuthenticationError:
    		return 'login_err'
	
	finally:
		server.quit()
if __name__ == '__main__':
	fromaddr = 'nikunj.sevens@gmail.com'
	toaddr='nikunj.sevens@gmail.com'
	sub = raw_input('enter the subject:')
	now = date.today().strftime("%d/%m/%y")
	msg = ("From:%s\r\nTo:%s \r\nSubject:%s\r\n\r\n Hello,\r\nThis is the message body.\r\n\r\nThank you." % (fromaddr,toaddr,sub))
	print now+'\n'
	print msg+'\n'
	success = send_message(fromaddr,toaddr,msg)
	
	if success=='login_err':
	    print 'Error logging in'
	getLastInbox()
	

