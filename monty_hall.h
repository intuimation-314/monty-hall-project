/**
 * @file monty_hall.h
 * @brief Header for Monty Hall problem simulation.
 *
 * Defines the MontyHall class for interactive gameplay and simulations,
 * along with utilities to visually display doors and log game statistics.
 */

 #ifndef MONTY_HALL_H
 #define MONTY_HALL_H
 
 #include <vector>
 #include <string>
 
 /**
  * @class MontyHall
  * @brief Simulates the Monty Hall problem with n doors.
  */
 class MontyHall {
 private:
     int doors;         ///< Number of doors
     int prizeDoor;     ///< Door hiding the car
     int userChoice;    ///< Player's selected door
     int hostOpens;     ///< Door opened by host (goat)
     bool switchChoice; ///< Whether player chose to switch
 
 public:
     /**
      * @brief Constructs a MontyHall game with a given number of doors.
      * @param numberOfDoors Number of doors to use (minimum 3)
      */
     MontyHall(int numberOfDoors = 3);
 
     /**
      * @brief Runs the interactive version of the game.
      */
     void runInteractiveGame();
 
     /**
      * @brief Runs multiple simulations of the game.
      * @param simulations Number of rounds to simulate
      */
     void runSimulation(int simulations);
 
     /**
      * @brief Simulates a single game round internally.
      * @return True if player wins, false if not
      */
     bool playSingleSimulation();
 };
 
 /**
  * @brief Prints ASCII door layout and game explanation.
  * @param numDoors Number of doors to display
  */
 void printIntroDiagram(int numDoors);
 
 /**
  * @brief Displays door layout in current game state.
  * @param numDoors Number of doors
  * @param revealedGoats Doors Monty revealed as goats
  * @param userPick User's door choice
  * @param prize The winning door
  * @param final If true, show final reveal (CAR/GOAT)
  */
 void displayDoors(int numDoors, std::vector<int> revealedGoats = {}, int userPick = -1, int prize = -1, bool final = false);
 
 /**
  * @brief Logs the result of a game or simulation round.
  * @param mode "Interactive" or "Simulation"
  * @param doors Number of doors used
  * @param switched Whether the user switched
  * @param won Whether the user won
  */
 void logGameResult(const std::string& mode, int doors, bool switched, bool won);
 
 /**
  * @brief Displays the logged game history from file.
  */
 void viewGameStats();
 
 #endif // MONTY_HALL_H
 