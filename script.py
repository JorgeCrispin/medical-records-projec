names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)
medical_records = list(zip(insurance_costs, names))
num_medical_records =len(medical_records)
#------------------
first_medical_record = medical_records[0]
medical_records

print(medical_records)

print("There are "+ str(num_medical_records) +" medical records")
print("--------------------------------")
print("Here is the first medical record: "+ str(first_medical_record))

medical_records.sort()
print("------------------------------")
print("Here are the medical records sorted by insurance cost: "+ str(medical_records))
print("----------------------------")
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))
print("--------------------------------")
priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

print("   -----------------------------------")

occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records. ")

print("   -------------------------------")

medical_records = list(zip(names, insurance_costs))
medical_records.sort()
print("The medical records sorted alphabetically : " + str(medical_records))

print("   -----------------------------------")

middle_five_records = medical_records[3:8]
print("The middle five records are :" + str(middle_five_records))