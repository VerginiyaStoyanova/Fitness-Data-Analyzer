# All METs values depending on the activity
def show_met():
    mets = [
        {'activity': 'Aerobic dance', 'MET': 5.0},
        {'activity': 'Aerobic stepping', 'MET': 8.5},
        {'activity': 'Archery', 'MET': 3.5},
        {'activity': 'Badminton', 'MET': 4.5},
        {'activity': 'Ballet', 'MET': 6.0},
        {'activity': 'Baseball or softball', 'MET': 7.0},
        {'activity': 'Basketball', 'MET': 4.5},
        {'activity': 'Bicycling, slow', 'MET': 3.5},
        {'activity': 'Bicycling, moderate', 'MET': 10.0},
        {'activity': 'Bicycling, fast', 'MET': 16.0},
        {'activity': 'Bowling', 'MET': 3.0},
        {'activity': 'Calisthenics, light to moderate', 'MET': 3.5},
        {'activity': 'Calisthenics, heavy, vigorous', 'MET': 8.0},
        {'activity': 'Canoeing', 'MET': 5.0},
        {'activity': 'Croquet', 'MET': 2.5},
        {'activity': 'Dancing, ballroom, slow', 'MET': 2.9},
        {'activity': 'Dancing, modern, fast', 'MET': 4.8},
        {'activity': 'Fencing', 'MET': 6.0},
        {'activity': 'Fishing, walking and standing', 'MET': 3.5},
        {'activity': 'Fishing in stream with waders', 'MET': 6.5},
        {'activity': 'Football', 'MET': 7.5},
        {'activity': 'Golf', 'MET': 4.4},
        {'activity': 'Gymnastics', 'MET': 4.0},
        {'activity': 'Hiking up hills', 'MET': 7.1},
        {'activity': 'Hockey, field or ice', 'MET': 8.0},
        {'activity': 'Horseback riding', 'MET': 4.0},
        {'activity': 'Ice skating', 'MET': 5.5},
        {'activity': 'Jogging, 12 min/mile', 'MET': 8.0},
        {'activity': 'Judo/karate/tae kwan do', 'MET': 10.0},
        {'activity': 'Kayaking', 'MET': 5.0},
        {'activity': 'Lacrosse', 'MET': 8.0},
        {'activity': 'Rollerblading', 'MET': 10.0},
        {'activity': 'Roller skating', 'MET': 7.0},
        {'activity': 'Running, 6 min/mile', 'MET': 16.0},
        {'activity': 'Running, 7 min/mile', 'MET': 14.0},
        {'activity': 'Running, 8 min/mile', 'MET': 12.5},
        {'activity': 'Running, 9 min/mile', 'MET': 11.0},
        {'activity': 'Running, 10 min/mile', 'MET': 10.0},
        {'activity': 'Skateboarding', 'MET': 5.0},
        {'activity': 'Skiing cross country, slow', 'MET': 7.0},
        {'activity': 'Skiing cross country, moderate', 'MET': 8.0},
        {'activity': 'Skiing cross country, racing uphill', 'MET': 16.5},
        {'activity': 'Skiing downhill, moderate', 'MET': 6.0},
        {'activity': 'Skiing down hill, vigorous', 'MET': 8.0},
        {'activity': 'Skin diving', 'MET': 12.5},
        {'activity': 'Snorkeling', 'MET': 5.0},
        {'activity': 'Snow shoeing', 'MET': 8.0},
        {'activity': 'Soccer, casual', 'MET': 7.0},
        {'activity': 'Stationary cycling, 50 watts', 'MET': 3.0},
        {'activity': 'Stationary cycling, 100 watts', 'MET': 5.5},
        {'activity': 'Stretching exercises, yoga', 'MET': 2.5},
        {'activity': 'Surfing', 'MET': 6.0},
        {'activity': 'Swimming recreational', 'MET': 6.0},
        {'activity': 'Swimming laps, moderate pace', 'MET': 7.0},
        {'activity': 'Swimming laps, sidestroke', 'MET': 8.0},
        {'activity': 'Swimming laps, fast', 'MET': 10.0},
        {'activity': 'Table tennis', 'MET': 4.0},
        {'activity': 'Tai chi', 'MET': 4.0},
        {'activity': 'Tennis', 'MET': 6.0},
        {'activity': 'Trampoline', 'MET': 3.5},
        {'activity': 'Volleyball', 'MET': 7.0},
        {'activity': 'Walking, slowly', 'MET': 2.5},
        {'activity': 'Walking, fast', 'MET': 5.0},
        {'activity': 'Water jogging', 'MET': 8.0},
        {'activity': 'Water polo', 'MET': 10.0},
        {'activity': 'Water skiing', 'MET': 6.0},
        {'activity': 'Weight lifting, heavy workout', 'MET': 6.0},
        {'activity': 'Wrestling', 'MET': 6.0},
    ]
    print('ACTIVITY\t\t\t\t\t\t\t\tMET VALUE')
    for index, met in enumerate(mets):
        print("{:<40} {:<10}".format(met['activity'], met['MET']))


# Calculate the Body Mass Index (BMI)
def calculate_bmi(weight, height):
    body_mass_index = weight / (height ** 2)
    return body_mass_index


# Calculate the estimated number of calories burned during exercise
def calculate_calories_burned(duration_in_minutes, body_weight):
    met_value = float(input('Enter the MET value from the above table: '))
    calories_per_minute = (met_value * 3.5 * body_weight) / 200
    total_calories = calories_per_minute * duration_in_minutes
    return total_calories


# Calculate the overweight people based on BMI
def filter_overweight_people(people_data):
    overweight_people = []
    for person in people_data:
        if person['BMI'] >= 25:
            overweight_people.append(person)
    return overweight_people


# Input validation to ensure that users enter valid data
def get_valid_alphabetic_input(name):
    while True:
        value = input(name).strip()
        if value.isalpha() or not value:
            return value
        print("Invalid input. Please enter alphabetic characters only.")


def get_valid_numeric_input(number):
    while True:
        try:
            value = float(input(number))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid input.")


# Main program
def main():
    people_data = []

    print("Enter fitness data for each person (Enter a blank name to finish):")
    while True:
        name = get_valid_alphabetic_input("Enter person's name: ")
        if not name:
            break
        weight = get_valid_numeric_input("Enter person's weight in kilograms: ")
        height = get_valid_numeric_input("Enter person's height in meters: ")
        duration = get_valid_numeric_input("Enter exercise duration in minutes: ")
        person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
        people_data.append(person)

    # show the MET values
    show_met()

    # print fitness data for every person in the group
    print("\nFitness Analysis:")
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        person['BMI'] = bmi
        calories_burned = calculate_calories_burned(person['duration'], person['weight'])
        print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned:.2f}")

    # print the overweight people in the group
    overweight_people = filter_overweight_people(people_data)
    if len(overweight_people) == 0:
        print("\nOverweight People: None")
    else:
        print("\nOverweight People:")
        for person in overweight_people:
            print(f"{person['name']}: BMI = {person['BMI']:.2f}")


if __name__ == '__main__':
    main()
