# import passwordGen as pg
#
# password = pg.Password()
# print(password.generating_password())

from passwordGen import main

password = main()
print("The password is generated successfully")
print(f"Password:\n{password}")
