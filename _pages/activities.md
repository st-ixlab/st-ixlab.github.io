---
layout: page
title: Activities
permalink: /activities/
nav: true
nav_order: 6
description: A collection of photos from our activities.
---

<div class="row">
{% for activity in site.activities %}
  <div class="col-md-4 col-sm-6">
    <div class="card mb-3">
      <a href="{{ activity.url | relative_url }}">
        {% if activity.img %}
          <img class="card-img-top" src="{{ activity.img | relative_url }}" alt="{{ activity.title }}">
        {% endif %}
        <div class="card-body">
          <h5 class="card-title">{{ activity.title }}</h5>
        </div>
      </a>
    </div>
  </div>
{% endfor %}
</div>
