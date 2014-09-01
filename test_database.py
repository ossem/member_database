from model import OssemDB
import nfc_lib

table = "Members"
ossem_db = "ossem_members.db"
members_sql = """create table Members
         (MemberID integer,
         FirstName text,
         LastName text,
         Handle text,
         PhoneNumber text,
         EmailAddress text,
         NFCTag text,
         primary key(MemberID))"""

scans_sql = """create table NFCScans
        (NFCTag text,
        DateScanned text,
        TimeScanned text,
        primary key(NFCTag)) """

member_database = OssemDB()
def test_create_table():
    member_database.create_table(ossem_db, "Members", members_sql)
    member_database.create_table(ossem_db, "NFCScans", scans_sql)

test_create_table()
