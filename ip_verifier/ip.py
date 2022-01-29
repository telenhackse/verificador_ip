import time


def ip_checker(ip_address):
    try:
        separated_address = ip_address.split('.')
        valid_ip = 0
        for i in separated_address:
            if int(i) >= 0 and int(i) <= 255:
                valid_ip += 1
        if valid_ip == 4:
            return True
        else:
            return False
    except:
        return False


print("███████████████████████████████████████")
user_in = input("Insera una ip " "ejemplo: 172.217.192.101: ")


if ip_checker(user_in):
    print("█████████████████████████████████████████████████████")
    print(f"Estupendo!! {user_in} es una direccion ip valida")
    print("█████████████████████████████████████████████████████")

else:
    print("█████████████████████████████████████████████████████")
    print(f"Que mal! {user_in} no es una direccion ip valida") 
    print("█████████████████████████████████████████████████████")