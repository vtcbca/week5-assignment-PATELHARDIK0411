C:\Users\scott>cd..

C:\Users>cd..

C:\>cd sqlite3

C:\sqlite3>.exit
'.exit' is not recognized as an internal or external command,
operable program or batch file.

C:\sqlite3>.quite
'.quite' is not recognized as an internal or external command,
operable program or batch file.

C:\sqlite3>sqlite3 student.db
SQLite version 3.36.0 2021-06-18 18:36:39
Enter ".help" for usage hints.
sqlite> create table student
   ...> (
   ...> id int primarykey,
   ...> f_name varchar(20),
   ...> l_name varchar(30),
   ...> address varchar(10),
   ...> pin_code varchar(50),
   ...> DOB varchar(40),
   ...> age varchar(30),
   ...> gender varchar(20),
   ...> stream varchar(10),
   ...> sem int
   ...> );
sqlite> insert into student values(1,'Hardik'.'patel','mota','394345','04-11-2004','19','male','BCA',3);
Error: no such column: Hardik.patel
sqlite> insert into student values(1,'Hardik','patel','mota','394345','04-11-2004','19','male','BCA',3);
sqlite> insert into student values(2,'dev','patel','palsana','394345','29-06-2005','18','male','BCA',3);
sqlite> insert into student values(2,'deep','patel','bardoli','392345','11-04-2002','20','male','BCA',3);
sqlite> insert into student values(2'Heer','patel','bardoli','392345','15-06-2005','18','fmale','BBA',3);
sqlite> insert into student values(2,'Hanee','panchal','surat','394180','02-07-2005','17','fmale','BBA',2);
sqlite> insert into student values(2,'ishani','mistry','surat','394180','01-01-2004','18','fmale','BBA',1);
sqlite> insert into student values(4,'riya','mistry','bardoli','394345','12-12-2003','20','fmale','BCA',4);
sqlite> insert into student values(5,'cute girl','patel','bardoli','394345','11-11-2002','21','fmale','BBA',6);
sqlite> insert into student values(6,'priya','patel','bardoli','394345','10-10-2004','19','fmale','BCA',5);
sqlite> insert into student values(7,'mansi','patel','bardoli','394345','17-03-2004','18','fmale','BBA',4);
sqlite> select*from student;
1|Hardik|patel|mota|394345|04-11-2004|19|male|BCA|3
2|dev|patel|palsana|394345|29-06-2005|18|male|BCA|3
2|deep|patel|bardoli|392345|11-04-2002|20|male|BCA|3
2|Heer|patel|bardoli|392345|15-06-2005|18|fmale|BBA|3
2|Hanee|panchal|surat|394180|02-07-2005|17|fmale|BBA|2
3|ishani|mistry|surat|394180|01-01-2004|18|fmale|BBA|1
4|riya|mistry|bardoli|394345|12-12-2003|20|fmale|BCA|4
5|cute girl|patel|bardoli|394345|11-11-2002|21|fmale|BBA|6
6|priya|patel|bardoli|394345|10-10-2004|19|fmale|BCA|5
6|mansi|patel|bardoli|394345|17-03-2004|18|fmale|BBA|4
sqlite>