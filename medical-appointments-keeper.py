print("Enter appointment details here.")
print("If you wish to stop just say \"quit\" when it asks for name")

file = open("medical-appointments.txt", "w+")

#do you wnt to emoty file

while True:
    name = input("Patient's name: ")
    details = input("Details: ")
    time = input("Set a time: ")

    file.write(f"Patient's name: {name} \n Details: {time} \n Time: {time} \n")

    if name.lower() == "quit":
        break

file.close()

print("Thank you, your to-do list has been created and made to a file in this same folder")