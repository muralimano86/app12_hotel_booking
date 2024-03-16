import pandas


class Hotel:
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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_dict = {"number":self.number, "expiration": expiration, "cvc": cvc, "holder": holder}

        if card_dict in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security["number"]==self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


df = pandas.read_csv("hotels.csv", dtype={"id":str})
df_cards = pandas.read_csv("cards.csv", dtype="str").to_dict(orient="records")
df_card_security = pandas.read_csv("card_security.csv", dtype="str")

print(df)
hotel_id = input("Enter the hotel id: ")
hotel = Hotel(hotel_id)
if hotel.available():
    creditcard = SecureCreditCard(number="1234")
    if creditcard.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if creditcard.authenticate(given_password="mypass1"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
        else:
            print("card authentication is failed")
    else:
        print("Credit card is not valid")
else:
    print("Hotel is not free")
