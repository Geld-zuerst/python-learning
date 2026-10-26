# ============================================================
# PYTHON STRINGS: COMPLETE EXPLAINED CODE
# ============================================================


# ============================================================
# 1. WHAT IS A STRING?
# ============================================================

# A string is text written inside quotes.
# Strings can contain letters, numbers, spaces and symbols.

name = "Python"

print(name)
print(type(name))
print(len(name))


# ============================================================
# 2. CREATING STRINGS
# ============================================================

single_quote = 'Hello'
double_quote = "World"
multi_line = """This is
a multi-line
string."""

print(single_quote)
print(double_quote)
print(multi_line)

# Converting another value into a string
number_as_string = str(123)
print(number_as_string)
print(type(number_as_string))

print(str(3.14))
print(str(True))
print(str([1, 2, 3]))

# Empty and non-empty strings
print(bool(""))      # False
print(bool(" "))     # True
print(bool("0"))     # True


# ============================================================
# 3. QUOTES INSIDE STRINGS
# ============================================================

print("It's a lovely day")
print('He said "Python is fun"')
print('It\'s also possible')


# ============================================================
# 4. INDEXING
# ============================================================

# Indexing accesses one character.
# Python starts counting from 0.

text = "Python"

print(text[0])       # P
print(text[1])       # y
print(text[-1])      # n
print(text[-2])      # o

# Safe handling of an invalid index
try:
    print(text[6])
except IndexError as error:
    print("IndexError:", error)


# ============================================================
# 5. SLICING
# ============================================================

# Syntax:
# string[start:stop:step]
#
# start is included.
# stop is excluded.

text = "Python Programming"

print(text[0:6])     # Python
print(text[7:18])    # Programming
print(text[:6])      # From beginning
print(text[7:])      # To the end
print(text[::2])     # Every second character
print(text[::-1])    # Reverse the string
print(text[-11:])    # Last 11 characters

# Slicing does not usually raise an error for large limits.
print(text[2:100])
print(text[100:])


# ============================================================
# 6. CONCATENATION
# ============================================================

# Concatenation means joining strings with +.

first_name = "Rahul"
last_name = "Kumar"

full_name = first_name + " " + last_name
print(full_name)

# You cannot directly add a string and a number.
age = 20

try:
    print("Age: " + age)
except TypeError as error:
    print("TypeError:", error)

print("Age: " + str(age))
print(f"Age: {age}")


# ============================================================
# 7. REPETITION
# ============================================================

# The * operator repeats a string.

print("Hi " * 3)
print("-" * 30)
print("ab" * 0 == "")


# ============================================================
# 8. MEMBERSHIP OPERATORS
# ============================================================

# in checks whether text exists inside another string.
# not in checks whether text does not exist.

text = "Python"

print("Py" in text)
print("Java" in text)
print("Java" not in text)
print("py" in text)       # Case-sensitive
print("" in text)         # Always True


# ============================================================
# 9. STRING COMPARISON
# ============================================================

print("apple" == "apple")
print("apple" != "Apple")
print("apple" < "banana")
print("zebra" > "apple")

# Case-insensitive comparison
print("Apple".lower() == "apple".lower())

# Use == for value comparison.
# Do not use is to compare text.

a = "hello"
b = "".join(["hel", "lo"])

print(a == b)


# ============================================================
# 10. LENGTH AND ITERATION
# ============================================================

text = "Hello World"

print(len(text))
print(len(""))

# Loop through every character
for character in "Python":
    print(character)

# Loop with index and character
for index, character in enumerate("Py3"):
    print(index, "->", character)


# ============================================================
# 11. STRING FORMATTING
# ============================================================

name = "Rahul"
age = 20
marks = 88.456

# f-string: recommended
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")
print(f"Name in capitals: {name.upper()}")

# format() method
print("My name is {}.".format(name))
print("{0} scored {1}. {0} passed!".format("Asha", 92))
print("{person} is from {city}".format(person="Ravi", city="Patna"))

# Old % formatting
print("Age = %d" % age)
print("Name: %s, Marks: %.1f" % ("Neha", marks))

# Format specifications
pi = 3.14159
number = 42

print(f"{pi:.2f}")       # Two decimal places
print(f"{number:05d}")   # Zero padding
print(f"{name:>10}")     # Right alignment
print(f"{name:<10}")     # Left alignment
print(f"{name:^10}")     # Centre alignment
print(f"{1_234_567:,}")  # Thousands separator
print(f"{0.256:.1%}")    # Percentage
print(f"{number:b}")     # Binary
print(f"{255:x}")        # Hexadecimal
print(f"{number=}")      # Debug format


# ============================================================
# 12. ESCAPE CHARACTERS
# ============================================================

# \n creates a new line.
# \t creates a tab.
# \\ creates a backslash.

print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Python\"")
print("C:\\Users\\Admin")


# ============================================================
# 13. RAW STRINGS
# ============================================================

# Raw strings treat backslashes as normal characters.
# They are useful for Windows paths and regular expressions.

path = r"C:\Users\Admin\Desktop"
print(path)

normal_path = "C:\new_folder"
raw_path = r"C:\new_folder"

print(normal_path)
print(raw_path)


# ============================================================
# 14. IMMUTABILITY
# ============================================================

# Strings cannot be changed directly.
# String methods return a new string.

text = "hello"

new_text = text.upper()

print(text)       # Original remains unchanged
print(new_text)   # New string

# Correct way to change a character
text = "Python"
text = "J" + text[1:]

print(text)

# Incorrect item assignment
try:
    text[0] = "X"
except TypeError as error:
    print("TypeError:", error)


# ============================================================
# 15. CASE CONVERSION METHODS
# ============================================================

text = "pYtHoN programming"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

# casefold() is useful for case-insensitive Unicode comparison
print("Straße".lower())
print("Straße".casefold())
print("STRASSE".casefold() == "Straße".casefold())


# ============================================================
# 16. ALIGNMENT METHODS
# ============================================================

text = "Python"

print(text.center(20, "*"))
print(text.center(20))
print(text.ljust(15, "."))
print(text.rjust(15, "."))
print("42".zfill(5))
print("-42".zfill(6))

# Simple table
items = [
    ("Pen", 10),
    ("Notebook", 45),
    ("Bag", 550)
]

print("Item".ljust(12) + "Price".rjust(8))
print("-" * 20)

for item, price in items:
    print(item.ljust(12) + str(price).rjust(8))


# ============================================================
# 17. SEARCH METHODS
# ============================================================

text = "Python Python"

# find() returns -1 if the text is absent
print(text.find("Python"))
print(text.find("Java"))

# rfind() searches from the right
print(text.rfind("Python"))

# index() raises ValueError if the text is absent
print(text.index("Python"))

try:
    print(text.index("Java"))
except ValueError as error:
    print("ValueError:", error)

# count() counts non-overlapping occurrences
print("banana".count("a"))
print("banana".count("an"))
print("aaaa".count("aa"))


# ============================================================
# 18. CHECKING METHODS
# ============================================================

print("Python".startswith("Py"))
print("Python".endswith("on"))

print("Python".isalpha())
print("123".isdigit())
print("123".isdecimal())
print("½".isnumeric())
print("Python123".isalnum())
print("python".islower())
print("PYTHON".isupper())
print("Python Programming".istitle())
print("   ".isspace())
print("student_name".isidentifier())
print("Python".isascii())
print("Hello".isprintable())

# Difference between digit, decimal and numeric
print("123".isdecimal())
print("²".isdigit())
print("½".isnumeric())


# ============================================================
# 19. PASSWORD CHECKER
# ============================================================

def check_password(password):
    if len(password) < 8:
        return "Too short"

    if password.isalpha() or password.isdigit():
        return "Use both letters and digits"

    if password.lower() == password:
        return "Add at least one uppercase letter"

    return "Strong password"


passwords = [
    "abc",
    "abcdefgh",
    "abcd1234",
    "Abcd1234"
]

for password in passwords:
    print(password.ljust(12), "->", check_password(password))


# ============================================================
# 20. REPLACE METHODS
# ============================================================

print("Python".replace("Python", "Java"))
print("banana".replace("a", "o"))
print("banana".replace("a", "o", 2))
print("a b c".replace(" ", ""))

# Remove a prefix
print("Mr.Rahul".removeprefix("Mr."))
print("Rahul".removeprefix("Mr."))

# Remove a suffix
print("report.pdf".removesuffix(".pdf"))
print("report.txt".removesuffix(".pdf"))


# ============================================================
# 21. TRANSLATE AND MAKETRANS
# ============================================================

# Replace characters one by one
translation_table = str.maketrans("ae", "12")

print("apple".translate(translation_table))

# Delete vowels
delete_vowels = str.maketrans("", "", "aeiou")

print("programming".translate(delete_vowels))


# ============================================================
# 22. SPLIT
# ============================================================

print("a,b,c".split(","))
print("  hello    big   world  ".split())
print("a,b,c,d".split(",", 2))
print("a,,b".split(","))

# rsplit() starts splitting from the right
print("a,b,c".rsplit(",", 1))
print("a,b,c".split(",", 1))

# splitlines()
text = "line1\nline2\r\nline3"

print(text.splitlines())
print(text.splitlines(keepends=True))


# ============================================================
# 23. PARTITION
# ============================================================

print("abc-def-ghi".partition("-"))
print("abc".partition("-"))

user, separator, domain = "student@college.edu".partition("@")

print(user)
print(domain)

# rpartition() splits at the last occurrence
print("abc-def-ghi".rpartition("-"))

file_name = "photo.final.jpg"
extension = file_name.rpartition(".")[-1]

print(extension)


# ============================================================
# 24. JOIN
# ============================================================

print("-".join(["a", "b", "c"]))
print("".join(["Py", "thon"]))
print(", ".join(["red", "green", "blue"]))
print(" ".join("Python"))

# Joining numbers requires conversion to strings
numbers = [1, 2, 3]

print(", ".join(map(str, numbers)))

# Split and join together
sentence = "python is easy"
words = sentence.split()
capitalized_words = [word.capitalize() for word in words]

print(" ".join(capitalized_words))


# ============================================================
# 25. STRIP, LSTRIP AND RSTRIP
# ============================================================

print(repr("  Python  ".strip()))
print(repr("  Python  ".lstrip()))
print(repr("  Python  ".rstrip()))

print("xxPythonyx".strip("xy"))
print("Hello!!!".rstrip("!"))

# Remove extra spaces inside text
messy_text = "  too    many   spaces  "
clean_text = " ".join(messy_text.split())

print(clean_text)


# ============================================================
# 26. ENCODING AND DECODING
# ============================================================

# encode() converts a string to bytes.
# decode() converts bytes back to a string.

data = "café".encode("utf-8")

print(data)
print(type(data))
print(data.decode("utf-8"))


# ============================================================
# 27. EXPANDTABS
# ============================================================

text = "Hello\tWorld"

print(repr(text.expandtabs(10)))


# ============================================================
# 28. FORMAT_MAP
# ============================================================

student = {
    "name": "Ravi",
    "age": 21
}

print("{name} is {age} years old".format_map(student))


# ============================================================
# 29. METHOD CHAINING
# ============================================================

raw_text = "  Hello, World  "

clean_text = raw_text.strip().lower().replace(",", "")

print(clean_text)

print("  PYTHON is Fun ".strip().title().split())


# ============================================================
# 30. BUILT-IN FUNCTIONS WITH STRINGS
# ============================================================

text = "Python"

print(len(text))
print(max(text))
print(min(text))
print(sorted(text))
print(list(reversed(text)))
print(list(enumerate("Hi")))
print(ord("A"))
print(chr(65))
print(list("abc"))
print(sorted(set("hello")))
print(int("42") + 1)

# Print the alphabet using ord() and chr()
alphabet = ""

for code in range(ord("a"), ord("a") + 26):
    alphabet += chr(code)

print(alphabet)


# ============================================================
# 31. PALINDROME CHECKER
# ============================================================

def is_palindrome(text):
    cleaned_text = "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )

    return cleaned_text == cleaned_text[::-1]


print(is_palindrome("Madam"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Python"))


# ============================================================
# 32. VOWEL COUNTER
# ============================================================

text = "Python Programming"
vowels = "aeiouAEIOU"
vowel_count = 0

for character in text:
    if character in vowels:
        vowel_count += 1

print("Vowels:", vowel_count)


# ============================================================
# 33. WORD STATISTICS
# ============================================================

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

print("Words:", len(words))
print("Longest:", max(words, key=len))
print("Title:", sentence.title())


# ============================================================
# 34. CHARACTER FREQUENCY
# ============================================================

text = "banana"
frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

print(frequency)


# ============================================================
# 35. CAESAR CIPHER
# ============================================================

def caesar(text, shift):
    result = ""

    for character in text:
        if character.isalpha():
            if character.isupper():
                base = ord("A")
            else:
                base = ord("a")

            shifted_character = chr(
                (ord(character) - base + shift) % 26 + base
            )

            result += shifted_character
        else:
            result += character

    return result


encrypted_text = caesar("Hello, World!", 3)

print(encrypted_text)
print(caesar(encrypted_text, -3))


# ============================================================
# 36. EMAIL SPLITTER
# ============================================================

email = "asha.verma@college.edu"

username, separator, domain = email.partition("@")

formatted_name = username.replace(".", " ").title()

print("User:", formatted_name)
print("Domain:", domain)
print("Educational email:", domain.endswith(".edu"))


# ============================================================
# 37. ANAGRAM CHECKER
# ============================================================

def is_anagram(first_text, second_text):
    first_text = first_text.replace(" ", "").lower()
    second_text = second_text.replace(" ", "").lower()

    return sorted(first_text) == sorted(second_text)


print(is_anagram("Listen", "Silent"))
print(is_anagram("Python", "Java"))


# ============================================================
# 38. REVERSE EACH WORD
# ============================================================

sentence = "hello world"

reversed_words = " ".join(
    word[::-1]
    for word in sentence.split()
)

print(reversed_words)


# ============================================================
# 39. RUN-LENGTH ENCODING
# ============================================================

def compress(text):
    if not text:
        return ""

    output = ""
    count = 1

    for index in range(1, len(text)):
        if text[index] == text[index - 1]:
            count += 1
        else:
            output += text[index - 1] + str(count)
            count = 1

    output += text[-1] + str(count)

    return output


print(compress("aaabbc"))


# ============================================================
# 40. FIRST NON-REPEATING CHARACTER
# ============================================================

def first_unique_character(text):
    for character in text:
        if text.count(character) == 1:
            return character

    return "none"


print(first_unique_character("swiss"))
print(first_unique_character("aabb"))


# ============================================================
# 41. OTP VALIDATOR
# ============================================================

def is_valid_otp(otp):
    return len(otp) == 6 and otp.isdecimal()


print(is_valid_otp("123456"))
print(is_valid_otp("12345"))
print(is_valid_otp("12a456"))


# ============================================================
# 42. INITIALS GENERATOR
# ============================================================

def get_initials(full_name):
    words = full_name.split()

    initials = [
        word[0].upper()
        for word in words
    ]

    return ".".join(initials) + "."


print(get_initials("asha kumari verma"))


# ============================================================
# 43. FILE EXTENSION
# ============================================================

def get_extension(file_name):
    separator, dot, extension = file_name.rpartition(".")

    if dot == "":
        return "No extension"

    return extension


print(get_extension("a.b.c.txt"))
print(get_extension("README"))


# ============================================================
# 44. USEFUL STRING RULES
# ============================================================

# 1. Strings are immutable.
# 2. Indexes start at 0.
# 3. The last character can be accessed using -1.
# 4. Slice stop positions are excluded.
# 5. Use f-strings for formatting.
# 6. Use == instead of is for comparing text.
# 7. Use in for yes/no searches.
# 8. Use find() when you need a position.
# 9. Use join() to combine many strings.
# 10. input() always returns a string.
# 11. Use int() or float() to convert numeric input.
# 12. Use strip().lower() to clean user input.


# ============================================================
# END OF COMPLETE PYTHON STRING CODE
# ============================================================