from patientsResult import patientsResult

def patientWithCovid19(patientsResult, numberOfSymptoms = 2):
    patientsSick = []

    for i, patient in enumerate(patientsResult):
        covid19Systems = [patient[0], patient[1], patient[5], patient[6]]
    
        if sum(covid19Systems) >= numberOfSymptoms:
            patientsSick.append(i)
    
    return patientsSick

patientsSuspected = patientWithCovid19(patientsResult)
print("Essa é a lista dos pacientes suspeitos de terem o Covid 19: ", patientsSuspected)
