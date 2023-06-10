#include <iostream>
#include "../include/Lobby.hpp"

namespace SchiffeVersenken{

    Lobby::Lobby(){
        for (int i=0; i<10; i++){
            game_ids.push_back(i);
            id_max=9;
        }
    };

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

        if (game_ids.size()==0){
            add_ids();
        }

        Spieler s1=queue[0];
        Spieler s2=queue[1];
        int id1=s1.get_id(), id2=s2.get_id();
        int new_g_id=game_ids[0];

        Spiel a(s1,s2, new_g_id);
        playing.insert(std::pair <int, Spieler>(id1, s1));
        playing.insert(std::pair <int, Spieler>(id2, s1));
        playing.at(id1).set_in_game(new_g_id);
        playing.at(id2).set_in_game(new_g_id);

        game_ids.erase(game_ids.begin());
        queue.erase(queue.begin());
        queue.erase(queue.begin()+1); //geändert

        games.insert(std::pair <int,Spiel>(a.get_game_id(), a));
        //spiele.push_back(a);
        std::cout << "Spiel erstellt" << std::endl;
        return a;        
    }

    Spieler Lobby::get_player1(){
        if (queue.size()==0){
            throw std::out_of_range("Die Queue ist leer");
        }
        return queue[0];
    }

    int Lobby::spiele_size(){                   //wenns klappt noch umbenennen
        return games.size();
        //return spiele.size();
    }

    int Lobby::queue_size(){
        return queue.size();
    }

    void Lobby::add_ids(){
        for (int i=id_max; i<id_max*2; i++){
            game_ids.push_back(i);
        }
        id_max*=2;
    }

    Spieler Lobby::player_by_id(int id){
        return playing.at(id);
    }

    Spiel Lobby::game_by_id(int id){
        return games.at(id);
    }
}