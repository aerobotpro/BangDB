###
###
###
###
###
###
###
###
###

def run(db_name):
    new_db = False
    try:
        db = open(db_name, "r")
    except Exception as E:
        new_db = True
        db = open(db_name, "w+");db.close()
        pass
    if new_db == True:
        uid = GET_NEW_UID(db_name)
        try:
            o = open(file_name, "a");o.write(uid);o.close()
        except Exception:
            raise FileError('Failed To Write New Universal ID To File!\n'
                            'Check For Multiple Files Or Permission Obstacles.')
            exit(1)
    else:
        pass
    
class db:
    uid = GET_UID(db)['uid']
    user_count = GET_UID(db)['user_count'] 
                
def ADD_USER_OBJECT(USER, PASS, DB):
    from random import randint
    OID = str(USER+str(randint(0, 500000)))
    a = open(DB, "a");a.write(str(f"{OID},{USER},{PASS}"));a.close()

def REMOVE_USER_OBJECT(OID, DB):
    with open(DB, "r") as f:
        lines = f.readlines()
    with open(DB, "w") as f:
        for line in lines:
            if line.strip("\n") != OID:
                pass

def GET_UID(db):
    d = open(db, "r")
    user_count = int(len(d.split("\n")) - 1)
    uid = str(b.readlines()[0]);d.close()
    return uid, user_count
    
def GET_NEW_UID(file_name):
    from random import randint
    p1 = bytearray(randint(0, 256), randint(0, 256), randint(0, 256))
    p2 = bytearray(randint(0, 256), randint(0, 256), randint(0, 256))
    p3 = bytearray(randint(0, 256), randint(0, 256), randint(0, 256))
    p4 = bytearray(randint(0, 256), randint(0, 256), randint(0, 256))
    a1 = bytearray(p1, p2);a2 = bytearray(p3, p4)
    uid = str(bytearray(a1, a2).decode("utf-8"))                    
    return uid
                

