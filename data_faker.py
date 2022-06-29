from faker import Faker
from datetime import datetime, timedelta
import random
import re


class data_faker:
    def __init__(self):
        self.faker = Faker()

    def genName(self):
        fakeName = self.faker.name()
        return fakeName

    def genEmail(self):
        fakeMail = self.faker.email()
        return fakeMail

    def genInt(self, start, end, iterate):
        fakeInt = self.faker.pyint(start, end, iterate)
        return str(fakeInt)

    def genUrl(self):
        fakeUrl = self.faker.image_url()
        return fakeUrl

    def genActive(self):
        fakeActive = self.faker.pybool()
        return fakeActive

    def genDescription(self):
        fakeDescription = self.faker.paragraph(nb_sentences=1)
        return fakeDescription

    def genDate(self):
        fakeDate = self.faker.date_between(datetime(2022, 1, 1))
        return str(fakeDate)

    def genBothify(self, format):
        fakeString = self.faker.bothify(text=format)
        return fakeString

    def currentTime(self):
        todayDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]
        todayDate += "+00"
        return todayDate

    def genRandomHour(self):
        hourInt = random.randint(1, 8)
        hour = hourInt
        return hour

    def setBackwards(self, time):
        pTime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f+00")
        dTime = pTime - timedelta(days=7)
        sTime = datetime.strftime(dTime, "%Y-%m-%d %H:%M:%S.%f")[:-4]
        sTime += "+00"
        return sTime

    def addTime(self, time, hour):
        pTime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f+00")
        dTime = pTime + timedelta(hours=hour)
        sTime = datetime.strftime(dTime, "%Y-%m-%d %H:%M:%S.%f")[:-4]
        sTime += "+00"
        return sTime

    def checkDay(self, time):
        day = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f+00")
        weekend = False
        if day.weekday() == 5 or day.weekday() == 6:
            weekend = True

        while weekend:
            day += timedelta(days=1)
            if day.weekday() != 5 and day.weekday() != 6:
                weekend = False

        sTime = datetime.strftime(day, "%Y-%m-%d %H:%M:%S.%f")[:-4]
        sTime += "+00"
        return sTime

    def check_work_time(self, time):
        shift_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f+00")
        clock_off = False
        if shift_time.hour < 9 or shift_time.hour >= 17:
            clock_off = True

        while clock_off:
            if shift_time.hour < 9:
                shift_time += timedelta(hours=1)
            if shift_time.hour >= 17:
                shift_time += timedelta(hours=16)
            if shift_time.hour > 9 and shift_time.hour < 17:
                clock_off = False

        sTime = datetime.strftime(shift_time, "%Y-%m-%d %H:%M:%S.%f")[:-4]
        sTime += "+00"
        return sTime
