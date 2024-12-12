from abc import ABC, abstractmethod

class AppointmentSystem(ABC):
    @abstractmethod
    def view_appointments(self):
        pass
    
    @abstractmethod
    def Create_appointment(self, patient_name,doctor_name, date, time):
        pass
    
    @abstractmethod
    def update_appointment(self, appointment_id,patient_name,doctor_name,new_date, new_time):
        pass
    
    @abstractmethod
    def Delete_appointment(self, appointment_id):
        pass
