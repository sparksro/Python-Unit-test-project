//
// Created by rob on 7/30/16.
//

#ifndef SHAPES_SQUARE_HPP
#define SHAPES_SQUARE_HPP
#include "rectangle.hpp"

class Square : public Rectangle{

public:

   void setSide1(double);
   void setSide2(double);

   double calcPerimeter();
   double calcArea();

   Square();
   Square(std::string,double = 0);
   ~Square();
};


#endif //SHAPES_SQUARE_HPP
