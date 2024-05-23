# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],  #딕셔너리 내에 리스트
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")