# This program simulates a simple traffic light system where the user can choose a traffic light color
# and the program responds accordingly.

distance_covered = 0

traffic_light = input('Please, Choose a traffic light color (Green, Red, Yellow): ').capitalize()
print(f'\nTraffic Light: {traffic_light}')

if traffic_light == 'Green':
    distance_covered += 1
    print(f'The light is {traffic_light}, the distance now is {distance_covered}')

elif traffic_light == 'Red':
    print(f'The light is {traffic_light} and the car has stopped')
    is_neutral = input('Do you want to put your car in neutral? yes/no: ').capitalize()

    if is_neutral == 'Yes':
        print('Vehicle in neutral')
    elif is_neutral == 'No':
        print('Nothing happens')
    else:
        print('Please type yes or no as an answer')

elif traffic_light == 'Yellow':
    distance_covered += 0.5
    print(f'The light is {traffic_light}, the distance now is {distance_covered}')
else:
    print('Please enter a valid traffic light color: green, red, or yellow.')