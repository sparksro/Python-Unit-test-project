//
// Created by rob on 7/30/16.
//

#include "square.hpp"

void Square::setSide1(double side1In) {
   side1 = side1In;
   side2 = side1In;
};
void Square::setSide2(double side2In) {
   side1 = side2In;
   side2 = side2In;
};

double Square::calcPerimeter() {
   return (2 * ( side1 + side2 ));
};
double Square::calcArea() {
   return (side1 * side2);
};

Square::Square() {};
Square::Square(std::string n,double s1) {
   setName(n);
   setSide1(s1);
   setSide2(s1);
};
Square::~Square() {};