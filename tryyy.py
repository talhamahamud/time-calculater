def add_time(inp, inp1):
    f1 = inp.split(' ')  # for inp
    f2 = f1[0].split(':')  # for inp
    list_time = map(int, f2)  # for f2
    int_time = list(list_time)  # for list_time

    s1 = inp1.split(':')  # for inp1
    s1_int = map(int, s1)  # for s1
    s1_list = list(s1_int)  # for s1

    # we added two number of 'int_times' and 's1_list'
    j = [int_time[0]+s1_list[0], int_time[1]+s1_list[1]]

    if j[0]<12 and j[1]<60 and f1[1] =="AM":
        print(f"{j[0]}:{j[1]} AM")
    
    elif j[0]<12 and j[1]<60 and f1[1] =="PM":
        print(f"{j[0]}:{j[1]} PM")
    
    elif j[0]>=12 and j[1]<60 and f1[1]=="AM":
        if j[0]>=24:
            dd=j[0]/24#A thing for find a day, sometime can't do its work *we are working on hour
            ff=dd-int(dd) # After point *we are working on hour
            hh=dd-ff # Before point *we are working on hour
            kk=j[0]-(hh*24) #hour in the expected day *we are working on hour
            #starting work on minute

            pp=j[1]/60
            mm=pp-int(pp) #After point
            nn=pp-mm #Before point 

            zz=int(kk+nn) #total hour
            aa=round(mm*60)#total minute
            if zz>11 and f1[1]=="AM":
                print(f"{zz-12}:{aa} PM ({int(hh)} days later)")
        else:
            print(f"{j[0]-12}:{j[1]} PM")
    
    elif j[0]>=12 and j[1]<60 and f1[1]=="PM":
        if j[0]>=24:
            dd=j[0]/24#A thing for find a day, sometime can't do its work *we are working on hour
            ff=dd-int(dd) # After point *we are working on hour
            hh=dd-ff # Before point *we are working on hour
            kk=j[0]-(hh*24) #hour in the expected day *we are working on hour
            #starting work on minute
            pp=j[1]/60
            mm=pp-int(pp) #After point
            nn=pp-mm #Before point 

            zz=int(kk+nn) #total hour
            aa=round(mm*60)#total minute
            if zz>11 and f1[1]=="PM":
                print(f"{zz-12}:{aa} AM ({int(hh+1)} days later)")
        else:
            print(f"{j[0]-12}:{j[1]} AM (next day)")

    elif j[0]<12 and j[1]>=60:
        n=j[1]/60
        p=n-int(n)#after point
        g=n-p#before point
        f=int(j[0]+g)#total hour
        d=round(p*60)#total minute

        if f<12 and d>=10 and f1[1]=="AM":
            print(f"{f}:{d} AM")
        elif f<12 and d<10 and f1[1]=="AM":
            print(f"{f}:0{d} AM")
        
        elif f<12 and d>=10 and f1[1]=="PM":
            print(f"{f}:{d} PM")
        elif f<12 and d<10 and f1[1]=="PM": 
            print(f"{f}:0{d} PM")
        
        elif f==12 and d>=10 and f1[1]=="PM":
            print(f"12:{d} AM (next day)")
        elif f==12 and d<10 and f1[1]=="PM":
            print(f"12:0{d} AM (next day)")
        
        elif f==12 and d>=10 and f1[1]=="AM":
            print(f"12:{d} PM")
        elif f==12 and d<10 and f1[1]=="AM":
            print(f"12:0{d} PM")
        
        elif f>12 and d>=10 and f1[1]=="AM":
            print(f"{f-12}:{d} PM")
        elif f>12 and d<10 and f1[1]=="AM":
            print(f"{f-12}:0{d} PM")
        
        elif f>12 and d>=10 and f1[1]=="PM":
            print(f"{f-12}:{d} AM (next day)")
        elif f>12 and d<10 and f1[1]=="PM":
            print(f"{f-12}:0{d} AM (next day)")

    elif j[0]>=13 and j[1]>=60:
        if j[0]>=24:
            dd=j[0]/24#A thing for find a day, sometime can't do its work *we are working on hour
            ff=dd-int(dd) # After point *we are working on hour
            hh=dd-ff # Before point *we are working on hour
            kk=j[0]-(hh*24) #hour in the expected day *we are working on hour
            #starting work on minute

            pp=j[1]/60
            mm=pp-int(pp) #After point
            nn=pp-mm #Before point 

            zz=int(kk+nn) #total hour
            aa=round(mm*60)#total minute

        elif j[0]<24:
            dd=j[0]-12
            #starting work on minute
            pp=j[1]/60
            mm=pp-int(pp) #After point
            nn=pp-mm #Before point 

            zz=int(dd+nn)#total hour
            aa=round(mm*60)#total minute
        
        if j[0]<24 and f1[1]=="AM":
            print (f"{zz}:{aa} PM")
        
        elif j[0]<24 and f1[1]=="PM":
            print(f"{zz}:{aa} AM (next day)")

        elif j[0]>24 and f1[1]=="AM":
            if zz>12:
                print(f"{zz-12}:{aa} PM ({int(hh)} days later)")
            elif zz==12:
                print(f"12:{aa} PM ({int(hh)} days later)")
            elif zz<=11:
                print(f"{zz}:{aa} AM ({int(hh)} days later)")

        elif j[0]>24 and f1[1]=="PM":
            if zz>12:
                print(f"{zz-12}:{aa} AM ({int(hh+1)} days later)")
            elif zz==12:
                print(f"12:{aa} AM ({int(hh+1)} days later)")
            elif zz<=11:
                print(f"{zz}:{aa} AM ({int(hh)})")

        

    print(j)

add_time('11:43 PM', '24:20')
