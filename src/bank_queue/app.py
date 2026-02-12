import sys
from src.bank_queue.manager import Customer, QueueManager
from src.bank_queue.announcer import announce_join, announce_serve

def main():
    manager = QueueManager("Main Lane")
    print("--- Bank Numerator System (Paperless) ---")

    while True:
        print("\n1. Join Queue")
        print("2. Call Next Customer")
        print("3. Check Queue Status")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            customer_id = input("Enter your ID: ")
            customer = Customer(customer_id, name)
            rank = manager.join_queue(customer)
            announce_join(customer, rank, manager.lane_name)

        elif choice == '2':
            customer = manager.call_next()
            announce_serve(customer, manager.lane_name)

        elif choice == '3':
            print(f"Current queue length: {manager.get_queue_length()}")

        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
