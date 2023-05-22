#include "../include/Schiffe.hpp"
#include <iostream>
#include <vector>

using namespace std;
namespace SchiffeVersenken
{
    Schiffe::Schiffe()
    {
        Schiffgrößen.push_back(5);
        Schiffgrößen.push_back(4);
        Schiffgrößen.push_back(3);
        Schiffgrößen.push_back(3);
        Schiffgrößen.push_back(2);
    }

    void Schiffe::schiffe_platzieren()
    {
        cout << "Es stehen dir folgende Schiffgrößen zum platzieren zur Verfügung: [ ";
        for (int i = 0; i < Schiffgrößen.size(); i++)
        {
            cout << Schiffgrößen[i] << " ";
        }
        cout << "]" << endl;
    }
}