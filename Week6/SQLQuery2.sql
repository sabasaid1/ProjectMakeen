DROP TABLE regist;
DROP TABLE issuing;
DROP TABLE CBlink;
DROP TABLE course;
DROP TABLE bookTopic;
DROP TABLE book;
DROP TABLE employee;
DROP TABLE student;
DROP TABLE borrower;
DROP TABLE department;
DROP TABLE college;

CREATE TABLE college  (cl_code character(3),
                       cl_name varchar(40) NOT NULL,
                       cl_dean varchar(30),
                      constraint college_pk_clcode PRIMARY  KEY (cl_code));

CREATE TABLE department  (dp_code character(4),
                          dp_name varchar(40) NOT NULL,
                          dp_hod varchar(30),
                          dp_col character(3), 
                      constraint department_pk_dpcode PRIMARY  KEY (dp_code),
                      constraint department_fk_dpcol FOREIGN KEY (dp_col) 
                               REFERENCES college (cl_code));   

CREATE TABLE borrower  (br_id numeric(6),
                        br_name varchar(40) NOT NULL,
                        br_dept character(4),
                        br_mobile# numeric(8), 
                        br_city varchar(20),
                        br_house# character(4),
                        br_type character(1),
                        constraint borrower_pk_brid PRIMARY  KEY (br_id),
                        constraint borrower_ch_brid CHECK (br_id > 0),
                        constraint borrower_ch_mobile# CHECK (br_mobile# > 90000000),
                        constraint borrower_ch_type CHECK (br_type in ('S','E')),
                        constraint borrower_fk_brdept FOREIGN KEY (br_dept) 
                               REFERENCES department (dp_code));

CREATE TABLE student (st_id numeric(6),
                      st_major varchar(30),
                      st_cohort numeric(4) not null,
                      constraint student_pk_stid PRIMARY  KEY (st_id),
                      constraint student_ch_stid CHECK (st_id > 0),
                      constraint student_fk_stid FOREIGN KEY (st_id) 
                               REFERENCES borrower (br_id));


CREATE TABLE employee (em_id numeric(6),
                       em_office# varchar(30),
                       em_ext# numeric(4) not null,
                      constraint employee_pk_emid PRIMARY  KEY (em_id),
                      constraint employee_ch_emid CHECK (em_id > 0),
                      constraint employee_ch_ext# CHECK (em_ext# > 1000),
                      constraint employee_fk_emid FOREIGN KEY (em_id) 
                               REFERENCES borrower (br_id)); 

CREATE TABLE book (bk_id numeric(6),
                   bk_title varchar(50) NOT NULL,
                   bk_edition numeric(2),
                   bk_#ofPages numeric(4),
                   bk_totalCopies numeric(5),
                   bk_remCopies numeric(5),
                   constraint book_pk_bkid PRIMARY  KEY (bk_id),
                   constraint book_ch_bkid CHECK (bk_id > 0),
                   constraint book_ch_bk#ofPages CHECK (bk_#ofPages > 0)); 

CREATE TABLE bookTopic (tp_bkid numeric(6),
                        tp_desc varchar(30) NOT NULL,
                        constraint bookTopic_fk_tpBkID FOREIGN KEY (tp_bkid) 
                               REFERENCES book (bk_id));    

CREATE TABLE course (cr_code character(8),
                   cr_title varchar(40) NOT NULL,
                   cr_CH numeric(2),
                   cr_#ofSec numeric(2),
                   cr_dept character(4),
                   constraint course_pk_crcode PRIMARY  KEY (cr_code),
                   constraint course_ch_crCH CHECK (cr_CH > 0),
                   constraint course_ch_cr#ofSec CHECK (cr_#ofSec > 0),
                   constraint course_fk_crDept FOREIGN KEY (cr_dept) 
                               REFERENCES department (dp_code));   

CREATE TABLE CBlink (li_crCode character(8),
                     li_bkId numeric(6),
                     li_usage character(1),
                     constraint CBlink_ch_liUsage CHECK (li_usage IN ('T','R')),
                     constraint CBlink_fk_liCrCode FOREIGN KEY (li_crCode) 
                               REFERENCES course (cr_code),
                     constraint CBlink_fk_liBkId FOREIGN KEY (li_bkID) 
                               REFERENCES book (bk_id));

CREATE TABLE regist (re_brID numeric(6),
                     re_crCode character(8),
                     re_semester character(6) NOT NULL,
                     constraint regist_fk_reBrID FOREIGN KEY (re_brID) 
                               REFERENCES borrower (br_id),
                     constraint regist_fk_reCrCode FOREIGN KEY (re_crCode) 
                               REFERENCES course (cr_code));       
                              

CREATE TABLE issuing (is_brID numeric(6),
                      is_bkID numeric(6),
                      is_dateTaken DATE  NOT NULL,
                      is_dateReturn DATE,
                      constraint issuning_ch_isDataReturn CHECK (is_dateReturn >= is_dateTaken),
                      constraint issuing_fk_isBrID FOREIGN KEY (is_brID) 
                               REFERENCES borrower (br_id),
                     constraint issuing_fk_isBkID FOREIGN KEY (is_bkID) 
                               REFERENCES book (bk_id));
                               

INSERT INTO college VALUES('COM', 'Economy', 'Prof. Fahim');

INSERT INTO college VALUES('SCI', 'Science', 'Prof. Salma');

INSERT INTO college VALUES('EDU', 'Education', 'Dr. Hamad');

INSERT INTO college VALUES('ART', 'Arts', 'Dr. Abdullah');



INSERT INTO department VALUES('INFS','Information Systems','Dr. Kamla','COM');

INSERT INTO department VALUES('FINA','Finance','Dr. Salim','COM');

INSERT INTO department VALUES('COMP','Computer Science','Dr. Zuhoor','SCI');

INSERT INTO department VALUES('BIOL','Biology','Dr. Othman','SCI');

INSERT INTO department VALUES('HIST','History','Dr. Said','EDU');

INSERT INTO department VALUES('CHEM', 'Chemistry', 'Dr. Alaa', 'SCI');



INSERT INTO borrower VALUES (92120,'Ali','INFS',99221133,'Seeb','231','S');

INSERT INTO borrower VALUES (10021,'Said','INFS',91212129,'Seeb','100','S');

INSERT INTO borrower VALUES (10023,'Muna','FINA', NULL, 'Barka','12','S');

INSERT INTO borrower VALUES (3000,'Mohammed','COMP',90000009,'Seeb','777','E');

INSERT INTO borrower VALUES (4000,'Nasser','INFS',99100199,'Sur','11','E');



INSERT INTO student VALUES(92120,'INFS',2012);

INSERT INTO student VALUES(10021,'INFS',2015);

INSERT INTO student VALUES(10023,'FINA',2015);



INSERT INTO employee VALUES(3000,'12',2221);

INSERT INTO employee VALUES(4000,'15',1401);



INSERT INTO book VALUES(1001,'Database1',2,450,150,65);

INSERT INTO book VALUES(1002,'Database2',3,300,100,100);

INSERT INTO book VALUES(2001,'Intro. to Finanace',1,300,75,40);

INSERT INTO book VALUES(3001,'Basic Op Mgmt',1,320,100,77);

INSERT INTO book VALUES(3002,'Chemistry Book',2,500,100,80);

INSERT INTO book VALUES(4001,'Biology',1,345,100,100);

INSERT INTO book VALUES(3003,'Management I',2,560,44,34);

INSERT INTO book VALUES(1003,'Java Prog.',3,555,50,50);



INSERT INTO bookTopic VALUES (1001,'Basic DB Skills');

INSERT INTO bookTopic VALUES (1001,'ERD');

INSERT INTO bookTopic VALUES (1001,'EERD');

INSERT INTO bookTopic VALUES (1002,'SQL');

INSERT INTO bookTopic VALUES (1002,'Pl/SQL');

INSERT INTO bookTopic VALUES (3001,'Management Skills');



INSERT INTO course VALUES('COMP4201', 'Database1', 3, 1,'COMP');

INSERT INTO course VALUES('COMP4202', 'Database2', 3, 2,'COMP');

INSERT INTO course VALUES('BIOL1000', 'Intro. To Biology', 3, 5,'BIOL');

INSERT INTO course VALUES('CHEM2000', 'Advanced Chemistry', 2, 2,'CHEM');



INSERT INTO CBlink VALUES('COMP4201',1001,'T');

INSERT INTO CBlink VALUES('COMP4201',1002,'R');

INSERT INTO CBlink VALUES('COMP4202',1002,'T');

INSERT INTO CBlink VALUES('BIOL1000',4001,'T');

INSERT INTO CBlink VALUES('CHEM2000',3002,'R');



INSERT INTO regist VALUES(92120,'COMP4201','FL2015');

INSERT INTO regist VALUES(10021,'COMP4202','FL2015');

INSERT INTO regist VALUES(92120,'BIOL1000','FL2015');

INSERT INTO regist VALUES(92120,'COMP4202','FL2016');

INSERT INTO regist VALUES(10021,'CHEM2000','FL2016');



INSERT INTO issuing VALUES(92120, 1001, '01-Sep-2015', '30-Oct-2015');

INSERT INTO issuing VALUES(10021, 1002, '30-Oct-2016', NULL);

INSERT INTO issuing VALUES(92120, 1002, '21-Feb-2015', '01-Jan-2016');

INSERT INTO issuing VALUES(92120, 3002, '30-Mar-2016', NULL);

INSERT INTO issuing VALUES(10021, 3002, '01-Dec-2014', NULL);

/*LAB4 6.a*/

Select * from course;

/*LAB4 6.b*/

Select * from department where dp_code like 'C%' ;
/*LAB4 6.c*/
Select * from employee where em_id = (Select Max(em_id)from employee);
/*LAB4 6.d*/



SELECT b.dp_name, c.cl_name
FROM department b, college c
WHERE b.dp_col = c.cl_code
ORDER BY b.dp_name;



SELECT d.dp_name, c.cl_name
FROM department d
JOIN college c ON d.dp_col = c.cl_code;

/*LAB4 6.e*/

SELECT bk_title , AVG(bk_totalCopies)
FROM book
GROUP BY bk_title

SELECT bk_title, SUM(bk_totalCopies) FROM book GROUP BY bk_title;SELECT bk_title , COUNT(bk_totalCopies)
FROM book
GROUP BY bk_title;


select * from book

/* lab5 Q1: a*/
ALTER TABLE regist ADD re_serial# INT;

EXEC sp_help 'regist';
/* lab5 Q1: b*/
CREATE SEQUENCE seq_regist_serial#
START WITH 1
INCREMENT BY 2 ;
/* lab5 Q1: c*/
UPDATE regist
SET re_serial# = NEXT VALUE FOR seq_regist_serial#;
/* lab5 Q1: d*/
INSERT INTO regist (re_brID, re_crCode, re_semester, re_serial#)
VALUES (92120, 'COMP4201', 'FL2023', NEXT VALUE FOR seq_regist_serial#);

INSERT INTO regist (re_brID, re_crCode, re_semester, re_serial#)
VALUES (10021, 'COMP4202', 'FL2023', NEXT VALUE FOR seq_regist_serial#);

select * from regist;

/* lab5 Q2: a*/

ALTER TABLE CBlink ADD li_key CHAR(8);
EXEC sp_help 'CBlink';
/* lab5 Q2: b*/

CREATE SEQUENCE seq_CBlink_key
START WITH 0
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9999
CYCLE;

/* lab5 Q2: c*/
select NEXT VALUE FOR seq_CBlink_key;

UPDATE CBlink
SET li_key = LEFT(li_crCode,4) + RIGHT('0000'+CAST(NEXT VALUE FOR seq_CBlink_key AS VARCHAR(4)),4);


/* lab5 Q3*/

INSERT INTO CBlink (li_crCode, li_bkId, li_usage,li_key)
VALUES ('COMP4201', '1001', 'T', NEXT VALUE FOR seq_CBlink_key);

INSERT INTO CBlink (li_crCode, li_bkId, li_usage,li_key)
VALUES ('COMP4201', '1001', 'T', NEXT VALUE FOR seq_CBlink_key);




/* lab5 Q4*/
CREATE UNIQUE INDEX idx_book_title ON book(bk_title);

select * from CBlink

/*Task1*/

select cr_dept , count(*), max(cr_CH)
from course
group by cr_dept


/*Task1 Q1*/
select cr_title, count(bk_title)
from book , course
group by cr_title 

/*Task1 Q2*/

select bk_title, bk_totalCopies
from book
where bk_totalCopies >50 and bk_totalCopies <= 100



select * from CBlink 

/*Task1 Q3*/
select DISTINCT br_dept, dp_code,br_city
from borrower,department
where br_city ='seeb'
order by dp_code  DESC;
/*TaskQ4*/
select dp_name,sum(bk_totalCopies)
from department,book,course,CBlink
where dp_code = cr_dept
and  bk_id = li_bkId
and cr_code = li_crCode
group by dp_name;












