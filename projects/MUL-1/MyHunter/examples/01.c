void shoot_duck(game_t *game, int x, int y)
{
    for (int i = 0; i < game->nb_ducks; i++) {
        if (game->ducks[i].x == x && game->ducks[i].y == y) {
            game->ducks[i].alive = 0;
            game->score += 10;
        }
    }
}
