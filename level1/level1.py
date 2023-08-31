def load_file(filename: str = "level1/input.1") -> list:
    with open(filename, "r") as file:
        file.readline()
        tickets = file.readline().split(" ")
        numeric_tickets = []
        for ticket in tickets:
            number = int(ticket)
            numeric_tickets.append(number)
        return numeric_tickets
     


def write_to_file(data: list, filename: str = "level1/level1_1.out") -> None:
    with open(filename, "w") as file:
        for line in data:
            file.write(line + "\n")



def counting_cars(tickets):
    current_count = 0
    max_count = 0
    cars_left = []
    for ticket in tickets:
        if ticket > 0:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count -= 1
    return max_count


if __name__ == "__main__":
    for input in range(1,4):
        tickets = load_file(f"level1/input.{input}")
        print(counting_cars(tickets))