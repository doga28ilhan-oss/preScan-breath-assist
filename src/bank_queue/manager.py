
class Customer:
    """Represents a customer in the bank queue."""
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name

class QueueManager:
    """Manages the queue of customers and assigns ranks."""
    def __init__(self, lane_name: str = "General"):
        self.lane_name = lane_name
        self.queue = []
        self.serving_count = 0

    def join_queue(self, customer: Customer) -> int:
        """Adds a customer to the queue and returns their rank."""
        self.queue.append(customer)
        return len(self.queue)

    def call_next(self) -> Customer:
        """Calls the next customer in the queue."""
        if not self.queue:
            return None
        customer = self.queue.pop(0)
        self.serving_count += 1
        return customer

    def get_queue_length(self) -> int:
        """Returns the current number of people in the queue."""
        return len(self.queue)
