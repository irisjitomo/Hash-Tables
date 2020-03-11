import hashlib as hl

n = 10
key = b"string"
key2 = "string1".encode()
key3 = b"lunch"

index = hash(key) % 8
print(index)
index2 = hash(key2) % 8
print(index2)
index3 = hash(key3) % 8
print(index3)

# for i in range(n):
#     print(hash(key))
#     print(hl.sha256(key).hexdigest())

# for i in range(n):
#     print(hash(key2))