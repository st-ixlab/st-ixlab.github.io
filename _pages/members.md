---
layout: page
permalink: /people/
title: Members
description: Members of the Interaction Lab
nav: true
nav_order: 3
---

<div class="members-page">
  <!-- Professor Section -->
  {% if site.data.members.professor %}
    <h2 class="members-section-title">Professor</h2>
    <div class="members-section">
      {% for prof in site.data.members.professor %}
        <div class="member-card professor-card">
          {% if prof.image %}
            <div class="member-image">
              <img src="{{ '/assets/img/' | append: prof.image | relative_url }}" alt="{{ prof.name }}" class="img-fluid rounded">
            </div>
          {% endif %}
          <div class="member-info">
            <h3 class="member-name">{{ prof.name }}</h3>
            <p class="member-title">{{ prof.title }}</p>
            {% if prof.email %}
              <p class="member-contact">Email: <a href="mailto:{{ prof.email }}">{{ prof.email }}</a></p>
            {% endif %}
            {% if prof.tel %}
              <p class="member-contact">Tel: {{ prof.tel }}</p>
            {% endif %}
            {% if prof.office %}
              <p class="member-contact">Office: {{ prof.office }}</p>
            {% endif %}
            {% if prof.education %}
              <div class="member-education">
                <h4>Education & Experience</h4>
                <ul>
                  {% for item in prof.education %}
                    <li>{{ item }}</li>
                  {% endfor %}
                </ul>
              </div>
            {% endif %}
          </div>
        </div>
      {% endfor %}
    </div>
  {% endif %}

  <!-- Graduate Students Section -->
  {% if site.data.members.graduate_students %}
    <h2 class="members-section-title">Graduate Students</h2>
    <div class="members-grid">
      {% for student in site.data.members.graduate_students %}
        <div class="member-card">
          {% if student.image %}
            <div class="member-image">
              <img src="{{ '/assets/img/' | append: student.image | relative_url }}" alt="{{ student.name }}" class="img-fluid rounded" onerror="this.src='{{ '/assets/img/members/placeholder.png' | relative_url }}'">
            </div>
          {% else %}
            <div class="member-image">
              <img src="{{ '/assets/img/members/placeholder.png' | relative_url }}" alt="{{ student.name }}" class="img-fluid rounded">
            </div>
          {% endif %}
          <div class="member-info">
            <h4 class="member-name">{{ student.name }}</h4>
            <p class="member-status">{{ student.status }}</p>
            {% if student.department %}
              <p class="member-detail">{{ student.department }}</p>
            {% endif %}
            {% if student.research_area %}
              <p class="member-detail">Research Area: {{ student.research_area }}</p>
            {% endif %}
            {% if student.email %}
              <p class="member-contact">Email: <a href="mailto:{{ student.email }}">{{ student.email }}</a></p>
            {% endif %}
          </div>
        </div>
      {% endfor %}
    </div>
  {% endif %}

  <!-- Undergraduate Students Section -->
  {% if site.data.members.undergraduate_students %}
    <h2 class="members-section-title">Undergraduate Students</h2>
    <div class="members-grid">
      {% for student in site.data.members.undergraduate_students %}
        <div class="member-card">
          {% if student.image %}
            <div class="member-image">
              <img src="{{ '/assets/img/' | append: student.image | relative_url }}" alt="{{ student.name }}" class="img-fluid rounded" onerror="this.src='{{ '/assets/img/members/placeholder.png' | relative_url }}'">
            </div>
          {% else %}
            <div class="member-image">
              <img src="{{ '/assets/img/members/placeholder.png' | relative_url }}" alt="{{ student.name }}" class="img-fluid rounded">
            </div>
          {% endif %}
          <div class="member-info">
            <h4 class="member-name">{{ student.name }}</h4>
            {% if student.division %}
              <p class="member-detail">{{ student.division }}</p>
            {% endif %}
            {% if student.research_area %}
              <p class="member-detail">Research Area: {{ student.research_area }}</p>
            {% endif %}
            {% if student.email %}
              <p class="member-contact">Email: <a href="mailto:{{ student.email }}">{{ student.email }}</a></p>
            {% endif %}
          </div>
        </div>
      {% endfor %}
    </div>
  {% endif %}

  <!-- Researchers Section -->
  {% if site.data.members.researchers %}
    <h2 class="members-section-title">Researcher</h2>
    <div class="members-grid">
      {% for researcher in site.data.members.researchers %}
        <div class="member-card">
          {% if researcher.image %}
            <div class="member-image">
              <img src="{{ '/assets/img/' | append: researcher.image | relative_url }}" alt="{{ researcher.name }}" class="img-fluid rounded" onerror="this.src='{{ '/assets/img/members/placeholder.png' | relative_url }}'">
            </div>
          {% else %}
            <div class="member-image">
              <img src="{{ '/assets/img/members/placeholder.png' | relative_url }}" alt="{{ researcher.name }}" class="img-fluid rounded">
            </div>
          {% endif %}
          <div class="member-info">
            <h4 class="member-name">{{ researcher.name }}</h4>
            {% if researcher.status %}
              <p class="member-status">{{ researcher.status }}</p>
            {% endif %}
            {% if researcher.department %}
              <p class="member-detail">{{ researcher.department }}</p>
            {% endif %}
            {% if researcher.research_area %}
              <p class="member-detail">Research Area: {{ researcher.research_area }}</p>
            {% endif %}
            {% if researcher.email %}
              <p class="member-contact">Email: <a href="mailto:{{ researcher.email }}">{{ researcher.email }}</a></p>
            {% endif %}
            {% if researcher.note %}
              <p class="member-note">{{ researcher.note }}</p>
            {% endif %}
          </div>
        </div>
      {% endfor %}
    </div>
  {% endif %}

  <!-- Alumni Section -->
  {% if site.data.members.alumni_graduates or site.data.members.alumni_undergraduates %}
    <h2 class="members-section-title">Alumni</h2>
    
    {% if site.data.members.alumni_graduates %}
      <h3 class="members-subsection-title">Graduates</h3>
      <div class="members-grid">
        {% for alum in site.data.members.alumni_graduates %}
          <div class="member-card">
            {% if alum.image %}
              <div class="member-image">
                <img src="{{ '/assets/img/' | append: alum.image | relative_url }}" alt="{{ alum.name }}" class="img-fluid rounded" onerror="this.src='{{ '/assets/img/members/placeholder.png' | relative_url }}'">
              </div>
            {% else %}
              <div class="member-image">
                <img src="{{ '/assets/img/members/placeholder.png' | relative_url }}" alt="{{ alum.name }}" class="img-fluid rounded">
              </div>
            {% endif %}
            <div class="member-info">
              <h4 class="member-name">{{ alum.name }}<br>{{ alum.degree }}</h4>
              {% if alum.department %}
                <p class="member-detail">{{ alum.department }}</p>
              {% endif %}
              {% if alum.research_area %}
                <p class="member-detail">Research Area: {{ alum.research_area }}</p>
              {% endif %}
              {% if alum.affiliation %}
                <p class="member-affiliation"><strong>{{ alum.affiliation }}</strong></p>
              {% endif %}
              {% if alum.affiliation_logo and alum.affiliation_logo != "" %}
                <div class="member-affiliation-logo">
                  {% assign file_ext = alum.affiliation_logo | split: '.' | last %}
                  {% if file_ext == 'svg' %}
                    <img src="{{ '/assets/img/' | append: alum.affiliation_logo | relative_url }}" alt="Affiliation logo" class="affiliation-logo-img">
                  {% else %}
                    <img src="{{ '/assets/img/' | append: alum.affiliation_logo | relative_url }}" alt="Affiliation logo" class="affiliation-logo-img">
                  {% endif %}
                </div>
              {% endif %}
            </div>
          </div>
        {% endfor %}
      </div>
    {% endif %}

    {% if site.data.members.alumni_undergraduates %}
      <h3 class="members-subsection-title">Undergraduates</h3>
      <div class="members-list">
        {% for alum in site.data.members.alumni_undergraduates %}
          <div class="alumni-item">
            <strong>{{ alum.name }}</strong>
            {% if alum.division %}
              , {{ alum.division }}
            {% endif %}
            {% if alum.affiliation and alum.affiliation != "" %}
              {% assign current_position = alum.affiliation | remove_first: "Now @ " %}
              (Current Position: {{ current_position }})
            {% endif %}
          </div>
        {% endfor %}
      </div>
    {% endif %}
  {% endif %}

  <!-- KIT Alumni Section (Toggleable) -->
  {% if site.data.members.kit_alumni_graduates or site.data.members.kit_alumni_undergraduates %}
    <details class="kit-alumni-section">
      <summary class="members-section-title kit-alumni-toggle">
        <span>KIT Alumni</span>
        <i class="fa-solid fa-chevron-down toggle-icon"></i>
      </summary>
      
      <div class="kit-alumni-content">
        {% if site.data.members.kit_alumni_graduates %}
          <h3 class="members-subsection-title">Graduate Students</h3>
          <div class="members-grid">
            {% for alum in site.data.members.kit_alumni_graduates %}
              <div class="member-card">
                {% if alum.image %}
                  <div class="member-image">
                    <img src="{{ '/assets/img/' | append: alum.image | relative_url }}" alt="{{ alum.name }}" class="img-fluid rounded" onerror="this.src='{{ '/assets/img/members/placeholder.png' | relative_url }}'">
                  </div>
                {% else %}
                  <div class="member-image">
                    <img src="{{ '/assets/img/members/placeholder.png' | relative_url }}" alt="{{ alum.name }}" class="img-fluid rounded">
                  </div>
                {% endif %}
                <div class="member-info">
                  <h4 class="member-name">{{ alum.name }}</h4>
                  {% if alum.affiliation and alum.affiliation != "" %}
                    <p class="member-affiliation"><strong>{{ alum.affiliation }}</strong></p>
                  {% endif %}
                  {% if alum.affiliation_logo and alum.affiliation_logo != "" %}
                    <div class="member-affiliation-logo">
                      <img src="{{ '/assets/img/' | append: alum.affiliation_logo | relative_url }}" alt="Affiliation logo" class="affiliation-logo-img">
                    </div>
                  {% endif %}
                </div>
              </div>
            {% endfor %}
          </div>
        {% endif %}

        {% if site.data.members.kit_alumni_undergraduates %}
          <h3 class="members-subsection-title">Undergraduate Students</h3>
          <div class="members-grid">
            {% for alum in site.data.members.kit_alumni_undergraduates %}
              <div class="member-card">
                {% if alum.image %}
                  <div class="member-image">
                    <img src="{{ '/assets/img/' | append: alum.image | relative_url }}" alt="{{ alum.name }}" class="img-fluid rounded" onerror="this.src='{{ '/assets/img/members/placeholder.png' | relative_url }}'">
                  </div>
                {% else %}
                  <div class="member-image">
                    <img src="{{ '/assets/img/members/placeholder.png' | relative_url }}" alt="{{ alum.name }}" class="img-fluid rounded">
                  </div>
                {% endif %}
                <div class="member-info">
                  <h4 class="member-name">{{ alum.name }}</h4>
                  {% if alum.affiliation and alum.affiliation != "" %}
                    <p class="member-affiliation"><strong>{{ alum.affiliation }}</strong></p>
                  {% endif %}
                  {% if alum.affiliation_logo and alum.affiliation_logo != "" %}
                    <div class="member-affiliation-logo">
                      <img src="{{ '/assets/img/' | append: alum.affiliation_logo | relative_url }}" alt="Affiliation logo" class="affiliation-logo-img">
                    </div>
                  {% endif %}
                </div>
              </div>
            {% endfor %}
          </div>
        {% endif %}
      </div>
    </details>
  {% endif %}
</div>

