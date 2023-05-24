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
        /**
         * @brief Konstruktor in dem die festen Schiffgrößen definiert werden
         * 
         */
        Schiffe();

        /**
         * @brief Es werden nacheinander einzelne Schiffe mit verschiedenen Schiffgrößen platziert
         * 
         */
        void schiffe_platzieren();

        /**
         * @brief Die eingegebenen Koordinaten werden überprüft ob sie valide sind und dann im Koordinaten Array Tupel gespeichert
         * 
         * @param a Ist die eingegebene Schiffgröße
         * @param x Ist die eingegebene x-Koordinate
         * @param y Ist die eingegebene y-Koordinate
         * @param direction Ist die eingebenene Richtung vertikal/horizontal
         */
        void koordinaten_einfügen(int a, int x, int y, string direction);

        /**
         * @brief Wenn 0 eingegeben wird, wird alles zurückgesetzt und es kann neu platziert wird
         * 
         */
        void reset();


    private:
        /**
         * @brief Die festen Schiffgrößen werden hier gespeichert
         * 
         */
        vector<int> Schiffgrößen;

        /**
         * @brief Die schon erstellten und entfernten Schiffe werden für das zurücksetzen hier gespeichert
         * 
         */
        vector<int> Schiffgrößen2;

        /**
         * @brief Die einzelnen Schiff Koordinaten werden hier gespeichert
         * 
         */
        vector<std::tuple<int,int>> Koordinaten;
    };
}