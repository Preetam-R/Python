def day_type(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Invalid day"

print(day_type("Monday"))    # Weekday
print(day_type("Saturday"))  # Weekend
print(day_type("Holiday"))   # Invalid day