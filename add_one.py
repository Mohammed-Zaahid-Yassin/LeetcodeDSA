n = int(input())
values = set(map(int, input().split())) if n > 0 else set()
new_value = int(input())

# Add new_value to values.
values.add(new_value)
print(len(values))
print(*sorted(values))
