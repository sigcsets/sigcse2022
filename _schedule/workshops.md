---
layout: page
order: 1
title: Schedule of Workshops
---

{% assign block = 0 %}
{% for workshop in site.data.workshops.workshops %}
   {% if block != workshop.block %}
      {% assign block = workshop.block %}
      <h2 id="block-{{block | downcase}}">Block {{block}} Workshops</h2>
   {% endif %}
   <h3>Workshop {{workshop.number}} : {{workshop.title}}</h3>
   <p><strong>Workshop organizers</strong> : {{workshop.presenters}}</p>
   <p><strong>Block {{workshop.block}}</strong></p>
   {{workshop.ad}}
{% endfor %}
