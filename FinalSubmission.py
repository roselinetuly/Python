import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from email import encoders
from email.mime.base import MIMEBase

# ------------ Group email ----------------------------------------
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
# to = ['roseline@transcombd.com', '']
to = ['rejaul.islam@transcombd.com', '']
# cc = ['', '']
cc = ['biswas@transcombd.com', 'yakub@transcombd.com']
bcc = ['roseline@transcombd.com']

recipient = to + cc + bcc

subject = "Python auto-email traning assignment of SKF - Outstanding"

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

msgText = MIMEText("""
<p style="text-align:left;">Dear Mr. Royel </p>
<p style="text-align:left;">Please see the following auto-email for the assignment SKF - Outstanding.</p><br>



<img src="cid:img1">
<img src="cid:img2">
<img src="cid:img3">
<img src="cid:img4">


<br><p style="text-align:left;"><b>Regards</b> <br><br>
Roseline Tuly Palma<br>
ISA - ERP<br>
</p>
                    """, 'html')

msg.attach(msgText)

# --------- Set Credit image in mail -----------------------
img = open('D:/PYTHON/ProjectTraining/FinalImage.png', 'rb')
img1 = MIMEImage(img.read())
img.close()
img1.add_header('Content-ID', '<img1>')
msgRoot.attach(img1)

img = open('D:/PYTHON/ProjectTraining/3Figure.png', 'rb')
img2 = MIMEImage(img.read())
img.close()
img2.add_header('Content-ID', '<img2>')
msgRoot.attach(img2)

img = open('D:/PYTHON/ProjectTraining/4Figure.png', 'rb')
img3 = MIMEImage(img.read())
img.close()
img3.add_header('Content-ID', '<img3>')
msgRoot.attach(img3)

img = open('D:/PYTHON/ProjectTraining/5Figure.png', 'rb')
img4 = MIMEImage(img.read())
img.close()
img4.add_header('Content-ID', '<img4>')
msgRoot.attach(img4)


# file_location = 'D:/PYTHON/ProjectTraining/ClosedToMatured.xlsx'
# filename = os.path.basename(file_location)
# attachment = open(file_location, "rb")
# part = MIMEBase('application', 'octet-stream')
# part.set_payload(attachment.read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
# msgRoot.attach(part)

# # ----------- Finally send mail and close server connection ---
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
server.sendmail(me, recipient, msgRoot.as_string())
server.close()
print('Mail Send')