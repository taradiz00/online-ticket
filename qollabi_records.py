import pyodbc
from faker import Faker
from datetime import timedelta
import datetime
import random
import string

fake= Faker()

# fake.unique.clear()

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-TAU57O5;'
    'Database=AirportDB;'
    'Trusted_Connection=yes;'
)

cursor=conn.cursor()  

                                                            #PASSENGER
query = """ INSERT INTO Passenger (Passenger_Name, Passport_Number, Email, Date_of_Birth, Gender, Phone_Number)
VALUES (?, ?, ?, ?, ?, ?)"""

def create_gender():
    gender = random.choice(['F', 'M'])
    return gender

def create_passport_num():
    passport = fake.unique.bothify(text='??######')
    return passport

def create_email():
    email = fake.unique.email()
    return email

def create_dob():
    dob = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d")
    return dob

def create_passenger_name(gender):
    if gender == 'F':
        return fake.name_female()
    else:
        return fake.name_male()

def create_phone():
    phone = fake.bothify("+##-###-###-####")
    return phone

for i in range(40):
    Gender = create_gender()
    Passenger_Name = create_passenger_name(Gender)
    Passport_Num = create_passport_num()
    Email = create_email()
    Date_of_Birth = create_dob()
    Phone = create_phone()
    cursor.execute(query, (Passenger_Name, Passport_Num, Email, Date_of_Birth, Gender, Phone))



                                                            #AIRLINE
query = """ INSERT INTO Airline (Airline_Name, Airline_Country, Airline_Website, Airline_Contact_Number) VALUES (?, ?, ?, ?) """

cursor.execute("SELECT Country_Name FROM Airport ORDER BY Airport_ID")
country_names = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Airport_Contact_Number FROM Airport ORDER BY Airport_ID")
country_numcodes = [row[0] for row in cursor.fetchall()]


used_websites = set()
used_airlines = set()

def create_airline_name(country_names):
    suffixes = ["Airways", "Airlines", "Air"]
    while True:
        airline_name =f"{country_names} {random.choice(suffixes)}".strip()
        if airline_name not in used_airlines:
            used_airlines.add(airline_name)
            return airline_name

def create_airline_website(airline_name):
    extensions = ["com", "net", "air", "aero"]
    domain = airline_name.replace(" ", "").lower()
    while True:
        website = f"www.{domain}.{random.choice(extensions)}"
        if website not in used_websites:
            used_websites.add(website)
            return website

def create_airline_contact_number(country_numcodes):
    phone = f'{country_numcodes}{'-'}{fake.msisdn()[:10]}' 
    return phone

for i in range(40):
    Airline_Name = create_airline_name(country_names[i])
    Airline_Country = country_names[i]
    Airline_Website = create_airline_website(Airline_Name)
    x = country_numcodes[i].find('-')
    r = country_numcodes[i][:x]
    Contact = create_airline_contact_number(r)
    cursor.execute(query, (Airline_Name, Airline_Country, Airline_Website, Contact))



                                                           #PILOT
query = """ INSERT INTO Pilot (Pilot_Name, License_Number, Pilot_Rank, Experience_Years, Pilot_Status, Contact_Number, Airline_ID) 
VALUES (?, ?, ?, ?, ?, ?, ?) """

cursor.execute("SELECT Airline_ID FROM Airline ORDER BY Airline_ID")
airline_ids = [row[0] for row in cursor.fetchall()]

used_license_numbers = set()

def create_pilot_name():
    pilot_name = fake.name()
    return pilot_name

def create_license_number():
    prefix = random.choice(["ATPL", "CPL", "PPL"])
    while True:
        license_number = fake.bothify(text = f"{prefix}-########")
        if license_number not in used_license_numbers:
            used_license_numbers.add(license_number)
            return license_number
        
def create_experience_years():
    exp_years = random.randint(1, 40)
    return exp_years

def create_pilot_rank(exp_years):
    ranks = ["Captain", "First Officer"]
    if 1<= exp_years <=10:
        return 'First Officer'
    else:
        return 'Captain'

def create_pilot_status():
    status = ["Active", "On Leave", "Retired"]
    pilot_exp = random.choice(status)
    return pilot_exp

def create_pilot_phone_number():
    pilot_phone_num = fake.bothify("+##-###-###-####")
    return pilot_phone_num

for i in range(40):
    Pilot_Name = create_pilot_name()
    License_Number = create_license_number()
    Experience_Years = create_experience_years()
    Pilot_Rank = create_pilot_rank(Experience_Years)
    Pilot_Status = create_pilot_status()
    Contact_Number = create_pilot_phone_number()
    Airline_ID = airline_ids[i]
    cursor.execute(query, (Pilot_Name, License_Number, Pilot_Rank, Experience_Years, Pilot_Status, Contact_Number, Airline_ID))



                                                           #CABIN CREW
query = """ INSERT INTO Cabin_Crew (Crew_Name, Crew_Role, Experience_Years, Crew_Status, Contact_Number, Airline_ID) 
VALUES (?, ?, ?, ?, ?, ?) """

cursor.execute("SELECT Airline_ID FROM Airline ORDER BY Airline_ID")
airline_ids = [row[0] for row in cursor.fetchall()]

def create_crew_name():
    crew_name = fake.name()
    return crew_name

def create_crew_role():
    roles = ["Flight Attendant", "Chief Attendant", "Safety Officer"]
    return random.choice(roles) 

def create_experience_years():
    exp_years = random.randint(1, 40)
    return exp_years

def create_crew_status(exp_years):
    status = ["Active", "Training"]
    if 1<= exp_years <= 2:
        return 'Training'
    else:
        return 'Active'

def create_crew_phone_number():
    crew_phone_num = fake.bothify("+##-###-###-####")
    return crew_phone_num

for i in range(40):
    Crew_Name = create_crew_name()
    Crew_Role = create_crew_role()
    Experience_Years = create_experience_years()
    Crew_Status = create_crew_status(Experience_Years)
    Contact_Number = create_crew_phone_number()
    Airline_ID = airline_ids[i]
    cursor.execute(query, (Crew_Name, Crew_Role, Experience_Years, Crew_Status, Contact_Number, Airline_ID))



                                                            #FLIGHT ROUTE
query = """ INSERT INTO Flight_Route (Origin_Airport_code, Destination_Airport_Code, Distance, Duration) 
VALUES (?, ?, ?, ?) """

cursor.execute("SELECT Airport_Code FROM Airport")
airport_cds = [row[0] for row in cursor.fetchall()]

def create_origin_airport_code(airport_cds):
    return airport_cds

def create_destination_airport_code():
    while True:
        des_code = ''.join(random.choices(string.ascii_uppercase, k=3))
        if des_code not in airport_cds:
            return des_code
        
def create_distance():
    distance = random.uniform(100,9999)
    return round(distance,2)

def create_duration():
    duration = datetime.time(hour = random.randint(0,23),
        minute = random.randint(0,59),
        second = random.randint(0,59)).strftime('%H:%M:%S')
    return duration

for i in range(40):
    Origin_Airport_Code = create_origin_airport_code()
    Destination_Airport_Code = create_destination_airport_code()
    Distance = create_distance()
    Duration = create_duration()
    cursor.execute(query, (Origin_Airport_Code, Destination_Airport_Code, Distance, Duration))



                                                           #RESERVATION
query = """ INSERT INTO Reservation (Reservation_Date, Reservation_Status, Payment_Status, Passenger_ID) 
VALUES (?, ?, ?, ?) """

cursor.execute("SELECT Passenger_ID FROM Passenger ORDER BY Passenger_ID")
passenger_ids = [row[0] for row in cursor.fetchall()]

def create_reservation_date():
    reservation_date = fake.date_time_between(start_date='-1M', end_date='now')
    return reservation_date

def create_reservation_status():
    res_status = ["Confirmed", "Cancelled"]
    reservation_status = random.choice(res_status)
    return reservation_status

def create_payment_status(reservation_status):
    pay_status = ["Paid", "Failed"]
    if reservation_status == 'Confirmed':
        return 'Paid'
    else:
        return 'Failed'

for i in range(40):
    Reservation_Date = create_reservation_date()
    Reservation_Status = create_reservation_status()
    Payment_Status = create_payment_status(Reservation_Status)
    Passenger_ID = passenger_ids[i]
    cursor.execute(query, (Reservation_Date, Reservation_Status, Payment_Status, Passenger_ID))


    
                                                             #AIRCRAFT
query = """ INSERT INTO Aircraft (Aircraft_Capacity, Aircraft_Status, Model, Manufacture_Year, Airline_ID) 
VALUES (?, ?, ?, ?, ?) """

cursor.execute("SELECT Airline_ID FROM Airline ORDER BY Airline_ID")
airline_ids = [row[0] for row in cursor.fetchall()]

def create_aircraft_capacity():
    capacity = random.randint(50,600)
    return capacity


def create_model():
    brands = ["Boeing", "Airbus", "Embraer", "Bombardier"]
    brand = random.choice(brands)
    number = random.randint(100, 999)
    suffix = random.choice (["", "-100", "-200", "-300", "-800", "-900", "ER", "MAX"])
    return f"{brand} {number}{suffix}"

def create_manufacture_year():
    manu = random.randint(2010,2025)
    return manu

def create_aircraft_status(manu):
    airc_status = ["Active", "Maintenance"]
    if 2010<= manu <= 2013:
        return 'Retired'
    else:
        return random.choice(airc_status)

for i in range(40):
    Aircraft_Capacity = create_aircraft_capacity()
    Manufacture_Year = create_manufacture_year()
    Aircraft_Status = create_aircraft_status(Manufacture_Year)
    Model = create_model()
    Airline_ID = airline_ids[i]
    cursor.execute(query, (Aircraft_Capacity, Aircraft_Status, Model, Manufacture_Year, Airline_ID))
    


                                                            #FLIGHT SCHEDULE
query = """ INSERT INTO FlightSchedule (Frequency, Effective_From, Effective_To, Arrival_Time, Departure_Time, Airline_ID, Flight_Route_ID) 
VALUES (?, ?, ?, ?, ?, ?, ?) """

cursor.execute("SELECT Airline_ID FROM Airline ORDER BY Airline_ID")
airline_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Flight_Route_ID FROM Flight_Route ORDER BY Flight_Route_ID")
flight_route_ids = [row[0] for row in cursor.fetchall()]

def create_flight_frequency():
    frq_status = ["Daily", "Weekly", "Monthly"]
    frequency_status = random.choice(frq_status)
    return frequency_status

def create_effective_to_from():
    effective_from = fake.date_time_between("now","+30d")
    effective_to = effective_from + timedelta(days=fake.random_int(min=30, max=180))
    return effective_from.strftime("%Y-%m-%d"), effective_to.strftime("%Y-%m-%d")

def create_arrival_departure():
    base_time = datetime(2000,1,1)
    departure_time = base_time.replace(
    hour=random.randint(0,23),
    minute=random.randint(0,59),
    second=0)
    duration_hours = random.randint(1,23)
    duration_mins = random.randint(0, 59)
    arrival_time = departure_time + timedelta(hours=duration_hours, minutes=duration_mins)
    return departure_time.strftime("%H:%M"), arrival_time.strftime("%H:%M")

for i in range(40):
    Frequency = create_flight_frequency()
    Effective_From, Effective_To = create_effective_to_from()
    Arrival_Time, Departure_Time = create_arrival_departure()
    Airline_ID = airline_ids[i]
    Flight_Route_ID = flight_route_ids[i]
    cursor.execute(query, (Frequency, Effective_From, Effective_To, Arrival_Time, Departure_Time, Airline_ID, Flight_Route_ID))



                                                            #TERMINAL
query = """ INSERT INTO Terminal (Terminal_Number, Terminal_Type, Terminal_Capacity, Airport_ID) 
VALUES (?, ?, ?, ?) """

cursor.execute("SELECT Airport_ID FROM Airport ORDER BY Airport_ID")
airport_ids = [row[0] for row in cursor.fetchall()]


def create_terminal_type():
    trm_type = ["Domestic", "International"]
    terminal_type = random.choice(trm_type)
    return terminal_type

def create_terminal_capacity():
    capacity = random.randint(11,25)
    return capacity

for i in range(40):
    Terminal_Number = i+1
    Airport_ID = airport_ids[i] 
    Terminal_Type = create_terminal_type()
    Terminal_Capacity = create_terminal_capacity()    
    cursor.execute(query, (Terminal_Number, Terminal_Type, Terminal_Capacity, Airport_ID))



                                                           #GATE
query = """ INSERT INTO Gate (Gate_Number, Gate_Status, Airport_ID, Terminal_Number) 
VALUES (?, ?, ?, ?) """

cursor.execute("SELECT Airport_ID, Terminal_Number FROM Terminal ORDER BY Airport_ID, Terminal_Number")
terminal_pairs = cursor.fetchall()

def create_gate_status():
    statuses = ['Open', 'Boarding', 'Closed', 'Maintenance']
    return random.choice(statuses)

for i in range(40):
    Gate_Number = i+1
    Gate_Status = create_gate_status()
    Airport_ID, Terminal_Number = terminal_pairs[i]
    cursor.execute(query, (Gate_Number, Gate_Status, Airport_ID, Terminal_Number))



                                                            #GROUND STAFF
query = """ INSERT INTO Ground_Staff (Staff_Name, Staff_Role, Staff_Shift, Contact_Number, Terminal_Number, Airport_ID) 
VALUES (?, ?, ?, ?, ?, ?) """

cursor.execute("SELECT Terminal_Number, Airport_ID FROM Terminal ORDER BY Terminal_Number, Airport_ID")
terminal_pairs = cursor.fetchall()

def create_staff_name():
    staff_name = fake.name()
    return staff_name

def create_staff_role():
    roles = ['Check_In', 'Baggage ', 'Security ', 'Maintenance']
    return random.choice(roles)

def create_staff_shift():
    shifts = ['Morning', 'Evening', 'Night']
    return random.choice(shifts)

def create_gstaff_phone_number():
    staff_phone_num = fake.bothify("+##-###-###-####")
    return staff_phone_num

for i in range(40):
    Staff_Name = create_staff_name()
    Staff_Role = create_staff_role()
    Staff_Shift = create_staff_shift()
    Contact_Number = create_gstaff_phone_number()
    Terminal_Number, Airport_ID = terminal_pairs[i]
    cursor.execute(query, (Staff_Name, Staff_Role, Staff_Shift, Contact_Number, Terminal_Number, Airport_ID))



                                                            #FLIGHT
query = """ INSERT INTO Flight
  (Flight_Number, Arrival_Time, Departure_Time, FlightStatus, FLightSchedule_ID,
 Aircraft_ID, Flight_Route_ID, Gate_Number, Pilot_ID, Terminal_Number, Airport_ID) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

cursor.execute("SELECT Country_Name FROM Airport ORDER BY Airport_ID")
country_names = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Gate_Number, Terminal_Number, Airport_ID FROM Gate ORDER BY Gate_Number, Terminal_Number, Airport_ID")
gate_pairs = cursor.fetchall()

cursor.execute("SELECT FlightSchedule_ID, Flight_Route_ID FROM FlightSchedule ORDER BY FlightSchedule_ID, Flight_Route_ID")
flight_pairs = cursor.fetchall()

cursor.execute("SELECT Aircraft_ID FROM Aircraft ORDER BY Aircraft_ID")
airc_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Pilot_ID FROM Pilot ORDER BY Pilot_ID")
pilot_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Arrival_Time FROM FlightSchedule ORDER BY FlightSchedule_ID")
arr_times = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Departure_Time FROM FlightSchedule ORDER BY FlightSchedule_ID")
dep_times = [row[0] for row in cursor.fetchall()]

def create_flight_number():
    flight_num_lst = random.choice([item[:2].upper() for item in country_names]) 
    return flight_num_lst + fake.bothify('###')

def create_departure_arrival(arr_times, dep_times):
    dep_date = fake.date_time_between("now", "+179d")
    arr_date = dep_date + timedelta(hours=fake.random_int(min=1, max=22))

    arr_datetime = f"{arr_date.strftime('%Y-%m-%d')} {arr_times}"
    dep_datetime = f"{dep_date.strftime('%Y-%m-%d')} {dep_times}"
    return arr_datetime, dep_datetime

def create_flight_status():
    flight_stat = ['Scheduled', 'Boarding', 'Delayed', 'Departed', 'Landed', 'Cancelled']
    flight_status = random.choice(flight_stat)
    return flight_status

for i in range(40):
    Flight_Number = create_flight_number()
    Arrival_Time, Departure_Time = create_departure_arrival(arr_times[i], dep_times[i])

    FlightStatus = create_flight_status()
    FlightSchedule_ID, Flight_Route_ID = flight_pairs[i]
    Aircraft_ID = airc_ids[i]
    Gate_Number, Terminal_Number, Airport_ID = gate_pairs[i]
    Pilot_ID = pilot_ids[i]
    cursor.execute(query, (Flight_Number, Arrival_Time, Departure_Time, FlightStatus, FlightSchedule_ID,
    Aircraft_ID, Flight_Route_ID, Gate_Number, Pilot_ID, Terminal_Number, Airport_ID))



    
                                                          #TICKET
query = """ INSERT INTO Ticket (Ticket_Number, Seat_Number, [Class], Issue_Date, [Price], Reservation_ID, Passenger_ID, Flight_ID) 
 VALUES (?, ?, ?, ?, ?, ?, ?, ?) """

cursor.execute("SELECT Reservation_ID FROM Reservation ORDER BY Reservation_ID")
rsrv_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Passenger_ID FROM Passenger ORDER BY Passenger_ID")
psng_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Flight_ID FROM Flight ORDER BY Flight_ID")
flight_ids = [row[0] for row in cursor.fetchall()]

def create_tick_num():
    tick_num = fake.bothify('??-####')
    return tick_num

cursor.execute("SELECT Model FROM Aircraft ORDER BY Aircraft_ID")
airc_models = [row[0] for row in cursor.fetchall()]

def create_seat_num(model):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
    
    s = (model[:model.find(" ")])
    if s == "Boeing":
        seat_num = str(random.randint(1,35)) + random.choice(letters)
        return seat_num
    elif s == "Airbus":
        seat_num = str(random.randint(1,60)) + random.choice(letters) 
        return seat_num
    elif s == "Bombardier":
        seat_num = str(random.randint(1,20)) + random.choice(letters) 
        return seat_num
    else:
        seat_num = str(random.randint(1,25)) + random.choice(letters) 
        return seat_num


def create_tick_class():
    classes = ['Economy', 'Business', 'First']
    class_type = random.choice(classes)
    return class_type

cursor.execute("SELECT Reservation_DATE FROM Reservation ORDER BY Reservation_ID")
rsrv_dates = [row[0] for row in cursor.fetchall()]

def create_issue_date(rsrv_dates):
    return id

def create_price():
    price = random.uniform(80,5000)
    return round(price,2)


for i in range(40):
    model = random.choice(airc_models) 
    Ticket_Number = create_tick_num()
    Seat_Number = create_seat_num(model)
    Class_Type= create_tick_class()
    Issue_Date = rsrv_dates[i]
    Price = create_price()
    Reservation_ID = rsrv_ids[i]
    Passenger_ID = psng_ids[i]
    Flight_ID = flight_ids[i]
    cursor.execute(query, (Ticket_Number, Seat_Number, Class_Type, Issue_Date, Price, Reservation_ID, Passenger_ID, Flight_ID))



                                                            #BAGGAGE
query = """ INSERT INTO Baggage (Baggage_Number, Baggage_Weight, Bag_Type, Ticket_ID) 
 VALUES (?, ?, ?, ?) """

cursor.execute("SELECT Ticket_ID FROM Ticket ORDER BY Ticket_ID")
tck_ids = [row[0] for row in cursor.fetchall()]


def create_bag_weight():
    weight = random.uniform(5,200)
    return round(weight,2)

def create_bag_type(weight):
    types = ['Carry-On','Checked']
    if weight >= 151:
        return 'Oversized'
    else:
        bag_type = random.choice(types)
        return bag_type


for i in range(40):
    Baggage_Number = i
    Baggage_Weight = create_bag_weight()
    Bag_Type = create_bag_type(Baggage_Weight)
    Ticket_ID = tck_ids[i]
    cursor.execute(query, (Baggage_Number, Baggage_Weight, Bag_Type, Ticket_ID))




                                                            #FLIGHT CREW
query = """ INSERT INTO Flight_Crew (Flight_ID, Crew_ID, Cabin_Crew_Name) 
 VALUES (?, ?, ?) """

cursor.execute("SELECT Flight_ID FROM Flight ORDER BY Flight_ID")
flight_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Crew_Name FROM Cabin_Crew ORDER BY Crew_ID")
crew_names = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Crew_ID FROM Cabin_Crew ORDER BY Crew_ID")
crw_ids = [row[0] for row in cursor.fetchall()]

for i in range(40):
    Flight_ID = flight_ids[i]
    Crew_ID = crw_ids[i]
    Cabin_Crew_Name = crew_names[i]
    cursor.execute(query, (Flight_ID, Crew_ID, Cabin_Crew_Name))



                                                          #FLIGHT STAFF
query = """ INSERT INTO Flight_Staff (Flight_ID, Staff_ID, Staff_Name) 
 VALUES (?, ?, ?) """

cursor.execute("SELECT Flight_ID FROM Flight ORDER BY Flight_ID")
flight_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Staff_ID FROM Ground_Staff ORDER BY Staff_ID")
crw_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Staff_Name FROM Ground_Staff ORDER BY Staff_ID")
staff_names = [row[0] for row in cursor.fetchall()]

for i in range(40):
    Flight_ID = flight_ids[i]
    Staff_ID = crw_ids[i]
    Staff_Name = staff_names[i]
    cursor.execute(query, (Flight_ID, Staff_ID, Staff_Name))

conn.commit()
conn.close()
print('Done!')