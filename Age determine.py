import datetime

# Get the current date
current_date = datetime.date.today()

# Define the Person class
class Person:
    # Function to initialize person details
    def details(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    # Method to determine person's age
    def cal_age(self):
        # Calculate age using date of birth and current date
        age = current_date.year - self.date_of_birth.year - ((current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

# Create an instance of the Person class
person = Person()

# Set person details
person.details('waiz', 'Pakistan', datetime.date(2007, 3, 21))

# Calculate and print age
age = person.cal_age()
print("Age your age is :", age)
