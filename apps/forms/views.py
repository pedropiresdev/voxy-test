from django.shortcuts import render

from apps.forms.forms import TextBox

CHARS_TO_EXCLUDE = ['.', ',', '!', '?', '"', ';', ':']


def remove_characters(words: list) -> list:
    for word in words:
        if word in CHARS_TO_EXCLUDE:
            words.remove(word)

    return words


def counter(request):

    if request.method == 'POST':

        text = TextBox(request.POST['texttocount'])

        if not text.is_valid():
            return render(request, 'forms/counter.html', {'error': 'Hi! Some text input is required.', 'on': 'active'})

        words = len(remove_characters(text.data.split()))

        return render(request, 'forms/counter.html',
                      {'word': words, 'text': text.data, 'on': 'active'})

    else:
        # returning HTML page if request.method is not POST
        return render(request, 'forms/counter.html', {'on': 'active'})
