---
layout: page
title: "For Authors"
meta_title: "Information for Authors for SIGCSE 2021"
permalink: "/authors/"
sidebar: authors
---

We have broken out submission guidelines by type. There are many ways to share the excellent work you are doing, and we would encourage you to consider all of them as you think about what would make the best vehicle for sharing your efforts with the larger community.

<ul>
    {% assign posts = site.authors | sort: 'order' %}
    {% for post in posts %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }} Submission Information</a></li>
    {% endfor %}
</ul>
