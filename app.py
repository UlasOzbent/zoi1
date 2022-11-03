from base64 import encode
from cProfile import label
from collections import UserList
import email
import json
from tabnanny import check
from flask import Flask, flash, redirect, render_template,request,url_for
import os
from werkzeug.utils import secure_filename
import pandas as pd
from openpyxl import load_workbook

from google.cloud import storage
import google.cloud.storage
import sys
from google.cloud import bigquery

import bcrypt

app = Flask(__name__, template_folder='templates', static_folder='static')
UPLOAD_FOLDER = 'static/data/'
app.secret_key = "secret_key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

check_loggin=0
currentUserName=''
filenames_for_current_user=[]
labels_for_current_user=[]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

PATH=os.path.join(os.getcwd(),'eloquent-hour-364711-17c2ec668540.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=PATH
storage_client=storage.Client(PATH)
bucket=storage_client.get_bucket('datas002')

client=bigquery.Client()

bucket_name = 'excel001'
project =  'eloquent-hour-364711'
Dataset_id = 'label'
Table_id = 'labelled'

def write_csv():
    destination_uri = 'gs://{0}/{1}'.format(bucket_name, 'datas.csv')
    dataset_ref = bigquery.DatasetReference(project,Dataset_id)
    table_ref = dataset_ref.table(Table_id)
    Extract_job = client.extract_table(
	    table_ref,
	    destination_uri, 
	    location='US'
    )
def remove_name(buck,val):
    for filename in list(buck.list_blobs(prefix='')):
        if filename.name==val:
            blob=buck.blob(filename.name)
            blob.delete()

@app.route("/",methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route("/home",methods=['GET','POST'])
def home_page():
    return render_template("index.html",username=currentUserName)

@app.route("/1",methods=["POST","GET"])
def upload():
    global currentUserName
    variable=request.files.get("file")
    print(variable)
    if variable and allowed_file(variable.filename):
        filename = secure_filename(variable.filename)
        print(filename)
        #variable.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        #UPLOADFILE2=os.path.join(os.getcwd(),filename)
        #print(UPLOADFILE2)
        blob=bucket.blob(filename)
        blob.upload_from_file(variable)
    if check_loggin==1:
        return render_template("upload.html",username=currentUserName)


@app.route("/2",methods=["GET","POST"])
def datas():
    if check_loggin==1:
        global currentUserName
        dir=[]
        for filename in list(bucket.list_blobs(prefix='')):
            dir.append(filename.name)
        if len(list(bucket.list_blobs(prefix=''))) == 0:
            #write_csv()
            return render_template("empty_uploaded.html",username=currentUserName)
        else:
            return render_template("datas.html",list=dir,length=len(dir),username=currentUserName)

def load_to_excel(var,label):
    name_list=[var]
    label_list=[label]
    print(label_list)
    print(name_list)
    df = pd.DataFrame({'Name': name_list,
                   'Label': label_list})
    writer = pd.ExcelWriter('static/excel/datas.xlsx', engine='openpyxl')
    # try to open an existing workbook
    writer.book = load_workbook('static/excel/datas.xlsx')
    # copy existing sheets
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    # read existing file
    reader = pd.read_excel('static/excel/datas.xlsx')
    # write out the new sheet
    df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

    writer.close()

def excel():
    df = pd.DataFrame({'Name': [],
                   'Label': []})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('static/excel/datas.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


@app.route("/3/<name>",methods=["POST","GET"])
def label_true(name):
    global currentUserName
    table_id='eloquent-hour-364711.label.labelled'
    rows_to_insert=[
        {u'Username':currentUserName,u'Filename':name,u'Label':'True'}
    ]

    errors=client.insert_rows_json(table_id,rows_to_insert)
    if errors==[]:
        print('New rows have been added')
    else:
        print('The error is:{errors}')
    remove_name(bucket,name)
    return redirect("/2")

@app.route("/4/<name>",methods=["GET","POST"])
def label_false(name):
    global currentUserName
    table_id='eloquent-hour-364711.label.labelled'
    rows_to_insert=[
        {u'Username':currentUserName,u'Filename':name,u'Label':'False'}
    ]

    errors=client.insert_rows_json(table_id,rows_to_insert)
    if errors==[]:
        print('New rows have been added')
    else:
        print('The error is:{errors}')
    remove_name(bucket,name)
    return redirect("/2")

def remove_file():
    for filename in list(bucket.list_blobs(prefix='')):
        blob=bucket.blob(filename.name)
        blob.delete()


@app.route("/5",methods=['GET','POST'])
def clear_file():
    remove_file()
    return redirect("/1")


@app.route("/register",methods=['GET','POST'])
def register():
    return render_template("register.html") 

@app.route("/register2",methods=['GET','POST'])
def register2():
    query = """
    SELECT username,email,password FROM `eloquent-hour-364711.label.users`
    """
    query_job = client.query(query)
    username=request.form.get('username')
    UserList=[]
    for row in query_job:
        UserList.append(row[0])
    if username in UserList:
        flash('Username is taken')
        return redirect("/register")
    else:

        email=request.form.get('email')
        password=request.form.get('password')
        hashPassword = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
        table_id='eloquent-hour-364711.label.users'
        rows_to_insert=[
            {u'Username':username,u'Email':email,u'Password':hashPassword.decode('utf-8')}
        ]
        errors=client.insert_rows_json(table_id,rows_to_insert)
        if errors==[]:
            print('New rows have been added')
        else:
            print('The error is:{errors}')
        flash("Account successfully created")
        return redirect("/register") 


@app.route("/6",methods=['GET','POST'])
def index():
    global check_loggin
    global currentUserName
    username=request.form.get('username')
    password=request.form.get('password')
    query = """
    SELECT username,email,password FROM `eloquent-hour-364711.label.users`
    """
    query_job = client.query(query)
    currentUserName=username
    is_username_correct=0
    for row in query_job:
        pw=str(row[2]).encode('utf-8')
        if username==row[0] :
            if bcrypt.checkpw(password.encode('utf-8'),pw):
                print(row[0],row[2])
                check_loggin=1
                is_username_correct=1
    if is_username_correct==1:
        return render_template("index.html",username=username)
    else:
        flash('Your username or password is incorrect.Try again.')
        return redirect("/")

@app.route("/logout",methods=['GET','POST'])
def logout():
    global check_loggin
    global currentUserName
    global filenames_for_current_user
    global labels_for_current_user
    check_loggin=0
    currentUserName=''
    filenames_for_current_user=[]
    labels_for_current_user=[]
    return redirect("/")

@app.route("/uploaded_data",methods=['GET','POST'])
def uploaded_data():
    global check_loggin
    if check_loggin==1:
        global currentUserName
        global filenames_for_current_user
        global labels_for_current_user
        filenames_for_current_user=[]
        labels_for_current_user=[]
        query = """
        SELECT username,filename,label FROM `eloquent-hour-364711.label.labelled`
        """
        query_job = client.query(query)
        for row in query_job:
            if row[0]==currentUserName:
                filenames_for_current_user.append(row[1])
                labels_for_current_user.append(row[2])
        return redirect("/labelled_data")

@app.route("/labelled_data")
def labelled_data():
    schedule=zip(filenames_for_current_user,labels_for_current_user)
    print(filenames_for_current_user)
    return render_template("uploaded.html",list=schedule,username=currentUserName)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 80)),host='127.0.0.1',debug=True)