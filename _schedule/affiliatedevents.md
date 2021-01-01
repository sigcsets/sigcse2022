---
layout: page
order: 1
title: Affiliated Event Schedule
sidebar: schedule_affiliatedevents
---

Workshops will take place duing these time blocks:
<ul>
{% for block in site.data.workshops.blocks %}
<li><a href="#block-{{block.block | downcase}}">Workshop Block {{block.block}} - {{ block.day }} & {{ block.time }}</a></li>
{% endfor %}
</ul>

{% assign block = "X" %}
{% assign position = -1 %}
{% for workshop in site.data.workshops.workshops %}
   {% if block != workshop.block %}
   {% assign block = workshop.block %}
   {% assign position = position | plus: 1 %}
   <h2 id="block-{{block | downcase}}">Block {{block}} Workshops</h2>
   {% endif %}
   <h3 id="workshop-{{workshop.number}}">Workshop {{workshop.number}} : {{workshop.title}}</h3>
   <p><strong>Workshop organizers</strong> : {{workshop.presenters}}</p>
   <p><strong>Block {{workshop.block}}</strong> - {{ site.data.workshops.blocks[position].day }} @ {{ site.data.workshops.blocks[position].time }}</p>
   {{workshop.ad}}
{% endfor %}