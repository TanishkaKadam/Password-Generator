import random

def generate_password(texts, numbers):
    specialchars = ['@', '$', '!', '#', '%', '&', '(', ')', '0', '3', '8', '<', '|']
    punctuation = ['<§>', '*', '+', '-', ':', '"', '/', '\\', '~', '?', '[', ']', '{', '}', '$', '!', '#', '%', '&', '(', ')', '_', '<', '|']
    alphabet_to_special = {'a': '@', 'o': '0', 's': '$', 'i': '!', 'r': '#', 'e': '3', 'b': '8', 'c': '(', 'k': '|'}

    string1 = random.choice(texts)
    string2 = random.choice([t for t in texts if t != string1])
    number = random.choice(numbers)

    string1 = ''.join([char.upper() if random.choice([True, False]) else char for char in string1])
    string2 = ''.join([char.upper() if random.choice([True, False]) else char for char in string2])

    combined_text = string1 + string2
    final_string = ''.join(random.sample(combined_text, len(combined_text)))

    final_string = ''.join([alphabet_to_special[char] if char in alphabet_to_special else char for char in final_string])

    insert_position = random.choice([0, len(final_string) // 2, len(final_string)])
    final_string = final_string[:insert_position] + str(number) + final_string[insert_position:]

    final_string += random.choice(punctuation)

    while len(final_string) < 8:
        final_string += random.choice(specialchars)

    return final_string

def generate_passwords(texts, numbers, num_passwords):
    if not (1 <= num_passwords <= 10):
        raise ValueError("Number of passwords should be between 1 and 10")

    passwords = []
    for _ in range(num_passwords):
        password = generate_password(texts, numbers)
        passwords.append(password)

    return passwords

if __name__ == "__main__":
    texts = input("Enter words separated by commas: ").split(',')
    texts = [text.strip() for text in texts]  # Remove any extra whitespace
    numbers = list(map(int, input("Enter numbers separated by commas: ").split(',')))
    num_passwords = int(input("Enter the number of passwords to generate (1-10): "))

    passwords = generate_passwords(texts, numbers, num_passwords)
    print("Generated Passwords:")
    for pwd in passwords:
        print(pwd)
