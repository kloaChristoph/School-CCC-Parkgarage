import math

def load_file(filename: str = "level5/input.1"):
    with open(filename, "r") as file:
        max_parking_spots = int(file.readline().split()[0])
        prices = [int(i) for i in file.readline().split()]
        weights = [int(i) for i in file.readline().split()]
        tickets = [int(i) for i in file.readline().split()]

        return max_parking_spots, prices, weights, tickets
    
def calc_income(max_parking_spots:int, prices:list[int], weights:list[int], tickets:list[int])-> int:
    income = 0
    parking_spots = [None for i in range(max_parking_spots)]
    queue = []
    for ticket in tickets:
        if ticket > 0:
            try:
                free_space = parking_spots.index(None)
                parking_spots[free_space] = ticket
            except ValueError:
                queue.append(ticket)

        if ticket < 0:
            try:
                used_space = parking_spots.index(abs(ticket))
            except ValueError:
                queue.remove(abs(ticket))
                continue
            parking_spots[used_space] = None
            income += prices[used_space]* math.ceil(weights[abs(ticket)-1]/100)
            if queue:
                parking_spots[used_space] = queue.pop(0)
    return income            

if __name__ == "__main__":
    for input in range(1,6):
        max_parking_spots, prices, weights, tickets = load_file(f"level5/input.{input}")
        print(calc_income(max_parking_spots, prices, weights, tickets))