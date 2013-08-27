from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from optparse import OptionParser
import unittest2, time, re, subprocess
from subprocess import Popen, PIPE, STDOUT

import json
from pprint import pprint

#os and sys needed to set the display port for the chrome browser
import os,sys
os.putenv("DISPLAY",":0")

URL = 'http://208.115.44.172:5435/'
if len(sys.argv) >= 2 :
    URL = sys.argv[1]+"/"

print("Using domain : %s" % URL)

LOGIN = "jon@joncrowell.org"
if len(sys.argv) >= 3 :
    LOGIN = sys.argv[2]
print("Using login : %s" % LOGIN)

PASSW = "Cr0w3l1"
if len(sys.argv) >= 4 :
    PASSW = sys.argv[3]
print("Using password : %s" % PASSW)

sys.argv = sys.argv[:1]

jon = False


class SeleniumTestSuite(unittest2.TestCase):
    # called only one time at the beginning -- like a static method
    @classmethod
    def setUpClass(cls):
        global jon
        print "jon = "+str(jon)
        if not jon:
            print "Checking for X server"
            if cls.isXRunning('X') == False:
                print "X not running, attempting to start"
                Popen('startx', shell=True, close_fds=True)
            else:
                print "X is running"
            cls.driver = webdriver.Chrome()
        else: # if jon
            cls.driver = webdriver.Firefox()

        cls.driver.implicitly_wait(3)
        cls.base_url = URL
        #cls.base_url = "http://demovcd.independenceit.com/"
        # we will need to be logged in for all tests, so we set that up here.
        cls.driver.get(cls.base_url + "login")
        cls.driver.find_element_by_id("login").clear()
        cls.driver.find_element_by_id("login").send_keys(LOGIN)
        cls.driver.find_element_by_id("password").clear()
        cls.driver.find_element_by_id("password").send_keys(PASSW)
        cls.driver.find_element_by_css_selector("button.btn.btn-primary").click()

        print "finished running setUpClass() "


    def assert_ui_at_link(self, link_id, ui_desc):
        print "\n============================================"
        print "clicking on "+link_id
        self.driver.find_element_by_id(link_id).click()
        # time.sleep(1) # horrible and should be removed
        self.assert_ui_data(ui_desc)

    def assert_contains_text_for_tag(self, tag, text_list):
        if len(text_list) == 0:
            return
        # print "<"+tag+"> - "+str(text_list)
        driver = self.driver
        tag_found_list = [False for t in text_list]
        tag_list = driver.find_elements_by_tag_name(tag)
        for element in tag_list:
            # if len(element.text) > 0:
            #     print tag+" element text = |"+element.text+"|"
            for idx1, text in enumerate(text_list):
                if text[0:2] == "~ ":
                    if text[2:] in element.text:
                        tag_found_list[idx1] = True
                        break
                else:
                    if text == element.text:
                        tag_found_list[idx1] = True
                        break
        for idx2, text_found in enumerate(tag_found_list):
            if not text_found:
                print "<"+tag+"> - '"+text_list[idx2]+"' not found!"
        for tag_found in tag_found_list:
            self.assertTrue(tag_found)


    def assert_ui_data(self, ui_data):
        for tag in ui_data:
            if tag != "submenus":
                self.assert_contains_text_for_tag(tag, ui_data[tag])

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    @classmethod
    def findProcess(cls, processN):
        ps     = subprocess.Popen("ps -eaf | grep "+processN, shell=True, stdout=subprocess.PIPE)
        output = ps.stdout.read()
        ps.stdout.close()
        ps.wait()

        return output
    @classmethod
    def isXRunning(cls, processN ):
        output = cls.findProcess(processN)
        if re.search('/usr/bin/'+processN, output) is None:
            return False
        else:
            return True


def load_json_ui_tests():
   with open('vcd_ui_description.json') as data_file:
        count = inject_ui_tests(json.load(data_file))
        print "injected "+str(count)+" test methods for unittest to invoke"

def inject_ui_tests(ui_desc):
    count = 0
    for link_id in ui_desc:
        ui_description = ui_desc[link_id]
        unittest_function = create_test_function(link_id, ui_description)
        setattr(SeleniumTestSuite, "test_"+link_id, unittest_function)
        count += 1
        if "submenus" in ui_description:
            count += inject_ui_tests(ui_description['submenus'])
    return count

def create_test_function(link_id, ui_desc):
    def test_function(self):
        self.assert_ui_at_link(link_id, ui_desc)
    return test_function


load_json_ui_tests()
if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    print path
    if "/Users/Jon/dev/iit/" in path:
        jon = True
        print "looks like we're running on Jon's machine"
    unittest2.main()


















    # def test_001_verify_home_page(self):
    #     driver = self.driver
    #     ui_data = self.ui_desc['Home']
    #     print "clicking on Home"
    #     driver.find_element_by_id("topmenu_home").click()
    #     self.assert_top_menu_bar_correct()
    #     self.assert_ui_data(ui_data)
    #     self.assert_submenus(ui_data['submenus'])


    # def test_002_verify_clients_page(self):
    #     driver = self.driver
    #     ui_data = self.ui_desc['Clients']
    #     print "clicking on Clients"
    #     driver.find_element_by_id("topmenu_clients").click()
    #     self.assert_top_menu_bar_correct()
    #     self.assert_ui_data(ui_data)
    #     self.assert_submenus(ui_data['submenus'])


    # def test_003_verify_quotes_page(self):
    #     driver = self.driver
    #     ui_data = self.ui_desc['Quotes']
    #     print "clicking on Quotes"
    #     driver.find_element_by_id("topmenu_quotes").click()
    #     self.assert_top_menu_bar_correct()
    #     self.assert_ui_data(ui_data)
    #     self.assert_submenus(ui_data['submenus'])


    # def test_004_verify_orders_page(self):
    #     driver = self.driver
    #     ui_data = self.ui_desc['Orders']
    #     print "clicking on Orders"
    #     driver.find_element_by_id("topmenu_orders").click()
    #     self.assert_top_menu_bar_correct()
    #     self.assert_ui_data(ui_data)
    #     self.assert_submenus(ui_data['submenus'])


    # def test_005_verify_resources_page(self):
    #     driver = self.driver
    #     ui_data = self.ui_desc['Resources']
    #     print "clicking on Resources"
    #     driver.find_element_by_id("topmenu_resources").click()
    #     self.assert_top_menu_bar_correct()
    #     self.assert_ui_data(ui_data)
    #     self.assert_submenus(ui_data['submenus'])


    # def test_006_verify_billing_page(self):
    #     driver = self.driver
    #     ui_data = self.ui_desc['Billing']
    #     print "clicking on Billing"
    #     driver.find_element_by_id("topmenu_billing").click()
    #     self.assert_top_menu_bar_correct()
    #     self.assert_ui_data(ui_data)
    #     self.assert_submenus(ui_data['submenus'])


    # def test_007_verify_settings_page(self):
    #     driver = self.driver
    #     ui_data = self.ui_desc['Settings']
    #     print "clicking on Settings"
    #     driver.find_element_by_id("topmenu_settings").click()
    #     self.assert_top_menu_bar_correct()
    #     self.assert_ui_data(ui_data)
    #     self.assert_submenus(ui_data['submenus'])


    # def test_009_verify_webtabs_page(self):
    #     driver = self.driver
    #     ui_data = self.ui_desc['Web Tabs']
    #     print "clicking on Web Tabs"
    #     driver.find_element_by_id("topmenu_webtabs").click()
    #     self.assert_top_menu_bar_correct()
    #     self.assert_ui_data(ui_data)
    #     self.assert_submenus(ui_data['submenus'])


    # def test_008_verify_master_page(self):
    #     driver = self.driver
    #     ui_data = self.ui_desc['Master']
    #     print "clicking on Master"
    #     driver.find_element_by_id("topmenu_master").click()
    #     self.assert_top_menu_bar_correct()
    #     self.assert_ui_data(ui_data)
    #     self.assert_submenus(ui_data['submenus'])






    # def assert_top_menu_bar_correct(self):
    #     self.assertTrue(self.is_element_present(By.ID, "topmenu_home"))
    #     self.assertTrue(self.is_element_present(By.ID, "topmenu_clients"))
    #     self.assertTrue(self.is_element_present(By.ID, "topmenu_quotes"))
    #     self.assertTrue(self.is_element_present(By.ID, "topmenu_orders"))
    #     self.assertTrue(self.is_element_present(By.ID, "topmenu_resources"))
    #     self.assertTrue(self.is_element_present(By.ID, "topmenu_billing"))
    #     self.assertTrue(self.is_element_present(By.ID, "topmenu_settings"))
    #     self.assertTrue(self.is_element_present(By.ID, "topmenu_webtabs"))
    #     self.assertTrue(self.is_element_present(By.ID, "topmenu_master"))

    # def assert_contains_table_heading(self, th_text_list):
    #     print th_text_list
    #     driver = self.driver
    #     th_found_list = [False for th in th_text_list]
    #     th_list = driver.find_elements_by_tag_name("th") # th is the tag for table heading
    #     for th in th_list:
    #         for idx, th_text in enumerate(th_text_list):
    #             if th.text == th_text:
    #                 th_found_list[idx] = True
    #                 break
    #     for idx, th_found in enumerate(th_found_list):
    #         if not th_found:
    #             print "th - "+th_text_list[idx]+" - not found"
    #     for th_found in th_found_list:
    #         self.assertTrue(th_found)

    # def assert_contains_button(self, button_text_list):
    #     print button_text_list
    #     driver = self.driver
    #     button_found_list = [False for button in button_text_list]
    #     button_list = driver.find_elements_by_tag_name("button") # button is the tag for table heading
    #     for button in button_list:
    #         for idx, button_text in enumerate(button_text_list):
    #             if button.text == button_text:
    #                 button_found_list[idx] = True
    #                 break
    #     for idx, button_found in enumerate(button_found_list):
    #         if not button_found:
    #             print "button - "+button_text_list[idx]+" - not found"
    #     for button_found in button_found_list:
    #         self.assertTrue(button_found)

    # def assert_contains_link_text(self, link_text_list):
    #     print link_text_list
    #     driver = self.driver
    #     link_text_found_list = [False for link_text in link_text_list]
    #     link_list = driver.find_elements_by_tag_name("a") # a is the link tag
    #     for link in link_list:
    #         for idx, link_text in enumerate(link_text_list):
    #             if link_text in link.text:
    #                 link_text_found_list[idx] = True
    #                 break
    #     for idx, text_found in enumerate(link_text_found_list):
    #         if not text_found:
    #             print "link - "+link_text_list[idx]+" - not found"
    #     for link_found in link_text_found_list:
    #         self.assertTrue(link_found)

    # def assert_contains_form_label(self, label_text_list):
    #     print label_text_list
    #     driver = self.driver
    #     label_text_found_list = [False for label_text in label_text_list]
    #     label_list = driver.find_elements_by_tag_name("label") # a is the label tag
    #     for label in label_list:
    #         for idx, label_text in enumerate(label_text_list):
    #             if label_text[0:2] == '~ ':
    #                 if label_text[2:] in label.text:
    #                     label_text_found_list[idx] = True
    #                     break
    #             else:
    #                 if label.text == label_text:
    #                     label_text_found_list[idx] = True
    #                     break
    #     for idx, text_found in enumerate(label_text_found_list):
    #         if not text_found:
    #             print "label - "+label_text_list[idx]+" - not found"
    #     for label_found in label_text_found_list:
    #         self.assertTrue(label_found)

    # def assert_contains_H1(self, h1_text_list):
        # print h1_text_list
        # driver = self.driver
        # h1_found_list = [False for text in h1_text_list]
        # h1_list = driver.find_elements_by_tag_name('h1')
        # for h1 in h1_list:
        #     for idx, h1_text in enumerate(h1_text_list):
        #         if h1.text == h1_text:
        #             h1_found_list[idx] = True
        #             break
        # for idx, h1_found in enumerate(h1_found_list):
        #     if not h1_found:
        #         print "h1 - "+h1_text_list[idx]+" - not found"
        # for h1_found in h1_found_list:
        #     self.assertTrue(h1_found)



        # # print "pprinting ui_data"
        # # pprint(ui_data)
        # self.assert_contains_H1(ui_data['h1_text_list'])
        # self.assert_contains_link_text(ui_data['a_text_list'])
        # self.assert_contains_table_heading(ui_data['th_text_list'])
        # self.assert_contains_form_label(ui_data['label_text_list'])
        # self.assert_contains_button(ui_data['button_text_list'])





    # def assert_submenus(self, submenus):
    #     for key in submenus:
    #         print "    clicking on: "+key
    #         self.driver.find_element_by_id(key).click()
    #         self.assert_ui_data(submenus[key])
