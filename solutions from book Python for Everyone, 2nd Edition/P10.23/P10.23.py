#P10.23

class Appointment:
    def __init__(self, description, date):
        self._description = description
        self._date = date

    def getAptDate(self):
        return self._date

    def getAptDesc(self):
        return self._description

    def occursOn(self):
        raise NotImplementedError

    def printAptDetails(self):
        raise NotImplementedError
    
    
class oneTime(Appointment):
    def __init__(self, description, date):
        super().__init__(description, date)

    def occursOn(self,  year, month, day):
        apt_date = self.getAptDate()
        apt_desc = self.getAptDesc()
        if (apt_date[4:] == year) & (apt_date[0:2] == month) & (apt_date[2:4] == day) :
            print("Appointment ", apt_desc)

    def printAptDetails(self):
        apt_date = self.getAptDate()
        apt_desc = self.getAptDesc()
        print("%s, %s" % (apt_desc, apt_date) + ", OneTime Appointment")

class Daily(Appointment):
     def __init__(self, description, date):
        super().__init__(description, date)

     def occursOn(self, year, month, day):
         apt_desc = self.getAptDesc()
         print("Appointment: ", apt_desc)

     def printAptDetails(self):
        apt_date = self.getAptDate()
        apt_desc = self.getAptDesc()
        print(apt_desc + ", Daily Appointment")

class Monthly(Appointment):
     def __init__(self, description, date):
        super().__init__(description, date)

     def occursOn(self, year, month, day):
         apt_date = self.getAptDate()
         apt_desc = self.getAptDesc()
         if apt_date[2:4] == day :
             print("Appointment: ", apt_desc)

     def printAptDetails(self):
        apt_date = self.getAptDate()
        apt_desc = self.getAptDesc()
        print("%s, %s" % (apt_desc, apt_date) + ", Monthly Appointment")


class main():
    def __init__(self):
        self._Apt = []

    def addAppointment(self, apttype, description, date):
        if apttype == "onetime":
            self._Apt.append(oneTime(description, date))
        elif apttype == "daily":
            self._Apt.append(Daily(description, "daily"))
        elif apttype == "monthly":
            self._Apt.append(Monthly(description, date))
            
    def getAptList(self):
        return self._Apt


    
choice = str(input("\nPlease enter choice:\n1. Check Appointments\n2. Add daily appointment\n3. Add Onetime appointment\n4. Add Monthly appointment\n5. Exit\nChoice:"))
ans = True
a = main()
while ans :
    if choice == '1' :              
        input_date = str(input("\nPlease enter a date (MMDDYY) to list your scheduled appointments on that date: "))
        Apt1 = a.getAptList()
        Apt_found = False 
        for i in range(len(Apt1)):
            Apt1[i].occursOn(input_date[4:], input_date[0:2], input_date[2:4])
            Apt_found = True
        if not Apt_found :
            print("No Appointments scheduled for the input date")
        choice = str(input("\nPlease enter another choice: "))
    elif choice == '2' :
        description = str(input("Please enter the appointment decription: "))
        date = str(input("Please enter the appointment date: "))
        apttype = "daily"
        #a = main()
        a.addAppointment(apttype, description, date)
        choice = str(input("\nPlease enter another choice: "))
    elif  choice == '3' :
        description = str(input("Please enter the appointment decription: "))
        date = str(input("Please enter the appointment date: "))
        apttype = "onetime"
        #a = main()
        a.addAppointment(apttype, description, date)
        choice = str(input("\nPlease enter another choice: "))
    elif  choice == '4' :
        description = str(input("Please enter the appointment decription: "))
        date = str(input("Please enter the appointment date: "))
        apttype = "monthly"
        #a = main()
        a.addAppointment(apttype, description, date)
        choice = str(input("\nPlease enter another choice: "))
    elif choice == '5' :
        ans = False
    else :
        ans = False
       
           
            
    

    
