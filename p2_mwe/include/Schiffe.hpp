#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <tuple>

using namespace std;
namespace SchiffeVersenken
{
    class Schiffe
    {
    public:
        Schiffe();
        void schiffe_platzieren();
        void koordinaten_einfügen(int a, int x, int y, string one_direction);
        void reset();

    private:
        vector<int> Schiffgrößen;
        vector<std::tuple<int,int>> Koordinaten;
        vector<int> Schiffgrößen2;
    };
}