from matrix import Matrix

while True:
    try:
        number_of_tests = int(input("Number of tests: "))
        if number_of_tests <= 0:
            raise ValueError
    except ValueError:
        print("Please, input a positive integer number!")
    else:
        break

while True:
    try:
        number_of_cities = int(input("Number of cities: "))
        if number_of_cities <= 0:
            raise ValueError
    except ValueError:
        print("Please, input a positive integer number of cities!")
    else:
        break

# Create a Matrix with size number_of_cities
matrix = Matrix(number_of_cities)
city_names = [number_of_cities]
current_city_index = 0

for _ in range(number_of_tests):
    for _ in range(number_of_cities):
        while True:
            city_name = input("City name: ")
            city_names.append(city_name)
            try:
                number_of_neighbors = int(input(f"Number of neighbors in {city_name}: "))
                if number_of_neighbors >= number_of_cities:
                    raise ValueError
            except ValueError:
                print("Please, input a positive integer number of the city`s neighbors!")
            else:
                break

        for _ in range(number_of_neighbors):
            while True:
                try:
                    nr_cost = input("Index of the city and transportation cost: ").split()
                    neighbor_city_index = int(nr_cost[0]) - 1
                    transportation_cost = int(nr_cost[1])
                    if neighbor_city_index == current_city_index or neighbor_city_index < 0 or transportation_cost < 1:
                        raise ValueError
                except ValueError:
                    print("Please, input two positive integer numbers separated by a space!")
                else:
                    matrix[current_city_index][neighbor_city_index] = transportation_cost
                    break

        current_city_index += 1

    matrix.floyd_warshall()

    while True:
        try:
            number_of_paths = int(input("Number of paths: "))
            if number_of_paths <= 0:
                raise ValueError
        except ValueError:
            print("Please, input a positive integer number of paths!")
        else:
            break

    for i in range(number_of_paths):
        while True:
            try:
                pair_of_cities = input("Source and destination cities: ").split()
                start_city = int(city_names.index(pair_of_cities[0])) - 1
                end_city = int(city_names.index(pair_of_cities[1])) - 1
            except ValueError:
                print("Input correct name of cities!")
            else:
                break

        print(matrix[start_city][end_city])
