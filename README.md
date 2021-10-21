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

- *Kinds* are predefined: 'headwear', 'outerwear', 'top', 'underwear', 'bottom', 'footwear', and 'accessory'

- *Subkinds* are user-defined attributes that further specify a kind (ex. "rain jacket" is a subkind of 'top')

- *Nicknames* are especially optional. When used, they should help identify the piece (ex. "my favorite shirt")

- *Brands* are straightforward (ex. "Louis Vuitton", "Yves Saint Laurent", "Dior", ect.)

- *Colors* are the major, dominant colors of a piece, and they must match a [predefined CSS color](https://matplotlib.org/3.1.0/_images/sphx_glr_named_colors_003.png) 

- *Accents* are the same as *colors* except they represent minor, subtle colors of a piece 

## Dependencies:
* [peewee](https://github.com/coleifer/peewee)
* [num2words](https://pypi.org/project/num2words/)

## How do I use Tenue?

Clone this repository, install Python 3 and the dependencies above, then execute main.py
