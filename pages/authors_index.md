---
layout: page
title: "For Authors"
meta_title: "Information for Authors for SIGCSE TS 2022"
permalink: "/authors/"
---

<!-- {% include covid-guidelines-alert.html %} -->

We have broken out submission guidelines by type. There are many ways to share the excellent work you are doing, and we would encourage you to consider all of them as you think about what would make the best vehicle for sharing your efforts with the larger community.

<!--
## SIGCSE TS 2022 Presentation Information

We are excited to announce that Pathable has been selected as the virtual platform for the 2022 SIGCSE Technical Symposium!  For information on how the different tracks will be run during the Symposium, please follow the links below:

<ul>
    {% assign posts = site.authors | sort: 'order' %}
    {% for post in posts %}
    <li><a href="{{ site.url }}{{ post.url }}#presenting-at-sigcse-ts-2022">{{ post.title }}</a></li>
    {% endfor %}
</ul>
-->

## SIGCSE TS 2022 Tracks
Follow the links below for detailed information about submission guidelines to the submission type.
<ul>
    {% assign posts = site.authors | sort: 'order' %}
    {% for post in posts %}
    <li><a href="{{ site.url }}{{ post.url }}">{{ post.track }}</a></li>
    {% endfor %}
</ul>
