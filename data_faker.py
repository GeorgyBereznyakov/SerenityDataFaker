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
        hourInt = random.randint(1, 3)
        hour = hourInt
        return hour

    def setBackwards(self, time):
        pTime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f+00")
        dTime = pTime - timedelta(days=1)
        sTime = datetime.strftime(dTime, "%Y-%m-%d %H:%M:%S.%f")[:-4]
        sTime += "+00"
        return sTime

    def addTime(self, time, hour):
        pTime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f+00")
        dTime = pTime + timedelta(hours=hour)
        sTime = datetime.strftime(dTime, "%Y-%m-%d %H:%M:%S.%f")[:-4]
        sTime += "+00"
        return sTime
