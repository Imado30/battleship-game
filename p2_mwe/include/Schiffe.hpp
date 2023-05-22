#pragma once
#include <iostream>
#include <vector>
#include <string>

using namespace std;
namespace SchiffeVersenken
{
    class Schiffe
    {
    public:
        Schiffe();
        void schiffe_platzieren();
        void koordinaten_einfügen(int a, int x, int y, string richtung);
        void reset();

    private:
        vector<int> Schiffgrößen;
        vector<int> Koordinaten;
        vector<int> Schiffgrößen2;
    };
}