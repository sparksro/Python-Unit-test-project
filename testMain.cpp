// Created by Rob Sparks on 7/30/16
//
// Purpose: write some classes that a python based test script can interact with / operate.
// Description: This main drives 4 different classes and their member functions.  They are described
// here as apposed to in the class files.
//
// Shape: shape.hpp and shape.cpp This is the base class. This could have been implemented as virtual
// but I wanted to run python based tests on it as well as the rest of the derived classes.  It has the
// following variables, setters, mutators, and constructors:
// name, getName(), setName(string), Shape(), Shape(string)
//
// Circle: circle.hpp and circle.cpp  Derived class of shape.  It has the following:
// radius, getRadius(), setRadius(), calcCircumference() calcArea(), Circle(), Circle(sting, double)
//
// Rectangle: rectangle.hpp and rectangle.cpp  Derived class of Shape. It has the following implemented:
// side1, side2, getSide1(), getSide2(), setSide1(double), setSide2(double), calcPerimeter(), double calcArea();
// Rectangle(), Rectangle(string,double,double);
//
// Square: square.hpp and square.cpp  Derived class of Rectangle. It has the following implemented:
// setSide1(double), setSide2(double), calcPerimeter(), calcArea(), Square(), Square(string,double);
// Because square inherits from rectangle the members listed above that are the same as rectangles
// override them.  Caution in using the setSideX() methods.  Use one or the other both sides will be
// set to the same value.  If you attempt to use both setSide1() and setSide2() the sides will be set
// which ever you use last.
//
// testMain.cpp This file contains all the tests that run on the above classes.  I can and could think of more to
// add but will stop as this was really just practice.  This main takes a number input to run a test and then
// ends.  The python script launches it multiple times and then runs all the tests.  This seems like a waist as
// the complied executable needs to be relaunched for each test but but things happen to fast for a while
// loop to be effective and keep the executable up and running.  You will see it runs quite fast despite and
// this is more a human thing than a computer thing I think.
//
#include <iostream>
#include <iomanip>
#include "circle.hpp"
#include "rectangle.hpp"
#include "square.hpp"

int main(){
   int input;
   std::cin>> input;
      // shape -base class
         //tests for:  default name, reset of same object name, constrctor set of name
   Shape s1;
      if (input == 1)//test-1
      {
         std::cout << s1.getName() << std::endl;
      }
      if (input == 2)//test-2
      {
         s1.setName("Base_class_shape");
         std::cout << s1.getName() << std::endl;
      }
      if (input == 3)//test-3
      {
         Shape s2 ("shape2");
         std::cout << s2.getName() << std::endl;
      }

//========================================================================================
   //circle -  derived class of shape
   Circle c1;
   //test default constructor and for default values
      if(input == 4)//test-4
      {
         std::cout << c1.getName() << std::endl;
      }
      if(input == 5)//test-5
      {
         std::cout << c1.getRadius() << std::endl;
      }

      //test the setter functions
      c1.setName("class_circle");
      c1.setRadius(5.00);
      if(input == 6)//test-6
      {
         std::cout << c1.getName() << std::endl;
      }
      if(input == 7)//test-7
      {
         std::cout << c1.getRadius() << std::endl;
      }
      //test circumfrance calculation and area calculation
      c1.setRadius(5.25);//test-8 & 9
      if(input == 8)
      {
         std::cout << std::setprecision(4) << c1.calcCircumference() << std::endl;
      }
      if(input == 9)
      {
         std::cout << std::setprecision(4) << c1.calcArea() << std::endl;
      }

      c1.setRadius(507.42);//test-10 & 11
      if(input == 10)
      {
         std::cout << std::setprecision(6) << c1.calcCircumference() << std::endl;
      }
      if(input == 11)
      {
         std::cout << std::setprecision(8) << c1.calcArea() << std::endl;
      }
      c1.setRadius(0);
      if(input == 12)//test-12 & 13
      {
         std::cout << std::setprecision(4) << c1.calcCircumference() << std::endl;
      }
      if(input == 13)
      {
         std::cout << std::setprecision(4) << c1.calcArea() << std::endl;
      }

//========================================================================================
   //Rectangle - derived class of shape
   // test of default constructor
   Rectangle r1;
      if (input == 14)//test-14
      {
         std::cout << r1.getName() << std::endl;
      }
      if (input == 15)//test-15
      {
         std::cout << r1.getSide1() << std::endl;
      }
      if (input == 16)//test-16
      {
         std::cout << r1.getSide2() << std::endl;
      }
   Rectangle r2 ("rectangle2", 5, 7);
      //test of three param constructor
      if (input == 17)//test-17
      {
         std::cout << r2.getName() << std::endl;
      }
      if (input == 18)//test-18
      {
         std::cout << r2.getSide1() << std::endl;
      }
      if (input == 19)//test-19
      {
         std::cout << r2.getSide2() << std::endl;
      }
      //test of calculations
      if (input == 20)//test-20
      {
         std::cout << std::setprecision(4) << r2.calcPerimeter() << std::endl;
      }
      if (input == 21)//test-21
      {
         std::cout << std::setprecision(4) << r2.calcArea() << std::endl;
      }
      // reset sides and test calculations again this time with larger numbers and decimal values
      r2.setSide1(100.47);
      r2.setSide2(135.57);
      if (input == 22)//test-22
      {
         std::cout << r2.getSide1() << std::endl;
      }
      if (input == 23)//test-23
      {
         std::cout << r2.getSide2() << std::endl;
      }
      if (input == 24)//test-24
      {
         std::cout << std::setprecision(5) << r2.calcPerimeter() << std::endl;
      }
      if (input == 25)//test-25
      {
         std::cout << std::setprecision(7) << r2.calcArea() << std::endl;
      }
//========================================================================================
   //Square -derived class of Rectangle
      Square sq1;
      if (input == 26)//test-26
      {
         std::cout << sq1.getName() << std::endl;
      }
      if (input == 27)//test-27
      {
         std::cout << sq1.getSide1() << std::endl;
      }
      if (input == 28)//test-28
      {
         std::cout << sq1.getSide2() << std::endl;
      }
      Square sq2 ("square2", 5);
      //test of three param constructor
      if (input == 29)//test-29
      {
         std::cout << sq2.getName() << std::endl;
      }
      if (input == 30)//test-30
      {
         std::cout << sq2.getSide1() << std::endl;
      }
      if (input == 31)//test-31
      {
         std::cout << sq2.getSide2() << std::endl;
      }
      if (input == 32)//test-32
      {
         if (sq2.getSide1() == sq2.getSide2())
            std::cout << "true" << std::endl;
         else
            std::cout <<"false - both sides are not the same." << std::endl;
      }
      //test of calculations
      if (input == 33)//test-33
      {
         std::cout << std::setprecision(4) << sq2.calcPerimeter() << std::endl;
      }
      if (input == 34)//test-34
      {
         std::cout << std::setprecision(4) << sq2.calcArea() << std::endl;
      }
      // reset sides and test calculations again this time with larger numbers and decimal values
      sq2.setSide1(115.47);
      sq2.setSide2(135.57);
      if (input == 35)//test-35
      {
         std::cout << sq2.getSide1() << std::endl;
      }
      if (input == 36)//test-36
      {
         std::cout << sq2.getSide2() << std::endl;
      }
      if (input == 37)//test-37
      {
         if (sq2.getSide1() == sq2.getSide2())
            std::cout << "true" << std::endl;
         else
            std::cout <<"false - both sides are not the same." << std::endl;
      }
      if (input == 38)//test-38
      {
         std::cout << std::setprecision(5) << sq2.calcPerimeter() << std::endl;
      }
      if (input == 39)//test-39
      {
         std::cout << std::setprecision(7) << sq2.calcArea() << std::endl;
      }

   return 0;
}