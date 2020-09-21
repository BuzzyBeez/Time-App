from datetime import datetime

class GettingTime:

    def __init__(self):
        self.now = datetime.now()

    def time_stamp(self):
        string_time = self.now.strftime("\n%A\n%m/%d/%Y\n%I:%M:%S\n")

        # print(stringTime)
        return string_time


# run = GettingTime()
# run.time_stamp()