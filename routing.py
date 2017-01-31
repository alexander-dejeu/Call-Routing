def route_cost_check(filename):
    data = open(filename, 'r')
    for line in data:
        print line
    print data

route_cost_check("phone-numbers-100.txt")
