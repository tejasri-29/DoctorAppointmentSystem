from AppointmentSystem import AppointmentSystem
class DoctorAppointmentSystem(AppointmentSystem):
    def init(self):
        self.appointments = {}
        self.appointment_counter = 1  

    def view_appointments(self):
        if not self.appointments:
            print("No appointments available.")
        else:
            print("Appointments:")
            for appointment_id, details in self.appointments.items():
                print(f"ID: {appointment_id}, Patient: {details['patient_name']},doctor: {details['doctor_name']}, Date: {details['date']}, Time: {details['time']}")
    
    def Create_appointment(self, patient_name,doctor_name, date, time):
        appointment_id = self.appointment_counter
        self.appointments[appointment_id] = {
            'patient_name': patient_name,
            'doctor_name':doctor_name,
            'date': date,
            'time': time
        }
        self.appointment_counter += 1
        print(f"Appointment added successfully! Appointment ID: {appointment_id}")
    
    def update_appointment(self, appointment_id,new_patient,new_doctor,new_date, new_time):
        if appointment_id in self.appointments:
            self.appointments[appointment_id]['patient_name'] = new_patient
            self.appointments[appointment_id]['doctor_name'] = new_doctor
            self.appointments[appointment_id]['date'] = new_date
            self.appointments[appointment_id]['time'] = new_time
        
            
            print(f"Appointment ID {appointment_id} updated successfully!")
        else:
            print("Appointment ID not found!")
    
    def Delete_appointment(self, appointment_id):
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]
            print(f"Appointment ID {appointment_id} deleted successfully!")
        else:
            print("Appointment ID not found!")
