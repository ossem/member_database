import sqlite3
import nfc_lib

class OssemDB():
    def __init__(self):
        self.ossem_db = "ossem_members.db"

    def create_table(self, db_name, table_name, sql):
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            cursor.execute("select name from sqlite_master where name=?",(table_name,))
            result = cursor.fetchall()
            keep_table = True
            if len(result) == 1:
                response = input("The table {0} already exists, do you wish to recreate it(y/n): ".format(table_name))
                if response == "y":
                    keep_table = False
                    print("The {0} table wil be recreated - all existing data will be lost".format(table_name))
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                else:
                    print("The existing table was kept")
            else:
                keep_table = False
            if not keep_table:
                cursor.execute(sql)
                db.commit()

    def new_member(self):
        first_name = input("Enter member's first name: ")
        last_name = input("Enter member's last name: ")
        handle = input("Enter member's handle: ")
        phone_number = input("Enter member's phone number: ")
        email_address = input("Enter member's email address: ")
        print("Fake NFC tag being generated...")
        nfc_tag = nfc_lib.create_nfc_tag()
        new_member = (first_name, last_name, handle, phone_number, email_address, nfc_tag)
        self.add_member(new_member, self.ossem_db)
        tag_to_write = (nfc_tag,)
        self.add_tag((tag_to_write), self.ossem_db)

    def add_member(self, values, db_name):
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            sql = "insert into Members (FirstName, LastName, Handle, PhoneNumber, EmailAddress, NFCTag) values (?,?,?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()

    def add_tag(self, values, db_name):
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            sql = "insert into NFCScans (NFCTag) values (?)"
            cursor.execute(sql,values)
            db.commit()

    def select_all_members(self, db_name):
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            cursor.execute("select * from Members")
            members = cursor.fetchall()
            return members

    def print_all_members(self):
        for member in self.select_all_members(self.ossem_db):
            print(member)
