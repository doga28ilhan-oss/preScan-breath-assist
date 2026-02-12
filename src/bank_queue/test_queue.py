import pytest
from src.bank_queue.manager import Customer, QueueManager
from src.bank_queue.announcer import announce_join, announce_serve

def test_customer_creation():
    customer = Customer("123", "John Doe")
    assert customer.customer_id == "123"
    assert customer.name == "John Doe"

def test_queue_joining():
    manager = QueueManager("Lane 1")
    customer1 = Customer("C1", "Alice")
    customer2 = Customer("C2", "Bob")

    rank1 = manager.join_queue(customer1)
    assert rank1 == 1
    assert manager.get_queue_length() == 1

    rank2 = manager.join_queue(customer2)
    assert rank2 == 2
    assert manager.get_queue_length() == 2

def test_call_next():
    manager = QueueManager("Lane 1")
    customer1 = Customer("C1", "Alice")
    manager.join_queue(customer1)

    called_customer = manager.call_next()
    assert called_customer.customer_id == "C1"
    assert manager.get_queue_length() == 0
    assert manager.serving_count == 1

def test_empty_queue_call():
    manager = QueueManager("Lane 1")
    called_customer = manager.call_next()
    assert called_customer is None

def test_announcements():
    customer = Customer("C1", "Alice")
    join_msg = announce_join(customer, 1, "Main")
    assert "Alice" in join_msg
    assert "rank in the lane is: 1" in join_msg

    serve_msg = announce_serve(customer, "Main")
    assert "NOW SERVING: Alice" in serve_msg
    assert "ID: C1" in serve_msg

def test_empty_announcement():
    serve_msg = announce_serve(None, "Main")
    assert "empty" in serve_msg
