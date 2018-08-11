#P10.22

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
       


    
Apt = []
Apt1 = oneTime("Travel India", "081217")
Apt.append(Apt1)
Apt2 = Daily("Church", "daily")
Apt.append(Apt2)
Apt3 = Monthly("Visit Dentist", "072017")
Apt.append(Apt3)
Apt4 = oneTime("Lawyer Appointment", "082017")
Apt.append(Apt4)
Apt5 = Daily("Daily Status meeting", "daily")
Apt.append(Apt5)
Apt6= Monthly("Settle Bills", "083017")
Apt.append(Apt6)


print("\nListed below are your currently scheduled appointments: \n")
for i in range(len(Apt)):
    Apt[i].printAptDetails()

choice = str(input("\nPlease enter choice:\n1. Check Appointments\n2. Exit\nChoice:"))
ans = True
while ans :
    if choice == '1' :
        input_date = str(input("\nPlease enter a date (MMDDYY) to list your scheduled appointments on that date: "))
        for i in range(len(Apt)):
            Apt[i].occursOn(input_date[4:], input_date[0:2], input_date[2:4])
        choice = str(input("\nPlease enter choice:\n1. Check Appointments\n2. Exit\nChoice:"))
    elif choice == '2' :
        ans = False
    else :
        ans = False
       
           
            
    

    
