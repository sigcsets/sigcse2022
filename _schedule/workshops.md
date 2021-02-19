---
layout: page
order: 1
title: Workshop Schedule
sidebar: schedule_workshops
---

<button onclick="topFunction()" id="toTopButton" title="Go to top">Back to Top</button> 

Workshops will take place duing these time blocks:
<ul>
{% for block in site.data.workshops.blocks %}
<li><a href="#block-{{block.block | downcase}}">Workshop Block {{block.block}} - {{ block.day }} @ {{ block.time }}</a></li>
{% endfor %}
</ul>

<strong>How to register for workshops</strong> : Workshops are a part of the SIGCSE Technical Symposium's main program.  You can add workshops to your Symposium registration when you register through Cvent for an additional cost.  <em>Symposium registration is required to attend any SIGCSE TS 2021 workshop.</em>

{% assign block = "X" %}
{% assign position = -1 %}
{% for workshop in site.data.workshops.workshops %}
{% if block != workshop.block %}
{% assign block = workshop.block %}
{% assign position = position | plus: 1 %}
<h2 class = "block_header" id="block-{{block | downcase}}">Block {{block}} Workshops</h2>
{% endif %}
<div class="card">
<div class="container">
<h3 id="workshop-{{workshop.number}}">Workshop {{workshop.number}} : {{workshop.title}}</h3>
<span class="alert-box workshop"><strong>Block {{workshop.block}}</strong> - {{ site.data.workshops.blocks[position].day }} / {{ site.data.workshops.blocks[position].time }}</span>
{% if workshop.url %}
<p><strong>Workshop website</strong> : <a href="{{workshop.url}}" target=_new>{{workshop.url}}</a></p>
{% endif %} 
<p><strong>Workshop organizers</strong> : {{workshop.presenters}}</p>
<p><strong>Block {{workshop.block}}</strong> - {{ site.data.workshops.blocks[position].day }} @ {{ site.data.workshops.blocks[position].time }}</p>
<p>{{workshop.ad}}</p>
</div>
</div>
{% endfor %}
