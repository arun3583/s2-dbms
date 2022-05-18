import pymongo
url="mongodb://localhost:27017"
conn = pymongo.MongoClient(url)
db=conn["College1"]
coll=db["Studlist1"]


print("Question 1\n")
for i in coll.find({"gender":"female","course":"MCA"},{"name.fname":1,"name.lname":1,"course":1,"gender":1}):
	print(i["name"]["fname"]+ " "+i["name"]["lname"]+ "   "+i["course"]+ "     "+i["gender"])
print("\nQuestion 2\n")
for i in coll.find({"gender":"male","grade":"A+"},{"name.fname":1,"name.lname":1,"grade":1,"gender":1}):
	print(i["name"]["fname"]+ " "+i["name"]["lname"]+ "   "+i["grade"]+ "     "+i["gender"])
print("\nQuestion 3\n")
for m in coll.find({"course":"MCA"}).sort("mark",-1).limit(1):
	print(m)
print("\nQuestion 4\n")
for s in coll.find().sort("course","Mechanical").sort("mark",-1).limit(3):
	print(s)
print("\nQuestion 5\n")
for i in coll.find({"gender":"female"},{"_id":0,"name.fname":1,"name.lname":1,"mark":1}):
	print(i)
print("\nQuestion 6\n")
for i in coll.find({"mark":{'$gt':80,'$lt':90}},{"_id":0,"name.fname":1,"name.lname":1,"course":1,"mark":1}):
	print(i)
print("\nQuestion 7\n")
for i in coll.find({"name.fname":{'$regex': '^V'}},{"_id":0,"name.fname":1,"name.lname":1}):
	print(i)
print("\nQuestion 8\n")
for i in coll.find({"address.city":"Kollam"},{"name.fname":1,"name.lname":1}):
	print(i)
print("\nQuestion 9\n")
for i in coll.find({'$nor':[{"address.city":"Kollam"},{"address.city":"Thiruvananthapuram"}]},{"name.fname":1,"name.lname":1,"address.city":1}):
	print(i["name"]["fname"]+ " "+i["name"]["lname"]+ "   "+i["address"]["city"])
print("\nQuestion 10\n")
for i in coll.find({'$or':[{"address.city":"Kollam"},{"address.city":"Thiruvananthapuram"}]},{"name.fname":1,"name.lname":1,"address.city":1}):
	print(i["name"]["fname"]+ " "+i["name"]["lname"]+ "   "+i["address"]["city"])
	

