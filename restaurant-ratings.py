# your code goes here
def rest_ratings(filepath):
    open_file = open(filepath)
    restaurant_dict = {}

    for line in open_file:
        line_list = line.rstrip().split(":")
        restaurant_dict[line_list[0]] = line_list[1]


    # test passed -- print restaurant_dict

    #sorted_list = restaurant_dict.keys()
    #sorted_list.sort()

    #print sorted_list
    
    new_sorted_list = sorted(restaurant_dict.keys())

    print new_sorted_list


rest_ratings("scores.txt")