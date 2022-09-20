---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---
<div id="this-school-year">
{% for category in site.school-year-tags %}
  <div class="archive-group">
    {% capture category_name %}{{ category }}{% endcapture %}
    <div id="#{{ category_name | slugize }}"></div>
    <p></p>

    <h1 class="category-head">{{ category_name }}</h1>
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.categories[category_name] %}
    <article class="archive-item">
      <h2><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h2>
    </article>
    {% endfor %}
  </div>
{% endfor %}
</div>
