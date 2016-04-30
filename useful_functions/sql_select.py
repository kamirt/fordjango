



"""Two tables — users and messages:
 
users [ uid, name ]
messages [ uid, msg ]

Use sqlite3 and create a database with relevant tables on SQL. And another one SQL-request must 
return selection from this two fields: username and number of messages.
""" 



CREATE  TABLE users(uid INTEGER PRIMARY KEY  NOT NULL  UNIQUE , name VARCHAR DEFAULT 255)
CREATE  TABLE messages (msg TEXT, uid INTEGER);
SELECT name, count (msg) FROM users JOIN messages ON users.uid = messages.uid group by name;























