#pragma once
#include <string>
#include <iostream>
#include <vector>

using namespace std;

namespace SchiffeVersenken
{

    class SpielBrett
    {

    public:
        SpielBrett(); // Konstruktor
        std::string Feld[10][10];

        void druckeSpielbrett();
        void set_value(int x, int y, string s);
        bool hit(int x, int y);
        void setzeSchiff(std::tuple<int,int> tupel);
    };
}