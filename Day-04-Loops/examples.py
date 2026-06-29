# ==============================
# LOOPS EXAMPLES
# ==============================

# Example 1: The 'for' Loop with range
print("--- FOR LOOP ---")
for i in range(5):
    print(f"Count: {i}")

# Example 2: The 'while' Loop
print("\n--- WHILE LOOP ---")
battery = 100
while battery > 90:
    print(f"Battery at {battery}%. Phone is running.")
    battery -= 5
print("Battery low!")

# Example 3: The 'break' Statement
print("\n--- BREAK ---")
for i in range(10):
    if i == 4:
        print("Hit number 4! Breaking out!")
        break
    print(i)

# Example 4: The 'continue' Statement
print("\n--- CONTINUE ---")
for i in range(5):
    if i == 2:
        print("Skipping 2!")
        continue
    print(i)
