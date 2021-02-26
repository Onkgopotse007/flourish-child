from edc_constants.constants import NOT_APPLICABLE, OTHER, NONE

from edc_list_data import PreloadData

list_data = {
    'flourish_child.childdiseases': [
        ('pneumonia', 'Pneumonia'),
        ('tuberculosis', 'tuberculosis'),
        ('Bronchiolitis', 'Bronchiolitis'),
        ('Laryngotracheobronchitis', 'Laryngotracheobronchitis / Croup'),
        ('□ Acute_diarrheal_disease ', 'Acute diarrheal disease '),
        ('Persistent_diarrheal_disease  ', 'Persistent diarrheal disease'),
        ('Meningitis', 'Meningitis'),
        ('Malaria', 'Malaria'),
        ('Measles', 'Measles'),
        ('Trauma', 'Trauma'),
        ('Febrile seizure ', 'Febrile seizure '),
        ('Malnutrition', 'Malnutrition'),
        ('Anemia', 'Anemia'),
        ('Surgical_reason', 'Surgical reason'),
        (OTHER, 'Other'),
    ],
    'flourish_child.chronicconditions': [
        ('Asthma', 'Asthma'),
        ('Hypertension', 'Hypertension'),
        ('Hypercholesterolemia', 'Hypercholesterolemia'),
        ('Heart disease', 'Heart disease'),
        ('Hepatitis B surface Ag positive', 'Hepatitis B surface Ag positive'),
        ('Chronic Hepatitis B carrier', 'Chronic Hepatitis B carrier'),
        ('Hepatitis C', 'Hepatitis C'),
        ('Diabetes', 'Diabetes'),
        (OTHER, 'Other, Specify'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
    'flourish_child.childmedications': [
        (NOT_APPLICABLE, 'Not Applicable'),
        ('Cholesterol medications', 'Cholesterol medications'),
        ('Vitamin D supplement', 'Vitamin D supplement'),
        (NONE, 'None'),
        ('Traditional medications', 'Traditional medications'),
        ('Hypertensive medications', 'Hypertensive medications'),
        ('Prenatal Vitamins', 'Prenatal Vitamins')
    ],
    'flourish_child.wcsdxadult': [
        ('Asymptomatic', 'Asymptomatic'),
        ('Persistent generalized lymphadeno',
         'Persistent generalized lymphadeno'),
        ('Unexplained moderate weight loss',
         'Unexplained moderate weight loss'),
        ('Recurrent resp tract infection', 'Recurrent resp tract infection'),
        ('Herpes zoster', 'Herpes zoster'),
        ('Angular cheilitis', 'Angular cheilitis'),
        ('Recurrent oral ulceration', 'Recurrent oral ulceration'),
        ('Papular pruritic eruptions', 'Papular pruritic eruptions'),
        ('Seborrhoeic dermatitis', 'Seborrhoeic dermatitis'),
        ('Fungal nail infections', 'Fungal nail infections'),
        ('Unexplained* severe weight loss', 'Unexplained* severe weight loss'),
        ('Unexplained persistent fever', 'Unexplained persistent fever'),
        ('Unexplained chronic diarrhoea', 'Unexplained chronic diarrhoea'),
        ('Persistent oral candidiasis', 'Persistent oral candidiasis'),
        ('Oral hairy leukoplakia', 'Oral hairy leukoplakia'),
        ('Pulmonary tuberculosis', 'Pulmonary tuberculosis'),
        ('Severe bacterial infections', 'Severe bacterial infections'),
        ('stomatitis/gingivitis/periodontis',
         'Stomatitis/gingivitis/periodontis'),
        ('anaemia/neutropaenia/thrombocytopa',
         'Anaemia/neutropaenia/thrombocytopa'),
        ('HIV wasting syndrome', 'HIV wasting syndrome'),
        ('Pneumocystis pneumonia', 'Pneumocystis pneumonia'),
        ('Recurrent severe bacterial pneumo',
         'Recurrent severe bacterial pneumo'),
        ('Chronic herpes simplex infection',
         'Chronic herpes simplex infection'),
        ('Oesophageal candidiasis', 'Oesophageal candidiasis'),
        ('Extrapulmonary tuberculosis', 'Extrapulmonary tuberculosis'),
        ('Kaposi\u2019s sarcoma', 'Kaposi\u2019s sarcoma'),
        ('Cytomegalovirus infection', 'Cytomegalovirus infection'),
        ('CNS toxoplasmosis', 'CNS toxoplasmosis'),
        ('HIV encephalopathy', 'HIV encephalopathy'),
        ('Exp cryptococcosis/meningitis', 'Exp cryptococcosis/meningitis'),
        ('Diss non-TB mycobacterial infection',
         'Diss non-TB mycobacterial infection'),
        ('Prog multifocal leukoencephalopathy',
         'Prog multifocal leukoencephalopathy'),
        ('Chronic cryptosporidiosis', 'Chronic cryptosporidiosis'),
        ('Chronic isosporiasis', 'Chronic isosporiasis'),
        ('Disseminated mycosis', 'Disseminated mycosis'),
        ('Recurrent septicaemia', 'Recurrent septicaemia'),
        ('Lymphoma', 'Lymphoma'),
        ('Invasive cervical carcinoma', 'Invasive cervical carcinoma'),
        ('Atypical disseminated leishmaniasis',
         'Atypical disseminated leishmaniasis'),
        ('Sympt nephropathy/cardiomyopathy',
         'Sympt nephropathy/cardiomyopathy'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
}

preload_data = PreloadData(
    list_data=list_data)
