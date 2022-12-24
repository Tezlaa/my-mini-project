from gsm import Gms_conect


if __name__=="__main__":
    main = Gms_conect()

    all_connect = main.get_all_connect()
    
    print(all_connect, end="\n\n")
    
    for module in all_connect:
        
        connect = main.connect_gms(module)
        
        if connect != "Error":
            main.check()

            main.close()
        else:
            print(f'{module} - error')
    
    input("end")
    