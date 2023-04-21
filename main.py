calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
        return(f'{num_of_days} days are {num_of_days*calculation_to_hours} {name_of_unit}')

def Validate_and_execute():
  try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("Enter a non-zero number")
        else:
            print("Its a -ve number")
  except ValueError:
        print("Your input isn't a number, please enter a number")

user_input = input("Hey user, enter the number of days, I'll convert it to hours\n")
Validate_and_execute()
