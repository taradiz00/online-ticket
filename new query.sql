CREATE DATABASE AirportDB;
GO

USE AirportDB;
GO

CREATE TABLE Passenger (
	Passenger_ID INT IDENTITY(1,1) PRIMARY KEY,
	Passenger_Name VARCHAR(100) NOT NULL,
	Passport_Number VARCHAR(50) NOT NULL,
	Email VARCHAR(100) NOT NULL,
	Date_of_Birth DATE,
	Gender CHAR(1) CHECK (Gender IN ('F', 'M')),
	Phone_Number VARCHAR(30),
	CONSTRAINT UQ_Passenger_Passport UNIQUE (Passport_Number),
	CONSTRAINT UQ_Passenger_Email UNIQUE (Email)
);
GO

/*ALTER TABLE Passenger
ADD Hashed_Password VARCHAR(255);
GO
*/

INSERT INTO Passenger(Passenger_Name, Passport_Number, Email, Date_of_Birth, Gender, Phone_Number)
VALUES 
('Tara Dizaji', 'M12345678', 'tara72019@gmail.com', '09-28-2001', 'F', '+98-383303839'),
('Neda Teimoori', 'N56348927', 'n_teimoori@yahoo.com', '10-11-1979', 'F', '+98-125047584');
GO

DBCC CHECKIDENT ('Passenger', RESEED, 40);
GO

/*DELETE FROM Passenger
WHERE Passenger_ID IN (41, 42);
GO
*/

CREATE TABLE Airline (
    Airline_ID INT IDENTITY(1,1) PRIMARY KEY,
	Airline_Name VARCHAR(100) NOT NULL,
	Airline_Country VARCHAR(50) NOT NULL,
	Airline_Website VARCHAR(100) NOT NULL,
	Airline_Contact_Number VARCHAR(15) NOT NULL,
	CONSTRAINT UQ_Airline_Name UNIQUE (Airline_Name),
	CONSTRAINT UQ_Airline_Website UNIQUE (Airline_Website)
);
GO

INSERT INTO Airline (Airline_Name, Airline_Country, Airline_Website, Airline_Contact_Number)
VALUES 
('Qatar Airways', 'Qatar', 'www.qatarairways.com', '+974-41445555'),
('Emirates', 'United Arab Emirates', 'www.emirates.com', '+971-600555555');
GO

SELECT IDENT_CURRENT('Airport');
GO

/*DELETE FROM Airline
WHERE Airline_ID IN (41, 42);
GO
*/

DBCC CHECKIDENT ('Airline', RESEED, 40);
GO


CREATE TABLE Airport (
    Airport_ID INT IDENTITY(1,1) PRIMARY KEY,
	Airport_Name VARCHAR(100) NOT NULL,
	Airport_Code CHAR(4) NOT NULL,
	Country_Name VARCHAR(100) NOT NULL,
	City_Name VARCHAR(100) NOT NULL,
	Airport_Capacity INT CHECK (Airport_Capacity >=100000),
	Airport_Contact_Number VARCHAR(15) NOT NULL,
	CONSTRAINT UQ_Airport_Name UNIQUE (Airport_Name),
	CONSTRAINT UQ_Airport_Code UNIQUE (Airport_Code)
);
GO

INSERT INTO Airport 
(Airport_Name, Airport_Code, Country_Name, City_Name, Airport_Capacity, Airport_Contact_Number)
VALUES 
('Istanbul Ataturk Airport', 'IST1', 'Turkey', 'Istanbul', 60000000, '+902124444444'),
('Imam Khomeini International Airport', 'IKIA', 'Iran', 'Tehran', 30000000, '+982155000111');
GO

/*ALTER TABLE Airline NOCHECK CONSTRAINT ALL;
DELETE FROM Airline;
ALTER TABLE Airline WITH CHECK CHECK CONSTRAINT ALL;
GO
*/


CREATE TABLE Pilot (
    Pilot_ID INT IDENTITY(1,1) PRIMARY KEY,
    Pilot_Name VARCHAR(100) NOT NULL,
	License_Number VARCHAR(50) NOT NULL,
	Pilot_Rank VARCHAR(20) NOT NULL CHECK (Pilot_Rank IN ('Captain', 'First Officer')),
	Experience_Years INT NOT NULL CHECK (Experience_Years BETWEEN 1 AND 40),
	Pilot_Status VARCHAR(15) NOT NULL CHECK (Pilot_Status IN ('Active', 'On Leave', 'Retired')),
	Contact_Number VARCHAR(25) NOT NULL,
	Airline_ID INT NOT NULL,
	FOREIGN KEY (Airline_ID) REFERENCES Airline(Airline_ID),
	CONSTRAINT UQ_Pilot_License UNIQUE (License_Number)
);
GO

INSERT INTO Pilot (Pilot_Name, License_Number, Pilot_Rank, Experience_Years, Pilot_Status, Contact_Number, Airline_ID)
VALUES 
('Armin Rahmani', 'LIC-IR-784512', 'Captain', 22, 'Active', '+989121234567', 1),
('Sara Mohammadi', 'LIC-TR-992314', 'First Officer', 7, 'On Leave', '+989302223344', 2);
GO

CREATE TABLE Cabin_Crew (
    Crew_ID INT IDENTITY(1,1) PRIMARY KEY,
	Crew_Name VARCHAR(100) NOT NULL,
	Crew_Role VARCHAR(50) NOT NULL CHECK (Crew_Role IN ('Flight Attendant', 'Chief Attendant', 'Safety Officer')),
	Experience_Years INT NOT NULL CHECK (Experience_Years BETWEEN 1 AND 40),
	Crew_Status VARCHAR(15) NOT NULL CHECK (Crew_Status IN ('Active', 'Training', 'On Leave')),
	Contact_Number VARCHAR(25) NOT NULL,
	Airline_ID INT NOT NULL,
	FOREIGN KEY (Airline_ID) REFERENCES Airline(Airline_ID)
);
GO

INSERT INTO Cabin_Crew (Crew_Name, Crew_Role, Experience_Years, Crew_Status, Contact_Number, Airline_ID)
VALUES 
('Sara Ahmadi', 'Flight Attendant', 5, 'Active', '+989123456789', 1),
('Reza Moradi', 'Chief Attendant', 12, 'Training', '+989112233445', 2);
GO

/*ALTER TABLE Cabin_Crew NOCHECK CONSTRAINT ALL;
DELETE FROM Cabin_Crew;
ALTER TABLE Cabin_Crew WITH CHECK CHECK CONSTRAINT ALL;
GO
*/
DBCC CHECKIDENT ('Cabin_Crew', RESEED, 0);
GO

CREATE TABLE Flight_Route (
    Flight_Route_ID INT IDENTITY(1,1) PRIMARY KEY,
	Origin_Airport_code CHAR(4) NOT NULL,
	Destination_Airport_Code CHAR(4) NOT NULL,
	Distance DECIMAL(6,2) NOT NULL,
	Duration TIME
);
GO

INSERT INTO Flight_Route (Origin_Airport_code, Destination_Airport_Code, Distance, Duration)
VALUES 
('OIIE', 'OMDB', 1200.50, '03:00:00'),
('EGLL', 'LFPG', 350.75, '01:15:00');  
GO

/*ALTER TABLE Flight_Route NOCHECK CONSTRAINT ALL;
DELETE FROM Flight_Route;
ALTER TABLE Flight_Route WITH CHECK CHECK CONSTRAINT ALL;
GO
*/
DBCC CHECKIDENT ('Flight_Route', RESEED, 0);
GO

CREATE TABLE Reservation (
    Reservation_ID INT IDENTITY(1,1) PRIMARY KEY,
	Reservation_Date DATETIME2 NOT NULL,
	Reservation_Status VARCHAR(20) NOT NULL CHECK (Reservation_Status IN ('Confirmed', 'Pending', 'Cancelled')),
	Payment_Status VARCHAR(20) NOT NULL CHECK (Payment_Status IN ('Paid', 'Pending', 'Failed')),
	Passenger_ID INT NOT NULL,
	FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID)
);
GO

INSERT INTO Reservation (Reservation_Date, Reservation_Status, Payment_Status, Passenger_ID)
VALUES 
('2025-11-01 10:30', 'Confirmed', 'Paid', 1),
('2025-11-02 15:45', 'Pending', 'Pending', 2);
GO

/*ALTER TABLE Baggage NOCHECK CONSTRAINT ALL;
DELETE FROM Baggage;
ALTER TABLE Baggage WITH CHECK CHECK CONSTRAINT ALL;
GO
*/

DBCC CHECKIDENT ('Baggage', RESEED, 0);
GO


CREATE TABLE FlightSchedule (
    FlightSchedule_ID INT IDENTITY(1,1) PRIMARY KEY,
	Frequency VARCHAR(20) NOT NULL CHECK (Frequency IN ('Daily', 'Weekly', 'Monthly')),
	Effective_From DATE NOT NULL,
	Effective_To DATE NOT NULL,
	Arrival_Time TIME NOT NULL,
	Departure_Time TIME NOT NULL,
	Airline_ID INT NOT NULL,
	Flight_Route_ID INT NOT NULL,
	FOREIGN KEY (Flight_Route_ID) REFERENCES Flight_Route(Flight_Route_ID),
	FOREIGN KEY (Airline_ID) REFERENCES Airline(Airline_ID),
	CHECK (Effective_To > Effective_From),
	CHECK (Arrival_Time <> Departure_Time)
);
GO

INSERT INTO FlightSchedule (Frequency, Effective_From, Effective_To, Arrival_Time, Departure_Time, Airline_ID, Flight_Route_ID)
VALUES 
('Daily', '2025-11-15', '2025-12-31', '18:30', '15:00', 1, 1),
('Weekly', '2025-11-20', '2026-01-20', '09:45', '06:30', 2, 2);  
GO


CREATE TABLE Aircraft (
    Aircraft_ID INT IDENTITY(1,1) PRIMARY KEY,
	Aircraft_Capacity INT CHECK (Aircraft_Capacity BETWEEN 50 AND 600) NOT NULL,
	Aircraft_Status VARCHAR(20) NOT NULL CHECK (Aircraft_Status IN ('Active', 'Maintenance', 'Retired')),
	Model VARCHAR(30) NOT NULL,
	Manufacture_Year INT NOT NULL CHECK (Manufacture_Year BETWEEN 2010 AND 2025),
	Airline_ID INT NOT NULL,
	FOREIGN KEY (Airline_ID) REFERENCES Airline(Airline_ID)
);
GO

INSERT INTO Aircraft (Aircraft_Capacity, Aircraft_Status, Model, Manufacture_Year, Airline_ID)
VALUES 
(180, 'Active', 'Boeing 737-800', 2015, 1),
(320, 'Maintenance', 'Airbus A330', 2018, 2);  
GO

CREATE TABLE Terminal (
	Terminal_Number INT NOT NULL,
	Terminal_Type VARCHAR(15) NOT NULL CHECK (Terminal_Type In ('Domestic', 'International')),
	Terminal_Capacity INT NOT NUll CHECK (Terminal_Capacity >10),
	Airport_ID INT NOT NULL,
	PRIMARY KEY (Airport_ID, Terminal_Number),
	FOREIGN KEY (Airport_ID) REFERENCES Airport(Airport_ID)
);
GO

INSERT INTO Terminal (Terminal_Number, Terminal_Type, Terminal_Capacity, Airport_ID)
VALUES 
(1, 'Domestic', 500, 1),
(2, 'International', 800, 1); 
GO

CREATE TABLE Gate (
    Gate_Number INT NOT NULL,
	Gate_Status VARCHAR(20) NOT NULL CHECK (Gate_Status IN ('Open', 'Boarding', 'Closed', 'Maintenance')),
	Terminal_Number INT NOT NULL,
	Airport_ID INT NOT NULL,
	PRIMARY KEY (Terminal_Number, Airport_ID, Gate_Number),
	FOREIGN KEY (Airport_ID, Terminal_Number) REFERENCES Terminal(Airport_ID, Terminal_Number)
);
GO
INSERT INTO Gate (Gate_Number, Gate_Status, Airport_ID, Terminal_Number)
VALUES 
(1, 'Boarding', 1, 1),
(2, 'Open', 1, 1);
GO

CREATE TABLE Ground_Staff (
    Staff_ID INT IDENTITY(1,1) PRIMARY KEY,
	Staff_Name VARCHAR(100) NOT NULL,
    Staff_Role VARCHAR(20) NOT NULL CHECK (Staff_Role IN ('Check_In', 'Baggage ', 'Security ', 'Maintenance')),
	Staff_Shift VARCHAR(15) NOT NULL CHECK (Staff_Shift IN ('Morning', 'Evening', 'Night')),
	Contact_Number VARCHAR(25) NOT NULL,
	Terminal_Number INT NOT NULL,
	Airport_ID INT NOT NULL,
	FOREIGN KEY (Airport_ID, Terminal_Number) REFERENCES Terminal(Airport_ID, Terminal_Number)
);
GO

INSERT INTO Ground_Staff 
(Staff_Name, Staff_Role, Staff_Shift, Contact_Number, Terminal_Number, Airport_ID)
VALUES
('Ali Karimi', 'Check_In', 'Morning', '+989123456789', 1, 1),
('Bita Mohammadi', 'Baggage', 'Evening', '+989876543210', 2, 1);
GO

CREATE TABLE Flight (
    Flight_ID INT IDENTITY(1,1) PRIMARY KEY,
	Flight_Number VARCHAR(10) NOT NULL,
	Arrival_Time DATETIME2 NOT NULL,
	Departure_Time DATETIME2 NOT NULL,
	FlightStatus VARCHAR(10) DEFAULT 'Scheduled' CHECK (FlightStatus IN ('Scheduled', 'Boarding', 'Delayed', 'Departed', 'Landed', 'Cancelled')),
	FLightSchedule_ID INT NOT NULL,
	Aircraft_ID INT NOT NULL,
	Flight_Route_ID INT NOT NULL,
	Gate_Number INT NOT NULL,
	Pilot_ID INT NOT NULL,
	Terminal_Number INT NOT NULL,
	Airport_ID INT NOT NULL,
	FOREIGN KEY (FLightSchedule_ID) REFERENCES FlightSchedule(FlightSchedule_ID),
	FOREIGN KEY (Aircraft_ID) REFERENCES Aircraft(Aircraft_ID),
	FOREIGN KEY (Flight_Route_ID) REFERENCES Flight_Route(Flight_Route_ID),
	FOREIGN KEY (Terminal_Number, Airport_ID, Gate_Number) REFERENCES Gate(Terminal_Number, Airport_ID, Gate_Number),
	FOREIGN KEY (Pilot_ID) REFERENCES Pilot(Pilot_ID)
);
GO

/*ALTER TABLE Flight
ALTER COLUMN Arrival_Time DATETIME2;
GO
*/

/*ALTER TABLE Flight
ALTER COLUMN Departure_Time DATETIME2;
GO
*/

INSERT INTO Flight (Flight_Number, Arrival_Time, Departure_Time, FlightStatus, FLightSchedule_ID, Aircraft_ID, Flight_Route_ID, Gate_Number, Pilot_ID, Terminal_Number, Airport_ID)
VALUES
('IR101', '2025-11-15 14:30', '2025-11-15 12:00', 'Scheduled', 1, 1, 1, 1, 1, 1, 1),
('IR202', '2025-11-16 18:45', '2025-11-16 16:15', 'Scheduled', 2, 2, 2, 2, 2, 1, 1);
GO

CREATE TABLE Ticket (
    Ticket_ID INT IDENTITY(1,1) PRIMARY KEY,
	Ticket_Number VARCHAR(20) NOT NULL,
	Seat_Number VARCHAR(5) NOT NULL,
	Class VARCHAR(15) NOT NULL CHECK (Class IN ('Economy', 'Business', 'First')),
	Issue_Date DATETIME2,
	Price Decimal(10,2),
	Reservation_ID INT,
	Passenger_ID INT,
	Flight_ID INT,
	CONSTRAINT UQ_Ticket_TkNum UNIQUE (Ticket_Number),
	FOREIGN KEY (Reservation_ID) REFERENCES Reservation(Reservation_ID),
	FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID),
	FOREIGN KEY (Flight_ID) REFERENCES Flight(Flight_ID)
);
GO

INSERT INTO Ticket (Ticket_Number, Seat_Number, Class, Issue_Date, Price, Reservation_ID, Passenger_ID, Flight_ID)
VALUES
('TCK-1001', '12A', 'Economy', '2025-11-10 09:15', 250.00, 1, 1, 1),
('TCK-1002', '2C', 'Business', '2025-11-11 14:45', 820.00, 2, 2, 2);
GO

/*ALTER TABLE Ticket
ALTER COLUMN Reservation_ID, Passenger_ID, Flight_ID INT NOT NULL;
GO
*/

/*ALTER TABLE Ticket
ALTER COLUMN Passenger_ID INT NOT NULL;
GO
*/

/*ALTER TABLE Ticket
ALTER COLUMN Flight_ID INT NOT NULL;
GO
*/

/*ALTER TABLE Ticket
ALTER COLUMN Price Decimal(10,2) NOT NULL;
GO
*/

CREATE TABLE Baggage (
    Baggage_Number INT NOT NULL,
	Baggage_Weight DECIMAL(5,2) NOT NULL,
	Bag_Type VARCHAR(20) CHECK (Bag_Type IN ('Carry-On','Checked','Oversized')) NOT NULL,
	Ticket_ID INT NOT NULL,
	PRIMARY KEY (Ticket_ID, Baggage_Number),
	FOREIGN KEY (Ticket_ID) REFERENCES Ticket(Ticket_ID)
);
GO

INSERT INTO Baggage (Baggage_Number, Baggage_Weight, Bag_Type, Ticket_ID)
VALUES 
(1, 18.5, 'Checked', 1),
(2, 23.0, 'Oversized', 2);
GO

CREATE TABLE Flight_Crew (
	Flight_ID INT NOT NULL,
	Crew_ID INT NOT NULL,
	PRIMARY KEY (Flight_ID, Crew_ID),
	FOREIGN KEY (Flight_ID) REFERENCES Flight(Flight_ID),
	FOREIGN KEY (Crew_ID) REFERENCES Cabin_Crew(Crew_ID)
);
GO

--ALTER TABLE Flight_Crew
--ADD Cabin_Crew_Name VARCHAR(100);
--GO

INSERT INTO Flight_Crew (Flight_ID, Crew_ID)
VALUES
(1,1),
(2,2);
GO

CREATE TABLE Flight_Staff (
    Flight_ID INT NOT NULL,
	Staff_ID INT NOT NULL,
	PRIMARY KEY (Flight_ID, Staff_ID),
	FOREIGN KEY (Flight_ID) REFERENCES Flight(Flight_ID),
	FOREIGN KEY (Staff_ID) REFERENCES Ground_Staff(Staff_ID)
);
GO

/*ALTER TABLE Flight_Staff
ADD Staff_Name VARCHAR(100);
GO
*/

INSERT INTO Flight_Staff (Flight_ID, Staff_ID)
VALUES
(2,1),
(1,2);
GO

CREATE PROCEDURE GetTicketsByPassenger
    @PassengerID INT
AS 
BEGIN
    SELECT
	    T.Ticket_ID,
		F.Flight_Number,
		F.Departure_Time,
		F.Arrival_Time
	FROM Ticket T
	JOIN Flight F ON T.Flight_ID = F.Flight_ID
	WHERE T.Passenger_ID = @PassengerID;
END;
GO

CREATE PROCEDURE AddNewReservation
	@PassengerID INT,
	@FlightID INT,
	@SeatNumber NVARCHAR(10),
	@TicketPrice DECIMAL(10,2)
AS
BEGIN
    SET NOCOUNT ON;
	DECLARE @ReservationID INT;
	INSERT INTO Reservation (Passenger_ID, Reservation_Date, Reservation_Status)
	VALUES (@PassengerID, GETDATE(), 'Confirmed');
	SET @ReservationID = SCOPE_IDENTITY();

	INSERT INTO Ticket (Reservation_ID, Flight_ID, Seat_Number, Price, Issue_Date)
	VALUES (@ReservationID, @FlightID, @SeatNumber, @TicketPrice, GETDATE());

	PRINT 'Reservation and ticket created successfully.';
END;
GO

CREATE PROCEDURE CancelReservation
    @ReservationID INT
AS
BEGIN
    SET NOCOUNT ON;
    IF EXISTS (SELECT 1 FROM Reservation WHERE Reservation_ID = @ReservationID)
    BEGIN
        UPDATE Reservation
        SET Reservation_Status = 'Cancelled'
        WHERE Reservation_ID = @ReservationID;
        PRINT 'Reservation has been successfully cancelled.';
    END
    ELSE
    BEGIN
        PRINT 'Error: Reservation not found.';
    END
END;
GO

CREATE TRIGGER trg_FlightStatusChange
ON Flight
AFTER UPDATE
AS
BEGIN
    IF UPDATE(FlightStatus)
	INSERT INTO Flight_History (Flight_ID, Old_Status, New_Status, Change_Date)
	SELECT 
	i.Flight_ID,
	d.FlightStatus AS Old_Status,
	i.FlightStatus AS New_Status,
	GETDATE() AS Change_Date
	FROM INSERTED i
	JOIN deleted d on i.Flight_ID = d.Flight_ID;
END;
GO