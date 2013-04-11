from datetime import date

class BarcodeDate(date):

    def __str__(self):
        return "{}{}{}".format(self.year, self.month,self.day)

    def response_deadline(self):
        delta = datetime.timedelte(days=20)
        return (datetime.datetime.combine(self,datetime.time(0,0,0)) + delta).date()

print(dir(BarcodeDate))
