import math
base_days = {"Mon": None , "Tue": None , "Wed": None , "Thurs": None ,"Fri": None , "Sat" : None, "Sun": None}
dday = base_days
class debt :
    def __init__(self,list,average):
        self.__list = list
        self.__avg = average
    def get_list(self):
        return self.__list
    def ask_debt(self):
        while True :
            call = input("What's your average sleep time per day (between 6-10)\n")
            try:
                if int(call) > 10 or int(call) < 6:
                    raise ValueError
                self.__avg = int(call)
                break
            except ValueError:
                print(f"{call} is unacceptable")
        print(f"this debt base on {call} hours")

        for i in self.__list :
            while True :
                ga = (input(f"{i}.sleeptime "))
                try:
                    if int(ga) > 24 :
                        raise ValueError
                    self.__list[i] = int(ga)
                    break
                except ValueError :
                    print(f"{ga} is unacceptable ,Please insert Integer")
    def cal_debt(self):
        c = 0
        a = 0
        for i in self.__list.values() :
            c = i-self.__avg
            a += c
        return int(a)
        # if a < 1 :
        #     return f"youhave{a}hourssleepdebt"
        # elif a > 25 :
        #     return f"Please do something else other than sleep"
        # elif a > 20 :
        #     return f"you have over sleep {a-20} hours"
        # else :
        #     return f"youhavenosleepdebt"


class sleep :
    def __init__(self, sleep,debt):
        self.__sleep = (sleep) #list
        self.__debt = int(debt)
    def set_sleep(self, new_sleep):
        self.__sleep = int(new_sleep)
    def get_sleep(self):
        return  self.__sleep
    def cal_sleep(self):
        d = -1 * int(self.__debt/9)
        # print("gggg",d,int(self.__sleep[0]) - (8+d),int(self.__sleep[0]) - (6+d),int(self.__sleep[0]) - (4+d))
        return int(self.__sleep[0]) - (8+d) , int(self.__sleep[0]) - (6+d) , int(self.__sleep[0]) - (4+d)
    def convert(self,agg):
        ll = []
        for i in agg :
            if 12 >= 12+i :
                ll.append(12+i)
            else:
                ll.append(i)
        return ll
class kkk:
    # def __init__(self,debt,sleep):
    #     self.__debt = debt
    #     self.__sleep = sleep
    def draw(self):
        print(
            " ____  _                 ____       _     _                     _ \n/ ___|| | ___  ___ _ __ |  _ \  ___| |__ | |_    __ _ _ __   __| |\n\___ \| |/ _ \/ _ \ '_ \| | | |/ _ \ '_ \| __|  / _` | '_ \ / _` |\n ___) | |  __/  __/ |_) | |_| |  __/ |_) | |_  | (_| | | | | (_| |\n"
            "|____/|_|\___|\___| .__/|____/ \___|_.__/ \__|  \__,_|_| |_|\__,_|\n/ ___|| | ___  ___|_|_|_   _(_)_ __ ___   ___    \n\___ \| |/ _ \/ _ \ '_ \| | | | '_ ` _ \ / _ \       \n ___) | |  __/  __/ |_) | | | | | | | | |  __/    \n"
            "|____/|_|\___|\___| .__/|_| |_|_| |_| |_|\___|        \n                  |_|             ")
        print("press [q] to quit  press [e] to start")
        while True :
            a = str(input())
            if a == "q" :
                quit()
            elif a == "e":
                break

    def PpDebt(self,debt):
        while True :
            a = debt
            a.ask_debt()
            k = a.cal_debt()
            if k < 0:
                print(f"you have {-1 * k} hours of sleepdebt")
                break
            elif k > 25:
                print(f"Please do something else other than sleep")
                dday = base_days
            elif k > 20:
                print(f"you have over sleep {k - 20} hours")
                break
            else:
                print(f"you haveno sleep debt")
                break
    def sleep_time(self):
        while True :
            try:
                usi = (input("insert time with(:) "))
                if ":" not in str(usi) or len(usi) > 5 :
                    raise ValueError
                else:
                    p = usi.split(":")
                if int(p[0]) <= 12 and int(p[0]) > 0 and int(p[1]) <= 60 and int(p[1]) >= 0:
                    if int(p[0][0]) == 0 :
                        p[0] = p[0][1]
                    break
            except ValueError:
                print("try another")
        return p
    def print_result(self,time,debt,sleep):
        print(f"If you wan't to awake at {time[0]}:{time[1]} you must be sleep at", end="")
        for i in sleep :
            print( f" {i}:{time[1]} p.m. ,", end = "")
        print(f"\n with your {-1*debt} sleep debt")

    def run(self):
        d = debt(dday,0)
        self.draw()
        self.PpDebt(d)
        # print(d.get_list())
        time = self.sleep_time()
        a = d.cal_debt()
        rr = sleep(time,a)
        rr.cal_sleep()
        p = rr.convert(rr.cal_sleep())
        self.print_result(time,a,p)
a = kkk()
a.run()
# a.run()

# draw()
# while True :
#     a = str(input())
#     if a == "q" :
#         quit()
#     elif a == "e":
#         break
#
# debt_1 = debt(dday,0)
# debt_1.ask_debt()
# PpDebt(debt_1)
# sleep = cal_sleep(9,debt_1.cal_debt())
# quit()
# q = run()
# q.draw()
# q.PpDebt()






#
# while True :
#
#
