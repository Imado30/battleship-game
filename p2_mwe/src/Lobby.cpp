#include <iostream>
#include "../include/Lobby.hpp"

namespace SchiffeVersenken{

    Lobby::Lobby(){};

    Spieler Lobby::spieler_erstellen(std::string name){
        Spieler x(name);
        queue.push_back(x);
        if(queue.size()>=2){
            spiel_erstellen();
        }
        return x;
    }

    bool Lobby::waiting(int id){
        for(Spieler element:queue){
            if(element.get_id()==id){
                return true;
            }
        }
        return false;
    }  

    Spiel Lobby::spiel_erstellen(){

        Spiel a(queue[0],queue[1]);
        queue.erase(queue.begin());
        queue.erase(queue.begin());

        spiele.push_back(a);

        return a;        
    }
}