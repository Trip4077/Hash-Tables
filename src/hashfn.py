#{
# array: []
# hashFunction: () --> return index in array
# }

def myHash1(key):
    return len( key )

# dog --> returs index 3

# Pros
# Deterministic
# Noninvertible

# Cons
# Not unique

def myHash2(key):
    return ( len( key ) % length_of_array ) + time.now()

# Pro
# Noninvertible
# Unique

# Con
# Not Deterministic

def djb2(key):
    our_salt = 5381
    hash_value = 0

    for char in key:
        hash_value += (our_salt << 5) + our_salt + ord( char )

    return hash_value



print( djb2("Mike") )