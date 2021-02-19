import cmd
import sys
from tenue.piece_operators import *
from tenue.outfit_operators import *
from tenue.search import *


class Shell(cmd.Cmd):
    # ASCII ART credit: https://www.oocities.org/spunk1111/cloth.htm
    # note: all backslashes shown in the ASCII art are 'escaped' with an additional backslash
    intro = "==jgs==!====!=====!=====!====!===!===!=====!===!===!====\n" \
            '      /`\\__/`\\   /`\\   /`\\  |~| |~|  /)=I=(\\  /`"""`\\\n' \
            '     |        | |   `"`   | | | | |  |  :  | |   :   |\n' \
            "     '-|    |-' '-|     |-' )/\\ )/\\  |  T  \\ '-| : |-'\n" \
            "       |    |     |     |  / \\// \\/  (  |\\  |  '---'\n" \
            "       '.__.'     '.___.'  \\_/ \\_/   |  |/  /\n" \
            '                                     |  /  /\n' \
            '                                     |  \\ /\n' \
            "                                     '--'`\n" \
            "Welcome to tenue."
    prompt = '(tenue) '

    def do_np(self, arg):
        """New piece. Creates a piece for the Wardrobe and prompts user to input its attributes."""
        # TODO: reorder to kind, subkind, colors, brand, nickname, accents
        create_piece(input_kind(), input_subkind(), input_nickname(), input_brand(), input_colors(), input_accents())

    def do_no(self, arg):
        """New outfit. Creates an blank outfit for the Lookbook."""
        create_outfit()

    def do_ap(self, arg):
        """Add piece to outfit. User must specify a outfit id followed by the piece ids they wish to add: ap <oid> <pid> <pid> <ect.>"""
        add_piece_to_outfit(arg)

    def do_rp(self, arg):
        """Remove piece from outfit. User must specify an outfit id followed by the piece ids they wish to remove: rp <oid> <pid> <pid> <ect.>"""
        remove_piece_from_outfit(arg)

    def do_ep(self, arg):
        """Edit piece. User must specify an piece id: ep <id>"""
        edit_piece(arg)

    def do_dp(self, arg):
        """Delete piece. User must specify a piece id: dp <id>"""
        delete_piece(arg)

    def do_do(self, arg):
        """Delete outfit. User must specify an outfit id: dp <id>"""
        delete_outfit(arg)

    def do_cp(self, arg):
        """Clone piece. User must specify an piece id: cp <id>"""
        clone_piece(arg)

    def do_co(self, arg):
        """Clone outfit. User must specify an outfit id: co <id>"""
        clone_outfit(arg)

    def do_sp(self, arg):
        """Search Pieces. User must specify one or multiple keywords: sw <keyword1> <keyword2> <ect.>"""
        search_pieces(arg)

    def do_so(self, arg):
        """Search Outfits. User must specify one or multiple keywords: sl <keyword1> <keyword2> <ect.>"""
        search_outfits(arg)

    def do_vp(self, arg):
        """View piece(s). Display all pieces, or view a specified piece: vp [piece_id]."""
        if not arg:
            print_all_pieces()
        else:
            if validate_piece_id(arg):
                print_single_piece(arg)

    def do_vo(self, arg):
        """View outfit(s). Display all outfits, or view a specified outfit: vo [outfit_id]."""
        if not arg:
            print_all_outfits()
        else:
            if validate_outfit_id(arg):
                print_outfit(arg)

    def do_x(self, arg):
        """E(x)it. Exit the shell."""
        print("Thank you for using tenue.")
        sys.exit()

    def do_exit(self, arg):
        """Exit. Exit the shell."""
        print("Thank you for using tenue.")
        sys.exit()

    def do_q(self, arg):
        """(Q)uit. Exit the shell."""
        print("Thank you for using tenue.")
        sys.exit()

    def do_quit(self, arg):
        """Quit. Exit the shell."""
        print("Thank you for using tenue.")
        sys.exit()
