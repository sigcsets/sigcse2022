---
layout: page
order: 1
title: Schedule of Workshops
---

## Workshops
{% for workshop in site.data.workshops.workshops %}
   <h3>{{workshop.title}}</h3>
   <p>{{workshop.ad}}</p>
{% endfor %}
