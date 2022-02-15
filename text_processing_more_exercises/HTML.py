title_article=input()
content_article=input()

print(f"<h1>\n\t{title_article}\n</h1>")
print(f"<article>\n\t{content_article}\n</article>")

data=input()
while not data=="end of comments":
    print(f"<div>\n\t{data}\n</div>")
    data=input()