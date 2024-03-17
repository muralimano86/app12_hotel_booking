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


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for reservation.
        Here is your booking confirmation
        Name: {self.name} 
        Hotel: {self.hotel.name}
        """

        return content



df = pandas.read_csv("hotels.csv", dtype={"id":str})

hotel1=Hotel(hotel_id="188")
hotel2=Hotel(hotel_id="134")

print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)

print(Hotel.watermark)