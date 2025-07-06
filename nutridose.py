
class Node:
    def __init__(self, parameter, value, recommendation):
        self.parameter = parameter
        self.value = value
        self.recommendation = recommendation
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, parameter, value, recommendation):
        new_node = Node(parameter, value, recommendation)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.parameter}: {current.value} | Recommendation: {current.recommendation}")
            current = current.next

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

NORMAL_RANGES = { 'Hemoglobin': (12.0, 17.5), 'Vitamin D': (20.0, 50.0), 'Calcium': (8.5, 10.5), 'Iron': (60.0, 170.0) }

RECOMMENDATIONS = { 'Hemoglobin': 'Take Iron supplements 15 mg/day', 'Vitamin D': 'Take Vitamin D3 2000 IU/day or sunlight exposure', 'Calcium': 'Consume dairy products and calcium supplements', 'Iron': 'Eat iron-rich foods like spinach, red meat' }

def check_deficiency(parameter, value):
    min_val, max_val = NORMAL_RANGES.get(parameter, (0, 0))
    if value < min_val:
        return f"Low {parameter}: {RECOMMENDATIONS.get(parameter)}"
    elif value > max_val:
        return f"High {parameter}: Adjust diet and consult physician"
    return None

def main():
    linked_list = LinkedList()
    queue = Queue()
    stack = Stack()

# Example test data
    example_data = {
    'Hemoglobin': 10.5,
    'Vitamin D': 15,
    'Calcium': 7.8,
    'Iron': 55
    }

# Process Example Data
    print("\nProcessing Example Data:\n")
    for param, val in example_data.items():
        rec = check_deficiency(param, val)
        if rec:
            linked_list.add_node(param, val, rec)
            queue.enqueue(rec)

    linked_list.display()

# Show Recommendations One by One
    print("\nRecommendations:")
    while not queue.is_empty():
        suggestion = queue.dequeue()
        print(f"-> {suggestion}")
        stack.push(suggestion)

# Undo Example
    print("\nUndo Last Recommendation:")
    last = stack.pop()
    print(f"Undone: {last}")

# Save to file
    with open("recommendations.txt", "w") as file:
        current = linked_list.head
        while current:
            file.write(f"{current.parameter}: {current.value} - {current.recommendation}\n")
            current = current.next

    print("\nRecommendations saved to recommendations.txt")

# ------------------ Manual Input Option ------------------
    print("\nNow try with your own data.")
    user_data = {}
    for param in NORMAL_RANGES:
        try:
            user_value = float(input(f"Enter your {param} value: "))
            user_data[param] = user_value
        except ValueError:
            print("Invalid input. Skipping this parameter.")

# Clear previous data
    linked_list = LinkedList()
    queue = Queue()

# Process User Data
    print("\nProcessing Your Data:\n")
    for param, val in user_data.items():
        rec = check_deficiency(param, val)
        if rec:
            linked_list.add_node(param, val, rec)
            queue.enqueue(rec)

    linked_list.display()

    print("\nYour Recommendations:")
    while not queue.is_empty():
        print(f"-> {queue.dequeue()}")

if __name__ == "__main__":
    main()