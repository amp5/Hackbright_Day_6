# your code goes here
def rest_ratings(filepath):
    open_file = open(filepath)
    restaurant_dict = {}
    for line in open_file:
        line_list = line.rstrip().split(":")
        restaurant_dict[line_list[0]] = line_list[1]


    print restaurant_dict

rest_ratings("scores.txt")