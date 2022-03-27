class user:
        count=0
        def __init__(self, name, email, id, phone,address):
            self.name=name
            self.email=email
            self.id=id
            self.phone=phone
            self.address=address
            user.count+=1
        def displayCount(self):
            print("There are %d users" % user.count)
        def displayDetails(self):
            print("Name:", self.name, ", Email:", self.email, ", Id:", self.id, "Phone:", self.phone, "address:", self.address)
e1=user("John", "Mjohn55@gmail.com", 80000,177332,"dhaka" )
e2=user("Mike", "mike12@gmail.com", 50000,17722 ,"dhaka")
e3=user("Derek", "derek23@gmail.com", 30000,17744,"dhaka")
e4=user("Raj", "raj12@gmail.com", 25000,1775,"dhaka")
e4.displayCount()
print("Details of all user:")
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()
e4.displayDetails()