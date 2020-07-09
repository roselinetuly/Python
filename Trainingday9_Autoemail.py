import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ------------ Group email ----------------------------------------
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
to = ['roseline@transcombd.com', '']
cc = ['', '']
bcc = ['', '']

recipient = to + cc + bcc
date = '09-Jul-2020'

subject = "Test report "

email_server_host = 'mail.transcombd.com'
port = 25

msgRoot['From'] = me

msgRoot['To'] = ', '.join(to)
msgRoot['Cc'] = ', '.join(cc)
msgRoot['Bcc'] = ', '.join(bcc)
msgRoot['Subject'] = subject

msg = MIMEMultipart()
msgRoot.attach(msg)
#
# msgText = MIMEText('This is the alternative plain text message.')
# msgAlternative.attach(msgText)

msgText = MIMEText(""" <img src="cid:img1" height='481', width='1280'>

                       
                       """, 'html')

msg.attach(msgText)
# <h1>Heading 1</h1>
# <h2>Heading 2</h2>
# <h3>Heading 3</h3>
# <h4>Heading 4</h4>
# <h5>Heading 5</h5>
# <h6>Heading 6</h6>
# # --------- Set Credit image in mail   -----------------------

img = open('./Assignment9_Roseline.png', 'rb')
img1 = MIMEImage(img.read())
img.close()
img1.add_header('Content-ID', '<img1>')
msgRoot.attach(img1)

# # ----------- Finally send mail and close server connection ---
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
server.sendmail(me, recipient, msgRoot.as_string())
server.close()
print('Mail Send')
