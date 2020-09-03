reason_label={'Certain infectious and parasitic diseases' : 1 ,
'Neoplasms' : 2 ,
'Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism' : 3 ,
'Endocrine, nutritional and metabolic diseases' : 4 ,
'Mental and behavioural disorders' : 5 ,
'Diseases of the nervous system' : 6 ,
'Diseases of the eye and adnexa' : 7 ,
'Diseases of the ear and mastoid process' : 8 ,
'Diseases of the circulatory system' : 9 ,
'Diseases of the respiratory system' : 10 ,
'Diseases of the digestive system' : 11 ,
'Diseases of the skin and subcutaneous tissue' : 12 ,
'Diseases of the musculoskeletal system and connective tissue' : 13 ,
'Diseases of the genitourinary system' : 14 ,
'Pregnancy, childbirth and the puerperium' : 15 ,
'Certain conditions originating in the perinatal period' : 16 ,
'Congenital malformations, deformations and chromosomal abnormalities' : 17 ,
'Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified' : 18 ,
'Injury, poisoning and certain other consequences of external causes' : 19 ,
'External causes of morbidity and mortality' : 20 ,
'Factors influencing health status and contact with health services.' : 21 ,
'Patient follow-up' : 22 ,
'Medical Consultation' : 23 ,
'Blood donation' : 24 ,
'Laboratory Examination' : 25 ,
'Unjustified Absence' : 26 ,
'Physiotherapy' : 27 ,
'Dental Consultation' : 28 ,
'No Reason' : 0 }

education_label={'High School':1,'Graduate':2,'Post Graduate':3,'Masters & Doctor':4}

class desc_value:

    def __init__(self,reason_label):
        self.reason=reason_label

    def get_value(self,r):
        #self.reason_label=

        # print(data_label[r])

        return self.reason[r]
















