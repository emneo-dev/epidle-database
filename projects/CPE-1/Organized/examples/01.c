int evaluate_expr(char *str)
{
    int result = 0;
    int num = 0;
    char op = '+';
    
    for (int i = 0; str[i]; i++) {
        if (str[i] >= '0' && str[i] <= '9')
            num = num * 10 + (str[i] - '0');
        if (str[i] == '+' || str[i] == '-' || str[i] == '*') {
            result = apply_op(result, num, op);
            op = str[i];
            num = 0;
        }
    }
    return (result);
}
