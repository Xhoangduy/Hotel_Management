# Hotel Management

## Introduction

**Hotel Management** is a hotel management system that allows customers to book rooms online and helps staff/managers easily track and handle operations related to rooms, customers, payments, and revenue reports. The system aims to automate and optimize hotel operations.

## Main Features

- **Online Room Booking:**  
  Customers can select room types, enter personal information, the number of guests, check-in and check-out dates, and submit booking requests via the web interface.

- **Room Management:**  
  View the list of rooms, detailed information for each room, room types, prices, images, descriptions, area, bed type, view, etc.

- **Create Rental Slips:**  
  Staff can create rental slips for guests, search for customer information and booking details.

- **Payment & Invoice Generation:**  
  Supports payment, calculates the total amount based on room type and length of stay, and generates invoices.

- **Revenue Reports:**  
  Administrators can view revenue reports and business statistics.

- **User Management & Authorization:**  
  Supports multiple roles such as customer, staff, administrator; each role has its own permissions.

## Technologies Used

- **Backend:** Python (Flask), SQLAlchemy ORM, SQLite/MySQL
- **Frontend:** HTML, CSS, JavaScript (Jinja2 Template)
- **Authentication:** Flask-Login
- **Administration:** Flask-Admin

## Getting Started

### 1. Set Up Environment

```bash
git clone https://github.com/Xhoangduy/Hotel_Management.git
cd Hotel_Management
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Initialize Database

- Configure the database information in `app/__init__.py` or `.env`
- Create the database:
```bash
python app/models.py
```

### 3. Run the Application

```bash
python app/index.py
```
Access at: [http://localhost:5000](http://localhost:5000)

## Project Structure

```
Hotel_Management/
├── app/
│   ├── __init__.py
│   ├── index.py        # Main route handling
│   ├── admin.py        # Administration, reports, authorization
│   ├── models.py       # Table definitions, ORM
│   ├── dao.py          # Data access/query functions
│   ├── templates/      # HTML templates
│   ├── static/         # Static files (images, css, js)
│   └── ...
├── requirements.txt
└── README.md
```

## Contribution

Please create a new issue to report bugs or propose features. Pull Requests (PRs) are always welcome!

## License

This project does not have a specific license published yet.

---

> © 2025 Xhoangduy. For more information, please contact via GitHub: [Xhoangduy](https://github.com/Xhoangduy)
