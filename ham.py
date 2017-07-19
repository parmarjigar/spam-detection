import pandas as pd
# import chardet
from sklearn.model_selection import train_test_split
from emails import email_contents
import matplotlib.pyplot as plt

labels=[]	
contents=[]
emailLabels=[]

with open('SMSSpamCollection','r') as f:
	filer=f.readlines()
	for line in filer:
		labels.append(line[:4].strip())
		contents.append(line[4:].strip())

	
with open('E:\python projects\Spam or Ham\CSDMC2010_SPAM\SPAMTrain.label' ,'r') as e:	
	email=e.readlines()
	for e in email:
		emailLabels.append(e.split(" ")[0].strip())
		
for i in range(len(emailLabels)):
	if emailLabels[i]=='1':
		emailLabels[i]='ham'
	else:
		emailLabels[i]='spam'
# print(emailLabels)			
		
email_content,email_test_cont=email_contents()
# print(len(emailLabels),len(email_content))
	
labels_train,labels_test,contents_train,contents_test=train_test_split(labels,contents,test_size=0.2,random_state=42)
email_label_train,email_label_test,email_content_train,email_content_test=train_test_split(emailLabels,email_content,test_size=0.2,random_state=42)

#combining sms and email Dataset

labels_train.extend(email_label_train)
labels_test.extend(email_label_test)
contents_train.extend(email_content_train)
contents_test.extend(email_content_test)

from sklearn.feature_extraction.text import CountVectorizer
count=CountVectorizer()

sms_transform=count.fit_transform(contents_train)
sms_test=count.transform(contents_test)
# print(count.vocabulary_)

from sklearn.feature_extraction.text import TfidfTransformer
features=TfidfTransformer()

feat=features.fit_transform(sms_transform)
contents1=features.transform(sms_test)

from sklearn import svm
clf=svm.LinearSVC(C=10000.0)#,kernel="rbf",gamma=0.6)
clf.fit(feat,labels_train)
pred=clf.predict(contents1)

from sklearn.metrics import accuracy_score
acc=accuracy_score(labels_test,pred)

print (acc)

ml=input("enter String: ")

chk=count.transform([ml])

trans=features.transform(chk)

print(clf.predict(trans))