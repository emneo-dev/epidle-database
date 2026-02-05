void execute_pipeline(char **cmd1, char **cmd2)
{
    int pipefd[2];
    pid_t pid1, pid2;
    
    pipe(pipefd);
    if ((pid1 = fork()) == 0) {
        dup2(pipefd[1], 1);
        close(pipefd[0]);
        execvp(cmd1[0], cmd1);
    }
    if ((pid2 = fork()) == 0) {
        dup2(pipefd[0], 0);
        close(pipefd[1]);
        execvp(cmd2[0], cmd2);
    }
    close(pipefd[0]);
    close(pipefd[1]);
}
