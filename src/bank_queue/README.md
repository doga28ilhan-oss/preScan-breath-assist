# Bank Queue System (Paperless Numerator)

This module implements a paperless queuing system for banks. It allows customers to join a queue by providing their ID and name, and then announces their turn by their rank and name.

## Features

- **Customer Registration**: Takes ID and Name as input.
- **Queue Management**: Automatically assigns ranks and manages the serving order.
- **Announcements**: Displays clear messages when a customer joins or is called.
- **Paperless**: Designed to replace traditional paper-based numerator systems.

## Architecture

- `manager.py`: Contains the `Customer` and `QueueManager` classes.
- `announcer.py`: Handles formatting and displaying queue announcements.
- `app.py`: Simple CLI interface for interacting with the system.
- `test_queue.py`: Unit tests for the system.

## Usage

To run the CLI application:

```bash
python -m src.bank_queue.app
```

## Running Tests

To run the unit tests:

```bash
pytest src/bank_queue/test_queue.py
```
