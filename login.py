
def login():
    print("=== LOGIN APLIKASI ===")

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == "admin" and password == "123":
        print("Login berhasil!")
    else:
        print("Username atau password salah!")


login()
