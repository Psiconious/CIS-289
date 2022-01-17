"""
Name: Trever Cluney
Date: 11.16.22
Email: tlcluney@dmacc.edu
Overview: Request user input for insurance quote by age, coverage type, accident history
"""


class InsuranceCoverage:

    """Class contains all information and functions for returning base coverage cost"""

    coverages = {16: [2593, 2957, 6930], 25: [608, 691, 1745], 35: [552, 627, 1564], 45: [525, 596, 1469],
                 55: [494, 560, 1363], 65: [515, 585, 1402]}

    def __init__(self):
        pass

    def get_base_coverage_amount(self, age, coverage_type):
        key_list = []
        user_base_coverage = 0
        for key in self.coverages.keys():
            key_list.append(key)
        for keys in key_list:
            if age >= keys:
                if coverage_type == "SM":
                    user_base_coverage = self.coverages[keys][0]
                elif coverage_type == "L":
                    user_base_coverage = self.coverages[keys][1]
                elif coverage_type == "F":
                    user_base_coverage = self.coverages[keys][2]
                else:
                    user_base_coverage = 0
        return user_base_coverage


class InsuranceQuote(InsuranceCoverage):

    user_name = ""
    user_age = 0
    coverage_level = "SM"
    agreement_response = ""
    previous_accidents = False
    insurance_coverage_cost = 0
    valid_coverage_level = ["SM", "L", "F"]
    valid_positive_response = ["y", "yes", "yeah", "true", "yup"]

    def __init__(self):
        pass

    def get_user_input(self):
        self.user_name = input("Please enter your name: ")
        valid = False
        while not valid:
            try:
                self.user_age = int(input("Please enter your age: "))
            except ValueError:
                print("Input required a whole number. Try again.")
                valid = False
            else:
                if self.user_age < int(list(self.coverages.keys())[0]):
                    print(f"{self.user_name}'s age is too young. Try again.")
                    valid = False
                else:
                    valid = True
        valid = False
        while not valid:
            self.coverage_level = input(f"Please enter a coverage level {self.valid_coverage_level}: ")
            self.coverage_level = self.coverage_level.upper()
            if self.coverage_level in self.valid_coverage_level:
                valid = True
            else:
                print("Coverage input not valid. Try again.")
                valid = False
        self.agreement_response = input("Have you had any accidents in the past? (y/n) ")
        self.agreement_response = self.agreement_response.lower()
        if self.agreement_response in self.valid_positive_response:
            self.previous_accidents = True
        else:
            self.previous_accidents = False
        pass

    def get_coverage_amount(self):
        base_amount = self.get_base_coverage_amount(self.user_age,self.coverage_level)
        if self.previous_accidents:
            self.insurance_coverage_cost = base_amount * 1.41
        else:
            self.insurance_coverage_cost = base_amount
        pass

    def print_annual_cost(self):
        self.get_coverage_amount()
        print(f"{self.user_name} has an annual insurance cost of ${self.insurance_coverage_cost:.2f}")
        pass


if __name__ == '__main__':

    iq = InsuranceQuote()
    iq.get_user_input()
    iq.print_annual_cost()
    pass
