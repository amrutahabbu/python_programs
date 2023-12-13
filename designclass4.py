import time

class Time:
    def __init__(self,current_hour,current_minutes,current_seconds):

         self.__hour = current_hour
         self.__min = current_minutes
         self.__sec = current_seconds

    def getSeconds(self):
        return self.__sec
    def gethour(self):
        return self.__hour
    def getMinutes(self):
        return self.__min

    def setTime(self,elapsedTime):

            total_seconds = elapsedTime
            self.__second = total_seconds % 60
            total_seconds //= 60
            self.__minute = total_seconds % 60
            total_seconds //= 60
            self.__hour = total_seconds % 24


currentTime = int(time.time())
curr_seconds = currentTime % 60
minutes = currentTime // 60
curr_minutes = minutes % 60
hours = minutes // 24
curr_hour = hours % 24

timeClass = Time(curr_hour,curr_minutes,curr_seconds)
timeClass.setTime(5550000)
print("Elapsedtime = ",timeClass.gethour(),":",timeClass.getMinutes(),":",timeClass.getSeconds())
