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
        queue.erase(queue.begin()+1); //geändert

        spiele.push_back(a);
        std::cout << "Spiel erstellt" << std::endl;
        return a;        
    }

    Spieler Lobby::get_player1(){
        if (queue.size()==0){
            throw std::out_of_range("Die Queue ist leer");
        }
        return queue[0];
    }

    int Lobby::spiele_size(){
        return spiele.size();
    }

    int Lobby::queue_size(){
        return queue.size();
    }
}