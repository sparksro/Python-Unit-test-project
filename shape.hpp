//
// Created by rob on 7/29/16.
//
#include <iostream>
#include <string>

#ifndef SHAPES_SHAPE_HPP
#define SHAPES_SHAPE_HPP


class Shape {

   protected:
      std::string name;

   public:
      //getters
      std::string getName();
      //setters
      void setName( std::string nameIn);

      //constructors
      Shape();
      Shape(std::string);
      ~Shape();

};


#endif //SHAPES_SHAPE_HPP
