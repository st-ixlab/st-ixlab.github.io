---
layout: about
title: Home
permalink: /
nav: true
nav_order: 1
custom_title: "<b>Seoultech <span style='color: #ff6464ea;'>IX</span>Lab</b>"
subtitle: # kept empty to avoid default rendering
profile:
  enabled: true
  image: lab_intro1.jpg
  align: full

selected_papers: false # includes a list of papers marked as "selected={true}"
social: false # includes social icons at the bottom of the page

announcements:
  enabled: false # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: true
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 12 # leave blank to include all the blog posts
---

<!-- Lab Introduction Section (Left 30%) -->
<div class="lab-intro-content">
  <p class="lead">
    The SEOULTECH Interaction Lab (IXLAB) explores the future of human-computer synergy through <span style="color: #ff6464ea; font-weight: bold;">AI-infused interactive computing</span>. We focus on designing intelligent, adaptive systems that understand complex human behaviors and contexts via multimodal sensing. By bridging adaptive intelligence with immersive environments, we strive to create <span style="color: #ff6464ea; font-weight: bold;">purposeful interaction paradigms</span> that empower individuals in an increasingly automated and augmented world.
  </p>
</div>

<!-- Research Pillars Section -->
<div class="row mt-2">
  <div class="col-12 mb-1"> <!-- Reduced mb-2 to mb-1, mt-3 to mt-2 -->
    <h2>Research Topics</h2>
  </div>
  <div class="col-md-6 mb-4">
    <div class="card h-100 border-0 shadow-sm topic-card"> <!-- Added topic-card class -->
      <div class="card-body">
        <h5 class="card-title">Immersive Spatial Computing</h5> <!-- Changed h3 to h5 -->
        <img src="{{ '/assets/img/topic1_one.png' | relative_url }}" class="img-fluid mb-3" alt="Immersive Spatial Computing" style="width: 100%; height: auto; border-radius: 4px;">
        <p class="card-text">Investigates the intersection of spatial usability and hardware mediation to optimize user immersion and interaction within AR, VR, and MR environments</p>
        <p class="card-text small text-muted">Selected publications:
          <a href="https://dl.acm.org/doi/10.1145/3706598.3714221">CHI '25</a>,
          <a href="https://dl.acm.org/doi/10.1145/3708359.3712087">IUI '25</a>,
          <a href="https://dl.acm.org/doi/10.1145/3706598.3713410">CHI '25</a>
        </p>
      </div>
    </div>
  </div>
  <div class="col-md-6 mb-4">
    <div class="card h-100 border-0 shadow-sm topic-card">
      <div class="card-body">
        <h5 class="card-title">Intelligence-Augmented & Generative Interaction</h5>
        <img src="{{ '/assets/img/topic2_one.png' | relative_url }}" class="img-fluid mb-3" alt="Generative Interaction" style="width: 100%; height: auto; border-radius: 4px;">
        <p class="card-text">Leverages Generative AI and Large Language Models (LLMs) to create adaptive, personalized content and intelligent interfaces that expand the boundaries of human creativity</p>
        <p class="card-text small text-muted">Selected publications:
          <a href="https://doi.org/10.1016/j.ijhcs.2025.103673">IJHCS '26</a>,
          <a href="https://doi.org/10.7717/peerj-cs.3170">PeerJ CS '24</a>,
          <a href="https://dl.acm.org/doi/10.1145/3681756.3697877">SIGGRAPH Asia '24</a>,
          <a href="https://dl.acm.org/doi/10.1145/3544549.3585872">CHI '23</a>
        </p>
      </div>
    </div>
  </div>
  <div class="col-md-6 mb-4">
    <div class="card h-100 border-0 shadow-sm topic-card">
      <div class="card-body">
        <h5 class="card-title">Multimodal Sensing Interfaces</h5>
        <img src="{{ '/assets/img/topic3_one.png' | relative_url }}" class="img-fluid mb-3" alt="Multimodal Sensing" style="width: 100%; height: auto; border-radius: 4px;">
        <p class="card-text">Explores innovative input modalities to enable seamless and discreet communication in diverse social and digital contexts</p>
        <p class="card-text small text-muted">Selected publications:
          <a href="https://dl.acm.org/doi/10.1145/3746058.3758359">UIST '25</a>,
          <a href="https://dl.acm.org/doi/10.1145/3706599.3720209">CHI '25</a>,
          <a href="https://doi.org/10.1080/10447318.2024.2348837">IJHCI '24</a>,
          <a href="https://dl.acm.org/doi/10.1145/3461615.3485428">ICMI '21</a>
        </p>
      </div>
    </div>
  </div>
  <div class="col-md-6 mb-4">
    <div class="card h-100 border-0 shadow-sm topic-card">
      <div class="card-body">
        <h5 class="card-title">Affective & Human-Centered Computing</h5>
        <img src="{{ '/assets/img/topic4_one.png' | relative_url }}" class="img-fluid mb-3" alt="Empathetic Computing" style="width: 100%; height: auto; border-radius: 4px;">
        <p class="card-text">Integrates affective state recognition and gaze visualization to foster social presence and optimize cognitive engagement in digital learning and communication.</p>
        <p class="card-text small text-muted">Selected publications:
          <a href="https://ieeexplore.ieee.org/document/11236281">ISMAR '24</a>,
          <a href="https://link.springer.com/article/10.1007/s10639-024-12697-w">EAIT '25</a>,
          <a href="https://dl.acm.org/doi/10.1145/3517031.3529238">ETRA '22</a>,
          <a href="https://dl.acm.org/doi/10.1145/3565066.3608702">MobileHCI '23</a>
        </p>
      </div>
    </div>
  </div>
</div>
<hr>

