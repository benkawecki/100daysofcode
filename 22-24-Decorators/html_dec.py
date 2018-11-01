from functools import wraps


def make_html(tag):
    def wrap(f):

        @wraps(f)
        def wrapper(text):
            tagged_text = f'<{tag}>{text}</{tag}>'
            return f(tagged_text)

        return wrapper
    return wrap


@make_html('first')
@make_html('second')
def get_text(text):
    return text


print(get_text('Ben'))
