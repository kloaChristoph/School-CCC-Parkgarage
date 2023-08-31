def load_file(filename: str = "level2/input.1") -> list:
    with open(filename, "r") as file:
        max_parking_spots = int(file.readline().split(" ")[0])
        tickets = file.readline().split(" ")
        numeric_tickets = []
        for ticket in tickets:
            number = int(ticket)
            numeric_tickets.append(number)
        return numeric_tickets, max_parking_spots


def counting_cars(tickets: list[int], max_parking_spots: int):
    current_count = 0
    max_count = 0
    current_queue = 0
    max_queue = 0

    for ticket in tickets:
        if ticket > 0:
            if current_count == max_parking_spots:
                current_queue +=1
                if current_queue > max_queue:
                    max_queue = current_queue
            else:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count

        else:
            if current_queue > 0:
                current_queue -= 1
            else:
                current_count -= 1

    return max_count, max_queue



if __name__ == "__main__":
    for input in range(2,6):
        tickets, max_parking_spots = load_file(f"level2/input.{input}")
        print(counting_cars(tickets, max_parking_spots))