#pragma once
#include <string>
#include <iostream>
#include <vector>

namespace SchiffeVersenken {

  class SpielBrett {

public:
    SpielBrett();  // Konstruktor
    std::string Feld[10][10];

    void druckeSpielbrett();
    void set_value(int x, int y, string s);
    bool hit(int x, int y);
    void setzeSchiff(int x, int y);
    void loescheSchiff(int x, int y);
};

}
