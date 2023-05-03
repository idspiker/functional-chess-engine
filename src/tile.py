from dataclasses import dataclass

from field_enumerations import TileColor, Team, Piece

@dataclass(frozen=True)
class Tile:
    tile_color: TileColor
    is_selected: bool
    occupant_team: Team
    piece: Piece
    has_moved: bool
    is_highlighted: bool

    def to_tuple(self):
        return (
            self.tile_color,
            self.is_selected,
            self.occupant_team,
            self.piece,
            self.has_moved,
            self.is_highlighted
        )

    def change_field(self, field_name, new_val):
        field_names = tuple(self.__dict__.keys())

        index = field_names.index(field_name)

        values = self.to_tuple()

        values = (*values[:index], new_val, *values[index + 1:])

        return Tile(*values)
