#################### Object Land ####################
#
# This needs to be in the directory starting with version 8!!!!
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
A3 = header()
#
class drl:
    # Line = 2    # starting line for data
    def __init__(self):
        	self.ZColumn_for_Excel_Format = "Index,Length,Start,Stop,Reqd,Type,Field Name,Count"
    def hi(self):
        fm = " From Object Land..."
        return 'Hello World'+fm
    def IND__Column_for_Excel_Format(self): 
        return ("Index,Length,Start,Stop,Reqd,Type,Field_Name,Count")
# Start first Alpha 
# Start first Alpha 
    def A0ARecord_Type(self): 
    	return ("2,1,2,R,AN,A,1")
    def A0BStudent_SSN(self): 
    	return ("9,3,11,R,N,B,2")
    def A0CFirst_Name(self): 
    	return ("20,12,31,R,AN,C,3")
    def A0DMiddle_Initial(self): 
    	return ("1,32,32,O,AN,D,4")
    def A0ELast_Name(self): 
    	return ("20,33,52,R,AN,E,5")
    def A0FName_Suffix(self): 
    	return ("5,53,57,O,AN,F,6")
    def A0GPrevious_SSN(self): 
    	return ("9,58,66,O,N,G,7")
    def A0HPrevious_Last_Name(self): 
    	return ("20,67,86,O,AN,H,8")
    def A0IEnrollment_Status(self): 
    	return ("1,87,87,R,A,I,9")
    def A0JStatus_Start_Date(self): 
    	return ("8,88,95,C,N,J,10")
    def A0KStreet_Line_1(self): 
    	return ("30,96,125,R,AN,K,11")
    def A0LStreet_Line_2(self): 
    	return ("30,126,155,O,AN,L,12")
    def A0MCity(self): 
    	return ("20,156,175,R,A,M,13")
    def A0NState(self): 
    	return ("2,176,177,R,A,N,14")
    def A0OZip(self): 
    	return ("9,178,186,C,AN,O,15")
    def A0PCountry(self): 
    	return ("15,187,201,C,AN,P,16")
    def A0QAnticipated_Graduation_Date(self): 
    	return ("8,202,209,C,N,Q,17")
    def A0RDate_of_Birth(self): 
    	return ("8,210,217,R,N,R,18")
    def A0STerm_Begin_Date(self): 
    	return ("8,218,225,R,N,S,19")
    def A0TTerm_End_Date(self): 
    	return ("8,226,233,R,N,T,20")
    def A0UFiller(self): 
    	return ("1,234,234,R,AN,U,21")
    def A0VDirectory_Block_Indicator(self): 
    	return ("1,235,235,R,A,V,22")
    def A0WNCES_CIP_Code_for_Major_1(self): 
    	return ("6,236,241,O,N,W,23")
    def A0XNCES_CIP_Code_for_Major_2(self): 
    	return ("6,242,247,O,N,X,24")
    def A0YMajor_Course_of_Study_1(self): 
    	return ("80,248,327,O,AN,Y,25")
    def A0ZMajor_Course_of_Study_2(self): 
    	return ("80,328,407,O,AN,Z,26")
# end first alpha
    def AA_Class_Credential(self): 
    	return ("1,408,408,C,A,AA,27")
    def AB_First_Time_Full_Time(self): 
    	return ("1,409,409,O,A,AB,28")
    def AC_Degree_Seeking(self): 
    	return ("1,410,410,O,A,AC,29")
    def AD_High_School_Code(self): 
    	return ("6,411,416,O,N,AD,30")
    def AE_Gender(self): 
    	return ("1,417,417,O,A,AE,31")
    def AF_Race_Ethnicity(self): 
    	return ("2,418,419,O,A,AF,32")
    def AG_College_Student_ID(self): 
    	return ("20,420,439,O,AN,AG,33")
    def AH_State_Student_ID(self): 
    	return ("30,440,469,O,AN,AH,34")
    def AI_Email(self): 
    	return ("128,470,597,O,AN,AI,35")
    def AJ_Good_Student(self): 
    	return ("1,598,598,O,A,AJ,36")
    def AK_Middle_Name(self): 
    	return ("35,599,633,O,AN,AK,37")
    def AL_Veterans_Status_Indicator(self): 
    	return ("1,634,634,O,A,AL,38")
    def AM_Reserved_for_CommIT_ID(self): 
    	return ("12,635,646,O,AN,AM,39")
    def AN_Pell_Grant_Recipient_Flag(self): 
    	return ("1,647,647,O,A,AN,40")
    def AO_Remedial_Flag(self): 
    	return ("1,648,648,O,A,AO,41")
    def AP_Citizenship_Flag(self): 
    	return ("1,649,649,O,A,AP,42")
    def AQ_Student_Phone_Type(self): 
    	return ("1,650,650,O,A,AQ,43")
    def AR_Preferred_Phone_Number_Flag(self): 
    	return ("1,651,651,O,A,AR,44")
    def AS_Student_Phone_Country_Code(self): 
    	return ("3,652,654,O,N,AS,45")
    def AT_Student_Phone_Number(self): 
    	return ("11,655,665,O,N,AT,46")
    def AU_Reserved_for_Move_To_OPEID_Future_CH_Functionality(self): 
    	return ("8,666,673,O,N,AU,47")
    def AV_Program_Indicator(self): 
    	return ("1,674,674,R,A,AV,48")
    def AW_Program_1_CIP_Code(self): 
    	return ("6,675,680,C,N,AW,49")
    def AX_Program_1_CIP_Year(self): 
    	return ("4,681,684,C,N,AX,50")
    def AY_Program_1_Credential_Level(self): 
    	return ("2,685,686,C,N,AY,51")
    def AZ_Published_Program_1_Length(self): 
    	return ("6,687,692,C,N,AZ,52")
# end second alpha
    def BA_Published_Program_1_Length_Measurement(self): 
    	return ("1,693,693,C,A,BA,53")
    def BB_Weeks_Program_1_Title_IV_Academic_Year(self): 
    	return ("6,694,699,C,N,BB,54")
    def BC_Program_1_Begin_Date(self): 
    	return ("8,700,707,C,N,BC,55")
    def BD_Program_1_Special_Program_Indicator(self): 
    	return ("1,708,708,C,A,BD,56")
    def BE_Program_1_Enrollment_Status(self): 
    	return ("1,709,709,C,A,BE,57")
    def BF_Program_1_Enrollment_Status_Effective_Date(self): 
    	return ("8,710,717,C,N,BF,58")
    def BG_Program_2_CIP_Code(self): 
    	return ("6,718,723,O,N,BG,59")
    def BH_Program_2_CIP_Year(self): 
    	return ("4,724,727,C,N,BH,60")
    def BI_Program_2_Credential_Level(self): 
    	return ("2,728,729,C,N,BI,61")
    def BJ_Published_Program_2_Length(self): 
    	return ("6,730,735,C,N,BJ,62")
    def BK_Published_Program_2_Length_Measurement(self): 
    	return ("1,736,736,C,A,BK,63")
    def BL_Weeks_Program_2_Title_IV_Academic_Year(self): 
    	return ("6,737,742,C,N,BL,64")
    def BM_Program_2_Begin_Date(self): 
    	return ("8,743,750,C,N,BM,65")
    def BN_Program_2_Special_Program_Indicator(self): 
    	return ("1,751,751,C,A,BN,66")
    def BO_Program_2_Enrollment_Status(self): 
    	return ("1,752,752,C,A,BO,67")
    def BP_Program_2_Enrollment_Status_Effective_Date(self): 
    	return ("8,753,760,C,N,BP,68")
    def BQ_Program_3_CIP_Code(self): 
    	return ("6,761,766,O,N,BQ,69")
    def BR_Program_3_CIP_Year(self): 
    	return ("4,767,770,C,N,BR,70")
    def BS_Program_3_Credential_Level(self): 
    	return ("2,771,772,C,N,BS,71")
    def BT_Published_Program_3_Length(self): 
    	return ("6,773,778,C,N,BT,72")
    def BU_Published_Program_3_Length_Measurement(self): 
    	return ("1,779,779,C,A,BU,73")
    def BV_Weeks_Program_3_Title_IV_Academic_Year(self): 
    	return ("6,780,785,C,N,BV,74")
    def BW_Program_3_Begin_Date(self): 
    	return ("8,786,793,C,N,BW,75")
    def BX_Program_3_Special_Program_Indicator(self): 
    	return ("1,794,794,C,A,BX,76")
    def BY_Program_3_Enrollment_Status(self): 
    	return ("1,795,795,C,A,BY,77")
    def BZ_Program_3_Enrollment_Status_Effective_Date(self): 
    	return ("8,796,803,C,N,BZ,78")
# end third alpha
    def CA_Program_4_CIP_Code(self): 
    	return ("6,804,809,O,N,CA,79")
    def CB_Program_4_CIP_Year(self): 
    	return ("4,810,813,C,N,CB,80")
    def CC_Program_4_Credential_Level(self): 
    	return ("2,814,815,C,N,CC,81")
    def CD_Published_Program_4_Length(self): 
    	return ("6,816,821,C,N,CD,82")
    def CE_Published_Program_4_Length_Measurement(self): 
    	return ("1,822,822,C,A,CE,83")
    def CF_Weeks_Program_4_Title_IV_Academic_Year(self): 
    	return ("6,823,828,C,N,CF,84")
    def CG_Program_4_Begin_Date(self): 
    	return ("8,829,836,C,N,CG,85")
    def CH_Program_4_Special_Program_Indicator(self): 
    	return ("1,837,837,C,A,CH,86")
    def CI_Program_4_Enrollment_Status(self): 
    	return ("1,838,838,C,A,CI,87")
    def CJ_Program_4_Enrollment_Status_Effective_Date(self): 
    	return ("8,839,846,C,N,CJ,88")
    def CK_Program_5_CIP_Code(self): 
    	return ("6,847,852,O,N,CK,89")
    def CL_Program_5_CIP_Year(self): 
    	return ("4,853,856,C,N,CL,90")
    def CM_Program_5_Credential_Level(self): 
    	return ("2,857,858,C,N,CM,91")
    def CN_Published_Program_5_Length(self): 
    	return ("6,859,864,C,N,CN,92")
    def CO_Published_Program_5_Length_Measurement(self): 
    	return ("1,865,865,C,A,CO,93")
    def CP_Weeks_Program_5_Title_IV_Academic_Year(self): 
    	return ("6,866,871,C,N,CP,94")
    def CQ_Program_5_Begin_Date(self): 
    	return ("8,872,879,C,N,CQ,95")
    def CR_Program_5_Special_Program_Indicator(self): 
    	return ("1,880,880,C,A,CR,96")
    def CS_Program_5_Enrollment_Status(self): 
    	return ("1,881,881,C,A,CS,97")
    def CT_Program_5_Enrollment_Status_Effective_Date(self): 
    	return ("8,882,889,C,N,CT,98")
    def CU_Program_6_CIP_Code(self): 
    	return ("6,890,895,O,N,CU,99")
    def CV_Program_6_CIP_Year(self): 
    	return ("4,896,899,C,N,CV,100")
    def CW_Program_6_Credential_Level(self): 
    	return ("2,900,901,C,N,CW,101")
    def CX_Published_Program_6_Length(self): 
    	return ("6,902,907,C,N,CX,102")
    def CY_Published_Program_6_Length_Measurement(self): 
    	return ("1,908,908,C,A,CY,103")
    def CZ_Weeks_Program_6_Title_IV_Academic_Year(self): 
    	return ("6,909,914,C,N,CZ,104")
    def DA_Program_6_Begin_Date(self): 
    	return ("8,915,922,C,N,DA,105")
    def DB_Program_6_Special_Program_Indicator(self): 
    	return ("1,923,923,C,A,DB,106")
    def DC_Program_6_Enrollment_Status(self): 
    	return ("1,924,924,C,A,DC,107")
    def DD_Program_6_Enrollment_Status_Effective_Date(self): 
    	return ("8,925,932,C,N,DD,108")
    def DE_Filler(self): 
    	return ("318,933,1250,R,AN,DE,109")
# end of object


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
class footer:
	def __init__(self):
		self.ZColumn_for_Excel_Format = "Length,Start,Stop,Reqd,Type"
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

T1 = footer()

