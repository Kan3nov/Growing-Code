def ft_count_harvest_recursive(days=None, current_day=1):
    if (days is None):
        days = int(input("Days until harvest: "))
    if (current_day == days):
        print("Day", current_day)
        print("Harvest time!")
        return
    elif (days == 0):
        print("Harvest time!")
        return
    elif (current_day < days):
        print("Day", current_day)
        ft_count_harvest_recursive(days, current_day+1)
