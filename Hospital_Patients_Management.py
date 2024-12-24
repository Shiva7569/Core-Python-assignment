def display_patients(patients):
    if patients:
        for patient in patients:
            print(patients)
    else:
        print("No patients.")

def search_patients_by_disease(patients, disease):
    return [patient['Name'] for patient in patients if patient['Disease'] == disease]
    
total_patients=int(input("Enter the total number of patients :"))
patients=[]
for _ in range(total_patients):
    name=input("Enter the patient name :")
    age=input("Enter the patient age :")
    disease=input("Enter the patient disease :")
    patients.append({"Name":name,"Age":age,"Disease":disease})
display_patients(patients)
search_disease=input("Enter desease to search patients :")
print("patients with",search_disease,search_patients_by_disease(patients,search_disease))