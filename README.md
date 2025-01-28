# Strong Password Generator Based on User Inputs



Introduction
This project is a Python-based Strong Password Generator designed to create memorable yet secure passwords. The passwords are generated using user-provided words and numbers, incorporating randomness, capitalization, and special character replacements to enhance security.

Unlike traditional random password generators, this tool creates passwords tailored to the user’s preferences while ensuring they are strong enough to withstand dictionary attacks and brute force attacks. The methodology is inspired by research on user-friendly password systems and best practices for secure password generation.


Features
User Input-Based Passwords: Users provide five words and two numbers as inputs for password generation.
Randomization: Random capitalization, shuffling of characters, and insertion of numbers ensure password unpredictability.
Special Character Substitution: Certain letters are replaced with visually similar special characters (e.g., a → @, o → 0) for enhanced security.
Multiple Password Generation: Generates up to 10 passwords in a single run.
Strength Validation: Ensures that all passwords meet a minimum length of 8 characters.
Defends Against Attacks: Resistant to brute force and dictionary attacks.


Methodology
The password generation algorithm is based on the following steps:

Users provide five words and two numbers as inputs.
Two random words and one random number are selected.
The selected words are randomly capitalized, shuffled, and combined.
Certain characters are substituted with special characters.
A number is inserted at a random position, and a special character is appended at the end.
The password is validated to ensure it meets the minimum length requirement.
The algorithm ensures that the generated passwords are both secure and easy to remember by combining user-specific inputs with randomness.


How to Use
Prerequisites
Python 3.x installed on your system.
Running the Code
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/strong-password-generator.git
cd strong-password-generator
Run the script:

bash
Copy
Edit
python generate_password.py
Follow the prompts:

Enter words separated by commas (e.g., apple, banana, cherry, date, elderberry).
Enter numbers separated by commas (e.g., 123, 456).
Enter the number of passwords to generate (1-10).
The generated passwords will be displayed on the terminal.

Example
Input:
vbnet
Copy
Edit
Enter words separated by commas: apple, banana, cherry, date, elderberry
Enter numbers separated by commas: 123, 456
Enter the number of passwords to generate (1-10): 3
Output:
less
Copy
Edit
Generated Passwords:
b@nA8na!123CHErry<
d@8at3El!dE!RRy(
CH8rry@123bAN!an~
Research Background
This project is inspired by the paper "Strong Password Generation Based on User Inputs" by Olivier Tremblay-Savard et al. The paper highlights the challenges of balancing password strength and memorability. The proposed algorithm combines user-provided inputs with randomized transformations to create strong, non-crackable passwords.



Key insights from the paper:

Generated passwords defend against dictionary attacks by avoiding predictable patterns and single words.
Incorporation of numbers, case-sensitive characters, and special symbols strengthens resistance against brute force attacks.
The system ensures user-friendliness by relying on familiar user inputs.
Experimental Results
The methodology was tested with various input combinations and evaluated using password strength checkers such as:

The Password Meter
Kaspersky Lab Password Checker
Password Checker Online
Results indicated that the generated passwords:

Achieved an average strength score of 94.88%.
Withstood cracking attempts with minimum brute force cracking time of 90 days and a maximum of 1,217,000 days.
Future Enhancements
Planned updates to this project include:

Online Interface: Develop a web-based application for easy access.
Advanced Input Validation: Reject overly simple or common inputs (e.g., "password", "1234").
User Feedback Loop: Collect feedback on password usability and memorability.
Extended Security Features: Incorporate measures to guard against social engineering attacks.
License
This project is licensed under the MIT License. See the LICENSE file for details.


[10.1109@IEMCON.2019.8936178.pdf](https://github.com/user-attachments/files/18574332/10.1109%40IEMCON.2019.8936178.pdf)

Acknowledgments
This project is based on the research conducted by Olivier Tremblay-Savard, Noman Mohammed, Farhana Zaman Glory, and Atif Ul Aftab at the University of Manitoba. The authors' insights into password security have been invaluable in shaping this implementation.

References
Tremblay-Savard, O., Mohammed, N., Glory, F. Z., & Aftab, A. U. (2019). Strong Password Generation Based on User Inputs. IEEE.
The Password Meter: https://passwordmeter.com
Kaspersky Password Checker: https://password.kaspersky.com
