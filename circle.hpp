//
// Created by rob on 7/29/16.
//
#include <string>
#ifndef SHAPES_CIRCLE_HPP
#define SHAPES_CIRCLE_HPP
#include "shape.hpp"

class Circle : public Shape {
private:
   double radius;

public:

   double getRadius();

   void setRadius(double radius);

   double calcCircumference();
   double calcArea();

   Circle();
   Circle(std::string,double);
   ~Circle();

};


#endif //SHAPES_CIRCLE_HPP
