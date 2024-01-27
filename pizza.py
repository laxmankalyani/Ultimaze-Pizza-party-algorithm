def calculate_pizza_distribution(num):
    slices = {
        "Large": 8,
        "Medium": 6,
        "Regular": 4,
        "Small": 1
    }
    l_p= num//slices["Large"]
    num %= slices["Large"]
    m_p = num // slices["Medium"]
    num %= slices["Medium"]
    r_p = num // slices["Regular"]
    num %= slices["Regular"]
    s_p = num // slices["Small"]
    num %= slices["Small"]

    total_slices = (l_p * slices["Large"] + (m_p * slices["Medium"]) + (r_p * slices["Regular"]) + (s_p * slices["Small"]))

    return l_p,m_p,r_p,s_p,total_slices


num = int(input())
l,m,r,s,total_slice=calculate_pizza_distribution(num)
print(f"if there are {num} individuals")
print(f"1. we wil have {l} large pizza")
print(f"2. we wil have {m} medium pizza")
print(f"3. we wil have {r} regular pizza")
print(f"4. we wil have {s} small pizza")
print("Total slices needed",total_slice)


