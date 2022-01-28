from peewee import *

db_name = 'data.db'
db = SqliteDatabase(db_name)


class Kind(Model):
    name = TextField()

    class Meta:
        database = db


class Color(Model):
    name = CharField()
    hex = CharField()

    class Meta:
        database = db


# TODO: rename subkind to something more readable
class Piece(Model):
    kind = ForeignKeyField(Kind)  # Kind
    subkind = TextField()  # Subkind
    description = TextField()  # Description
    brand = TextField()  # Brand

    class Meta:
        database = db


class PieceColor(Model):
    piece = ForeignKeyField(Piece, backref='piece_colors')
    color = ForeignKeyField(Color, backref='color_pieces')

    class Meta:
        database = db


# accents are minor colors. a white shirt with a black logo has a black accent.
class PieceAccent(Model):
    piece = ForeignKeyField(Piece, backref='piece_accents')
    accent = ForeignKeyField(Color, backref='accent_pieces')

    class Meta:
        database = db


class Outfit(Model):
    # outfits no longer have a description
    # desc = TextField()

    class Meta:
        database = db


class OutfitPiece(Model):
    outfit = ForeignKeyField(Outfit, backref='outfit_pieces')
    piece = ForeignKeyField(Piece, backref='piece_outfits')

    class Meta:
        database = db
