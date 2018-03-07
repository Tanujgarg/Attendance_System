from cse.models import *
from cse.Files.Form_data import *


# class TotalLectures:
#     def __init__(self, roll_no):
#         self.wt_total = WT.objects.filter(roll_no=roll_no).all().count()
#         self.se_total = SE.objects.filter(roll_no=roll_no).all().count()
#         self.mc_total = MC.objects.filter(roll_no=roll_no).all().count()
#         self.cd_total = CD.objects.filter(roll_no=roll_no).all().count()
#         self.eit_total = EIT.objects.filter(roll_no=roll_no).all().count()
#         self.bie_total = BIE.objects.filter(roll_no=roll_no).all().count()
#         self.wt_lab_total = WTLab.objects.filter(roll_no=roll_no).all().count()
#         self.se_lab_total = SELab.objects.filter(roll_no=roll_no).all().count()
#         self.eit_lab_total = EITLab.objects.filter(roll_no=roll_no).all().count()


class DataByRollNo:
    def __init__(self, roll_no):
        wt = WT.objects.filter(roll_no=roll_no).all()
        cd = CD.objects.filter(roll_no=roll_no).all()
        mc = MC.objects.filter(roll_no=roll_no).all()
        eit = EIT.objects.filter(roll_no=roll_no).all()
        eit_lab = EITLab.objects.filter(roll_no=roll_no).all()
        se = SE.objects.filter(roll_no=roll_no).all()
        se_lab = SELab.objects.filter(roll_no=roll_no).all()
        bie = BIE.objects.filter(roll_no=roll_no).all()
        wt_lab = WTLab.objects.filter(roll_no=roll_no).all()

        self.wt_total = wt.count()
        self.wt_present = wt.filter(status=True).count()
        try:
            wt_avg = (self.wt_present / self.wt_total) * 100
            self.wt_avg = round(wt_avg, 2)
        except ZeroDivisionError:
            self.wt_avg = 'N.A.'

        self.cd_total = cd.count()
        self.cd_present = cd.filter(status=True).count()
        try:
            cd_avg = (self.cd_present / self.cd_total) * 100
            self.cd_avg = round(cd_avg, 2)
        except ZeroDivisionError:
            self.cd_avg = 'N.A.'

        self.mc_total = mc.count()
        self.mc_present = mc.filter(status=True).count()
        try:
            mc_avg = (self.mc_present / self.mc_total) * 100
            self.mc_avg = round(mc_avg, 2)
        except ZeroDivisionError:
            self.mc_avg = 'N.A.'

        self.eit_total = eit.count()
        self.eit_present = eit.filter(status=True).count()
        try:
            eit_avg = (self.eit_present / self.eit_total) * 100
            self.eit_avg = round(eit_avg, 2)
        except ZeroDivisionError:
            self.eit_avg = 'N.A.'

        self.se_total = se.count()
        self.se_present = se.filter(status=True).count()
        try:
            se_avg = (self.se_present / self.se_total) * 100
            self.se_avg = round(se_avg, 2)
        except ZeroDivisionError:
            self.se_avg = 'N.A.'

        self.bie_total = bie.count()
        self.bie_present = bie.filter(status=True).count()
        try:
            bie_avg = (self.bie_present / self.bie_total) * 100
            self.bie_avg = round(bie_avg, 2)
        except ZeroDivisionError:
            self.bie_avg = 'N.A.'

        self.wt_lab_total = wt_lab.count()
        self.wt_lab_present = wt_lab.filter(status=True).count()
        try:
            wt_lab_avg = (self.wt_lab_present / self.wt_lab_total) * 100
            self.wt_lab_avg = round(wt_lab_avg, 2)
        except ZeroDivisionError:
            self.wt_lab_avg = 'N.A.'

        self.se_lab_total = se_lab.count()
        self.se_lab_present = se_lab.filter(status=True).count()
        try:
            se_lab_avg = (self.se_lab_present / self.se_lab_total) * 100
            self.se_lab_avg = round(se_lab_avg, 2)
        except ZeroDivisionError:
            self.se_lab_avg = 'N.A.'

        self.eit_lab_total = eit_lab.count()
        self.eit_lab_present = eit_lab.filter(status=True).count()
        try:
            eit_lab_avg = (self.eit_lab_present / self.eit_lab_total) * 100
            self.eit_lab_avg = round(eit_lab_avg, 2)
        except ZeroDivisionError:
            self.eit_lab_avg = 'N.A.'





def total_lectures(roll_no):
    wt_total = []
    se_total = []
    mc_total = []
    cd_total = []
    eit_total = []
    bie_total = []
    wt_lab_total = []
    se_lab_total = []
    eit_lab_total = []
    a1 = DataByRollNo(roll_no)
    wt_total.append(a1.wt_total)
    se_total.append(a1.se_total)
    mc_total.append(a1.mc_total)
    cd_total.append(a1.cd_total)
    eit_total.append(a1.eit_total)
    bie_total.append(a1.bie_total)
    wt_lab_total.append(a1.wt_lab_total)
    se_lab_total.append(a1.se_lab_total)
    eit_lab_total.append(a1.eit_lab_total)
    return list(zip(wt_total, se_total, mc_total, bie_total, eit_total,
                    cd_total, wt_lab_total, se_lab_total, eit_lab_total))




def req_lectures(roll_no):
    wt_req1 = []
    se_req1 = []
    mc_req1 = []
    cd_req1 = []
    bie_req1 = []
    eit_req1 = []
    wt_lab_req1 = []
    se_lab_req1 = []
    eit_lab_req1 = []
    objct1 = DataByRollNo(roll_no)
    wt_r1 = objct1.wt_total * 0.75
    wt_req1.append(round(wt_r1, 2))
    se_r1 = objct1.se_total * 0.75
    se_req1.append(round(se_r1, 2))
    mc_r1 = objct1.mc_total * 0.75
    mc_req1.append(round(mc_r1, 2))
    cd_r1 = objct1.cd_total * 0.75
    cd_req1.append(round(cd_r1, 2))
    eit_r1 = objct1.eit_total * 0.75
    eit_req1.append(round(eit_r1, 2))
    bie_r1 = objct1.bie_total * 0.75
    bie_req1.append(round(bie_r1, 2))
    wt_lab_r1 = objct1.wt_lab_total * 0.75
    wt_lab_req1.append(round(wt_lab_r1, 2))
    se_lab_r1 = objct1.se_lab_total * 0.75
    se_lab_req1.append(round(se_lab_r1, 2))
    eit_lab_r1 = objct1.eit_lab_total * 0.75
    eit_lab_req1.append(round(eit_lab_r1, 2))

    return list(zip(wt_req1, se_req1, mc_req1, bie_req1, eit_req1, cd_req1,
                    wt_lab_req1, se_lab_req1, eit_lab_req1))




def present_and_avg(data):
    wt1 = []
    se1 = []
    mc1 = []
    cd1 = []
    bie1 = []
    eit1 = []
    wt_lab1 = []
    se_lab1 = []
    eit_lab1 = []
    wt_avg1 = []
    se_avg1 = []
    mc_avg1 = []
    cd_avg1 = []
    bie_avg1 = []
    eit_avg1 = []
    wt_lab_avg1 = []
    se_lab_avg1 = []
    eit_lab_avg1 = []
    for i in data:
        obj1 = DataByRollNo(i)
        wt1.append(obj1.wt_present)
        se1.append(obj1.se_present)
        mc1.append(obj1.mc_present)
        cd1.append(obj1.cd_present)
        bie1.append(obj1.bie_present)
        eit1.append(obj1.eit_present)
        wt_lab1.append(obj1.wt_lab_present)
        se_lab1.append(obj1.se_lab_present)
        eit_lab1.append(obj1.eit_lab_present)
        wt_avg1.append(obj1.wt_avg)
        se_avg1.append(obj1.se_avg)
        mc_avg1.append(obj1.mc_avg)
        cd_avg1.append(obj1.cd_avg)
        bie_avg1.append(obj1.bie_avg)
        eit_avg1.append(obj1.eit_avg)
        wt_lab_avg1.append(obj1.wt_lab_avg)
        se_lab_avg1.append(obj1.se_lab_avg)
        eit_lab_avg1.append(obj1.eit_lab_avg)
        # print(wt)
    return list(zip(data, wt1, wt_avg1, se1, se_avg1, mc1, mc_avg1, bie1, bie_avg1, eit1, eit_avg1, cd1,
                    cd_avg1, wt_lab1, wt_lab_avg1, se_lab1, se_lab_avg1, eit_lab1, eit_lab_avg1))


