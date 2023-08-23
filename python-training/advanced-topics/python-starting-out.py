# ---------- #
  # Bro Code #
# ---------- #



# ARGS  -   a parameter allows a function to take variable number of parameters 
#           by packing them into a Tuple (single asterik)

def add(*parameters):
    sum = 0
    for x in parameters:
        sum += x
    print(sum)

add(3,6,6,4,1)

# KWARGS    -   a parameter allows a function to take variable number of parameters 
#               by packing them into a Dictionary (double asteriks)

def user(**parameters):
    print("Welcome ")
    for key, value in parameters.items():
        print(value)

user("bobbyabuchi", "bobby@mail.com")