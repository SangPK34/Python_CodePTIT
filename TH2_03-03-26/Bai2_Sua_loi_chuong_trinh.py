t_t = input()
h_k_c = t_t[-2:].lower()
if h_k_c == "py":
    print(t_t, "là tệp mã nguồn Python")
else:
    print(t_t, "không phải là tệp mã nguồn Python")