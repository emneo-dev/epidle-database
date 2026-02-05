void handle_client(int client_fd, server_t *server)
{
    char buffer[1024];
    int bytes_read;
    
    while ((bytes_read = read(client_fd, buffer, 1024)) > 0) {
        buffer[bytes_read] = '\0';
        parse_command(buffer, server);
    }
    close(client_fd);
}
