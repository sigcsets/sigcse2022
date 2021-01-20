---
layout: page
order: 1
title: SIGCSE TS 2021 Keynotes
sidebar: schedule_keynotes
---

<button onclick="topFunction()" id="toTopButton" title="Go to top">Back to Top</button> 

The 52nd ACM Technical Symposium on Computer Science Education is honored to have an amazing group of keynote speakers this year!

{% for keynote in site.data.keynotes.keynotes %}
<div class="card">
<div class="row t30">
<div class="large-6 columns" style="text-align: center"> <!-- Start first column -->
<img src="{{ site.url }}/images/keynotes/{{ keynote.headshot }}"/>
</div>
<div class="large-6 columns">
<h2>{{ keynote.speaker }}</h2><h3>{{ keynote.affiliation }}</h3>
</div>
</div> <!-- End Row -->
<div class="container">
<span class="alert-box keynote">{{ keynote.session }} - {{ keynote.day}} at {{ keynote.time }}</span>
<h2 id="{{id}}">{{ keynote.title }}</h2>
<p>{{ keynote.description }}</p>
</div>
</div>
{% endfor %}