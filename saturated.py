 """You are provided with a number ’n’. Your task is to tell whether that number is saturated. 
 A saturated number is a number which is made by exactly two digits."""

 ip_num = input()
    res = ""
    for i in range(len(ip_num)):
        if ip_num[i] not in res:
            res = res + ip_num[i]
    
    if len(res) > 2:
        print("Unsaturated")
    else:
        print("Saturated")

    print(pk_find_min(ip_list))
