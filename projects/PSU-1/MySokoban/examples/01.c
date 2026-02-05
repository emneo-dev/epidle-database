int push_box(map_t *map, int y, int x, int dy, int dx)
{
    if (map->grid[y + dy][x + dx] == 'X')
        return (0);
    if (map->grid[y + dy][x + dx] == '#')
        return (0);
    map->grid[y + dy][x + dx] = 'X';
    map->grid[y][x] = ' ';
    return (1);
}
