from faker import Faker
from datetime import datetime


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
        return fakeInt

    def genUrl(self):
        fakeUrl = self.faker.image_url()
        return fakeUrl

    def genActive(self):
        fakeActive = self.faker.pybool()
        return fakeActive

    def genTicketId(self):
        fakeTicket = self.faker.bothify(text="??##?-###???-?##?")
        return fakeTicket

    def genDescription(self):
        fakeDescription = self.faker.paragraph(nb_sentences=1)
        return fakeDescription

    def genDate(self):
        fakeDate = self.faker.date_between(datetime(2022, 1, 1))
        return str(fakeDate)
