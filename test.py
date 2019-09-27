#!/usr/bin/python3

import bangdb
bangdb.run("my_db")

##Add Default User-Object
bangdb.ADD_USER_OBJECT("test_user", "", "my_db")

##Remove Default User-Object
bangdb.REMOVE_USER_OBJECT("test_user", "", "my_db")

##Macro Usage
new_user = "John"
bangdb.run("my_db_foo_backup")

bangdb.ADD_USER_OBJECT(new_user, "", "my_db")
bangdb.ADD_USER_OBJECT(new_user, "", "my_db_foo_backup")


bangdb.REMOVE_USER_OBJECT(new_user, "", "my_db")
bangdb.REMOVE_USER_OBJECT(new_user, "", "my_db2")

