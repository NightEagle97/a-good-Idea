import ast


def requirements_for_renting():
    verification = input("Enter verification details: ")
    pick_time = input("Enter pick-up time: ")
    drop_time = input("Enter drop-off time: ")
    total_drivers = int(input("Enter number of drivers: "))

    requirements = {
        "Verification": verification,
        "Pick-up Time": pick_time,
        "Drop-off Time": drop_time,
        "Number of Drivers": total_drivers
    }
    
    print("Requirements for renting have been recorded.")
    # print(requirements)


def add_car():
    password = input("Please Enter The Password: ")

    if password != "CarRentals.com":
        print("Incorrect Password.")
        return

    car_color = input("Enter the color of the car: ").lower()
    
    try:
        drive_km = int(input("Enter the KMs driven: "))
    except ValueError:
        print("Integer values only for KMs driven.")
        return
    
    overall_condition = input("Enter the overall condition of the car: ").lower()
    car_variant = input("Enter the car variant: ").lower()
    car_brand = input("Enter the brand of the car: ").lower()
    car_name = input("Enter the car name: ").lower()

    car_details = {
        "Car Color": car_color,
        "KM Driven": drive_km,
        "Overall Condition": overall_condition,
        "Model Of The Car": car_variant,
        "Brand Of The Car": car_brand,
        "Name Of The Car": car_name
    }

    with open("D:\\New Projs\\Rentals\\DB.txt", "a") as db_file:
        db_file.write(f"{str(car_details)}\n")

    with open("D:\\New Projs\\Rentals\\Available.txt", "a") as available_file:
        available_file.write(f"{str(car_details)}\n")

    print(f"{car_brand}'s {car_name} in {car_color} color has been successfully added!")


def cars_rented():
    # This function can be implemented as needed
    pass


def cars_available():
    try:
        with open("D:\\New Projs\\Rentals\\Available.txt", "r") as file:
            cars = file.readlines()
            
            if cars:
                car_details = []
                print("Available Cars:")
                for car in cars:
                    car_details.append(car.strip())
                print(car_details[1])
            else:
                print("No cars available.")
    except FileNotFoundError:
        print("No available cars file found.")


def main():
    while True:
        print("\n\tWelcome To The Rentals!\n\t1. See Available Cars\n\t2. Rent A Car\n\t3. Add A Car\n\t4. Exit\n")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                cars_available()
            elif choice == 2:
                requirements_for_renting()
            elif choice == 3:
                add_car()
            elif choice == 4:
                print("Thank you for working with us!")
                break
            else:
                print("\n\tSorry! Not a valid option.")
        except ValueError:
            print("\n\tSorry! Not a valid option.")


if __name__ == "__main__":
    main()
