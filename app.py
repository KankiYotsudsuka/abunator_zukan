# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:22:08 2020

@author: School
"""
from flask import Flask,render_template,request,redirect,url_for,abort
app = Flask(__name__)

import sys
sys.path.append("/abunator_zukan/")

#図鑑用クラスのインポート
import pic_book

#図鑑へのリンク
@app.route('/pic_book/<key>',methods = ['GET'] )
def zukan(key):
    if 'true' in key and len(key) == 14:
        global linker
        linker = key
        return render_template('/picture_book.html',\
        key = linker)

@app.route('/return/<key>',methods = ['GET'])
def initial(key):
    linker = key
    return redirect('https://abunatorroute.azurewebsites.net/return/' + linker)

#図鑑から解説への直通のリンク
@app.route('/picture_book/<key>',methods = ['POST'])
def kaisetu(key):
    linker = key
    if request.method == 'POST':
        no = request.form['no']
    else:
        no = "13"
    resultList = pic_book.result(no)
    name = resultList[1]
    dealing = resultList[2]
    rank = resultList[3] 
    return render_template('/explanation.html',\
        no = no,\
        name = name,\
        dealing = dealing,\
        rank = rank,\
        key = linker)

@app.route('/refer/<key>', methods = ['GET'])
def referrence(key):
    if 'true' in key and len(key) >= 14:
        linker = key[0:13] + 'e'
        name = key[14:]
        no = pic_book.resNo(name)
        resultList = pic_book.result(no)
        dealing = resultList[2]
        rank = resultList[3] 
        return render_template('/explanation.html',\
        no = no,\
        name = name,\
        dealing = dealing,\
        rank = rank,\
        key = linker)



if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)