from tenue.core import *
from tenue.print_statements import *
from tenue.validators import *


# create outfit in the database, return outfit object
def create_outfit():
    new_outfit_id = Outfit.create().get_id()
    print(("Outfit #" + str(new_outfit_id) + " created.").center(console_width))
    print_outfit(new_outfit_id)
    return new_outfit_id


# given arg, delete an outfit, return nothing
def delete_outfit(arg):
    if validate_outfit_id(arg):
        Outfit.delete().where(Outfit.id == arg).execute()  # delete piece
        OutfitPiece.delete().where(OutfitPiece.outfit_id == arg).execute()  # delete its associated pieces
        print("Outfit #" + arg + " deleted.")
    return


# duplicate an outfit in the database, making a new outfit and reassigning all pieces from old outfit
def clone_outfit(args):
    if validate_outfit_id(args):
        new_outfit_id = create_outfit()
        piece_ids = Piece.select().join(OutfitPiece).where(OutfitPiece.outfit == args)
        for piece_id in piece_ids:
            add_piece_to_outfit(str(new_outfit_id) + " " + str(piece_id))
        print_outfit(new_outfit_id)
        print(("Outfit #" + str(args) + " duplicated to Outfit #" + str(new_outfit_id)).center(console_width))


# given outfit, prompt user to add pieces to that outfit
def add_piece_to_outfit(args):
    if multiple_args_exist(args):
        args = args.split()
        if validate_outfit_id(args[0]):
            oid = args.pop(0)
            for arg in args:
                if validate_piece_id(arg):
                    shortname = piece_shortname(arg)
                    OutfitPiece.create(outfit=oid, piece=Piece.get(Piece.id == arg))
                    print((shortname + " added to Outfit #" + oid + ".").center(console_width))
    return


# given arg, remove a piece from its outfit, return nothing
def remove_piece_from_outfit(args):
    if multiple_args_exist(args):
        args = args.split()
        if validate_outfit_id(args[0]):
            oid = args.pop(0)
            for arg in args:
                if validate_piece_id(arg):
                    if validate_piece_id_in_outfit(oid, arg):
                        shortname = piece_shortname(arg)
                        # piece exists in outfit, remove it!!!
                        OutfitPiece.delete().where((OutfitPiece.outfit_id == oid)
                                                   & (OutfitPiece.piece_id == arg)).execute()
                        print((shortname + " removed from Outfit #" + oid + ".").center(console_width))
    return
