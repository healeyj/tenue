# tenue

*Tenue* is the French word for outfit.

## a text-based wardrobe manager

tenue is a command-line wardrobe manager.

## features:
* catalog your clothes
* modify outfits in seconds
* search clothes and outfits with keywords
---
## design specifications:
**Pieces** of clothing have 6 optional attributes: *kind, subkind, nickname, brand, colors,* and *accents*.

*Kind* is predefined in *init_db.py*:
> ['',
         'headwear',
         'outerwear',
         'top',
         'underwear',
         'bottom',
         'footwear',
         'accessory'  # ex. belts, socks, masks, jewelry, ect.
         ]

*Subkind* is a user-defined attribute to further specify a kind (ex. "rain jacket", "jeans", "sneakers", ect.).

*Nickname* should help identify the piece (ex. "my favorite shirt").

*Brand* is straightforward (ex. "Nike", "Levi's", "Gucci", ect.).

*Colors* must match a [CSS4 color from matplotlib](https://matplotlib.org/3.1.0/_images/sphx_glr_named_colors_003.png). This is a multivalued attribute that represents the major colors of the piece.

*Accents* are the same as colors except it represents minor colors on a piece (ex. a navy Ralph Lauren polo shirt with an embroidered red logo has a red accent).

---

An **outfit** *(une tenue)* is an arrangement of pieces.
## dependencies:
* [peewee](https://github.com/coleifer/peewee)
* [num2words](https://pypi.org/project/num2words/)

## instructions:

Clone the repo, install Python and the dependencies above, then execute main.py
