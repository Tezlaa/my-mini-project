from gsm import Gsm


if __name__ == "__main__":
    main = Gsm()

    all_connect = main.get_all_connect()
    
    print(all_connect, end="\n\n")
    
    for module in all_connect:
        connect = main.connect_gsm(module)
        if connect != "Error":
            main.check()
            main.close()
        else:
            print(f'{module} - error')
    
    input("end")
    
    