# file name : index.py
# pwd : /project_name/app/main/index.py

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
import random

# 추가할 모듈이 있다면 추가

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/main', methods=['GET'])
def index():
    # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
    testData = 'testData array'


    return render_template('/main/index.html', testDataHtml=testData)

@main.route('/random2/<number>', methods=['GET'])
def random2(number):
    # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
    testData = []
    num=int(number)

    for k in range(0, num):

        reg_no = []
        mul_factor = [1, 3, 7, 1, 3, 7, 1, 3, 5]
        sum = 0

        target1 = '110'  # 서울,경기청 고정

        target2 = random.randrange(1, 79)
        target2 = str(target2).rjust(2, '0')

        target3 = random.randrange(0, 9999)
        target3 = str(target3).rjust(4, '0')

        result = ''
        result = str(target1) + str(target2) + str(target3)

        array = []
        for i in result:
            array.append(i)

        for idx, j in enumerate(array):
            a = int(j) * int(mul_factor[idx])
            sum = sum + a
        sum = sum + ((int(array[8]) * 5) / 10)

        sidliy = int(sum % 10)

        if sidliy != 0:
            sum = 10 - sidliy
        else:
            sum = 0

        array.append(str(sum))
        b = ''.join(array)
        #print(b)
        testData.append(b)



    return render_template('/main/random.html', testDataHtml=testData)
