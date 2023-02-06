sale_amount = int(input("Enter the amount of sale: "))

def calculate_discount(sale_amount):
    if sale_amount > 5000:
        return sale_amount*.45
    elif sale_amount > 3000:
        return sale_amount*.3
    elif sale_amount>1000:
        return sale_amount*.15
    else:
        return sale_amount


print("The final sale amount is $ ", calculate_discount(sale_amount))
