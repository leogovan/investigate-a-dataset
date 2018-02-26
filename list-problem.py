cast_list = [['Chris Pratt',
              'Bryce Dallas Howard',
              'Irrfan Khan',
              "Vincent D'Onofrio",
              'Nick Robinson'],
             ['Tom Hardy',
              'Charlize Theron',
              'Hugh Keays-Byrne',
              'Nicholas Hoult',
              'Josh Helman'],
             ['Shailene Woodley',
              'Theo James',
              'Kate Winslet',
              'Ansel Elgort',
              'Miles Teller'],
             ['Harrison Ford',
              'Mark Hamill',
              'Carrie Fisher',
              'Adam Driver',
              'Daisy Ridley'],
             ['Vin Diesel',
              'Paul Walker',
              'Jason Statham',
              'Michelle Rodriguez',
              'Dwayne Johnson'],
             ['Leonardo DiCaprio',
              'Tom Hardy',
              'Will Poulter',
              'Domhnall Gleeson',
              'Paul Anderson']]

print(type(cast_list[0][0]))

cast_list_two = []


def cast_list_func(x, empty_list):
    counter = 0
    for i in x:
        empty_list.append(x[counter][0])
        counter = counter + 1


cast_list_func(cast_list, cast_list_two)


print(cast_list_two[:5])
