def calculate_expression(expr):
    try:
        expr = expr.replace('x', '*').replace('÷', '/')
        result = eval(expr, {"__builtins__": {}})
        if isinstance(result, float):
            result = round(result, 4)
        if '/' in expr:
            nums = expr.split('/')
            if len(nums) == 2 and nums[0].isdigit() and nums[1].isdigit():
                quotient = int(nums[0]) // int(nums[1])
                remainder = int(nums[0]) % int(nums[1])
                return f"Result: {result} (Quotient: {quotient}, Remainder: {remainder})"
        return f"Result: {result}"
    except Exception:
        return "Invalid expression. Please try something like 5+6 or 10/3."
