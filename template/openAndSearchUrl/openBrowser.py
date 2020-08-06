import webbrowser
new = 1
urls = [ "https://webUrl", "https://webUrl1", "https://webUrl2" ]
for i in range(len(urls)):
  webbrowser.open(urls[i], new=new)