---
layout: page
permalink: /publications/
title: Publication
description: 
nav: true
nav_order: 4
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

<div class="row">
  <div class="col-sm-11">
    {% include bib_search.liquid %}
    
    <div class="publications">
      <!-- Regular Publications -->
      <h2 class="bibliography">Publications</h2>
      {% bibliography --query @*[note!=Under review] %}

      <!-- Under Review Section -->
      <h2 class="bibliography">Under Review</h2>
      {% bibliography --query @*[note~=Under review]* --group_by none %}
    </div>
  </div>

  <div class="col-sm-1">
    {% include year_sidebar.liquid %}
  </div>
</div>
