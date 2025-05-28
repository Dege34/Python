# MIT License
# Copyright (c) 2025 Dogan Ege Bulte
# GitHub: https://github.com/Dege34
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



import sqlite3

DB_PATH = "gym.db"

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS INSTRUCTOR (
        FisCode TEXT PRIMARY KEY,
        Name TEXT NOT NULL,
        Surname TEXT NOT NULL,
        BirthDate DATE,
        Email TEXT,
        Telephone TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS COURSES (
        CodC TEXT PRIMARY KEY,
        Name TEXT NOT NULL,
        CType TEXT NOT NULL,
        Level INTEGER CHECK (Level BETWEEN 1 AND 4)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PROGRAM (
        FisCode TEXT,
        Day TEXT CHECK (Day IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')),
        StartTime INTEGER CHECK (StartTime BETWEEN 6 AND 22),
        Duration INTEGER CHECK (Duration BETWEEN 15 AND 60),
        CodC TEXT,
        Room TEXT NOT NULL,
        PRIMARY KEY (CodC, Day),
        FOREIGN KEY (FisCode) REFERENCES INSTRUCTOR(FisCode),
        FOREIGN KEY (CodC) REFERENCES COURSES(CodC)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Yeaahh, Database created successfully!!") 