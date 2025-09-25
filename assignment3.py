
# Global counter is used to create unique ticket IDs
count = 10000  # Starting point for ticket numbering

class BookingSystem:#it stores all the booking which are created
    all_bookings = [] 

    def __init__(self): #we used a constructor for initializing a booking which we will be working
        #Single Responsibilty Principle only handles on storing objects
        
        global count
        count += 1  #unique id for each booking
        self.ticket_id = count
        self.costumer_id = ""
        self.costumer_first_name = ""
        self.costumer_last_name = ""
        self.total_cost = 0.0
        self.status = "Pending"
        self.reference_number = "None"
        
        #adding abject to the list
        #Used DRY,TO ADD ALL THE BOOKING IN A SINGLE LIST
        BookingSystem.all_bookings.append(self)

    def costumer_info(self):
        """
        TO COLLECT COSTUMER DETAILS
        SRP BECAUSE, IT ONLY COLLECTS COSTUMER DATAS"""

        self.date = input("What is the date (dd/mm/yyyy): ")
        self.costumer_id = input("What is the Staff ID (Passport/Driving License required): ")
        self.costumer_first_name = input("What is the customer First Name: ")
        self.costumer_last_name = input("What is the customer Last Name: ")

    def ferry_service_details(self):
        
        
    # KISS, a loop for adding the cost of service
        
        try:
            services = int(input("Enter how many services you want to book: "))
            for _ in range(services):
                service_name = input("Enter what kind of service you want: ")
                price = float(input("Enter a price of it: "))
                self.total_cost += price
        except ValueError:
            print("Error Occured! Please enter correctly.")

    def booking_approval(self):
        
            # YAGNI, not adding unnecessary checks 
        
        if self.status == "Approved":
            self.reference_number = (self.costumer_id)[:3] + str(self.ticket_id)[-3:]
        else:
            self.status = "Pending"
            self.reference_number = "Not available"

    def respond_booking(self):

        # choice for approval or rejection of booking
        # Separation of Concerns, only handels logic of a status
        
        if self.status == "Pending":
            choice = input("Please respond to the bookings in your preferences (approve/not approve): ").lower()
            if choice == "approve":
                self.status = "Approved"
                self.reference_number = (self.costumer_id)[:3] + str(self.ticket_id)[-3:]
            elif choice == "not approve":
                self.status = "Not approved"
                self.reference_number = "Not available"
        else:
            print("The booking has been completed already.")

    def display_booking_info(self):
        
        #for displaying all the detail of the booking
        #SRP, it is only responsible for displaying booking info
        
        print("\nPRINTING BOOKING DETAILS")
        print("Date:", self.date)
        print("Customer ID:", self.costumer_id)
        print("First Name:", self.costumer_first_name)
        print("Last Name:", self.costumer_last_name)
        print("Ticket ID:", self.ticket_id)
        print("Status:", self.status)
        print("Approval Reference Number:", self.reference_number)
        print("Total Cost:", self.total_cost)

    def booking_statistics(self):
        
        # for displaying statistics of all the bookings
        #DRY, loop for overall booking count instead of seperating counting multiple times 
        
        total = len(BookingSystem.all_bookings)
        approved = 0
        pending = 0
        not_approved = 0

        for booking in BookingSystem.all_bookings:
            if booking.status == "Approved":
                approved += 1
            elif booking.status == "Pending":
                pending += 1
            elif booking.status == "Not approved":
                not_approved += 1

        print("\nBooking Statistics")
        print(f"Total bookings submitted: {total}")
        print(f"Approved bookings: {approved}")
        print(f"Pending bookings: {pending}")
        print(f"Not approved bookings: {not_approved}")


def main():

    # Main menu to make easy to access individual method by using if/elif/else statement loop for the booking system.
    #KISS, a simple loop for menu system which is easy to understand (simple loop menu, easy to understand)
    while True:
        print("\nFerry Booking System Menu")
        print("1. New Booking")
        print("2. Display Booking Statistics")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            booking = BookingSystem()
            booking.costumer_info()
            booking.ferry_service_details()
            booking.booking_approval()
            booking.respond_booking()
            booking.display_booking_info()

        elif choice == "2":
            if BookingSystem.all_bookings:
                booking.booking_statistics()
            else:
                print("No bookings available.")

        elif choice == "3":
            print("Quit the system.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
