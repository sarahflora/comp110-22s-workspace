"""Trying out dictionaries."""

schools = {}
print(schools)

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")