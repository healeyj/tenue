from tenue.schema import *
from num2words import num2words

# piece attribute, attribute width, attribute color to print
piece_attribute_print_order = [['id', 4],
                               ['kind', 12],
                               ['color', 12],
                               ['brand', 15],
                               ['subkind', 18],
                               ['accent', 18],
                               ['nickname', 18]
                               ]
piece_property_widths = [elems[1] for elems in piece_attribute_print_order]
console_width = sum(piece_property_widths) + len(piece_property_widths)


# given attribute and piece id, return a formatted string that includes all the results of some multivalued attr
#   currently just used for colors and accents, but works for any multivalued attributes
def concat_multivalued_attributes_to_string(attribute, piece_id):
    results_string = ""
    # piece_features is a peewee call for all results of some multivalued attribute
    piece_features = None
    piece_features_count = 0
    if attribute == "colors":
        piece_features = Color.select().join(PieceColor).join(Piece).where(Piece.id == piece_id)
        piece_features_count = piece_features.count()
    elif attribute == "accents":
        piece_features = Color.select().join(PieceAccent).join(Piece).where(Piece.id == piece_id)
        piece_features_count = piece_features.count()
    # concat results
    for idx, feature in enumerate(piece_features):
        if idx == 0:
            if piece_features_count == 1 or piece_features_count == 2:
                results_string += feature.name
            else:
                results_string += (feature.name + ",")
        elif (idx + 1) != piece_features_count:
            results_string += (" " + feature.name + ",")
        elif idx + 1 == piece_features_count:
            results_string += (" and " + feature.name)
    return results_string.capitalize()


def print_outfit(outfit_id):
    target_outfit = Outfit.get(Outfit.id == outfit_id)
    print((" " + ("outfit #" + (str(outfit_id)))))
    # sort outfit by piece kinds
    sorted_outfit_pieces = []  # not yet sorted but whatever
    for outfit_piece in target_outfit.outfit_pieces:
        sorted_outfit_pieces.append([outfit_piece, outfit_piece.piece.kind.id])
    sorted_outfit_pieces.sort(key=lambda x: x[1], reverse=False)
    # print sorted outfit
    accessory_flag = 0
    print("\n        clothes:")
    for outfit_piece in sorted_outfit_pieces:
        # this is hacky
        if outfit_piece[0].piece.kind.name == 'accessory':
            accessory_flag += 1
        if accessory_flag == 1:
            print("\n        accessories:")
            accessory_flag += 1
        # end of hackiness
        print_piece_outfit_view(outfit_piece[0].piece.id)
    # if outfit is empty, print some text to notify user
    if not OutfitPiece.select().where(OutfitPiece.outfit_id == outfit_id):
        print_divider_hyphens()
        print(("Outfit #" + str(outfit_id) + " is empty.").center(console_width))
        print_divider_hyphens()
    else:
        print("")
        print_divider_hyphens()
    return


def print_piece_outfit_view(piece_id):
    # add 10 spaces for alignment
    special_piece_id_print = '{:<13}'.format(("        [" + str(piece_id) + "] "))
    print(special_piece_id_print + piece_shortname(piece_id))
    return


def print_piece(piece_id):
    target_piece = Piece.get(Piece.id == piece_id)
    piece_info = []
    for my_list in piece_attribute_print_order:
        if my_list[0] != 'color' and my_list[0] != 'accent' and my_list[0] != 'kind':
            piece_info.append([getattr(target_piece, my_list[0]), my_list[1]])
        else:
            if my_list[0] == 'color':
                piece_info.append([concat_multivalued_attributes_to_string("colors", piece_id), my_list[1]])
            elif my_list[0] == 'accent':
                piece_info.append([concat_multivalued_attributes_to_string("accents", piece_id), my_list[1]])
            else:
                piece_info.append([target_piece.kind.name, my_list[1]])
    print_divider_piece_grid()
    for elements in piece_info:
        p_elem = (str(elements[0])[:elements[1] - 3] + "...") if len(str(elements[0])) > elements[1] else str(elements[0])
        print(p_elem.center(elements[1]) + "|", end='')
    print("")
    return


def print_piece_headers():
    print_divider_hyphens()
    for idx, elements in enumerate(piece_attribute_print_order):
        print(elements[0].center(elements[1]) + "|", end='')
    print("")
    return


def print_all_pieces():
    print_divider_hyphens()
    print("")
    print("PIECES:".center(console_width))
    print("")
    print_piece_headers()
    for piece in Piece.select().order_by(Piece.kind, Piece.subkind, Piece.brand):
        print_piece(piece.id)
    print_divider_hyphens()
    pieces_count = Piece.select().count()
    print(
        ("The database contains " + num2words(pieces_count) +
         " (" + str(Piece.select().count()) +
         ") piece(s).").center(console_width))
    return


def print_single_piece(piece_id):
    print_piece_headers()
    print_piece(piece_id)
    print_divider_hyphens()


def print_all_outfits():
    print_divider_hyphens()
    print("")
    print("OUTFITS:".center(console_width))
    print("")
    print_divider_hyphens()
    for outfit in Outfit.select():
        print_outfit(outfit.id)
    outfits_count = Outfit.select().count()
    print(
        ("The database contains " + num2words(outfits_count) +
         " (" + str(Outfit.select().count()) +
         ") outfit(s).").center(console_width))
    return


def print_divider_piece_grid():
    for elements in piece_attribute_print_order:
        for n in range(elements[1]):
            print("-", end='')
        print("|", end='')
    print("")
    return


def print_divider_hashes():
    for n in range(console_width):
        print("#", end='')
    print("")
    return


def print_divider_squiqqlies():
    for n in range(console_width):
        print("~", end='')
    print("")
    return


def print_divider_hyphens():
    for n in range(console_width):
        print("–", end='')
    print("")
    return


def print_divider_underscores():
    for n in range(console_width):
        print("_", end='')
    print("")
    return


def print_divider_periods():
    for n in range(console_width):
        print(".", end='')
    print("")
    return


# given piece_id, return a string that is its colors, nickname, brand, and subkind
def piece_shortname(piece_id):
    target_piece = Piece.get(Piece.id == piece_id)
    shortname = str(concat_multivalued_attributes_to_string("colors", piece_id))
    if target_piece.nickname != "":
        shortname += (" " + str(target_piece.nickname))
    if target_piece.brand != "":
        shortname += " " + str(target_piece.brand)
    if target_piece.subkind != "":
        shortname += (" " + str(target_piece.subkind))
    return shortname
