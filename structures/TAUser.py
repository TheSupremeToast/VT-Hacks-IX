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
        self.assigned_student = 0
        self.meeting_start = None
        self.meeting_end = None

    
    '''
    Assigns a student to this TA
    '''
    def assign(self, student_id: int):
        if self.in_hours() and self.assigned_student == 0:
            self.assigned_student = student_id
            self.meeting_start = datetime.datetime.now()
        else:
            raise RuntimeError("Can't assign student to TA, a student is already currently assigned or the TAs office hours are not in session.")


    '''
    Unassigns a student to this TA
    '''
    def unassign(self):
        if self.assigned_student != 0:
            self.meeting_end = datetime.datetime.now()
        self.assigned_student = 0


    '''
    Gets the duration of the last meeting, if there was no last meeting, None is returned
    '''
    def get_last_meeting_duration(self):
        if self.meeting_start is None:
            return None
        if self.assigned_student == 0:
            return self.meeting_end.timestamp() - self.meeting_start.timestamp()
        return datetime.datetime.now().timestamp() - self.meeting_start.timestamp()
    

    '''
    Returns the currently assigned student for this TA, 0 if no student is assigned
    '''
    def get_assigned_student(self) -> int:
        return self.assigned_student


    '''
    Gets the class ID that this TA is available for
    '''
    def get_class_id(self) -> str:
        return self.class_id


    '''
    Gets the TA User ID
    '''
    def get_ta_id(self) -> int:
        return self.user_id


    '''
    Gets the TA's hours of availability for today
    '''
    def get_hours(self) -> list:
        return [self.start_hours, self.end_hours]


    '''
    Checks whether or not the TA's hours are in session
    '''
    def in_hours(self) -> bool:
        return self.start_hours < datetime.datetime.now() < self.end_hours


    '''
    Checks if the TA is currently available to take a student
    '''
    def is_available(self) -> bool:
        return self.assigned_student == 0 and self.in_hours()
