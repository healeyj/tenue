from tenue.validators import *

# TODO: add examples to each input prompt


# prompt user to input kind, return kind id
def input_kind():
    kind = input("Piece kind?\n")
    input_validated = 0
    while input_validated == 0:
        if validate_kind(kind) == 1:
            input_validated = 1
        else:
            print("Please try again, a piece must have a valid kind.")
            kind = input("Piece kind?\n")
    return Kind.get(Kind.name == kind)


# prompt user to input subkind, return string
# TODO: rename subkind to something more readable
def input_subkind():
    return parse_blank_input(input("Piece subkind?\n"))


# prompt user to input description, return string
def input_description():
    return parse_blank_input(input("Piece description?\n"))


# prompt user to input brand, return string
def input_brand():
    return parse_blank_input(input("Piece brand?\n"))


# prompt user to input colors, return list of color models
def input_colors():
    piece_colors = []
    color = ""
    while color != 'x':
        color = input("Piece color? Type x to stop adding colors.\n")
        if color != 'x' and validate_color(color) == 1:
            piece_colors.append(Color.get(Color.name == color))
        elif color != 'x':
            print("Please try again.")
    return piece_colors


# prompt user to input accents, return list of color models
def input_accents():
    piece_accents = []
    accent = ""
    while accent != 'x':
        accent = input("Piece accent? Type x to stop adding accents.\n")
        if accent != 'x' and validate_color(accent) == 1:
            piece_accents.append(Color.get(Color.name == accent))
        elif accent != 'x':
            print("Please try again.")
    return piece_accents


# if input is empty, convert it with 'none' to prevent null fields in the database
def parse_blank_input(string):
    if string == "":
        return ""
    else:
        return string
