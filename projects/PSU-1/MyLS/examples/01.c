int main(int ac, char **av)
{
    int opt;
    int l_flag = 0;
    
    while ((opt = getopt(ac, av, "lRartd")) != -1) {
        if (opt == 'l')
            l_flag = 1;
    }
    return (0);
}
