import uuid
import hashlib

# Generate a UUID
def short_id():
    unique_id = uuid.uuid4()

    # Hash the UUID using SHA-256
    hashed_id = hashlib.sha256(unique_id.bytes).hexdigest()

    # Take the first 8 characters of the hash for a shorter ID
    short_id = hashed_id[:8]
