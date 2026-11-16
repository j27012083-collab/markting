#creat tables in the dadtbase
# import sqlite3
# con = sqlite3.connect('movies.db')
# cursor = con.cursor
# cursor.execute("CREATE TABLE IF NOT EXISTS movie('name TEXT,commnt TEXT, year TEXT)")
# cursor.execute("INSERT INTO movie ")
# con.commit()
# con.close()
from flask import Flask, render_template, request, redirect  # أدوات فلاسك: التطبيق، عرض الصفحة، قراءة الفورم، التحويل
import sqlite3  # مكتبة قاعدة البيانات

app = Flask(__name__)  # إنشاء التطبيق

def get_db():  # دالة بتفتح القاعدة
    con = sqlite3.connect('movies.db')  # فتح الاتصال بالملف
    con.execute("CREATE TABLE IF NOT EXISTS comments(name TEXT, student_id TEXT, comment TEXT)")  # إنشاء الجدول لو مش موجود
    return con  # إرجاع الاتصال

@app.route('/', methods=['GET', 'POST'])  # الصفحة الرئيسية بتقبل عرض وإرسال
def home():  # الدالة الرئيسية
    con = get_db()  # فتح القاعدة
    if request.method == 'POST':  # لو حد داس زرار الإرسال
        name = request.form['name']  # أخذ الاسم من الفورم
        student_id = request.form['student_id']  # أخذ الـ ID من الفورم
        comment = request.form['comment']  # أخذ التعليق من الفورم
        con.execute("INSERT INTO comments VALUES (?, ?, ?)", (name, student_id, comment))  # الحفظ في القاعدة (علامات ? بتحمي من الاختراق)
        con.commit()  # تثبيت الحفظ
        con.close()  # قفل الاتصال
        return redirect('/')  # رجوع للصفحة عشان الـ refresh ميكررش الإرسال
    rows = con.execute("SELECT * FROM comments").fetchall()  # قراءة كل التعليقات
    con.close()  # قفل الاتصال
    return render_template('index.html', rows=rows)  # عرض الصفحة مع التعليقات

if __name__ == '__main__':  # لو الملف اتشغل مباشرة
    app.run(debug=True)  # تشغيل السيرفر