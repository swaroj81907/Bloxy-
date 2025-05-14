from configs.search_module import perform_search
from configs.calculator import calculate_expression

def get_bot_response(user_input, search=False, calculate=False):
    user_input = user_input.strip().lower()

    default_replies = {
        "hi": "Hello!",
        "hello": "Hi there!",
        "how are you": "I'm a bot, but I'm running smoothly!",
        "who made you": "I was developed using Python and Flask with Google Search API!",
    }

    if not user_input:
        return "Please say something!"

    if calculate:
        return calculate_expression(user_input)

    if search:
        return perform_search(user_input)

    for key in default_replies:
        if key in user_input:
            return default_replies[key]

    return "Sorry, I don't understand. Try using Search or Calculate!"
