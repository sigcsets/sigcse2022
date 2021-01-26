---
layout: page
order: 1
title: Supporter Sessions Schedule
sidebar: schedule_supportersessions
---

<button onclick="topFunction()" id="toTopButton" title="Go to top">Back to Top</button> 

{% for supportersession in site.data.supportersessions.supportersessions %}
<div class="card">
<div class="container">
<h2 id="event-{{supportersession.event | downcase}}">{{ supportersession.title }}</h2>
<span class="alert-box papersession">{{ supportersession.day }} / {{ supportersession.time }}</span>
<p><strong>Sponsored by {{ supportersession.supporter }}</strong></p>
{% if supportersession.url %}
<p><strong>Event website</strong> : <a href="{{supportersession.url}}" target=_new>{{supportersession.url}}</a></p>
{% endif %}
<p><strong>Presenters</strong> : {{supportersession.presenters}}</p>
<p>{{supportersession.description}}</p>
<img alt="{{supportersession.supporter}}"
                   src="{{site.url}}/images/supporter_logos/frontpage/{{supportersession.image}}"
                   />
</div>
</div>
{% endfor %}