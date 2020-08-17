import smtplib as s
obj=s.SMTP('smtp.gmail.com',587)
obj.starttls()
obj.login('rpkagoswami@gmail.com','hqokrvwlfxrqanil')
subject='mail using python'
body='hey whatsup stay safe stay healthy'
message='subject:{}\n\n{}'.format(subject,body)
listofaddress=['prachisweet97@gmail.com']
obj.sendmail('rpkagoswami@gmail.com',listofaddress,message)
print('dbcu')
obj.quit()