#!/usr/bin/python
"""nclsutil.py

Usage:  nslcutil.py (-f | --2xlsx    ) <ifile> <ofile>
        nslcutil.py (-c | --testcsv  ) <ifile> <logfile>
        nslcutil.py (-x | --testxls  ) <ifile> <logfile>
        nslcutil.py (-s | --tespace  ) <ifile> <logfile>    
        nslcutil.py (-t | --testtab  ) <ifile> <logfile>
        nslcutil.py (-m | --transmit ) <ifile>
        nslcutil.py (-h | --details  )
        nslcutil.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
import os
import re
import sys
import stat
import subprocess
import signal
import time
import io
import csv
import string
#W import openpyxl
from docopt import docopt
#
from subprocess import call
#
# Boilerplate imports for Python 2 / Python 3 mutual compatiibility
#
# from __future__ import print_function  # Make print a function
#W from six.moves  import input           # Use raw_input when I say input
from os.path    import expanduser      # Cross-platform home directory finder
#
# This slug is based upon the work of Kevin Cole... 
__author__     = "Flint"
__copyright__  = "Copyright 2016, Goddard College (02/01/2016)"
__credits__    = ["Flint"]  # Authors and bug reporters
__license__    = "GPL I"
__version__    = "0.07"
__maintainer__ = "Flint"
__email__      = "flint@flint.com"
__status__     = "Development"  # "Prototype", "Development" or "Production"
__appname__    = "NSLC file utililty"
#
# Load Globals
# global alfadefs
#
# Load landers
# Column for Excel Format Index 
length = 0 
start = 1 
stop = 2
reqd = 3
dtype = 4
fieldname = 6
count = 7
spreadsheet = "example.xlsx"
csvfile = "example.csv"
#
    # print "Counting the header we are currently at line "+str(D1.Line)+" of the spreadsheet: "+spreadsheet
#

class header:
    def __init__(self):
        self.Column_for_Excel_Format = "Length,Start,Stop,Reqd,Type"
        def Record_Type(self): 
                return ("A,2,1,2,R,AN")
        def School_Code(self): 
                return ("B,6,3,8,R,N")
        def Branch_Code(self): 
                return ("C,2,9,10,R,N")
        def Academic_Term(self): 
                return ("D,15,11,25,R,AN")
        def Standard_Report_Flag(self): 
                return ("E,1,26,26,R,A")
        def Certification_Date(self): 
                return ("F,8,27,34,R,N")
        def Reporting_Level(self): 
                return ("G,1,35,35,R,A")
        def Filler(self): 
                return ("H,1215,36,1250,R,AN")
#
h1=header()
#
class drl:
    Line = 2    # starting line for data
    def __init__(self):
        self.Column_for_Excel_Format = "Index,Length,Start,Stop,Reqd,Type,Field Name,Count"
    def hi(self):
        fm = " From Object Land..."
        return 'Hello World'+fm
    def IND__Column_for_Excel_Format(self): 
        return ("Index,Length,Start,Stop,Reqd,Type,Field_Name,Count")
# Start first Alpha 
    def A0ARecord_Type(self): 
        return ("2,1,2,R,AN,AN,A,1")
    def A0BStudent_SSN(self): 
        return ("9,3,11,R,N,N,B,2")
    def A0CFirst_Name(self): 
        return ("20,12,31,R,AN,AN,C,3")
    def A0DMiddle_Initial(self): 
        return ("1,32,32,O,AN,AN,D,4")
    def A0ELast_Name(self): 
        return ("20,33,52,R,AN,AN,E,5")
    def A0FName_Suffix(self): 
        return ("5,53,57,O,AN,AN,F,6")
    def A0GPrevious_SSN(self): 
        return ("9,58,66,O,N,N,G,7")
    def A0HPrevious_Last_Name(self): 
        return ("20,67,86,O,AN,AN,H,8")
    def A0IDegree_Concentration(self): 
        return ("9,1,87,87,R,A,I,9")
    def A0JEnrollment_Status(self): 
        return ("1,87,87,R,A,N,J,10")
    def A0KStatus_Start_Date(self): 
        return ("8,88,95,C,N,AN,K,11")
    def A0LStreet_Line_1(self): 
        return ("30,96,125,R,AN,AN,L,12")
    def A0MStreet_Line_2(self): 
        return ("30,126,155,O,AN,A,M,13")
    def A0NCity(self): 
        return ("20,156,175,R,A,A,N,14")
    def A0OState(self): 
        return ("2,176,177,R,A,AN,O,15")
    def A0PZip(self): 
        return ("9,178,186,C,AN,AN,P,16")
    def A0QCountry(self): 
        return ("15,187,201,C,AN,N,Q,17")
    def A0RAnticipated_Graduation_Date(self): 
        return ("8,202,209,C,N,N,R,18")
    def A0SDate_of_Birth(self): 
        return ("8,210,217,R,N,N,S,19")
    def A0TTerm_Begin_Date(self): 
        return ("8,218,225,R,N,N,T,20")
    def A0UTerm_End_Date(self): 
        return ("8,226,233,R,N,AN,U,21")
    def A0VFiller(self): 
        return ("1,234,234,R,AN,A,V,22")
    def A0WDirectory_Block_Indicator(self): 
        return ("1,235,235,R,A,N,W,23")
    def A0XNCES_CIP_Code_for_Major_1(self): 
        return ("6,236,241,O,N,N,X,24")
    def A0YNCES_CIP_Code_for_Major_2(self): 
        return ("6,242,247,O,N,AN,Y,25")
    def A0ZMajor_Course_of_Study_1(self): 
        return ("80,248,327,O,AN,AN,Z,26") 
# end first alpha
    def AA_Major_Course_of_Study_2(self):
        return ("80,328,407,O,AN,A,AA,27")
    def AB_Class_Credential(self): 
        return ("1,408,408,C,A,A,AB,28")
    def AC_First_Time_Full_Time(self): 
        return ("1,409,409,O,A,A,AC,29")
    def AD_Degree_Seeking(self): 
        return ("1,410,410,O,A,N,AD,30")
    def AE_High_School_Code(self): 
        return ("6,411,416,O,N,A,AE,31")
    def AF_Gender(self): 
        return ("1,417,417,O,A,A,AF,32")
    def AG_Race_Ethnicity(self): 
        return ("2,418,419,O,A,AN,AG,33")
    def AH_College_Student_ID(self): 
        return ("20,420,439,O,AN,AN,AH,34")
    def AI_State_Student_ID(self): 
        return ("30,440,469,O,AN,AN,AI,35")
    def AJ_Email(self): 
        return ("128,470,597,O,AN,A,AJ,36")
    def AK_Good_Student(self): 
        return ("1,598,598,O,A,AN,AK,37")
    def AL_Middle_Name(self): 
        return ("35,599,633,O,AN,A,AL,38")
    def AM_Veterans_Status_Indicator_(self): 
        return ("1,634,634,O,A,AN,AM,39")
    def AN_Reserved_for_CommIT_ID(self): 
        return ("12,635,646,O,AN,A,AN,40")
    def AO_Pell_Grant_Recipient_Flag(self): 
        return ("1,647,647,O,A,A,AO,41")
    def AP_Remedial_Flag(self): 
        return ("1,648,648,O,A,A,AP,42")
    def AQ_Citizenship_Flag(self): 
        return ("1,649,649,O,A,A,AQ,43")
    def AR_Student_Phone_Type(self): 
        return ("1,650,650,O,A,A,AR,44")
    def AS_Preferred_Phone_Number_Flag(self): 
        return ("1,651,651,O,A,N,AS,45")
    def AT_Student_Phone_Country_Code(self): 
        return ("3,652,654,O,N,N,AT,46")
    def AU_Student_Phone_Number(self): 
        return ("11,655,665,O,N,N,AU,47")
    def AV_Reserved_for_Move_To_OPEID_Future_CH_Functionality(self): 
        return ("8,666,673,O,N,A,AV,48")
    def AW_Program_Indicator(self): 
        return ("1,674,674,R,A,N,AW,49")
    def AX_Program_1_CIP_Code(self): 
        return ("6,675,680,C,N,N,AX,50")
    def AY_CIP_Year(self): 
        return ("4,681,684,C,N,N,AY,51")
    def AZ_Program_1_Credential_Level(self): 
        return ("2,685,686,C,N,N,AZ,52")
    def BA_Published_Program_1_Length(self): 
        return ("6,687,692,C,N,A,BA,53")
    def BB_Published_Program_1_Length_Measurement(self): 
        return ("1,693,693,C,A,N,BB,54")
    def BC_Weeks_Program_1_Title_IV_Academic_Year(self): 
        return ("6,694,699,C,N,N,BC,55")
    def BD_Program_1_Begin_Date(self): 
        return ("8,700,707,C,N,A,BD,56")
    def BE_Special_Program_Indicator(self): 
        return ("1,708,708,C,A,A0XNCES_CIP_Code_for_Major_1A,BE,57")
    def BF_Program_1_Enrollment_Status(self): 
        return ("1,709,709,C,A,N,BF,58")
    def BG_Program_1_Enrollment_Status_Effective_Date(self): 
        return ("8,710,717,C,N,N,BG,59")
    def BH_Program_2_CIP_Code(self): 
        return ("6,718,723,O,N,N,BH,60")
    def BI_CIP_Year(self): 
        return ("4,724,727,C,N,N,BI,61")
    def BJ_Program_2_Credential_Level(self): 
        return ("2,728,729,C,N,N,BJ,62")
    def BK_Published_Program_2_Length(self): 
        return ("6,730,735,C,N,A,BK,63")
    def BL_Published_Program_2_Length_Measurement(self): 
        return ("1,736,736,C,A,N,BL,64")
    def BM_Weeks_Program_2_Title_IV_Academic_Year(self): 
        return ("6,737,742,C,N,N,BM,65")
    def BN_Program_2_Begin_Date(self): 
        return ("8,743,750,C,N,A,BN,66")
    def BO_Special_Program_Indicator(self): 
        return ("1,751,751,C,A,A,BO,67")
    def BP_Program_2_Enrollment_Status(self): 
        return ("1,752,752,C,A,N,BP,68")
    def BQ_Program_2_Enrollment_Status_Effective_Date(self): 
        return ("8,753,760,C,N,N,BQ,69")
    def BR_Program_3_CIP_Code(self): 
        return ("6,761,766,O,N,N,BR,70")
    def BS_CIP_Year(self): 
        return ("4,767,770,C,N,N,BS,71")
    def BT_Program_3_Credential_Level(self): 
        return ("2,771,772,C,N,N,BT,72")
    def BU_Published_Program_3_Length(self): 
        return ("6,773,778,C,N,A,BU,73")
    def BV_Published_Program_3_Length_Measurement(self): 
        return ("1,779,779,C,A,N,BV,74")
    def BW_Weeks_Program_3_Title_IV_Academic_Year(self): 
        return ("6,780,785,C,N,N,BW,75")
    def BX_Program_3_Begin_Date(self): 
        return ("8,786,793,C,N,A,BX,76")
    def BY_Special_Program_Indicator(self): 
        return ("1,794,794,C,A,A,BY,77")
    def BZ_Program_3_Enrollment_Status(self): 
        return ("1,795,795,C,A,N,BZ,78")
    def CA_Program_3_Enrollment_Status_Effective_Date(self): 
        return ("8,796,803,C,N,N,CA,79")
    def CB_Program_4_CIP_Code(self): 
        return ("6,804,809,O,N,N,CB,80")
    def CC_CIP_Year(self): 
        return ("4,810,813,C,N,N,CC,81")
    def CD_Program_4_Credential_Level(self): 
        return ("2,814,815,C,N,N,CD,82")
    def CE_Published_Program_4_Length(self): 
        return ("6,816,821,C,N,A,CE,83")
    def CF_Published_Program_4_Length_MeasuremEent(self): 
        return ("1,822,822,C,A,N,CF,84")
    def CG_Weeks_Program_4_Title_IV_Academic_Year(self): 
        return ("6,823,828,C,N,N,CG,85")
    def CH_Program_4_Begin_Date(self): 
        return ("8,829,836,C,N,A,CH,86")
    def CI_Special_Program_Indicator(self): 
        return ("1,837,837,bin,A,A,CI,87")
    def CJ_Program_4_Enrollment_Status(self): 
        return ("1,838,838,C,A,N,CJ,88")
    def CK_Program_4_Enrollment_Status_Effective_Date(self): 
        return ("8,839,846,C,N,N,CK,89")
    def CL_Program_5_CIP_Code(self): 
        return ("6,847,852,O,N,N,CL,90")
    def CM_CIP_Year(self): 
        return ("4,853,856,C,N,N,CM,91")
    def CN_Program_5_Credential_Level(self): 
        return ("2,857,858,C,N,N,CN,92")
    def CO_Published_Program_5_Length(self): 
        return ("6,859,864,C,N,A,CO,93")
    def CP_Published_Program_5_Length_Measurement(self): 
        return ("1,865,865,C,A,N,CP,94")
    def CQ_Weeks_Program_5_Title_IV_Academic_Year(self): 
        return ("6,866,871,C,N,N,CQ,95")
    def CR_Program_5_Begin_Date(self): 
        return ("8,872,879,C,N,A,CR,96")
    def CS_Special_Program_Indicator(self): 
        return ("1,880,880,C,A,A,CS,97")
    def CT_Program_5_Enrollment_Status(self): 
        return ("1,881,881,C,A,N,CT,98")
    def CU_Program_5_Enrollment_Status_Effective_Date(self): 
        return ("8,882,889,C,N,N,CU,99")
    def CV_Program_6_CIP_Code(self): 
        return ("6,890,895,O,N,N,CV,100")
    def CW_CIP_Year(self): 
        return ("4,896,899,C,N,N,CW,101")
    def CX_Program_6_Credential_Level(self): 
        return ("2,900,901,C,N,N,CX,102")
    def CY_Published_Program_6_Length(self): 
        return ("6,902,907,C,N,A,CY,103")
    def CZ_Published_Program_6_Length_Measurement(self): 
        return ("1,908,908,C,A,N,CZ,104")
    def DA_Weeks_Program_6_Title_IV_Academic_Year(self): 
        return ("6,909,914,C,N,N,DA,105")
    def DB_Program_6_Begin_Date(self): 
        return ("8,915,922,C,N,A,DB,106")
    def DC_Special_Program_Indicator(self): 
        return ("1,923,923,C,A,A,DC,107")
    def DD_Program_6_Enrollment_Status(self): 
        return ("1,924,924,C,A,N,DD,108")
    def DE_Program_6_Enrollment_Status_Effective_Date(self): 
        return ("8,925,932,C,N,AN,DE,109")
    def DF_Filler(self): 
        return ("318,933,1250,R,AN,DF,110")
#
D1 = drl()              # instantiate the drl class to D1 data type
# D1.__dict__.keys()         # example of  combined output
# dir(D1)                # prints keys as list
# D1.__dict__            # prints the class as a dictionary
# D1.__dict__.keys()         # prints the keys as a list
# out=D1                 # assign the instance optional
# print out.D110_Filler          # view a particular attribute
#            # Determine type
# print D1.D110_Filler.split(",") `   # output as a list of strings
# print D1.D110_Filler.split(",")[2]  # a particular value
# print dir(D110_Filler)
# print dline.readline()
#
##
#
class Footer:
    def __init__(self):
        self.Column_for_Excel_Format = "Length,Start,Stop,Reqd,Type"
        def Record_Type(self): 
                return ("A,2,1,2,R,AN")
        def Number_of_F(self): 
                return ("B,6,3,8,R,N")
        def Number_of_Q(self): 
                return ("C,6,9,14,R,N")
        def Number_of_H(self): 
                return ("D,6,15,20,R,N")
        def Number_of_L(self): 
                return ("E,6,21,26,R,N")
        def Number_of_W(self): 
                return ("F,6,27,32,R,N")
        def Number_of_G(self): 
                return ("G,6,33,38,R,N")
        def Number_of_A(self): 
                return ("H,6,39,44,R,N")
        def Number_of_X(self): 
                return ("I,6,45,50,R,N")
        def Number_of_D(self): 
                return ("J,6,51,56,R,N")
        def Total_Record_Count(self): 
                return ("K,8,57,64,R,N")
        def Filler(self): 
                return ("L,1186,65,1250,R,AN")

t1 = Footer()

#################### Function Land ####################
#
def poplst():
    """
    Takes ordered directory objects and makes them into a global list of methods
    """
    global alfadefs  #makes this dictionary global
    alfadefs = {'key':'value'}
    key=0
    while key <= 110:
        value = dir(D1)[key]
        alfadefs[key] = "D1."+value+"()"
        key=key+1
    # test this with
    # eval(alfadefs[79]) 
    # len(eval(alfadefs[7]).split("," ))
    # print alfadefs[n]+"\t"+eval(alfadefs[n]) 
    # return eval(alfadefs[n]) 
    # return alfadefs[n] 
    # print alfadefs[n][3:-2]+"\t"+eval(d[n])
    # print (alfadefs[n][3:-2],eval(d[n])) 
    # return alfadefs[n] 
    # return eval(alfadefs[n])
    print " alfadefs is ready to go..."

def criterion(n):
    """
    Takes ordered directory objects and compares them to a line of input.
    """
    d = {'key':'value'}
    key=0
    while key <= 110:
        value = dir(D1)[key]
        d[key] = "D1."+value+"()"
        key=key+1
    # test this with
    # eval(d[79]) 
    # len(eval(d[7]).split("," ))
    # print d[n]+"\t"+eval(d[n]) 
    # return eval(d[n]) 
    # return d[n] 
    # print d[n][3:-2]+"\t"+eval(d[n])
    # return d[n] 
    # return (d[n][3:-2],eval(d[n])) 
    print d[n][3:-2]+"\t"+eval(d[n])
    criteria = eval(alfadefs[n]).split("," )
    # Conditions
    # print "Required = " + criteria[3]
    if   criteria[3] == 'R': print " - Required"
    elif criteria[3] == 'O': print " - Optional"
    elif criteria[3] == 'C': print " - Conditional"
    else: print "error"
    #
    # Conditions
    # print "Type     = " + criteria[4]
    if   criteria[4] == 'A' : 
	print " - Alpha"
    	# print "abc".isalpha()
    	print criteria[4].isalpha()
    elif criteria[4] == 'N' : 
	print " - Numeric"
    	# print "123".isdigit()
	print criteria[4].isdigit()
    elif criteria[4] == 'AN': print " - Alpha Numeric"
    # print "1bc".isalnum()
    else: print "error"
    #
    print "Length   = " + criteria[0]
    print "Start    = " + criteria[1]
    print "Stop     = " + criteria[2]
    #
    print "Column Alpha = " + criteria[6]
    print "Column Numbr = " + criteria[7]

def ccrider(file):
    """
    Takes one ordered directory object and compares it to an element in a line of input.
    """
    of = open(file, 'r')
    i = 1
    while True:
	line = of.readline()
	# EOF or blank line, stop...
	if line == '': break 
	print("{:0>2d} ".format(i))  + "  ",  #zero padded, fancy...
	mylist = line.split(',')
	if mylist[0]=="Record Type": line = of.readline() #skip header
	#D print line
	mylist = line.split(',')
	j=1  # record in line
	#D
	# print mylist[j]
	# print str(mylist[j]) 
	print "  "  + ssnok(str(mylist[j])),
	print "\t" + fname(str(mylist[j+1])),
	print "\t"  +  miok(str(mylist[j+2]))
	i += 1  # record number

def ssnok(SSN):
	j=1  # record in line
	criteria = eval(alfadefs[j]).split(',')
	print "  SSN numeric? " + str(SSN.isdigit()),
	# print len(SSN) 
	if len(SSN) != int(criteria[0]): status = "SSN Wrong!"
	else:
	 	status = "SSN OK"
	return status

def fname(FNAME):
	j=2  # record in line
	criteria = eval(alfadefs[j]).split(',')
	print "\tFNAME letters? " + str(FNAME.isalpha()),
	# print FNAME 
	if len(FNAME) >= int(criteria[0]): status = "FNAME Wrong!"
	else:
	 	status = "FNAME OK"
	return status

def miok(MI):
	j=3  # record in line
	criteria = eval(alfadefs[j]).split(',')
	print "MI letters " + str(MI.isalpha()),
	# print MI 
	if len(MI) >= int(criteria[0]): status = "OK No MI "
	else:
	 	status = "OK MI "
	return status
	
# load line
def csvln(file,n):
    """
    Tests an individual comma separated value line using D1 dlt class methods
    """
    #D print "Welcome to csvln!"
    of = open(file, 'r')
    line = of.readline()
    # print line
    mylist = line.split(',')
    if mylist[0]=="Record Type":
	# print n
	i=0
	# add insertion of an A3 record print alfadefs[n]+"\t"+eval(alfadefs[n])here
	while i < n: 			#advance to proper record
             line = of.readline()
	     # print line
	     i=i+1
        mylist = line.split(',')
	# print mylist
	j=1  # record in line
	SSN = mylist[j]
	#D print "SSN = " + SSN
	criteria = eval(alfadefs[j]).split(',')
	#D print "length " + criteria[0] 
	# print criteria[1]
    # test this with
    # eval(d[79]) 
    # len(eval(d[7]).split("," ))
    # print d[n]+"\t"+eval(d[n]) 
    # return eval(d[n]) 
    # return d[n] 
    # print d[n][3:-2]+"\t"+eval(d[n])
    # return d[n] 
    # return (d[n][3:-2],eval(d[n])) 
    # print alfadefs[j][3:-2]+"\t"+eval(alfadefs[j])
    # criteria = eval(alfadefs[j]).split("," )
    # Conditions
    # print "Required = " + criteria[3]
    #D if   criteria[3] == 'R': print " - Required"
    #D elif criteria[3] == 'O': print " - Optional"
    #D elif criteria[3] == 'C': print " - Conditional"
    #D else: print "error"
    #
    # Conditions
    # print "Type     = " + criteria[4]
    #D if   criteria[4] == 'A' : 
    #D 	print " - Alpha"
    #D  print "abc".isalpha()
    #D print criteria[4].isalpha()
    #D elif criteria[4] == 'N' : 
    #D print " - Numeric"
    #D  print "123".isdigit()
    #D print criteria[4].isdigit()
    #D elif criteria[4] == 'AN': print " - Alpha Numeric"
    # print "1bc".isalnum()
    #D else: print "error"
    #
    #D print "Length   = " + criteria[0]
    #D print "Start    = " + criteria[1]
    #D print "Stop     = " + criteria[2]
    #
    #D print "Column Alpha = " + criteria[6]
    #D print "Column Numbr = " + criteria[7]

    print "SSN numeric? " + str(SSN.isdigit()),
    # print len(SSN) 
    if len(SSN) != int(criteria[0]): print "\tSSN Wrong!"
    else:
	print "\tSSN OK!"



def csvlt(file):
    """
    Tests an individual comma separated value line using D1 dlt class methods
    """
    print "Welcome to csvlt!"
    of = open(file, 'r')
    line = of.readline()
    # print line
    mylist = line.split(',')
    if mylist[0]=="Record Type":
	# add insertion of an A3 record here
        line = of.readline()
        mylist = line.split(',')
        print mylist[1]
        print alfadefs[1]
        criteria = eval(alfadefs[1]).split(',')
        print criteria[0]
        print criteria[1]

if __name__ == '__main__':
    args = docopt(__doc__, version=__file__ +" " + __version__ )
    #D  print(args)


#
#################### Menu Land ####################
#

if args['--2xlsx'] or args['-f']:
    print "You are at the 2xlsx routine -"
    print args['<ifile>']+"  " + args['<ofile>']
    print "This routine is not yet operational"
elif args['--testxls'] or args['-x']:
    print "You are at the testxls routine -"
    print args['<ifile>']+"  " + args['<logfile>']
    print "This routine is not yet operational"
elif args['--testcsv'] or args['-c']:
    print "You are at the testcsv routine -"
    print "This routine is not yet operational but is used for testing"
    #T 
    poplst()
    csvlt(csvfile)
    print args['<ifile>']+"  " + args['<logfile>']
elif args['--testtab'] or args['-t']:
    print "You are at the testtab routine -"
    print args['<ifile>']+"  " + args['<logfile>']
    print "This routine is not yet operational but is used for testing"
    #T
    n=2
    poplst()
    print alfadefs[n]
    print alfadefs[n]+"\t"+eval(alfadefs[n])
elif args['--tespace'] or args['-s']:
    print "You are at the tespace routine -"
    print args['<ifile>']+"  " + args['<logfile>']
    print "This routine is not yet operational"
elif args['--transmit'] or args['-m']:
    print "You are at the transmit routine -"
    print args['<ifile>']
elif args['--details']:
    os.system('cls' if os.name == 'nt' else 'clear')
    print "You are at the detail routine -"
    ''' Prints the main story about this program.'''
    print "\tWelcome to the "+__appname__+" Version: "+__version__  
    print 'This is %s documentation: A general tool for NSLC support' %  os.path.basename(__file__)
    print 'This tool is currently in the %s stage, at version %s' % (__status__, __version__)
    print 'This code, produced by %s, is a work product produced for hire. It is' % __maintainer__
    print '%s, and licensed under the %s ' % ( __copyright__, __license__ )
    print "for operating this tool see commands below:"
    print "Summary usage is:"
    print "\t %s -h" % __file__
    print "Detailed Usage:"  
    print "\t%s  -f  or  --2xlsx    <ifile> <ofile>" %__file__
    print "   Converts CSV output of Goddard SIS NSLC to a Microsoft Excel XLSX format."  
    print "\t%s   -c  or  --testcsv  <ifile> <logfile>" %__file__
    print "   Tests the CSV output of Goddard SIS NSLC to conform with NSLC requirements."  
    print "\t%s   -x  or  --testxls  <ifile> <logfile>" %__file__
    print "   Tests if a Microsoft Excel XLSX format file conforms with NSLC requirements."  
    print "\t%s   -t  or  --testtab  <ifile> <logfile>" %__file__
    print "   Tests if a TAB seperated file conforms with NSLC requirements." 
    print "\t%s   -s  or  --tespace  <ifile> <logfile>" %__file__
    print "   Tests if a fixed field file conforms with NSLC requirements."  
    print "\t%s   -m  or  --transmit ) <ifile>" %__file__
    print "   Transmitts <infile> to the NSLC destination."  
    print "Where:"
    print "\t'<ifile>' & '<ofile>' are required as fully pathed filenames."
    print "\t'<logfile>' is optional, and defaults to standard output."

