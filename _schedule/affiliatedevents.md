---
layout: page
order: 1
title: Affiliated Event Schedule
sidebar: schedule_affiliatedevents
---

Affiliated Events will take place the week before the Technical Symposium.

{% for affiliatedevent in site.data.affiliatedevents.affiliatedevents %}
<h2 id="event-{{affiliatedevent.event | downcase}}">{{ affiliatedevent.title }}</h2>
{% if affiliatedevent.url %}
<p><strong>Event website</strong> : <a href="{{affiliatedevent.url}}">{{affiliatedevent.url}}</a></p>
{% endif %}
<p><strong>Event organizers</strong> : {{affiliatedevent.organizers}}</p>
<p>{{ affiliatedevent.day }} @ {{ affiliatedevent.time }}</p>
{{affiliatedevent.description}}
{% endfor %}