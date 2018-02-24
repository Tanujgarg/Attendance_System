from cse.models import *
import cse.Files.Form_data


# def data_by_roll_no(roll_no):
#
#     wt = WT.objects.filter(roll_no=roll_no).all()
#     cd = CD.objects.filter(roll_no=roll_no).all()
#     mc = MC.objects.filter(roll_no=roll_no).all()
#     eit = EIT.objects.filter(roll_no=roll_no).all()
#     eit_lab = EITLab.objects.filter(roll_no=roll_no).all()
#     se = SE.objects.filter(roll_no=roll_no).all()
#     se_lab = SELab.objects.filter(roll_no=roll_no).all()
#     bie = BIE.objects.filter(roll_no=roll_no).all()
#     wt_lab = WTLab.objects.filter(roll_no=roll_no).all()
#
#     wt_total = wt.count()
#     wt_present = wt.filter(status=True).count()
#     try:
#         wt_avg = (wt_present / wt_total) * 100
#         wt_avg = round(wt_avg, 2)
#     except ZeroDivisionError:
#         wt_avg = 'N.A.'
#
#     cd_total = cd.count()
#     cd_present = cd.filter(status=True).count()
#     try:
#         cd_avg = (cd_present / cd_total) * 100
#         cd_avg = round(cd_avg, 2)
#     except ZeroDivisionError:
#         cd_avg = 'N.A.'
#
#     mc_total = mc.count()
#     mc_present = mc.filter(status=True).count()
#     try:
#         mc_avg = (mc_present / mc_total) * 100
#         mc_avg = round(mc_avg, 2)
#     except ZeroDivisionError:
#         mc_avg = 'N.A.'
#
#     eit_total = eit.count()
#     eit_present = eit.filter(status=True).count()
#     try:
#         eit_avg = (eit_present / eit_total) * 100
#         eit_avg = round(eit_avg, 2)
#     except ZeroDivisionError:
#         eit_avg = 'N.A.'
#
#     se_total = se.count()
#     se_present = se.filter(status=True).count()
#     try:
#         se_avg = (se_present / se_total) * 100
#         se_avg = round(se_avg, 2)
#     except ZeroDivisionError:
#         se_avg = 'N.A.'
#
#     bie_total = bie.count()
#     bie_present = bie.filter(status=True).count()
#     try:
#         bie_avg = (bie_present / bie_total) * 100
#         bie_avg = round(bie_avg, 2)
#     except ZeroDivisionError:
#         bie_avg = 'N.A.'
#
#     wt_lab_total = wt_lab.count()
#     wt_lab_present = wt_lab.filter(status=True).count()
#     try:
#         wt_lab_avg = (wt_lab_present / wt_lab_total) * 100
#         wt_lab_avg = round(wt_lab_avg, 2)
#     except ZeroDivisionError:
#         wt_lab_avg = 'N.A.'
#
#     se_lab_total = se_lab.count()
#     se_lab_present = se_lab.filter(status=True).count()
#     try:
#         se_lab_avg = (se_lab_present / se_lab_total) * 100
#         se_lab_avg = round(se_lab_avg, 2)
#     except ZeroDivisionError:
#         se_lab_avg = 'N.A.'
#
#     eit_lab_total = eit_lab.count()
#     eit_lab_present = eit_lab.filter(status=True).count()
#     try:
#         eit_lab_avg = (eit_lab_present / eit_lab_total) * 100
#         eit_lab_avg = round(eit_lab_avg, 2)
#     except ZeroDivisionError:
#         eit_lab_avg = 'N.A.'
#     return {
#         'wt_total': wt_total,
#         'wt_present': wt_present,
#
#     }


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


objct = DataByRollNo(6315010)
wt_r = objct.wt_total * 0.75
wt_req = round(wt_r, 2)
se_r = objct.se_total * 0.75
se_req = round(se_r, 2)
mc_r = objct.mc_total * 0.75
mc_req = round(mc_r, 2)
cd_r = objct.cd_total * 0.75
cd_req = round(cd_r, 2)
eit_r = objct.eit_total * 0.75
eit_req = round(eit_r, 2)
bie_r = objct.bie_total * 0.75
bie_req = round(bie_r, 2)
wt_lab_r = objct.wt_lab_total * 0.75
wt_lab_req = round(wt_lab_r, 2)
se_lab_r = objct.se_lab_total * 0.75
se_lab_req = round(se_lab_r, 2)
eit_lab_r = objct.eit_lab_total * 0.75
eit_lab_req = round(eit_lab_r, 2)

wt_total = objct.wt_total
se_total = objct.se_total
mc_total = objct.mc_total
cd_total = objct.cd_total
eit_total = objct.eit_total
bie_total = objct.bie_total
wt_lab_total = objct.wt_lab_total
se_lab_total = objct.se_lab_total
eit_lab_total = objct.eit_lab_total


