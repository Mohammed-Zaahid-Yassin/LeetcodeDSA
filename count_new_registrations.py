n, m = map(int, input().split())

registered = set()

if n > 0:
    registered.update(map(int, input().split()))

new_registrations = 0

if m > 0:
    incoming = map(int, input().split())
    for user_id in incoming:
        if user_id not in registered:
            registered.add(user_id)
            new_registrations += 1

print(new_registrations)
print(len(registered))
