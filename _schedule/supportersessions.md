---
layout: page
order: 1
title: Supporter Sessions Schedule
sidebar: schedule_supportersessions
---

<button onclick="topFunction()" id="toTopButton" title="Go to top">Back to Top</button> 

{% for category in site.data.supporters %}


{% for supporter in category[1]  %}
{% if supporter.sessions %}
<div class="row">
    <h2 id="supporter-{{supporter.name | downcase}}" class="text-center" style="border-top: 1px solid #ccc; background-color:#52bdf9; font-family: Lato, Helvetica Neue, Helvetica, Arial, sans-serif; font-weight: bold; color: white;">{{category[0]}} Supporter</h2>
</div>
<p>
<table style="border: 0px; width: 100%;">
    <tr>
        <td style="vertical-align: middle; font-weight: bold; font-size: xx-large;">{{supporter.name}}</td>
        <td style="text-align: right;"><img alt="{{supporter.name}}"
                   src="{{site.url}}/images/supporter_logos/frontpage/{{supporter.image}}"
                   /></td>
    </tr>
</table>
{% for supportersession in supporter.sessions %}
<div class="card">
    <div class="container">
        <h3 id="event-{{supportersession.title | downcase | replace: " ", "_" }}">{{ supportersession.title }}</h3>
        <span class="alert-box papersession">{{ supportersession.day }} / {{ supportersession.time }}</span>

{% if supportersession.url %}
<p><strong>Event website</strong> : <a href="{{supportersession.url}}" target=_new>{{supportersession.url}}</a></p>
{% endif %}
<p><strong>Presenters</strong> : {{supportersession.presenters}}</p>
<p>{{supportersession.description}}</p>
<p><img alt="{{supporter.name}}"
                   src="{{site.url}}/images/supporter_logos/frontpage/{{supporter.image}}"
                   /></p>
</div>
</div>

{% endfor %}

</p>
{% endif %}
{% endfor %}

{% endfor %}
