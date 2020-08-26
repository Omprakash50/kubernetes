import smtplib as s
	op=s.SMTP("smtp.gmail.com",587)
	op.starttls()
	op.login("omprakash.21910935@viit.ac.in","Geetaom@1710")
	subject="Job failed"
	boby="Your website is not accessible to client"
	message="Subject:{}\n\n{}".format(subject,boby)
	listOfAddress=["choudharyomprakash147@gmail.com"]
    op.sendmail("choudharyomprakash",listOfAddress,message)
	op.quit()
