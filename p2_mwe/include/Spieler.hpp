#pragma once
#include <iostream>
#include "../include/Spielbrett.hpp"
#include "../include/Schiffe.hpp"
#include <string>
#include <memory>

namespace SchiffeVersenken{

    class Spieler{
    public:
        /**
         * @brief Construct a new Spieler object
         * 
         * @param Name - Name des Spielers
         */
        Spieler(std::string Name);

        /**
         * @brief der Spieler gibt einen Schussversuch ab
         * 
         * @param x - x-Koordinate des Ziels
         * @param y - y-Koordinate des Ziels
         */
        //bool Schießen(int x, int y);

        /**
         * @brief Get the own sb object
         * 
         * @return std::shared_ptr<SpielBrett> 
         */
        //std::shared_ptr<SpielBrett> get_own_sb();

        /**
         * @brief Set the ene sb object
         * 
         * @param ensb Shared Pointer auf own_sb des Gegners
         */
        //void set_ene_sb(std::shared_ptr<SpielBrett> ensb);

        int get_id();

        void set_in_game(int id);

        int get_in_game();

        Schiffe get_ship();

        void add_tuple(int x, int y);

        void set_x(int x);

        void set_y(int y);

        int get_x();

    private:
        /**
         * @brief Hilfsfunktion zur Darstellung aller Schüsse auf den jeweiligen Spielbrettern
         * 
         * @param x x-Koordinate des zu markierenden Punktes
         * @param y y-Koordinate des zu markierenden Punktes
         * @param value "X" wenn Treffer, "O" wenn Fehlschuss
         */        
        //void markieren(int x, int y, std::string value);

        /**
         * @brief Name des Spielers
         * 
         */
        std::string name;

        /**
         * @brief id zur Identifikation des Spielers
         * 
         */
        size_t id;

        /*
        /**
         * @brief speichert das eigene Spielbrett
         * 
         */
        //SpielBrett own_sb;

        /**
         * @brief Spielbrett, das die eigenen Schussversuche enthält
         * 
         */
        //SpielBrett opview;

        /**
         * @brief Shared Pointer auf das Spielbrett des Gegners
         * 
         */
        //std::shared_ptr<SpielBrett> ene_sb;
        
        Schiffe ship;

        int in_game;

        int x;

        int y;
    };

}