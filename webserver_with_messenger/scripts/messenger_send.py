import cgitb; cgitb.enable()
import cgi; fields = cgi.FieldStorage()
import sqlite3
import UserAccountSet
from UserAccountPropertySet import UserAccount
import Session

print("""\
Content-Type: text/html
\r\n
""")

recipient = fields.getvalue("recipient")
message = fields.getvalue("message")

if recipient is None or message is None: 
    print(open("messenger_send.html", "r").read().replace("<?recipient>", recipient or "").replace("<?message>", message or ""))
else:
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('create table if not exists messages (ID Integer primary key autoincrement, sender String, recipient String, message String)')
#Can't figure out how to get the sender's account id from the session.
    sender = Session.get_account_id()
    c.execute('insert into messages (sender, recipient, message) values (' + 
    sender + ',' + recipient + ',' + message + ')')
    print(open("messager_sent_message.html", "r").read()
    .replace("<?message>", message)
    .replace("<?recipient>", recipient)
    .replace("<?sender>", sender))
    
