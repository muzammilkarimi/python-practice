class student:


    def getdata(self):
        '''self.uid=101
        self.name='mak'
        self.address='bihar'
        self.fee=5000'''
        print("Enter student id")
        self.uid=input()
        print("Enter the student name")
        self.name=input()
        print("Enter the student address")
        self.address=input()
        print("Enter the student fee")
        self.fee=input()

    def showdata(self):
        print('uid',self.uid)
        print('name',self.name)
        print('address',self.address)
        print('fee',self.fee)


obj=student()
obj.getdata()
obj.showdata()
