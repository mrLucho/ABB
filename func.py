import csv
from time import sleep

from selenium import webdriver
# for explicit wait and conditions
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from selenium.webdriver.common.by import By
from collections import namedtuple
class Driver(webdriver.Chrome):
    def __init__(self):
        os.environ['PATH'] = r"C:\SeleniumDrivers"
        super().__init__()
        self.implicitly_wait(3)
        self.maximize_window()
        self.QA = {}
        self.qLst = []

    def land_first_page(self):
        self.get(r'https://backtoschoolwithabb.pl/quiz/')
    def startQuiz(self):
        startBtn = self.find_element(By.ID,"cf7mls-next-btn-cf7mls_step-1")
        startBtn.click()

    def loadQ_A(self):
        with open('dict.csv',newline='') as file:
            reader = csv.reader(file,delimiter=',')
            for row in reader:
                self.QA[row[0]] = str(row[1])

    def getAnswer(self,questNum):
        que = self.qLst[questNum]
        return self.QA[que]



    def answer(self,answerStr:str,order):
        fieldset = self.find_element(By.CSS_SELECTOR,f'fieldset[data-cf7mls-order="{order}"]')
        if not fieldset:
            print('no found fieldset')
        btn = fieldset.find_elements(By.CLASS_NAME,"wpcf7-list-item-label")
        for sm in btn[:3]:
            if sm.text.__contains__(answerStr):
                print('selected',sm.text)
                sm.click()
            else:
                print(sm.text)


    def goAhead(self,order):
        dalejBtn = self.find_element(By.ID,f"cf7mls-next-btn-cf7mls_step-{order}")
        dalejBtn.click()

    def getAllQuest(self):
        question = self.find_elements(By.CLASS_NAME, 'wpcf7-form-control-wrap')
        # print(len(question))
        # for i in question:
        #     print(i.get_attribute("data-name"))
        new = question[::2]
        new = new[:10]
        for elem in new:
            self.qLst.append(elem.get_attribute("data-name"))

        # print()
        # for i in new:
        #     print(i.get_attribute("data-name"))

    def main(self):
        self.land_first_page()
        self.loadQ_A()
        self.implicitly_wait(30)
        self.startQuiz()
        sleep(0.5)
        self.getAllQuest()
        for i in range(9):

            print(i + 1,self.qLst[i])
            timeToWait = 0.2
            sleep(timeToWait)

            ans = self.getAnswer(i)
            # if ans:
            self.answer(ans,i+1)
            sleep(timeToWait)

            self.goAhead(i+2)

        #     # else:
        #     # print('not found in DB')


#         paste text of answer
