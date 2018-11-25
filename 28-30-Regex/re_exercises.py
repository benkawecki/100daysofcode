import re


def extract_course_times(str):
    """Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']"""
    timestamp = re.compile(r'\d{2}:\d{2}')
    return timestamp.findall(str)



def get_all_hashtags_and_links(str):
    """Write a regular expression that returns this list:
       ['http://pybit.es/requests-cache.html', '#python', '#APIs']"""
    hastags_and_links = re.compile(r'((?:#|http)\S+)')
    return hastags_and_links.findall(str)


def match_first_paragraph(str):
    """Write a regular expression that returns  'pybites != greedy' """
    first_para = re.compile(r'<p>(.*?)</p>')
    return first_para.match(str).group(1)



if __name__ == "__main__":
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    print('Course Times:')
    print(extract_course_times(flask_course))

    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    print('Hashtags and links:')
    print(get_all_hashtags_and_links(tweet))
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    print('First Para:')
    print(match_first_paragraph(html))
