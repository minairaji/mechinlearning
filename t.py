users = []

while True:
    print("\n1- ثبت کاربر")
    print("2- نمایش کاربران")
    print("3- خروج")

    choice = input("انتخاب: ")

    if choice == "1":
        name = input("نام: ")
        family = input("نام خانوادگی: ")
        age = int(input("سن: "))
        city = input("شهر: ")

        user = {
            "name": name,
            "family": family,
            "age": age,
            "city": city
        }

        users.append(user)
        print("کاربر ثبت شد.")

    elif choice == "2":
        if len(users) == 0:
            print("هیچ کاربری ثبت نشده است.")
        else:
            print("\n===== لیست کاربران =====")
            for user in users:
                print("--------------------")
                print("نام:", user["name"])
                print("نام خانوادگی:", user["family"])
                print("سن:", user["age"])
                print("شهر:", user["city"])

    elif choice == "3":
        print("خروج از برنامه")
        break

    else:
        print("گزینه نامعتبر است.")