def find_gcd(ekah, dvau):
    if dvau == 0:
        return ekah

    print(dvau)

    return find_gcd(dvau, ekah % dvau)
    # Using Euclidean Algo, here second number is used becuase we want to print the reminder as in Euclidean algo reminder is the GCD.


print(find_gcd(45, 30))
