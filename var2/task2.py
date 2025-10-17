class HourClock:
    def __init__(self, hours):
        self.hours = hours
        
    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self,value):
        if not  isinstance(value, int) or not 1 <= value <= 12:
            raise ValueError('Некорректное время')
        self._hours = value
         
time = HourClock(7) 
#1
print(time.hours)  
time.hours = 9 
print(time.hours)
#2
try: 
    time.hours = 15
except ValueError as e: 
    print(e) 
#3   
try: 
    HourClock('pizza time 🕷') 
except ValueError as e: 
    print(e)

    