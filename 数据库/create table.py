import pymysql
db=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='python',
    charset='utf8'
)

#db=pymysql.connect("localhost","root","123456","python")

cursor=db.cursor()

sql="""
    create table student(
    id smallint(4) unsigned not null primary key  auto_increment,
    name char(40) null,
    course char(40) null) 
"""
try:
    cursor.execute(sql)
    db.commit()
    print("创建成功")
except:
    db.rollback()
    print("创建失败")

db.close()