import sqlite3

"""
student_query -q 1 -p CNO 选择了课程号为CNO的学生学号
student_query -q 2 -p SNO 学号为SNO的学生选择的所有课程的课程号和成绩
student_query -q 3 -p CNAME 选择了课程名为CNAME的学生的姓名
student_query -q 4 -p SNAME 姓名为SNAME的学生所选所有课程的课程名，学时，学分和开课学期号
student_query -q 5 -p SCORE 查询成绩在SCORE分以上的学生姓名、课程号和成绩
student_query -q 6 -p SCORE 统计选课平均分低于SCORE的学生学号和成绩
student_query -q 7 -p SNAME 统计姓名为SNAME的学生选修的课程数
student_query -q 8 -p CNAME 查询课程名为CNAME的课程的最高分、最低分和平均分
"""
conn = sqlite3.connect('SCT.db')
print("open DB successfully...")

with open('cmd.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        cmd = line.split(' ')
        if cmd[2] == "1":
            cursor = conn.execute("SELECT snum FROM SC WHERE cnum='%s'" % cmd[4])
            print("\n学号")
            for row in cursor:
                print(row[0])
        if cmd[2] == "2":
            cursor = conn.execute("SELECT cnum,score FROM SC WHERE snum='%s'" % cmd[4])
            print("\n课程号\t成绩")
            for row in cursor:
                print(row[0], row[1])
        if cmd[2] == "3":
            cursor = conn.execute(
                "SELECT sname FROM student,SC,course WHERE cname='%s' AND course.cnum=SC.cnum AND student.snum=SC.snum" %
                cmd[4])
            print("\n姓名")
            for row in cursor:
                print(row[0])
        if cmd[2] == "4":
            cursor = conn.execute(
                "SELECT cname,chours,credit,Csemster FROM student,course, SC WHERE sname='%s' AND student.snum=SC.snum AND course.cnum=SC.cnum" %
                cmd[4])
            print("\n课程名\t课时\t学分\t学期")
            for row in cursor:
                print(row[0], row[1], row[2], row[3])
        if cmd[2] == "5":
            cursor = conn.execute(
                "SELECT sname,cnum,score FROM student,SC WHERE score>%d AND student.snum=SC.snum" % int(cmd[4]))
            print("\n姓名\t课程号\t成绩")
            for row in cursor:
                print(row[0], row[1], row[2])
        if cmd[2] == "6":
            cursor = conn.execute(
                "SELECT snum,score FROM SC WHERE score GROUP BY cnum HAVING avg(score)<%d" % int(cmd[4]))
            print("\n学号\t成绩")
            for row in cursor:
                print(row[0], row[1])
        if cmd[2] == "7":
            cursor = conn.execute(
                "SELECT COUNT(SC.snum) FROM student,SC WHERE student.snum=SC.snum AND sname='%s'" % (cmd[4]))
            print("\n课程数")
            for row in cursor:
                print(row[0])

        if cmd[2] == "8":
            cursor = conn.execute(
                "SELECT MAX(score),MIN(score),AVG(score) FROM course,SC WHERE course.cnum=SC.cnum AND cname='%s'" % (
                    cmd[4]))
            print("\n最高分\t最低分\t平均分")
            for row in cursor:
                print(row[0], row[1], row[2])
