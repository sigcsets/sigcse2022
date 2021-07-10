---
layout: page
title: "For Reviewers"
meta_title: "Information for Reviewers for SIGCSE TS 2022"
permalink: "/reviewers/"
sidebar: reviewers
---

We have broken out submission guidelines by type. There are many ways to share the excellent work you are doing, and we would encourage you to consider all of them as you think about what would make the best vehicle for sharing your efforts with the larger community.

<h2>
	<p>Follow the links below for detail information about submission guidelines to the submission type.</p>
<ul>
    {% assign posts = site.reviewers | sort: 'order' %}
    {% for post in posts %}
    {% if post.track != 'XXX' %} 
    <li><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></li>
    {% else %}
    <li>{{ post.track }} (TBA)</li>
    {% endif %}
    {% endfor %}
</ul>
