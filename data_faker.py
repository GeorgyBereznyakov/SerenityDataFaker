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
        todayDate = ""
        todayDate += datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]
        todayDate += "+00"
        return todayDate

    def genRandomHour(self):
        hourInt = random.randint(1, 3)
        hour = hourInt
        return hour

    def addTimeString(self, currentTime, hour):
        match = re.search(r"\d\d\d\d-", currentTime)
        currentYear = int(match.group().strip("-"))
        # print(currentYear)

        match = re.search(r"-\d\d-", currentTime)
        currentMonth = int(match.group().strip("-"))
        # print(currentMonth)

        match = re.search(r"-\d\d\s", currentTime)
        currentDay = int(match.group().strip("-"))
        # print(currentDay)

        match = re.search(r"\s\d\d", currentTime)
        currentHour = int(match.group())
        # print(currentHour)

        match = re.search(r":\d\d:", currentTime)
        currentMinute = int(match.group().strip(":"))
        # print(currentMinute)

        match = re.search(r":\d\d\.", currentTime)
        currentSecond = int(match.group().strip(":").strip("."))
        # print(currentSecond)

        currentHour += hour

        if currentHour > 9:
            newHour = " " + str(currentHour)
            newTime = re.sub(r"\s\d\d", newHour, currentTime)
        else:
            newHour = " 0" + str(currentHour)
            newTime = re.sub(r"\s\d\d", newHour, currentTime)
        if currentHour >= 24:
            currentDay += 1
            currentHour = 0
            newHour = " 0" + str(currentHour)
            newTime = re.sub(r"\s\d\d", newHour, currentTime)
            if currentDay > 9:
                day = "-" + str(currentDay) + " "
                newTime = re.sub(r"-\d\d\s", day, newTime)
            else:
                day = "-0" + str(currentDay) + " "
                newTime = re.sub(r"-\d\d\s", day, newTime)
        # print(newTime)
        return newTime


# df = data_faker()
# print(df.todaysDate())
