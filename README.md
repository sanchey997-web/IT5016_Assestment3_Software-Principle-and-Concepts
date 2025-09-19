# IT5016_Assestment3_Software-Principle-and-Concepts

# Ferry Booking System  

## Overview  
The **Ferry Booking System** is a simple Python program that allows users to:  
- Create new bookings  
- Collect customer details  
- Add ferry services and calculate total costs  
- Approve or reject bookings  
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

