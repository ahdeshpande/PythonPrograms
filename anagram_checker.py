def question1(s, t):
    """
    Determine whether some anagram of t is a substring of s

    :param s: String
    :param t: String
    :return: Boolean

    """
    # Either string cannot be empty
    if len(s) and len(t) > 0:
        # Create a dictionary where all the keys are the characters of the
        # string and value as 0
        s_dict = {}
        for letter in s:
            if letter in s_dict.keys():
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1

        # Counter to check how many matches
        counter = 0

        # Iterate through all characters and check if they are present in the
        #  main string
        # If present then pop the key. This takes care if there exists a
        # repeated character
        for character in t:
            if character in s_dict.keys():
                s_dict[character] -= 1
                if s_dict[character] == 0:
                    s_dict.pop(character)
                counter += 1

        # Check if counter is equal to the length of string 't'
        if counter == len(t):
            return True
        else:
            return False
    else:
        print("Either string cannot be empty")
        return False


# Testing with given, true, false and special cases
print("Anagram Checker!")
print("True Cases")
s = "udacity"
t = "ad"
print("s : " + s + "\t" + "t : " + t)
print("Is anagram? " + str(question1(s, t)))

s = "udacity"
t = "city"
print("s : " + s + "\t" + "t : " + t)
print("Is anagram? " + str(question1(s, t)))

print("False Cases")
s = "udacity"
t = "sad"
print("s : " + s + "\t" + "t : " + t)
print("Is anagram? " + str(question1(s, t)))

s = "udacity"
t = "acidity"
print("s : " + s + "\t" + "t : " + t)
print("Is anagram? " + str(question1(s, t)))

print("Special Cases")
s = "udacity"
t = ""
print("s : " + s + "\t" + "t : " + t)
print("Is anagram? " + str(question1(s, t)))

s = "udacity"
t = "aa"
print("s : " + s + "\t" + "t : " + t)
print("Is anagram? " + str(question1(s, t)))

s = "abhiraj"
t = "aa"
print("s : " + s + "\t" + "t : " + t)
print("Is anagram? " + str(question1(s, t)))

# Time Complexity: O(n)
# Space Complexity: O(n)
