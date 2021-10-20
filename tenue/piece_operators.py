from tenue.core import *
from tenue.print_statements import *
from tenue.prompt_user_input import *
from tenue.validators import *


# TODO: reorder to kind, subkind, colors, brand, nickname, accents
# given args, create piece in the database, return piece object
def create_piece(kind_id, subkind, nickname, brand, colors, accents):
    new_piece = Piece.create(kind_id=kind_id, subkind=subkind, nickname=nickname, brand=brand)
    for color in list(set(colors)):  # remove duplicate colors with set()
        PieceColor.create(piece=new_piece, color=color)
    for accent in list(set(accents)):  # remove duplicate accents with set()
        PieceAccent.create(piece=new_piece, accent=accent)
    print_single_piece(new_piece.id)
    print("")
    print((piece_shortname(new_piece.id) + " created.").center(console_width))
    return new_piece


# given arg, delete a piece, return nothing
def delete_piece(arg):
    if validate_piece_id(arg):
        shortname = piece_shortname(arg)
        Piece.delete().where(Piece.id == arg).execute()  # delete piece
        PieceColor.delete().where(PieceColor.piece_id == arg).execute()  # delete its associated colors
        PieceAccent.delete().where(PieceAccent.piece_id == arg).execute()  # delete its associated accents
        OutfitPiece.delete().where(OutfitPiece.piece_id == arg).execute()  # delete its associated pieces
        print((shortname + " deleted.").center(console_width))
    return


# duplicate a piece in the database, making a new piece and reassigning all the attributes from old piece
def clone_piece(args):
    if validate_piece_id(args):
        old_piece = Piece.get(Piece.id == args)
        old_piece_colors = Color.select().join(PieceColor).join(Piece).where(Piece.id == old_piece.id)
        old_piece_accents = Color.select().join(PieceAccent).join(Piece).where(Piece.id == old_piece.id)
        new_piece = create_piece(old_piece.kind.id, old_piece.subkind, old_piece.nickname, old_piece.brand,
                                 old_piece_colors, old_piece_accents)
        print((piece_shortname(old_piece.id) + " duplicated to Piece #" + str(new_piece.id)).center(console_width))


# input target property, target piece, and args, then modify piece attributes in database if args are valid
# TODO: refactor this
def edit_piece_switcher(target_prop, target_piece, args):
    if target_prop == 'kind':
        if len(args) > 0:
            my_kind = " ".join(args)
            if validate_kind(my_kind):
                # only reassign a kind if it is valid
                target_piece.kind = Kind.get(Kind.name == my_kind)
        else:
            # assign empty field if args are empty
            target_piece.kind = ""
    elif target_prop == 'subkind':
        if len(args) > 0:
            target_piece.subkind = " ".join(args)
        else:
            target_piece.subkind = ""
    elif target_prop == 'nickname':
        if len(args) > 0:
            target_piece.nickname = " ".join(args)
        else:
            target_piece.nickname = ""
    elif target_prop == 'brand' or target_prop == 'brands':
        if len(args) > 0:
            target_piece.brand = " ".join(args)
        else:
            target_piece.brand = ""
    # TODO: refactor the 2 following elif statements
    elif target_prop == 'color' or target_prop == 'colors':
        # reset existing piece colors, then create new ones if args are given
        PieceColor.delete().where(PieceColor.piece_id == target_piece.id).execute()
        if len(args) > 0:
            for arg in list(set(args)):
                if validate_color(arg):
                    # only assign colors if they are valid
                    PieceColor.create(piece=target_piece, color=Color.get(Color.name == arg))
        # reset piece colors if no args given
    elif target_prop == 'accent' or target_prop == 'accents':
        # reset existing piece accents, then create new ones if args are given
        PieceAccent.delete().where(PieceAccent.piece_id == target_piece.id).execute()
        if len(args) > 0:
            for arg in list(set(args)):
                if validate_color(arg):
                    PieceAccent.create(piece=target_piece, accent=Color.get(Color.name == arg))


# given piece, prompt user to specify one of its properties, then allow them to edit it
def edit_piece(args):
    if multiple_args_exist(args):
        args = args.split()
        pid = args.pop(0)
        if validate_piece_id(pid):
            target_piece = Piece.get(Piece.id == pid)
            target_prop = args.pop(0).lower()
            edit_piece_switcher(target_prop, target_piece, args)
            target_piece.save()
            print_single_piece(pid)
            print("")
            print((piece_shortname(pid) + ' updated.').center(console_width))
        else:
            print("Invalid piece property, please try again.")
    return
