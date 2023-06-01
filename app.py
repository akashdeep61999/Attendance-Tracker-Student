import pandas as pd
import re,datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


Java_Theory='1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'
Java_Lab_A="1Ik4guLKNHQz7ZC0LwTeCGl23G66vm9xWEwzhgcwrzJA"
Java_Lab_B="1--xishZY_sgONYzStNwhgkoFf3Pj7yn_CDAiDlJnhUg"
mst_java='Award_list_Java.xlsx'
sub_java='Submission_list_Java.xlsx'

Python_Theory='1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'
Python_Lab_A="1Ik4guLKNHQz7ZC0LwTeCGl23G66vm9xWEwzhgcwrzJA"
Python_Lab_B="1--xishZY_sgONYzStNwhgkoFf3Pj7yn_CDAiDlJnhUg"
mst_Python='Award_list_Java.xlsx'
sub_Python='Submission_list_Java.xlsx'

CC_Theory='1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'
CC_Lab_A="1Ik4guLKNHQz7ZC0LwTeCGl23G66vm9xWEwzhgcwrzJA"
CC_Lab_B="1--xishZY_sgONYzStNwhgkoFf3Pj7yn_CDAiDlJnhUg"
mst_CC='Award_list_Java.xlsx'
sub_CC='Submission_list_Java.xlsx'

DBMS_Theory='1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'
DBMS_Lab_A="1Ik4guLKNHQz7ZC0LwTeCGl23G66vm9xWEwzhgcwrzJA"
DBMS_Lab_B="1--xishZY_sgONYzStNwhgkoFf3Pj7yn_CDAiDlJnhUg"
mst_DBMS='Award_list_Java.xlsx'
sub_DBMS='Submission_list_Java.xlsx'

SCAakashsir='1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'
SCAshivamsir='1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'

MPWshivamsir='1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'
MPWakashsir='1wqrXEnrXBk_4rRhvjR3rURNBwlqIw0JA22YiZnTpp5k'

@app.route("/")
def home():
    return render_template("teacher.html")


@app.route("/checksub",methods=['POST'])
def checksub():
   
    if request.method == 'POST':
        teacher = request.form['language']
    return render_template("subject.html",teacher=teacher)


@app.route('/subject', methods=['POST'])
def subject():
    if request.method == 'POST':
        subject = request.form['language']
        return render_template('first_page.html', subject=subject)


@app.route("/search", methods=["POST"])
def search():
    a=1
    submit_value = request.form['submit']
    if submit_value == 'Java_Theory':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Java_Theory

    elif submit_value == 'Java_Lab_A':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Java_Lab_A

    elif submit_value == 'Java_Lab_B':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Java_Lab_B

    elif submit_value == 'Python_Theory':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Python_Theory

    elif submit_value == 'Python_Lab_A':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Python_Lab_A

    elif submit_value=="Python_Lab_B":
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = Python_Lab_B

    elif submit_value == 'CC_Theory':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = CC_Theory

    elif submit_value == 'CC_Lab_A':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = CC_Lab_A

    elif submit_value == 'CC_Lab_B':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = CC_Lab_B

    elif submit_value == 'DBMS_Theory':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = DBMS_Theory

    elif submit_value == 'DBMS_Lab_A':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = DBMS_Lab_A

    elif submit_value == 'DBMS_Lab_B':
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = DBMS_Lab_B

    elif submit_value == 'SCAakashsir':
        a=0
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = SCAakashsir

    elif submit_value == 'SCAshivamsir':
        a=0
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = SCAshivamsir

    elif submit_value == 'MPWshivamsir':
        a=0
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = MPWshivamsir

    elif submit_value == 'MPWakashsir':
        a=0
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)
        gsheetid = MPWakashsir


    else:
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'
        mst_df = pd.read_excel(mst_java)
        sub_df=pd.read_excel(sub_java)



    sheet_name = "Data"
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
    df = pd.read_csv(gsheet_url)
    name1 = request.form['username']
        
    #for MST marks display
    
    lis = []

    for index, row in mst_df.iterrows():
        if name1!='':
            if row['Roll no'] == int(name1):
                lis.append(row.tolist())
                mst1=lis[0][1]
                mst2=lis[0][2]
                mst3=lis[0][3]

     #for Submission marks display
    
    lis1= []

    for index, row in sub_df.iterrows():
        if name1!='':
            if row['Roll no'] == int(name1):
                lis1.append(row.tolist())
                sub1=lis1[0][1]
                sub2=lis1[0][2]
                sub3=lis1[0][3]
        
    try:
        def clean_column(col):

            col = re.sub(r'[^\w\s]+', ' ', col)
            col = re.sub(r'\s+', ' ', col)
            col = col.strip()
            return col
        for col in df.columns:
            df.rename(columns={col:clean_column(col)}, inplace=True)

        if name1 in df.columns:
            att = df[name1]
            att = list(att)
            date = list(df["Date"])
            result = list(zip(date,att))

            result = [(datetime.datetime.strptime(d, '%d/%m/%Y'), v) for d, v in result]
            sorted_list = sorted(result, key=lambda x: x[0])
            sorted_list = [(d.strftime('%d/%m/%Y'), v) for d, v in sorted_list]

            counts = {'P': 0, 'A': 0}

            for _, value in sorted_list:
                counts[value] += 1

            p_count = counts['P']
            a_count = counts['A']
            n=len(sorted_list)
            generate_list = lambda n: list(range(1, n+1))
            return render_template('home.html',submit_value=submit_value,a=a, sorted_list=sorted_list, p_count=p_count, a_count=a_count,Sr_no=generate_list(n),name1=name1,lis=lis,mst1=mst1,mst2=mst2,mst3=mst3,sub1=sub1,sub2=sub2,sub3=sub3)
        else:
            return render_template('founderror.html',a=a)
    except Exception as e:
        return f"Java Theory Error"


@app.route("/recentatt",methods=['POST'])
def recentatt():
    submit_value = request.form['submit']
    if submit_value == 'Java_Theory':
        gsheetid = Java_Theory
    elif submit_value == 'Java_Lab_A':
        gsheetid = Java_Lab_A
    elif submit_value == 'Java_Lab_B':
        gsheetid = Java_Lab_B

    elif submit_value == 'Python_Theory':
        gsheetid =Python_Theory
    elif submit_value == 'Python_Lab_A':
        gsheetid = Python_Lab_A
    elif submit_value=="Python_Lab_B":
        gsheetid = Python_Lab_B

    elif submit_value == 'CC_Theory':
        gsheetid = CC_Theory
    elif submit_value == 'CC_Lab_A':
        gsheetid = CC_Lab_A
    elif submit_value == 'CC_Lab_B':
        gsheetid = CC_Lab_B

    elif submit_value == 'DBMS_Theory':
        gsheetid = DBMS_Theory
    elif submit_value == 'DBMS_Lab_A':
        gsheetid = DBMS_Lab_A
    elif submit_value == 'DBMS_Lab_B':
        gsheetid = DBMS_Lab_B
    
    elif submit_value == 'SCAshivamsir':
        gsheetid = SCAshivamsir
    elif submit_value == 'SCAakashsir':
        gsheetid = SCAakashsir

    elif submit_value == 'MPWshivamsir':
        gsheetid = MPWshivamsir

    elif submit_value == 'MPWakashsir':
        gsheetid = MPWakashsir

    else:
        gsheetid = '1v_14EKTFW_UrgueMh2p4qwu8vXo8epVlNlpn4aQKMsw'

    sheet_name = "Data"
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
    df = pd.read_csv(gsheet_url)
    df = df.drop(['Timestamp'], axis=1)

    date_list = df['Date'].tolist() # List of Dates

    def clean_column(col):
        col = re.sub(r'[^\w\s]+', ' ', col)
        col = re.sub(r'\s+', ' ', col)
        col = col.strip()
        return col

    try:
        for col in df.columns:
            df.rename(columns={col: clean_column(col)}, inplace=True)
        columns_recent_Att = list(df.columns)
        last_row = list(df.iloc[-1])
        recent_Att = [(columns_recent_Att, value) for columns_recent_Att, value in zip(columns_recent_Att, last_row)]
        p_count = 0
        a_count = 0
        for key, value in recent_Att[1:]:
            p_count += value.count('P')
            a_count += value.count('A')
        Total = p_count + a_count
        Sr_no = [i + 1 for i in range(len(recent_Att) - 1)]
        return render_template('recentatt.html', gsheetid=gsheetid,recent_Att=recent_Att,date_list=date_list, submit_value=submit_value, p_count=p_count, a_count=a_count, Total=Total, Sr_no=Sr_no)
    except Exception as e:
        return "Recent att Error: " + str(e)


@app.route('/attbydate',methods=['POST'])
def attbydate():
    if request.method == 'POST':
        date = request.form['date']
        gsheetid=request.form['gsheetid']
        sheet_name = "Data"
        gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
        df = pd.read_csv(gsheet_url)
        df = df.drop(['Timestamp'], axis=1)

        def clean_column(col):
            col = re.sub(r'[^\w\s]+', ' ', col)
            col = re.sub(r'\s+', ' ', col)
            col = col.strip()
            return col
        for col in df.columns:
            df.rename(columns={col: clean_column(col)}, inplace=True)
        

        filtered_df = df[df['Date'] == date]

        # Save the columns of the matching rows to a single list
        lis = filtered_df.values.flatten().tolist()

        roll_no = df.columns.tolist()



        recent_Att = [(roll_no, value) for roll_no, value in zip(roll_no, lis)]
        p_count = 0
        a_count = 0
        try:
            for key, value in recent_Att[1:]:
               p_count += value.count('P')
               a_count += value.count('A')
            Total = p_count + a_count
            Sr_no = [i + 1 for i in range(len(recent_Att)-1)]
            
            return render_template("attbydate.html",recent_Att=recent_Att,Sr_no=Sr_no,p_count=p_count, a_count=a_count, Total=Total)

        except Exception as e:
            return f"Java Theory Register Error"
        
    else:
        return render_template('Register.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
