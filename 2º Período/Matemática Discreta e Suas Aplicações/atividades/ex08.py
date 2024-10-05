A = {1,2,3}
C = {1,2,3,4,5}
D = {5,3,4,2,1}

print(f"A ⊂ C = {A.issubset(C) and  A != C}")
print(f"D ⊆  C = {D.issubset(C)}")