//
// Created by rob on 7/30/16.
//

#include "rectangle.hpp"

   double Rectangle::getSide1() {
      return side1;
   };
   double Rectangle::getSide2() {
      return side2;
   };

   void Rectangle::setSide1(double side1In) {
      side1 = side1In;
   };
   void Rectangle::setSide2(double side2In) {
      side2 = side2In;
   };

   double Rectangle::calcPerimeter() {
      return (2 * ( side1 + side2 ));
   };
   double Rectangle::calcArea() {
      return (side1 * side2);
   };

   Rectangle::Rectangle() {
      side1 = 0;
      side2 = 0;
   };
   Rectangle::Rectangle(std::string n,double s1,double s2) {
      setName(n);
      setSide1(s1);
      setSide2(s2);
   };
   Rectangle::~Rectangle() {};