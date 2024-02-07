def change_domain(email, new_domain):
    username = email.split('@')[0]
    return f"{username}@{new_domain}"
print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp') == 'spam@ipp.u-tokyo.ac.jp')