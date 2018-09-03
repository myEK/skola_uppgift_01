# skola_uppgift_01

class dag:
        // Classem 
        // importera tiden
        from datetime import datetime

        now = datetime.now() // hemmtar tiden
        mm = str(now.month)  // Månader
        dd = str(now.day)    // Dagar
        yyyy = str(now.year) // år
        hour = str(now.hour) // tima
        me = str(now.minute) // minuter
        ss = str(now.second) // sekund
        print (dd + "/" + mm + "-" + yyyy + "  " + hour + ":" + me + ":" + ss)


dag() // köra klassens funtion "dag"
