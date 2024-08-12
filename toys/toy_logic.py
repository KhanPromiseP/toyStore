def toydata():
    name = input("Enter the toy's name: ")
    category = input("Enter the toy's category: ")
    supply_price = float(input("Enter the supply price: "))
    sale_price = float(input("Enter the sale price: "))
    quantity_sold = int(input("Enter the quantity sold: "))
    
 
    toy = {
        'name': name,
        'category': category,
        'supply_price': supply_price,
        'sale_price': sale_price,
        'quantity_sold': quantity_sold
    }
    
    benefit = (sale_price - supply_price) * quantity_sold
    print(f"Benefit gained from {name} toy: {benefit}")
    
    return toy
def toysdata():
    toys = []
    toynum = int(input('Enter the number of toys you want to add: '))
    for _ in range(toynum):
        toy = toydata()
        toys.append(toy)
    return toys

def totalbenefit(toys):
    total_benefit = 0
    for toy in toys:
        benefit = (toy['sale_price'] - toy['supply_price']) * toy['quantity_sold']
        total_benefit += benefit
    return total_benefit

# Function to find the most sold toy
def mostSold(toys):
    most_sold_name = ""
    highest_quantity = -1
    for toy in toys:
        if toy['quantity_sold'] > highest_quantity:
            highest_quantity = toy['quantity_sold']
            most_sold_name = toy['name']
    return most_sold_name

# Function to find the best product
def bestProduct(toys):
    best_name = ""
    highest_benefit = -1
    for toy in toys:
        benefit = (toy['sale_price'] - toy['supply_price']) * toy['quantity_sold']
        if benefit > highest_benefit:
            highest_benefit = benefit
            best_name = toy['name']
    return best_name

# Function to find the worst product
def worstProduct(toys):
    worst_name = ""
    lowest_ratio = float('inf')
    for toy in toys:
        benefit = (toy['sale_price'] - toy['supply_price']) * toy['quantity_sold']
        if toy['quantity_sold'] > 0:
            ratio = (benefit ** 2) / toy['quantity_sold']
            if ratio < lowest_ratio:
                lowest_ratio = ratio
                worst_name = toy['name']
    return worst_name
