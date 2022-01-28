from tenue.print_statements import *


# given keywords, search pieces, print results
def search_pieces(keywords):
    print_piece_headers()
    results = Piece.select()
    for keyword in keywords.split():
        # TODO: ignore hyphens and apostrophes in user input and in searched fields
        # &= operator for exclusive search
        # "|" vs. "or" matters a lot, as well as the order of operations
        results &= ((Piece.select().join(Kind).where(Kind.name == keyword))
                    or ((Piece.select().join(PieceColor).join(Color).where((Color.name.contains(keyword))))
                    | (Piece.select().join(PieceAccent).join(Color).where((Color.name.contains(keyword)))))
                    or (Piece.select().where((Piece.subkind.contains(keyword)) | (Piece.description.contains(keyword)) |
                                             (Piece.brand.contains(keyword)))))
    for p in results.order_by(Piece.kind, Piece.subkind, Piece.brand):
        print_piece(p)
    print_divider_hyphens()
    print(('Search keyword(s) "' + keywords + '" matched ' + str(len(results)) + ' piece(s).').center(console_width))
    return


# given keywords, search outfits, print results
def search_outfits(keywords):
    results = Outfit.select()
    for keyword in keywords.split():
        # &= operator for exclusive search
        # "|" vs. "or" matters a lot, as well as the order of operations
        results &= (Outfit.select().join(OutfitPiece).join(Piece).join(Kind).where(Kind.name == keyword)
                    or ((Outfit.select().join(OutfitPiece).join(Piece).join(PieceColor).join(Color).where(
                        (Color.name.contains(keyword)))) | Outfit.select().join(OutfitPiece).join(Piece).join(
                        PieceColor).join(Color).where((Color.name.contains(keyword))))
                    or (Outfit.select().join(OutfitPiece).join(Piece).where(
                        (Piece.subkind.contains(keyword)) | (Piece.description.contains(keyword)) |
                        (Piece.brand.contains(keyword)))))
    for o in results:
        print_outfit(o)
    print(('Search keyword(s) "' + keywords + '" matched ' + str(len(results)) + ' outfit(s).').center(console_width))
    return
