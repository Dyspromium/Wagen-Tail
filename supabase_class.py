
class User_Supabase:
    def __init__(self, id, mail, fullname, age):
        self.fullname = fullname
        self.age = age
        self.id = id
        self.mail = mail
        self.balance = 0


class Contact_Supabase:
    def __init__(self, fullname, age, id, rate, travel_id, is_driver, dest_from, dest_to):
        self.fullname = fullname
        self.age = age
        self.id = id
        self.rate = rate
        self.travel_id = travel_id
        self.is_driver = is_driver
        self.dest_from = dest_from
        self.dest_to = dest_to



class Message_Supabase:
    def __init__(self, message, date, seen, sender):
        self.message = message
        self.date = date
        self.seen = seen
        self.sender = sender

