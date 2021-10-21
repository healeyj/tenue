# Tenue wardrobe manager

Tenue is a command-line application. It runs on Python and SQL.

*Tenue* is the French word for outfit.

    ==jgs==!====!=====!=====!====!===!===!=====!===!===!====
       /`\__/`\   /`\   /`\  |~| |~|  /)=I=(\  /`"""`\
      |        | |   `"`   | | | | |  |  :  | |   :   |
      '-|    |-' '-|     |-' )/\ )/\  |  T  \ '-| : |-'
        |    |     |     |  / \// \/  (  |\  |  '---'
        '.__.'     '.___.'  \_/ \_/   |  |/  /
                                      |  /  /
                                      |  \ /
                                      '--'`

## Features:
* catalog your clothes
* modify outfits in seconds
* search clothes and outfits with keywords

## Supported commands:
- np - Create new piece
- cp - Clone/Duplicate piece
- ep - Edit piece
- dp - Delete piece
- no - Create outfit
- ap - Add piece to outfit
- rp - Remove piece from outfit
- co - Clone/Duplicate outfit
- do - Delete outfit
- vp - View specific piece
- vo - View specific outfit
- sp - Search pieces
- so - Search outfits

## Design specifications:
**Pieces** of clothing have 6 optional attributes: *kind, subkind, nickname, brand, colors, and accents*.

- *Kinds* are predefined in *init_db.py*: 'headwear', 'outerwear', 'top', 'underwear', 'bottom', 'footwear', and 'accessory'.

- *Subkinds* are user-defined attributes that further specify a kind (ex. "rain jacket" is a subkind of 'top', "jeans" are a subkind of 'bottom', "sneakers" are a subkind of 'footwear', ect.).

- *Nicknames* are especially optional. When used, they should help identify the piece (ex. "my favorite shirt").

- *Brands* are straightforward (ex. "Louis Vuitton", "Yves Saint Laurent", "Dior", ect.).

- *Colors* must match a [valid CSS color](https://matplotlib.org/3.1.0/_images/sphx_glr_named_colors_003.png). This is a multivalued attribute that represents the major colors of the piece.

- *Accents* functions the same as colors except it represents colors of a piece that are subtle but still visible. 

## Dependencies:
* [peewee](https://github.com/coleifer/peewee)
* [num2words](https://pypi.org/project/num2words/)

## How do I use tenue?

Clone this repository, install Python 3 and the dependencies above, then execute main.py
