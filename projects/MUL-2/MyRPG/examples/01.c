void move_player(player_t *player, sfKeyCode key, map_t *map)
{
    int new_x = player->x;
    int new_y = player->y;
    
    if (key == sfKeyLeft)
        new_x--;
    else if (key == sfKeyRight)
        new_x++;
    if (map->tiles[new_y][new_x] != '#') {
        player->x = new_x;
        player->y = new_y;
    }
}
