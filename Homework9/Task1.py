class Company:
    """A class representing a company."""

    def __init__(self, name, headquarters, employees):
        """Initialize the company."""
        self.name = name
        self.headquarters = headquarters
        self.employees = employees

    def __repr__(self):
        """Return a string representation of the company."""
        return f"Company(name={self.name}, headquarters={self.headquarters}, employees={self.employees})"

    def get_name(self):
        """Return the name of the company."""
        return self.name

    def get_headquarters(self):
        """Return the headquarters of the company."""
        return self.headquarters

    def get_employees(self):
        """Return the number of employees in the company."""
        return self.employees

    # Class attributes
    num_employees = 0

    # Class method
    @classmethod
    def get_total_number_of_employees(cls):
        """Return the total number of employees across all companies."""
        return sum(company.num_employees for company in cls._companies)

    # Static method
    @staticmethod
    def is_company_valid(name, headquarters, employees):
        """Return True if the company is valid, False otherwise."""
        if not isinstance(name, str):
            return False
        if not isinstance(headquarters, str):
            return False
        if not isinstance(employees, int):
            return False
        return True
