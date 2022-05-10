
import pymongo
url="mongodb://localhost:27017/"
s=pymongo.MongoClient(url)
db=s["College"]
coll=db["Stud_list"]
#for x in coll.find({"gender":"female","course":"MCA"},{"name":1,"_id":0,"mark":1}):
#	print(x)
#for x in coll.find({"course":"MCA"}).sort("mark",-1).limit(1):
#	print(x["name"]["fname"]+" "+x["name"]["lname"])
#	print(x["address"]["house_name"]+" "+x["address"]["city"])
#	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"])
#for i in coll.find({"gender":"male","grade":"A+"}):
#	print(i["name"]["fname"]+" "+i["name"]["lname"])

#for x in coll.find({"course":"Mechanical"}).sort("mark",-1).limit(3):
#	print(x["name"]["fname"]+" "+x["name"]["lname"])
#for x in coll.find({"gender":"female","mark":{"$gt": 90}}):
#	print(x["name"]["fname"]+" "+x["name"]["lname"])
#	print(x["address"]["house_name"]+" "+x["address"]["city"])
#	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
#for x in coll.find({"gender":"female","mark":{"$lt": 90,"$gt":80}}):
#	print(x["name"]["fname"]+" "+x["name"]["lname"])
#	print(x["address"]["house_name"]+" "+x["address"]["city"])
#	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
#for x in coll.find({"name.fname":{"$regex":"^D"}}):
#	print(x["name"]["fname"]+" "+x["name"]["lname"])
#	print(x["address"]["house_name"]+" "+x["address"]["city"])
#	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
#for x in coll.find({"address.city":"Kollam"}):
#	print(x["name"]["fname"]+" "+x["name"]["lname"])
#	print(x["address"]["house_name"]+" "+x["address"]["city"])
#	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
#for x in coll.find({"$nor":[{"address.city":"Kollam"},{"address.city":"Thiruvananthapuram"}]}):
#	print(x["name"]["fname"]+" "+x["name"]["lname"])
#	print(x["address"]["house_name"]+" "+x["address"]["city"])
#	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
for x in coll.find({"address.city":{"$in":["Kollam","Thiruvananthapuram"]}}):
	print(x["name"]["fname"]+" "+x["name"]["lname"])
	print(x["address"]["house_name"]+" "+x["address"]["city"])
	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
