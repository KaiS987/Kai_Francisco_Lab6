def encoder(password):
    pass_list = list(str(password))
    new_pass = ''
    for each_num in pass_list:
        each_num = str(int(each_num)+3)
        new_pass += each_num[-1]
    return int(new_pass)
