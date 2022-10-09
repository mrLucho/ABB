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

    def land_first_page(self):
        self.get(r'https://backtoschoolwithabb.pl/quiz/')
    def startQuiz(self):
        startBtn = self.find_element(By.ID,"cf7mls-next-btn-cf7mls_step-1")
        startBtn.click()
    def identifyQuestion(self):
        # WebDriverWait(self,3).until(EC.presence_of_element_located((By.XPATH,'//span[contains(@class,"form-title")]')))
        question = self.find_element(By.XPATH,'//span[contains(@class,"form-title")]')
        # question = self.find_element(By.CSS_SELECTOR, 'span[class="form-title"]')
        # return question.text class="wpcf7-form-control-wrapper"
        print(question.text)

    def loadQ_A(self):
        with open('dict.csv',newline='') as file:
            reader = csv.reader(file,delimiter=',')
            for row in reader:
                self.QA[row[0]] = row[1]

    def getAnswer(self,questionName:str):
        for key in self.QA.keys():
            if questionName == key:
                return self.QA[key]

    def answer(self,answerStr:str):
        btn = self.find_element(By.CSS_SELECTOR,f'input[value="{answerStr}"]')
        btn.click()
        pass
    def goAhead(self):
        dalejBtn = self.find_element(By.CLASS_NAME,"cf7mls_next cf7mls_btn action-button")
        dalejBtn.click()


    def main(self):
        self.land_first_page()
        self.implicitly_wait(30)
        self.startQuiz()
        sleep(0.5)
        self.identifyQuestion()