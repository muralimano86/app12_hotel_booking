import pandas


class Hotel:
    watermark = "The Real Estate Company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == hotel_id, "name"].squeeze()

    def book(self):
        """ Book the hotel """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """ Check the availability of the hotel """
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # Overwriting magic method
    def __eq__(self, other):
       if self.hotel_id == other.hotel_id:
           return True
       else:
           return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for reservation.
        Here is your booking confirmation
        Name: {self.the_customer_name} 
        Hotel: {self.hotel.name}
        """

        return content

    @property
    def the_customer_name(self):
        name = self.name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2


df = pandas.read_csv("hotels.csv", dtype={"id":str})

hotel1=Hotel(hotel_id="188")
hotel2=Hotel(hotel_id="134")

# Instance method
print(hotel1.available())

# Instance variable
print(hotel1.name)
print(hotel2.name)

# Class variable
print(hotel1.watermark)
print(hotel2.watermark)

# Class variable
print(Hotel.watermark)

# Class method
print(Hotel.get_hotel_count(df))
print(hotel1.get_hotel_count(df))

# Class property
# Behaves like variable but uses method
ticket = ReservationTicket(customer_name="john smith ", hotel_object=hotel1)
print(ticket.the_customer_name)
print(ticket.generate())

# Static method
# It does not relate to an instance but relates to Class
converted = ReservationTicket.convert(10)
print(converted)