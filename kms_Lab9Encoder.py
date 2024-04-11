def encode(password):
    pass_list = list(str(password))
    new_pass = ''
    for each_num in pass_list:
        each_num = str(int(each_num)+3)
        new_pass += each_num[-1]
    return int(new_pass)


if __name__ == '__main__':
  while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    choice = int(input("Please enter an option: "))
    if choice == 1:
      password = input("Please enter your password to encode: ")
      encoded_pass = encode(password)
      print("Your password has been encoded and stored!\n")
    elif choice == 2:
      print(f"The encoded password is {encoded_pass}, and the original password is {password}.")
    elif choice == 3:
      quit()

