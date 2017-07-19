HOME_URL="E:\python projects\Spam or Ham\CSDMC2010_SPAM\SPAMTrain.label"
import os
def email_contents():
	with open(HOME_URL,'r') as f:
		em=f.readlines()
	labels=[]
	emails=[]
	for line in em:
		labels.append(line.split(" ")[0].strip())
		emails.append(line.split(" ")[1].strip())

	# print(emails[0])
	TRAIN_URL="E:\\python projects\\Spam or Ham\\CSDMC2010_SPAM\\Train_new\\"
	TEST_URL="E:\\python projects\\Spam or Ham\\CSDMC2010_SPAM\\Test_new\\"
	email_train_cont=[]
	email_test_cont=[]
	for email in emails:
		with open(os.path.join(TRAIN_URL,email),encoding="latin1") as f:
			content=f.read()
			email_train_cont.append(content)
		
	test_data=os.listdir(TEST_URL)
	for mail in test_data:
		with open(os.path.join(TEST_URL,mail),encoding='latin1') as m:
			test=m.read()
			email_test_cont.append(test)
	return email_train_cont,email_test_cont

# re.compile('<.*?>')
	


	