import sqlite3
from view import Frontend
from model import OssemDB

user_interface = Frontend()
member_database = OssemDB()
keep_running = ""
while keep_running != "q":
    keep_running = user_interface.select_option()
    if keep_running == "1":
        member_database.new_member()
    if keep_running == "2":
        member_database.print_all_members()
