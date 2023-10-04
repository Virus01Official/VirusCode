import os

# Define the code template
code_template = """
#include <iostream>
#include <string>
#include <unordered_map>
#include <sstream>

std::unordered_map<std::string, double> numericVariables; // Store numeric variable names and values

// Function to evaluate expressions
double evaluateExpression(const std::string& expression);

{custom_code}

int main() {{
    // Example usage

    // Set numeric variables using "var" syntax
    numericVariables["x"] = 5.0;

    // Create a loop using the "task.loop" syntax
    executeLoop("loop 3"); // This will execute the loop 3 times

    return 0;
}}
"""

# Function to generate and save code to a file
def generate_code_file(filename, custom_code):
    with open(filename, 'w') as file:
        file.write(code_template.format(custom_code=custom_code))

# List all files in the current directory with a ".vc" extension
for filename in os.listdir('.'):
    if filename.endswith('.vc'):
        custom_code = input(f"Enter custom code for '{filename}':\n")
        generate_code_file(filename.replace('.vc', '.cpp'), custom_code)

print("Code generation completed.")
