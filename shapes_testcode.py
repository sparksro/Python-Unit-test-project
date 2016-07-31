# testcodePY_27.py by Rob Sparks
#
# This python based test script operates and compiles a C++ based set of class files.
# You can view the list of file names in the compile script line (# 82 and 83) bellow. The C++ executable
# name is specified there as well and is currently set as shapes. You can read more about
# the C++ files them selves in the testMain.cpp file header.  It outputs the test results to a text file
# with the name of shapes_test_results.txt to the same directory containing that the script and the class files.
#
# This script should run in 2.x or 3.x versions of python. It is actually tested to run in 2.7 and 3.5
# but has not been tested in earlier or versions between.  If you experience an error try one or the other
# confirmed tested versions.
#
# Tests bellow are implemented with a standard function called test_base.  It is feed parameters
# for the tests see explanations in function header bellow.

from signal import alarm, signal, SIGALRM
import sys
import subprocess
import time
from subprocess import Popen
from subprocess import PIPE

outFile = open("shapes_test_results.txt", "w")
py_version = sys.version_info[0] # get the version of python that this is being run in
# outFile.write("The py version is: " + str(py_version)+ "\n")

class Alarm(Exception):
   pass
def alarm_handler(signum, frame):
   raise Alarm
signal(SIGALRM, alarm_handler)

passedTests = 0 # variable to count passed tests

# ********             main test function                   **********
# This function runs all the tests implemented for the shapes based classes.  It adapts
# to either Python 2.7 or 3.5 tested but I suspect it will at least work successfully in the
# range between.
# params:
#       file - name of the executable file to call to run the test. Currently only one.
#       testString - the value you are expecting from the test in string format
#       testNumber - the number of the test that will be called from the C++ testMain.cpp file
#       testDescription - detailed description of the test. Try to stay bellow 80 chars
#       passedTest - int value keeping track of passed tests
#
def test_base(file, testString, testNumber, testDescription, passedTests):
    #py_version = sys.version_info[0]

    try:
        p = Popen([file], stdin=PIPE, stdout=subprocess.PIPE)
        alarm(5)
        try:
            # make changes so that this will run in 2.x python or 3.x
            # currently tested with 2.7 and 3.5
            str = ''
            if (2 is py_version):
                str = p.communicate(testNumber)[0]

            elif (3 is py_version): # python 3.x takes a little more explicit conversion
                bytes = testNumber.encode()
                bytes_returned = p.communicate(bytes)[0]
                str = bytes_returned.decode("utf-8")
            else:
                outFile.write("\t This script does not currently support your version of python. Try 2.7 or 3.5 \n")
                exit()
            if str == testString:
                outFile.write("\t" + testDescription + " - passed.\n")
                passedTests += 1
                return passedTests
            else:
                outFile.write("\t" + testDescription + " - failed.\n")
                outFile.write("\t\tExpected value: " + testString + "\t\tOutput value: " + str + "\n")
                return passedTests
            alarm(0)
        except Alarm:
            outFile.write('\tInfinite loop in test ' + testNumber + '?\n')
            p.kill()
    except OSError:
        outFile.write('\The executable was not found.\n')

try:
   subprocess.check_call(["g++", "shape.hpp", "shape.cpp", "circle.hpp", "circle.cpp", "testMain.cpp",
                          "rectangle.hpp", "rectangle.cpp", "square.hpp", "square.cpp", "-o", "shapes"])
except subprocess.CalledProcessError:
   outFile.write('\nCompilation encountered errors.\n')

#  *********              Tests - separated by class *               *********
# ------------------------------------------------------------------------------
# Shape base class - test 1
outFile.write("\n ****  Unit Tests for Shape, Circle, Rectangle and Square classes -tested: "
              + str(time.strftime("%m/%d/%Y")) + " " + str(time.strftime("%I:%M %p")) + " in Python: " +
              str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]) + "  ****\n")
outFile.write("\nShapes Base Class - Tests.\n")
file = "./shapes"
testString = 'no-name\n'
testNumber = '1'
testDescription = "Shapes class-test 1: default constructor set correctly test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Shape base class - test 2
testString = 'Base_class_shape\n'
testNumber = '2'
testDescription = "Shapes base class-test 2: member function setName() name re-set test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Shape base class test 3
testString = 'shape2\n'
testNumber = '3'
testDescription = "Shapes base class-test 2: member function setName() name re-set test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# ------------------------------------------------------------------------------
# Circle derived class of Shape - test 4
outFile.write("\nCircle derived Class - Tests.\n")
testString = 'no-name\n'
testNumber = '4'
testDescription = "Shapes base class-test 2: member function setName() name re-set test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Circle derived class of Shape - test 5
testString = '0\n'
testNumber = '5'
testDescription = "Circle class-test 5: default constructor default radius value assignment test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Circle derived class of Shape -test 6
testString = 'class_circle\n'
testNumber = '6'
testDescription = "Circle class-test 6: member function setName() test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Circle derived class of Shape -test 7
testString = '5\n'
testNumber = '7'
testDescription = "Circle class-test 7: member function setRadius() test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Circle derived class of Shape -test 8 & 9
testString = '32.99\n'
testNumber = '8'
testDescription = "Circle class-test 8: member function calcCircumference() test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

testString = '86.59\n'
testNumber = '9'
testDescription = "Circle class-test 9: member function calcArea() test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Circle derived class of Shape -test 10
testString = '3188.12\n'
testNumber = '10'
testDescription = "Circle class-test 10: member function calcCircumference() test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Circle derived class of Shape -test 11
testString = '808881.75\n'
testNumber = '11'
testDescription = "Circle class-test 11: member function calcArea() test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Circle derived class of Shape -test 12
testString = '0\n'
testNumber = '12'
testDescription = "Circle class-test 12: member function calcCircumference() test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Circle derived class of Shape -test 13
testString = '0\n'
testNumber = '13'
testDescription = "Circle class-test 13: member function calcArea() test"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# ------------------------------------------------------------------------------
# Rectangle derived class of Shape -test 14
outFile.write("\nRectangle derived Class - Tests.\n")
testString = 'no-name\n'
testNumber = '14'
testDescription = "Rectangle class-test 14: default constructor test of default name"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Rectangle derived class of Shape -test 15
testString = '0\n'
testNumber = '15'
testDescription = "Rectangle class-test 15: default constructor set of side 1 "
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Rectangle derived class of Shape -test 16
testString = '0\n'
testNumber = '16'
testDescription = "Rectangle class-test 16: default constructor set of side 2"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# rectangle r2
# Rectangle derived class of Shape -test 17
testString = 'rectangle2\n'
testNumber = '17'
testDescription = "Rectangle class-test 17: 3 parm constructor test of set name"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Rectangle derived class of Shape -test 18
testString = '5\n'
testNumber = '18'
testDescription = "Rectangle class-test 18: 3 parm constructor test of set of side 1 "
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Rectangle derived class of Shape -test 19
testString = '7\n'
testNumber = '19'
testDescription = "Rectangle class-test 19: test of setSide1() member function"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Rectangle derived class of Shape -test 20
testString = '24\n'
testNumber = '20'
testDescription = "Rectangle class-test 20: test of setSide2() member function"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# reset of side and test again with different values
# Rectangle derived class of Shape -test 21
testString = '35\n'
testNumber = '21'
testDescription = "Rectangle class-test 21: test of calcPerimeter()"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Rectangle derived class of Shape -test 22
testString = '100.47\n'
testNumber = '22'
testDescription = "Rectangle class-test 22: test of setSide1() member function"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Rectangle derived class of Shape -test 23
testString = '135.57\n'
testNumber = '23'
testDescription = "Rectangle class-test 23: test of setSide2() member function"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Rectangle derived class of Shape -test 24
testString = '472.08\n'
testNumber = '24'
testDescription = "Rectangle class-test 24: test of calcPerimeter()"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Rectangle derived class of Shape -test 25
testString = '13620.72\n'
testNumber = '25'
testDescription = "Rectangle class-test 25: test of calcArea()"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# ------------------------------------------------------------------------------
# Square derived class of Rectangle -test 26
outFile.write("\nSquare derived Class - Tests.\n")
testString = 'no-name\n'
testNumber = '26'
testDescription = "Square class-test 26: default constructor test of default name"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Square derived class of Rectangle -test 27
testString = '0\n'
testNumber = '27'
testDescription = "Square class-test 27: default constructor set of side 1 "
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Square derived class of Rectangle -test 28
testString = '0\n'
testNumber = '28'
testDescription = "Square class-test 28: default constructor set of side 2"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# square sq2
# Square derived class of Rectangle -test 29
testString = '- Test simulated error to view output\n'
testNumber = '29'
testDescription = "Square class-test 29: 3 parm constructor test of set name"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Square derived class of Rectangle -test 30
testString = '5\n'
testNumber = '30'
testDescription = "Square class-test 30: 3 parm constructor test of set of side 1 "
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Square derived class of Rectangle -test 31
testString = '5\n'
testNumber = '31'
testDescription = "Square class-test 31: 3 parm constructor test of set of side 1 "
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Square derived class of Rectangle -test 32
testString = 'true\n'
testNumber = '32'
testDescription = "Square class-test 32: both sides are the same value of last set"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Square derived class of Rectangle -test 33
testString = '20\n'
testNumber = '33'
testDescription = "Square class-test 33: test of calcPerimeter() function"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Square derived class of Rectangle -test 34
testString = '25\n'
testNumber = '34'
testDescription = "Square class-test 34: test of calcArea()"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# reset of side and test again with different values
# Square derived class of Rectangle -test 35
testString = '135.57\n'
testNumber = '35'
testDescription = "Square class-test 35: test of setSide1() member function"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Square derived class of Rectangle -test 36
testString = '135.47 -test of the tester\n'
testNumber = '36'
testDescription = "Square class-test 36: test of setSide2() member function"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Square derived class of Rectangle -test 37
testString = 'true\n'
testNumber = '37'
testDescription = "Square class-test 37: test that both sides are the same"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Square derived class of Rectangle -test 38
testString = '542.28\n'
testNumber = '38'
testDescription = "Square class-test 38: test of calcPerimeter()"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Square derived class of Rectangle -test 39
testString = '18379.22\n'
testNumber = '39'
testDescription = "Square class-test 39: test of calcArea()"
passedTests = test_base(file, testString, testNumber, testDescription, passedTests)

# Ending print out stuff ----------------------------------------------------------
totalTests = 39 # this number is currently hand annotated
outFile.write('\n %d tests passed out of a total of' % passedTests)
outFile.write(' %d.\n' % totalTests )
outFile.write("Testing complete\n")
outFile.close()

