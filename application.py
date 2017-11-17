import trip


def main():
    userorigin = input("Where do you want to be your starting position? Please use the place and the state. " 
                       "Example: San Jose Airport CA ")
    userdestination = input("Where do you want to be your final destination? Please use the place and the state." 
                            "Example: Berkeley CA ")
    usermode = input("How do you want to travel? Please choose driving, bicycling, or walking ")

    user = trip.Trip(userorigin, userdestination, usermode, "false")
    print(user)
    print(user.distance)
    print(user.duration)


main()
