void update_plane(plane_t *plane, int simulation_time)
{
    float angle = plane->angle * M_PI / 180;
    
    plane->x += cos(angle) * plane->speed * simulation_time;
    plane->y += sin(angle) * plane->speed * simulation_time;
}
