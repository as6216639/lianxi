#1.导入python链接mysql数据库的库
import pymysql
#2.创建connection链接对象
db=pymysql.connect("localhost","root","123456","python")
#3.创建cursor对象
cursor=db.cursor()
#4.创建sql语句
sql="""
    create table student(
    id smallint(4) unsigned not null primary key auto_increment,
    name varchar(40) not null,
    course varchar(40) not null)
    """
try:
    #5.执行sql语句
    cursor.execute(sql)
    #6.提交到数据库
    db.commit()
    print("创建成功")
except:
    #.假如创建数据库失败，应该事务回滚
    db.rollback()
    print("创建失败")
#8.关闭数据库
db.close()