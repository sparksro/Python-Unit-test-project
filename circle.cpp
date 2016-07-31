//
// Created by rob on 7/29/16.
//

#include "circle.hpp"

double Circle::getRadius() {
   return radius;
}

void Circle::setRadius(double radiusIn) {
   radius = radiusIn;
}

double Circle::calcCircumference() {
  return (2 * 3.1415 * radius);
}

double Circle::calcArea() {
   return (3.1415926536 * (radius*radius) );
}

Circle::Circle(){
    name = "no-name";
    radius = 0.00;
};

Circle::Circle(std::string nameIn, double radiusIn)
{
   setName(nameIn);
   setRadius(radiusIn);
};

Circle::~Circle(){};
