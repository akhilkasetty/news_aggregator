from django.shortcuts import render



# Create your views here.
def home(request):
    import requests
    import json
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=aa527e57e7024a87a5e6711a0db524e2')
    data = requests.get(url)
    api_data = json.loads(data.content)
    return render(request, 'news_blog/home.html', {'data': api_data})
