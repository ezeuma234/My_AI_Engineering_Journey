from collections import deque

customers = deque()


def add_customer(name):
    customers.append(name)

def serve_customer():
   if customers:
        customer =  customers.popleft()
        print("Serving:", customer)
   else:
       print("No customers waiting.")


    

add_customer("Uma")
add_customer("John")
add_customer("Eileen")

print(customers)

serve_customer()
serve_customer()
serve_customer()

print(customers)