# -*- coding: utf8 -*-
import os, sys
import test_run , test_list, test_results, test_html

clearscreen = "cls"
testpath = ".\\test_runs\\"

#MAIN MENU
def menu():
    os.system(clearscreen)
    print("""
    #==============================#
    #             MENU             #
    #==============================#
    1 - Set env or exe to test
    2 - Start test
    3 - Manual operation
    4 - List of test
    5 - Result of tests
    0 - Exit
    ================================
    """)
    choice = input("Entry your choice [Enter]:  ")
    return choice

#TAKE CHOICE AND LAUNCH MODULE
choice = ""
while choice != "0":    
    choice = menu()
    if choice == "1":
        os.system(clearscreen)
        test_run.run_tests(testpath)
    elif choice == "2":
        os.system(clearscreen)
        test_list.list_tests()
    elif choice == "3":
        os.system(clearscreen)
        test_results.show_test_results(testpath)
    elif choice == "4":
        os.system(clearscreen)
        test_html.test_html_report(testpath)
    elif choice == "5":
        os.system(clearscreen)
        print("""
    ================================
    MWS Inspector
    ================================
    At first you have to setup which exe you want to setup
    You can choose the exe from orignal path, input path manually
    or connect to exe in debug mode.
    Then choose which test you want to run. 
        """)
        input("Naciśnij [Enter]:  ")

