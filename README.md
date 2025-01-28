# Project Name : Strong Password Generator Based on User Inputs



## Introduction 

This project is a Python-based Strong Password Generator designed to create memorable yet secure passwords. The passwords are generated using user-provided words and numbers, incorporating randomness, capitalization, and special character replacements to enhance security.
Unlike traditional random password generators, this tool creates passwords tailored to the user’s preferences while ensuring they are strong enough to withstand dictionary attacks and brute force attacks. The methodology is inspired by research on user-friendly password systems and best practices for secure password generation.


## Features 

- User Input-Based Passwords: Users provide five words and two numbers as inputs for password generation.
- Randomization: Random capitalization, shuffling of characters, and insertion of numbers ensure password unpredictability.
- Special Character Substitution: Certain letters are replaced with visually similar special characters (e.g., a → @, o → 0) for enhanced security.
- Multiple Password Generation: Generates up to 10 passwords in a single run.
- Strength Validation: Ensures that all passwords meet a minimum length of 8 characters.
- Defends Against Attacks: Resistant to brute force and dictionary attacks.


## Methodology 

The password generation algorithm is based on the following steps:
  1. Users provide five words and two numbers as inputs.
  2. Two random words and one random number are selected.
  3. The selected words are randomly capitalized, shuffled, and combined.
  4. Certain characters are substituted with special characters.
  5. A number is inserted at a random position, and a special character is appended at the end.
  6. The password is validated to ensure it meets the minimum length requirement.
The algorithm ensures that the generated passwords are both secure and easy to remember by combining user-specific inputs with randomness.


## How to Use

### Prerequisites
- Python 3.x installed on your system.

### Running the Code 
1. Clone this repository:
     git clone https://github.com/your-username/strong-password-generator.git
     cd strong-password-generator

2. Run the script:
    python generate_password.py

3. Follow the prompts:
    - Enter words separated by commas (e.g., apple, banana, cherry, date, elderberry).
    - Enter numbers separated by commas (e.g., 123, 456).
    - Enter the number of passwords to generate (1-10).

4. The generated passwords will be displayed on the terminal.


### Example :
  Input
    ![Screenshot 2025-01-28 194411](https://github.com/user-attachments/assets/79013038-2f97-440a-81c6-13be1f2fae58)

  Output 
    ![Screenshot 2025-01-28 194422](https://github.com/user-attachments/assets/413a8d0b-fc23-48a9-bd44-ecb688f88ab3)


## Research Background

This project is inspired by the paper "Strong Password Generation Based on User Inputs" by Olivier Tremblay-Savard et al. The paper highlights the challenges of balancing password strength and memorability. The proposed algorithm combines user-provided inputs with randomized transformations to create strong, non-crackable passwords.

### Key insights from the paper:

Generated passwords defend against dictionary attacks by avoiding predictable patterns and single words.
Incorporation of numbers, case-sensitive characters, and special symbols strengthens resistance against brute force attacks.
The system ensures user-friendliness by relying on familiar user inputs.
    

## Experimental Results

The methodology was tested with various input combinations and evaluated using password strength checkers such as:
  - The Password Meter
  - Kaspersky Lab Password Checker
  - Password Checker Online
    
Results indicated that the generated passwords:
  - Achieved an average strength score of 94.88%.
  - Withstood cracking attempts with minimum brute force cracking time of 90 days and a maximum of 1,217,000 days.


## Future Enhancements  

Planned updates to this project include:
  1. Online Interface: Develop a web-based application for easy access.
  2. Advanced Input Validation: Reject overly simple or common inputs (e.g., "password", "1234").
  3. User Feedback Loop: Collect feedback on password usability and memorability.
  4. Extended Security Features: Incorporate measures to guard against social engineering attacks.

## License 
     
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

This project is based on the research conducted by Olivier Tremblay-Savard, Noman Mohammed, Farhana Zaman Glory, and Atif Ul Aftab at the University of Manitoba. The authors' insights into password security have been invaluable in shaping this implementation.

## References

1. Tremblay-Savard, O., Mohammed, N., Glory, F. Z., & Aftab, A. U. (2019). Strong Password Generation Based on User Inputs. IEEE.
   Link: [10.1109@IEMCON.2019.8936178.pdf](https://github.com/user-attachments/files/18574842/10.1109%40IEMCON.2019.8936178.pdf)
3. The Password Meter: https://passwordmeter.com
4. Kaspersky Password Checker: https://password.kaspersky.com

  


   
