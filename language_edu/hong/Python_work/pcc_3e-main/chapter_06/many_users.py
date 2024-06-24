users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'job': 'scientest',
        'salary': 1000,
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'job': 'developer',
        'salary': 20000,
        },

    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    for k,v in user_info.items():
        print(f"key = {k}, value ={v}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")