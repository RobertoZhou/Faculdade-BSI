C = {2, 3, 4}

print(f"C ⊂ C = {C.issubset(C)}")

print("{1, 2}", "∈ C = {}".format({1, 2} in C))  # Falso

print(f"∅ ⊂ C = {set().issubset(C)}")