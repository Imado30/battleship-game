#include "/home/odin/Projekt2/p2_mwe/include/Spieler.hpp"
#include <iostream>
#include <functional>

namespace SchiffeVersenken{

    Spieler::Spieler(std::string Name){
        name=Name;
        id=std::hash<std::string>()(Name);
    }


}