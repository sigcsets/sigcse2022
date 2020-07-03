---
layout: page
title: "Symposium Committee"
meta_title: "Symposium Committee for SIGCSE TS 2021"
permalink: "/committee/"
# sidebar: committee
---

{% for comm in site.data.committee %}
<a name = "{{comm[0] | remove: " " }}"></a>  <!-- create anchors from committee name with no spaces -->
<h2>{{comm[0]}}</h2>
<table width="100%">
  <caption>Email: <a href="{{comm[1].email}}">{{comm[1].email}}</a></caption>
  <tr><th scope="col">Name</th><th scope="col">Institution</th></tr>
    {% for memb in comm[1].members %}
      <tr>
        <td>{{memb.name}}</td>
        {% if memb.inst %}
          <td>{{memb.inst}}</td>
        {% else %}
          <td>&nbsp;</td>
        {% endif %}
      </tr>
    {% endfor %}
</table>
{% endfor %}

