#  Ferry Booking System

##  Overview
The Ferry Booking System is a small python program that allows the user to:

- Create new bookings  
- Collect customer details  
- Include ferry services and locate overall costs.  
- Approve or reject bookings  
- Disclose single booking details.  
- View the booking statistics (approved, not approved, pending)   
It also demonstrates how principles of software design, namely, the concepts of SRP, DRY, KISS, YAGNI and Separation of Concerns were applied.

##  Features
- Unique Ticket ID generation  
- Customer info collection  
- A number of ferry services that are cost calculating.  
- Display booking details  
- Booking statistics summary  
- Menu-based interface is easy to use.  

##  Code Structure
- Global Counter (count) - Executes the generation of ticket IDs that are unique.  
- BookingSystem Class - This class is used to do bookings through the assistance of OOP(object oriented programming).  

### Methods
- __init__() - Sets up booking object.  
- customer-info() - collects customer information.  
- Added services and prices - ferry-service-add()  
- approval of booking - Approval logic.  
- respond_booking() - Approve/reject booking.  
- show booking - Prints booking details.  
- booking-statistics() - Shows overall statistics.  
- main() Function - Floating menu user interface.  


## Applied Software Designs Principles.

### 1. SRP (Single Responsibility Principle)  
Each method has only one job.  
E.g.: customer information is just collected in customer-info.  

### 2. KISS (Keep It Simple, Stupid)  
- Menu system has a basic loop.  
- Addition of the services is made possible with the assistance of the basic for loop.  

### 3. DRY (Don’t Repeat Yourself)  
- All of the reservations are made in BookingSystem.all_bookings.  
- Statistics is used in one loop instead of developing multiple counters.  

### 4. YAGNI (You Aren’t Gonna Need It)  
- Minimum number of features only the ones which are required.

### 5. Separation of Concerns  
- The various procedures are divided into input, logic and output.  
An example: statistics is a book that does not require an input, but statistics.  

## Reflection
- The clean code and software design concepts make sense and are important as I now realize through this project.
- SRP exposed me to the realization of how the code would still be easier to maintain once it is made of methods that are devoted to a single task.
- KISS and DRY made me understand that the less the better and that repetition should be avoided as it brings about complexity.
- The YAGNI principle made me avoid over complicating the features.
Finally, Separation of Concerns has also assisted me to learn that code can be subdivided into distinct components in an attempt to make reading and debugging code easier.


## Future Improvements
- Improve verification of user entries (e.g. valid date, numeric costs)
- Add a convenient user interface (User Interface or web application)
- Prepare reports (e.g. PDF receipts on bookings)
- Allow the cancellations or schedule changes of booking.
- Numerous user support: user log in and user roles.
