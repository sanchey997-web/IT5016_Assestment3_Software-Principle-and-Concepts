# IT5016_Assestment3_Software-Principle-and-Concepts

# Ferry Booking System  

## Overview  
The **Ferry Booking System** is a simple Python program that allows users to:  
- Create new bookings  
- Collect customer details  
- Add ferry services and calculate total costs  
- Approve or reject booki# IT5016_Assestment3_Software-Principle-and-Concepts

# Ferry Booking System  

## Overview  
The Ferry Booking System is a basic python application that enables one to:  
- Create new bookings  
- Collect customer details  
- Add ferries and divide the total costs.  
- Approve or reject bookings  
- Show personal reservation information.  
- See booking statistics (accepted, awaiting, rejected)  

It is a project that is aimed at beginners studying Object-Oriented Programming (OOP) in Python.  
It is also an illustration of applying the principles of software design:  
Separation of Concerns, SRP, DRY, KISS and YAGNI.  

##  Features  
 Unique Ticket ID generation  
 Customer info collection  
 Various ferry services with costs calculations.  
 Acceptance or rejection of booking.  
 Display booking details  
 Booking statistics summary  
 Single menu-based interface.  

##  Code Structure  
- **Global Counter (`count)` → Produces unique ticket IDs.  
    - **BookingSystem Class** → This class is used to deal with booking based on OOP.  
      - `__init__()` → Initializes booking object.  
      - `costumer_info()` → Gathers information about customers.  
      - `ferry-service-add-service/ferry-service-add-price()` Adds new services and prices.  
      - `booking_approval()` → Approval logic.  
      - `respond_booking()` → Approve/Reject booking.  
      - `print booking information()` → Displays the information about the booking.  
      - booking statistics() - Displays total statistics.  
    - **Function main()` Function** → Offers menu based user interaction.  

Software Design Principles Implemented.  

### 1. Single Responsibility Principle (SRP).  
Each method has **only one job**.  
Example: costumer information only gathers customer information: costumer_info.  

### 2. **KISS (Keep It Simple, Stupid)**  
- Menu system is based on a simple loop.  
The addition of the services is carried out with the help of a simple for-loop.  

### 3. **DRY (Don’t Repeat Yourself)**  
- Bookings are held in all_bookings BookingSystem.  
- A single loop is used to do statistics rather than multiple counters.  

### 4. **YAGNI (You Aren’t Gonna Need It)**  
- No redundant checks or functionality (just what is needed).  

### 5. **Separation of Concerns**  
- The separation between input, logic and output is done into different methods.  
- E.g. booking statistics() is not receiving input, but statistics.  

ngs  
- Display individual booking details  
- View booking statistics (approved, pending, not approved)  

This project is designed for **beginners** learning **Object-Oriented Programming (OOP)** in Python.  
It also demonstrates the use of **software design principles**:  
**SRP, DRY, KISS, YAGNI, and Separation of Concerns**.  

##  Features  
 Unique Ticket ID generation  
 Customer info collection  
 Multiple ferry services with cost calculation  
 Booking approval or rejection  
 Display booking details  
 Booking statistics summary  
 Simple menu-driven interface  

##  Code Structure  
- **Global Counter (`count`)** → Generates unique ticket IDs.  
    - **`BookingSystem` Class** → Handles bookings using OOP principles.  
      - `__init__()` → Initializes booking object.  
      - `costumer_info()` → Collects customer details.  
      - `ferry_service_details()` → Adds services and prices.  
      - `booking_approval()` → Manages approval logic.  
      - `respond_booking()` → Approve/Reject booking.  
      - `display_booking_info()` → Prints booking details.  
      - `booking_statistics()` → Shows overall statistics.  
    - **`main()` Function** → Provides menu-based user interaction.  

##  Software Design Principles Applied  

### 1. **SRP (Single Responsibility Principle)**  
Each method has **only one job**.  
Example: `costumer_info()` only collects customer data.  

### 2. **KISS (Keep It Simple, Stupid)**  
- Menu system uses a **simple loop**.  
- Adding services is done using a **basic for-loop**.  

### 3. **DRY (Don’t Repeat Yourself)**  
- All bookings are stored in `BookingSystem.all_bookings`.  
- One loop handles statistics instead of writing multiple counters.  

### 4. **YAGNI (You Aren’t Gonna Need It)**  
- No unnecessary checks or features (only what’s required).  

### 5. **Separation of Concerns**  
- Input, logic, and output are separated into different methods.  
- Example: `booking_statistics()` handles only statistics, not input.  

