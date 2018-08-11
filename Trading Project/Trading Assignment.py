import datetime
import csv
import os


class PerformanceData :

   def __init__(self, date, open1, high, low, close, volume, adj_close):
      self._date = date
      self._open = open1
      self._close = close
      self._high = high
      self._low = low
      self._volume = volume
      self._adj_close = adj_close
      self._str = ""

   
   def __str__(self) :
      self._str = 'date: {} Open: {} High: {} Low: {} Close: {} Volume: {}'.format(self._date, self._open, self._high, self._low, self._close, self._volume, self._adj_close)


   def getdata(self) :
      self.__str__()
      return self._str

   def getDate(self) :
      return self._date
   
   def getOpen(self) :
      return self._open

   def getHigh(self) :
      return self._high

   def getLow(self) :
      return self._low

   def getClose(self) :
      return self._close

   def getVolume(self) :
      return self._volume

   def getAdjClose(self) :
      return self._adj_close

   

class TransactionHistory :

   def __init__(self, filename) :
      self._filename = filename
      self._csvfile = csv.reader(open(filename,'r'))
      self._open = ""
      self._close = ""
      self._high = ""
      self._low = ""
      self._file_list = []
      for row in self._csvfile:
         x = PerformanceData(row[0],row[1],row[2],row[3], row[4],row[5],row[6])
         file_list1 = [x.getDate(),x.getOpen(),x.getHigh(),x.getLow(),x.getClose(),x.getVolume(),x.getAdjClose()]
         self._file_list.append(file_list1)
      self._file_list.reverse()
                  
         
                        

   def gethistory(self, daynum) :
      return self._file_list[daynum]
        

class TransactionHistoryDriver :    

      def __init__(self, filename, daynum) :
         _obj = TransactionHistory(filename)
         _obj.gethistory(daynum)


class MarketSimulation :

   def __init__(self, filename, buy_price, sell_price, currentDay) :
      self._currentDay = currentDay
      self._filename = filename
      self._date = ""
      self._open = ""
      self._close = ""
      self._high = ""
      self._low = ""
      self._volume = ""
      self._buy_price = buy_price
      self._sell_price = sell_price
      
      

   def getYesterDaysClosingData(self):
      trans_hist_obj = TransactionHistory(self._filename)
      yest_trade = trans_hist_obj.gethistory(self._currentDay - 1)
      if choice == '3' :
         print(yest_trade[0]," ",yest_trade[3]," - ",yest_trade[2])
      self._open = yest_trade[1]
      self._close = yest_trade[4]
      self._high = yest_trade[2]
      self._low = yest_trade[3]
      
   def executableBuyTrade(self):
      if self._buy_price >= 0 :
         if self._buy_price >= float(self._low) :
            #print("A buy trade could go through as the offer to buy price ", self._buy_price, " is greater than the low price for the day ", self._low)
            return True
         else :
            #print("A buy trade could NOT go through as the offer to buy price ", self._buy_price, " is lesser than the low price for the day ", self._low)
            print("Trade Executed:  False")
            return False

   def executableSellTrade(self):
      if self._sell_price >= 0 :
         if self._sell_price <= float(self._high) :
            #print("Sell can go through as the offer to sell price ", self._sell_price, " is less than the high of the day ", self._high)
            return True      
         else :
            #print("Sell CANNOT go through as the offer to sell price ", self._sell_price, " is greater than the high of the day ", self._high)
            print("Trade Executed:  False")
            return False

   def advanceDay(self):
       print("Current Day value: ", self._currentDay)
       self._currentDay += 1
       global currentDay
       currentDay = self._currentDay
       print("Advanced Day value: ", currentDay)


class MarketSimulationDriver :
   def __init__(self, filename, buy_price, sell_price, currentDay) :
         self._simulationobj = MarketSimulation(filename, buy_price, sell_price, currentDay)                                          
         self._simulationobj.getYesterDaysClosingData()
         self._simulationobj.executableBuyTrade()
         self._simulationobj.executableSellTrade()
         self._simulationobj.advanceDay()
         


class Trade :
   def __init__(self, filename, trade_type, shares, offer_price, init_balance, curr_holding, currentDay, trade_symbol) :
      self._ticker = 'T'
      self._filename = filename
      self._trade_type = trade_type
      self._shares = shares
      self._trade_symbol = trade_symbol
      self._offer_price = offer_price
      self._init_balance = init_balance
      self._curr_holding = curr_holding
      self._currentDay = currentDay
      if trade_type == "Buy" :
         self._buy_price = offer_price
         self._sell_price = 0
      else :
         self._sell_price = offer_price
         self._buy_price = 0
      
       
            
   def buytrade(self):
      buytrade_obj = MarketSimulation(self._filename, self._buy_price, self._sell_price, self._currentDay)
      buytrade_obj.getYesterDaysClosingData()
      buytrade_return = buytrade_obj.executableBuyTrade()
      if buytrade_return == True :
         if self._init_balance >= self._shares * self._buy_price :      
            print("Trade Executed:  True")
            global init_balance
            self._init_balance = self._init_balance - ( self._shares * self._buy_price)
            global curr_holding
            self._curr_holding = self._curr_holding + self._shares
            init_balance = self._init_balance
            curr_holding = self._curr_holding
            #self._currentDay += 1
            global currentDay
            currentDay = self._currentDay
            curr_trade_list = [self._trade_symbol,"Buy",self._shares,self._buy_price]
            global trade_completed
            trade_completed.append(curr_trade_list)
         else :
            print("Trade Executed:  False")

   def selltrade(self):
          selltrade_obj = MarketSimulation(self._filename, self._buy_price, self._sell_price, self._currentDay)
          selltrade_obj.getYesterDaysClosingData()
          selltrade_return = selltrade_obj.executableSellTrade()
          if selltrade_return == True :
             if self._init_balance >= self._shares * self._sell_price :            
                print("Trade Executed:  True")
                global init_balance
                self._init_balance = self._init_balance + (self._shares * self._sell_price)
                global curr_holding
                self._curr_holding = self._curr_holding - self._shares
                init_balance = self._init_balance
                curr_holding = self._curr_holding
                #self._currentDay += 1
                global currentDay
                currentDay = self._currentDay
                curr_trade_list = [self._trade_symbol,"Sell",self._shares,self._sell_price]
                global trade_completed
                trade_completed.append(curr_trade_list)
             else :
                print("Trade Executed:  False")

    
      


class Account :
       def __init__(self, filename, offer_price, init_balance, trade_type, shares, curr_holding, currentDay, trade_symbol) :
          self._init_balance = init_balance
          self._filename = filename
          self._offer_price = offer_price
          self._holding = curr_holding
          self._trade_type = trade_type
          self._shares = shares
          self._trade_symbol = trade_symbol
          self._currentDay = currentDay          
          if choice == '1' or choice == '2' :
             trade_obj = Trade(filename, self._trade_type, self._shares, self._offer_price, self._init_balance, self._holding, self._currentDay, self._trade_symbol)          
             if self._trade_type == 'Buy' :
                self._trade_return = trade_obj.buytrade()
             else :
                self._trade_return = trade_obj.selltrade()
                                

       def printAccountStatement(self):     
          global init_balance
          global curr_holding
          global trade_completed
          print("Balance: ", init_balance)
          print("Holding: ", curr_holding)
          print("Trade Completed: ", trade_completed)
          
          

class AccountDriver :
   def __init__(self, filename, offer_price, init_balance, trade_type, shares, curr_holding, currentDay, trade_symbol) :
      self._filename = filename
      self._offer_price = offer_price
      self._init_balance = init_balance
      accountdriver_obj = Account(filename, offer_price, init_balance, trade_type, shares, curr_holding, currentDay, trade_symbol)
      accountdriver_obj.buytrade()
      accountdriver_obj.selltrade()
      accountdriver_obj.printAccountStatement()
      
     
working_dir = os.getcwd()
filepath = working_dir + "\\T.csv"

init_balance = float(input("Enter the initial balance: "))
curr_holding = 0
currentDay = 1
trade_completed = []

choice = str(input("Please enter choice:\n1. Buy\n2. Sell\n3. Yesterday Price Range\n4. Advance Day\n9. Print Statement\n99. Done\nChoice:"))
ans = True
while ans :
   if choice == '1' :
      symbol = str(input("Symbol: "))
      shares = int(input("Shares: "))
      offer_price = float(input("Offer Price: "))
      print("Trade: ",symbol.upper(),",Buy, ",shares,", ", offer_price)
      Account(filepath, offer_price, init_balance, "Buy", shares, curr_holding, currentDay, symbol.upper())
      choice = str(input("Please enter choice:"))
   elif choice == '2' :
      symbol = str(input("Symbol: "))
      shares = int(input("Shares: "))
      offer_price = float(input("Offer Price: "))
      print("Trade: ",symbol.upper(),",Sell,",shares,",", offer_price) 
      Account(filepath, offer_price, init_balance, "Sell", shares, curr_holding, currentDay, symbol.upper())
      choice = str(input("Please enter choice:"))
   elif choice == '9' :
      offer_price = 0
      acc_driver_obj = Account(filepath, offer_price, init_balance, "", 0, curr_holding, currentDay, "")
      acc_driver_obj.printAccountStatement()
      choice = str(input("Please enter choice:"))
   elif choice == '3' :
      print("Yesterday's price range: ")
      buy_price = 0
      sell_price = 0
      market_simulation_obj = MarketSimulation(filepath, buy_price, sell_price, currentDay)
      market_simulation_obj.getYesterDaysClosingData()
      choice = str(input("Please enter choice:"))
   elif choice == '4' :
      market_simulation_obj = MarketSimulation(filepath, buy_price, sell_price, currentDay)
      market_simulation_obj.advanceDay()
      choice = str(input("Please enter choice:"))
   elif choice == '99' :
      ans = False
   else :
      ans = False
      
      
   
   
                  

   
   
   
   

   
   












         
