from .manager import Customer

def announce_join(customer: Customer, rank: int, lane_name: str):
    """Announces when a customer joins the queue."""
    message = (
        f"Welcome, {customer.name}! "
        f"You have been added to the {lane_name} lane. "
        f"Your current rank in the lane is: {rank}."
    )
    print(message)
    return message

def announce_serve(customer: Customer, lane_name: str):
    """Announces when it's a customer's turn to be served."""
    if not customer:
        message = f"The {lane_name} lane is currently empty."
    else:
        message = (
            f"NOW SERVING: {customer.name} (ID: {customer.customer_id}) "
            f"from the {lane_name} lane. Please proceed to the counter."
        )
    print("\n" + "="*len(message))
    print(message)
    print("="*len(message) + "\n")
    return message
