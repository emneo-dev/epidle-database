int check_hit(boat_t *boat, int x, int y)
{
    for (int i = 0; i < boat->size; i++) {
        if (boat->pos[i].x == x && boat->pos[i].y == y) {
            boat->pos[i].hit = 1;
            return (1);
        }
    }
    return (0);
}
