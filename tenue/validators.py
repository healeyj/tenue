from tenue.schema import *


# given arg, ensure it is an integer, then check if it exists in the database
def validate_outfit_id(arg):
    try:
        int(arg)  # throw ValueError if not an integer
        query = Outfit.select().where(Outfit.id == arg)
        if query.exists():
            return 1
    except ValueError:
        print("Arg is not an integer.")
    print("Invalid outfit id, please try again.")
    return 0


# given arg, ensure it is an integer, then check if it exists in the database
def validate_piece_id(arg):
    try:
        int(arg)  # throw ValueError if not an integer
        query = Piece.select().where(Piece.id == arg)
        if query.exists():
            return 1
    except ValueError:
        print("Arg is not an integer.")
    print("Invalid piece id, please try again.")
    return 0


# given args, check if the piece is in the outfit
def validate_piece_id_in_outfit(outfit_id, piece_id):
    if OutfitPiece.select().where((OutfitPiece.outfit_id == int(outfit_id))
                                  & (OutfitPiece.piece_id == int(piece_id))):
        return 1
    print("Outfit #" + str(outfit_id) + " does not contain Piece #" + str(piece_id))
    return 0


# given kind as string, return 1 if exists
def validate_kind(kind):
    kind_count = Kind.select().count()
    query = Kind.select().where(Kind.name == kind)
    if query.exists():
        return 1
    else:
        print(kind + " does not exist in the Kind table.")
        kind_string = ""
        for idx, kind in enumerate(Kind.select()):
            kind_string += kind.name
            if (idx + 1) != kind_count:
                kind_string += ", "
        print("Valid kinds: " + kind_string)
        return 0


# given color as string, return 1 if exists
def validate_color(color):
    color_count = Color.select().count()
    query = Color.select().where(Color.name == color)
    if query.exists():
        return 1
    else:
        print(color + " does not exist in the Color table.")
        color_string = ""
        for idx, color in enumerate(Color.select()):
            color_string += color.name
            if (idx + 1) != color_count:
                color_string += ", "
        print("Valid colors: " + color_string)
        return 0
