from gsm import Gms_conect


if __name__=="__main__":
    main = Gms_conect()

    print(main.get_all_connect())
    print(main.get_available_connect())
    main.connect_gms(main.get_available_connect()[0])
    
    main.check()
    
    main.close()
    input("end")
    