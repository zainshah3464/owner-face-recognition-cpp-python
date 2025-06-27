#include <iostream>
#include <cstdlib>  // for system()

int main() {
    std::cout << "🔓 Launching Face Recognition System..." << std::endl;

    // Full path to your Python file (change as needed)
    std::string command = R"(python "H:\Main-Sarver\Projects\Final Versions\Testing Project\3.py")";


    int result = system(command.c_str());

    if (result == 0) {
        std::cout << "✅ Python script executed successfully." << std::endl;
    } else {
        std::cout << "❌ Failed to run Python script." << std::endl;
    }

    return 0;
}
