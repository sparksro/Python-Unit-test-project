//
// Created by rob on 7/29/16.
//

#include "shape.hpp"

// getters
std::string Shape::getName() {
   return this->name;
}

//setters
void Shape::setName( std::string nameIn) {
   name = nameIn;
}
//constructors
Shape::Shape() {
   name = "no-name";
};
Shape::Shape(std::string n) {
   setName(n);
}
//destructor
Shape::~Shape() {};
