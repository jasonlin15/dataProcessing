## Overview
This project implements an in-memory key-value database in Python that supports transactional operations. The database allows for transactions to be initiated, committed, or rolled back, ensuring atomic updates to the key-value pairs.

## How to Run the Code

### Prerequisites
- Python 3.x installed on your machine.

### Instructions
1. **Clone the Repository**:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Sample Usage**:
   - Ensure you are in the directory containing the code files.
   - Open a terminal or command prompt and run the following command:
     ```sh
     python sample_usage.py
     ```
   - The sample usage script demonstrates starting a transaction, adding key-value pairs, committing, and rolling back transactions.

3. **Using the Database**:
   - You can create your own scripts to interact with the `KeyValueDatabase` class. Import the class and follow the sample usage pattern to perform transactions.

## Sample Usage
Here’s an example of how to use the `KeyValueDatabase`:

```python
from key_value_database import KeyValueDatabase

db = KeyValueDatabase()

# Start a transaction
db.begin_transaction()

# Perform some operations
db.put("key1", 100)
db.put("key2", 200)
print(db.get("key1"))  # Should print 100

# Commit the transaction
db.commit()

# Check main data
print(db.get("key1"))  # Should print 100
```

## Assignment Enhancements for the Future
To make this assignment an “official” assignment, consider the following modifications:
1. **Clarify Instructions**: Clearly define the behavior when multiple transactions are attempted to start simultaneously and the expected behavior of the `get` method within and outside of transactions.
2. **Additional Methods**: Include additional methods such as `delete(key)` for completeness.
3. **Automated Testing**: Integrate automated tests to verify the functionality, including edge cases like nested transactions and concurrent access.
