//
// Created by rob on 7/30/16.
//

#ifndef SHAPES_RECTANGLE_HPP
#define SHAPES_RECTANGLE_HPP
# include "shape.hpp"

class Rectangle : public Shape {

   protected:
      double side1;
      double side2;

   public:
      double getSide1();
      double getSide2();

      void setSide1(double);
      void setSide2(double);

      double calcPerimeter();
      double calcArea();

      Rectangle();
      Rectangle(std::string,double = 0,double = 0);
      ~Rectangle();




};


#endif //SHAPES_RECTANGLE_HPP
