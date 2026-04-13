def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for x in range(1, days + 1):
        print("Day", x)


def ft_count_harvest_recursive(days=None):
    if (days is None):
        days = int(input("Days until harvest: "))
    elif (days == 0):
        return
    print("Day", days)
    ft_count_harvest_recursive(days - 1)
