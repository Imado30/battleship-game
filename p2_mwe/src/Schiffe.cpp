#include "../include/Schiffe.hpp"
#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;
namespace SchiffeVersenken
{
    Schiffe::Schiffe()
    {
        Schiffgrößen.push_back(6);
        Schiffgrößen.push_back(5);
        Schiffgrößen.push_back(4);
        Schiffgrößen.push_back(3);
        Schiffgrößen.push_back(2);
    }

    void Schiffe::reset()
    {
        for (int i = 0; i < Schiffgrößen2.size(); i++)
        {
            Schiffgrößen.push_back(Schiffgrößen2[i]);
        }
        for (int i = 0; i < Schiffgrößen2.size(); i++)
        {
            Schiffgrößen2.pop_back();
        }
    }

    void Schiffe::koordinaten_einfügen(int a, int x, int y, string direction)
    {
        if (direction == "r")
        {
            vector<tuple<int,int>> überschneiden_array;
            for (int i = 0; i < a; i++)
            {
                tuple<int, int> überschneiden(x+i, y);
                überschneiden_array.push_back(überschneiden);
            }

            for (const auto &tupel : Koordinaten)
            {
                for (const auto& tupel2 : überschneiden_array)
                {
                    if (tupel2 == tupel)
                    {
                        throw invalid_argument("Schiff kann nicht eingefügt werden, da sich die Schiffe sonst kreuzen");
                    }
                }
            }

            if (x + a > 9)
            {
                throw std::invalid_argument("Schiff kann nicht in die Koordinate eingefügt werden. Das Schiff überschreitet sonst das Spielfeld");
            }

            else
            {
                for (int i = 0; i < a; i++)
                {
                    std::tuple<int, int> schiff(x+i, y);
                    Koordinaten.push_back(schiff);
                }
            }
        }

        else if (direction == "v")
        {
            vector<tuple<int,int>> überschneiden_array2;
            for (int i = 0; i < a; i++)
            {
                tuple<int, int> überschneiden2(x, y+i);
                überschneiden_array2.push_back(überschneiden2);
            }

            for (const auto &tupel : Koordinaten)
            {
                for (const auto& tupel2 : überschneiden_array2)
                {
                    if (tupel2 == tupel)
                    {
                        throw invalid_argument("Schiff kann nicht eingefügt werden, da sich die Schiffe sonst kreuzen");
                    }
                }
            }

            if (y + a > 9)
            {
                throw std::invalid_argument("Schiff kann nicht in die Koordinate eingefügt werden. Das Schiff überschreitet sonst das Spielfeld");
            }

            else
            {
                for (int i = 0; i < a; i++)
                {
                    std::tuple<int, int> schiff(x, y + i);
                    Koordinaten.push_back(schiff);
                }
            }
        }
    }

    void Schiffe::schiffe_platzieren()
    {
        while (Schiffgrößen.size() != 0)
        {
            // geordnetes Schiffgrößen Array wird nach jeder Eingabe dem Spieler vorgezeigt
            std::sort(std::begin(Schiffgrößen), std::end(Schiffgrößen), std::greater<>());

            cout << "Es stehen dir folgende Schiffgrößen zum platzieren zur Verfügung: [ ";
            for (int i = 0; i < Schiffgrößen.size(); i++)
            {
                cout << Schiffgrößen[i] << " ";
            }
            cout << "]" << endl
                 << "Gebe die Schiffgröße an, mit der du anfangen willst                                 (0 ist der Reset Button, falls du alles neu anordnen willst)" << endl;

            // Eingabe der Schiffgröße
            int eingabe;
            cin >> eingabe;
            cout << endl;

            // 0 wäre der Reset Button
            if (eingabe != 0)
            {
                // neues Array wo eingabe und die restlichen Schiffgrößen eingefügt und sortiert werden
                vector<int> überprüfen;
                überprüfen.push_back(eingabe);
                for (int i = 0; i < Schiffgrößen.size(); i++)
                {
                    if (Schiffgrößen[i] != eingabe)
                        überprüfen.push_back(Schiffgrößen[i]);
                }
                std::sort(std::begin(überprüfen), std::end(überprüfen), std::greater<>());

                // Es wird auf gleichheit der Arrays überprüft. Ist die Eingabe keine Zahl aus den Schiffgrößen, sind die Arrays ungleich => Exception
                if (überprüfen == Schiffgrößen)
                {
                    // Hier müssen noch überall exceptions hin!!!
                    int x_koordinate;
                    int y_koordinate;
                    string richtung;

                    cout << "Gib die x-Koordinate ein für Schiff Größe: " << eingabe << endl;
                    cin >> x_koordinate;
                    if (x_koordinate < 0 || x_koordinate > 9)
                    {
                        throw std::invalid_argument("Eingegebenes Element ist nicht auf der x-Achse (0 - 9)");
                    }

                    cout << "Gib die y-Koordinate ein für Schiff Größe: " << eingabe << endl;
                    cin >> y_koordinate;
                    if (y_koordinate < 0 || y_koordinate > 9)
                    {
                        throw std::invalid_argument("Eingegebenes Element ist nicht auf der y-Achse (0 - 9)");
                    }

                    cout << "gib h für horizontal und v für vertikal ein " << endl;
                    cin >> richtung;
                    if (richtung != "h" && richtung != "v")
                    {
                        throw std::invalid_argument("Eingegebenes Element ist weder h (horizontal) noch v (vertikal)");
                    }

                    try
                    {
                        Schiffe::koordinaten_einfügen(eingabe, x_koordinate, y_koordinate, richtung);
                    }
                    catch (const std::invalid_argument e)
                    {
                        cout << "ERROR: '" << e.what() << "'" << endl;
                        break;
                    }

                    // Die Eingabe wird durch Positionen tauschen im Array aus Schiffgrößen entfernt und in anderes Array eingefügt
                    for (int i = 0; i < Schiffgrößen.size(); i++)
                    {
                        if (Schiffgrößen[i] == eingabe)
                        {
                            Schiffgrößen2.push_back(Schiffgrößen[i]);
                            int last_element = Schiffgrößen[Schiffgrößen.size() - 1];
                            int current_element = Schiffgrößen[i];
                            Schiffgrößen[i] = last_element;
                            Schiffgrößen[Schiffgrößen.size()] = current_element;
                            Schiffgrößen.pop_back();

                            // überprüfen Array muss geleert werden
                            for (int i = 0; i < überprüfen.size(); i++)
                            {
                                überprüfen.pop_back();
                            }
                        }
                    }
                }
                else
                {
                    throw std::invalid_argument("Eingegebenes Element gehört nicht zu den Schiffsgrößen");
                }
            }
            else
            {
                Schiffe::reset();
            }
        }
    }
}