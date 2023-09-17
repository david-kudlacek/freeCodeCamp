def add_time(start, duration, day=""):
    # Function variables
    minutes = int()
    hours = int()
    days = int()  # Number of passed days
    period = str()  # AM or PM

    # Only used if optional arg day is specified
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day = int()

    # Get current day from list and set index
    if day != "":
        day = (day.lower()).capitalize()  # Format input day
        current_day = weekdays.index(day)

    # Slice start time into hours, minutes and period (AM or PM)
    sliced_str = str()
    for char in start:
        if char in [':', 'A', 'P']:
            if char == ':':
                hours = int(sliced_str.strip())
                sliced_str = ""
                continue
            minutes = int(sliced_str.strip())
            if char == 'A':
                period = "AM"
                break
            period = "PM"
            break
        sliced_str = sliced_str + char

    # Break down duration time into minutes
    for index, char in enumerate(duration):
        if char == ":":
            duration = int(duration[:index]) * 60 + int(duration[index + 1:])
            break

    # Calculate new time
    while duration > 60:
        hours = hours + 1
        duration = duration - 60
    minutes = minutes + duration
    if minutes >= 60:  # Calculate minutes if outside bounds
        hours = hours + 1
        minutes = minutes - 60
    while hours >= 12:  # Change period and days if outside bounds
        if period == "AM":
            period = "PM"
        else:
            days = days + 1
            if day != "":
                if current_day < 6:
                    current_day = current_day + 1
                else:
                    current_day = 0
            period = "AM"
        if hours == 12 and minutes > 0:
            break
        else:
            hours = hours - 12
    if minutes < 10:  # Add zero if minutes in units
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)

    if day == "":
        if days == 0:
            new_time = f"{str(hours)}:{minutes} {period}"
        elif days == 1:
            new_time = f"{str(hours)}:{minutes} {period} (next day)"
        else:
            new_time = f"{str(hours)}:{minutes} {period} ({days} days later)"
    else:
        if days == 0:
            new_time = f"{str(hours)}:{minutes} {period}, {weekdays[current_day]}"
        elif days == 1:
            new_time = f"{str(hours)}:{minutes} {period}, {weekdays[current_day]} (next day)"
        else:
            new_time = f"{str(hours)}:{minutes} {period}, {weekdays[current_day]} ({days} days later)"

    return new_time
