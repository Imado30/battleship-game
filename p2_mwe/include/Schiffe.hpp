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
         * @brief Die eingegebenen Koordinaten werden überprüft ob sie valide sind und dann im Koordinaten Array Tupel gespeichert
         * 
         * @param a Ist die eingegebene Schiffgröße
         * @param x Ist die eingegebene x-Koordinate
         * @param y Ist die eingegebene y-Koordinate
         * @param direction Ist die eingebenene Richtung vertikal/horizontal
         */
        void koordinaten_einfügen(int a, int x, int y, string direction);

        /**
         * @brief überprüft im die Koordinate getroffen wurde. Wenn true, dann wird die Koordinate aus dem Koordinaten Array entfernt
         * 
         * @param koordinate 
         * @return true 
         * @return false 
         */
        bool hit(int x, int y);

        /**
         * @brief aus x und y wird ein tupel erstellt und in Koordinaten eingefügt
         * 
         * @param x 
         * @param y 
         */
        void tupel_erstellen(int x, int y);

        /**
         * @brief Get the tupel object
         * 
         * @param index 
         * @return std::tuple<int,int> 
         */
        std::tuple<int,int> get_tupel(int index);

        /**
         * @brief Get the size object
         * 
         * @return int 
         */
        int get_size();

        /**
         * @brief Gibt alle Koordinaten zurück
         * 
         * @return std::vector<std::tuple<int,int>> 
         */
        std::vector<std::tuple<int,int>> get_koordinaten();

    private:
        /**
         * @brief Die einzelnen Schiff Koordinaten werden hier gespeichert
         * 
         */
        vector<std::tuple<int,int>> Koordinaten;
    };
}