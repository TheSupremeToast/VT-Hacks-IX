import datetime

class TAUser:

    '''
    Initializes the TA User
    '''
    def __init__(self, user_id: int, class_id: str, start_hours: datetime.datetime, end_hours: datetime.datetime):
        self.user_id = user_id
        self.class_id = class_id
        self.start_hours = start_hours
        self.end_hours = end_hours

    
    '''
    Assigns a student to this TA
    '''
    def assign(self, student_id):
        self.assigned_student = student_id


    '''
    Unassigns a student to this TA
    '''
    def unassign(self):
        self.assigned_student = 0

    
    '''
    Returns the currently assigned student for this TA, 0 if no student is assigned
    '''
    def get_assigned_student(self):
        return self.assigned_student


    '''
    Gets the class ID that this TA is available for
    '''
    def get_class_id(self):
        return self.class_id

    '''
    Gets the TA User ID
    '''
    def get_ta_id(self):
        return self.user_id


    '''
    Gets the TA's hours of availability for today
    '''
    def get_hours(self):
        return [self.start_hours, self.end_hours]


    '''
    Checks whether or not the TA's hours are in session
    '''
    def in_hours(self):
        return self.start_hours < datetime.datetime.now() < self.end_hours


    '''
    Checks if the TA is currently available to take a student
    '''
    def is_available(self):
        return self.assigned_student == 0 and self.in_hours()
