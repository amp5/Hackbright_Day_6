# your code goes here
def rest_ratings(filepath):
    open_file = open(filepath)
    restaurants_dict = {}

    for line in open_file:
        # line_list = line.rstrip().split(":")
        # restaurant_dict[line_list[0]] = line_list[1]

        restaurant, score = line.rstrip().split(':')
        restaurants_dict[restaurant] = score

    # test passed -- print restaurant_dict

    #sorted_list = restaurant_dict.keys()
    #sorted_list.sort()

    #print sorted_list
    
    #sorted(restaurant_dict.keys())

    for rest_name in sorted(restaurants_dict.keys()):
        #rating = restaurant_dict.get(k)

    # print new_sorted_list

        print "Restauarant '%s' is rated at %s." % (rest_name, restaurants_dict[rest_name])


rest_ratings("scores.txt")