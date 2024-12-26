# file_hashing.py - Generate File Hash
import hashlib

def hash_file(file_path):
    """
    Generates SHA256 hash for a given file.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()
