from DoctorAppointmentSystem import DoctorAppointmentSystem

def main():
    doctor_system = DoctorAppointmentSystem()

    while True:
        print("\nHi, WELCOME TO THE CLINIC:")
        print("1. View Appointments")
        print("2. Create Appointment")
        print("3. Update Appointment")
        print("4. Delete Appointment")
        print("5. Exit")
        
        choice = input("Please choose an option (1-5): ")

        if choice == '1':
            doctor_system.view_appointments()
    
        elif choice == '2':
            patient_name = input("Enter patient name: ")
            doctor_name = input("Enter doctor name: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            doctor_system.Create_appointment(patient_name, doctor_name, date, time)
        
        elif choice == '3':
            appointment_id_input = input("Enter appointment ID to update: ")
            if appointment_id_input.isdigit():
                appointment_id = int(appointment_id_input)
                if appointment_id in doctor_system.appointments:
                    new_patient = input("Enter new patient name: ")
                    new_doctor = input("Enter new doctor name: ")
                    new_date = input("Enter new appointment date (YYYY-MM-DD): ")
                    new_time = input("Enter new appointment time (HH:MM): ")
                    doctor_system.update_appointment(appointment_id, new_patient, new_doctor, new_date, new_time)
                else:
                    print("Error: Appointment ID not found!")
            else:
                print("Invalid input! Please enter a valid appointment ID (numeric).")
        
        elif choice == '4':
            appointment_id_input = input("Enter appointment ID to cancel: ")
            if appointment_id_input.isdigit():
                appointment_id = int(appointment_id_input)
                if appointment_id in doctor_system.appointments:
                    doctor_system.Delete_appointment(appointment_id)
                else:
                    print("Error: Appointment ID not found!")
            else:
                print("Invalid input! Please enter a valid appointment ID (numeric).")
        
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select an option between 1 and 5.")

if _name_ == "_main_":
    main()
