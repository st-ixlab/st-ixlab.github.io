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


<!-- New Horizontal Layout -->
<div class="row mt-2">
  <div class="col-12 mb-1">
    <h2>Research Topics</h2>
  </div>

  <!-- Topic 1 -->
  <div class="col-12 mb-4">
    <div class="card h-100 border-0 shadow-sm topic-card">
      <div class="row g-0 align-items-center">
        <div class="col-md-5 p-3">
            <img src="{{ '/assets/img/topic1_new.png' | relative_url }}" class="img-fluid rounded" alt="Immersive Spatial Computing" style="width: 100%; height: auto;">
        </div>
        <div class="col-md-7">
          <div class="card-body">
            <h5 class="card-title">Immersive Spatial Computing</h5>
            <p class="card-text">We investigate the intersection of spatial usability and hardware mediation to optimize user immersion and interaction within AR, VR, and MR environments. By bridging the gap between physical and virtual worlds, we aim to design intuitive interaction paradigms for mixed reality workspaces and enhance cognitive augmentation through spatially-aware interfaces.</p>
            <p class="card-text small text-muted mb-1">Selected publications:</p>
            <ul class="small text-muted mb-0" style="padding-left: 1.2rem;">
              <li>[CHI '25] <a href="https://dl.acm.org/doi/10.1145/3706598.3714221">Through the Looking Glass, and What We Found There: A Comprehensive Study of User Experiences with Pass-Through Devices in Everyday Activities</a></li>
              <li>[IUI '25] <a href="https://dl.acm.org/doi/10.1145/3708359.3712087">A picture is worth a thousand words? Investigating the Impact of Image Aids in AR on Memory Recall for Everyday Tasks</a></li>
              <li>[CHI '25] <a href="https://dl.acm.org/doi/10.1145/3706598.3713410">Understanding User Behavior in Window Selection using Dragging for Multiple Targets</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Topic 2 -->
  <div class="col-12 mb-4">
    <div class="card h-100 border-0 shadow-sm topic-card">
      <div class="row g-0 align-items-center">
        <div class="col-md-5 p-3">
             <img src="{{ '/assets/img/topic2_new.png' | relative_url }}" class="img-fluid rounded" alt="Generative Interaction" style="width: 100%; height: auto;">
        </div>
        <div class="col-md-7">
          <div class="card-body">
            <h5 class="card-title">Intelligence-Augmented & Generative Interaction</h5>
            <p class="card-text">We leverage Generative AI and Large Language Models (LLMs) to create adaptive, personalized content and intelligent interfaces that expand the boundaries of human creativity. We study how AI can act as a collaborative partner in creative tasks, ensure safe and appropriate content generation, and deliver context-aware information in spatial computing environments.</p>
            <p class="card-text small text-muted mb-1">Selected publications:</p>
            <ul class="small text-muted mb-0" style="padding-left: 1.2rem;">
              <li>[IJHCS '26] <a href="https://doi.org/10.1016/j.ijhcs.2025.103673">SnapSound: Empowering everyone to customize sound experience with Generative AI</a></li>
              <li>[PeerJ CS '24] <a href="https://doi.org/10.7717/peerj-cs.3170">Mitigating Inappropriate Concepts in Text-to-Image Generation with Attention-guided Image Editing</a></li>
              <li>[ISMAR '24] <a href="https://ieeexplore.ieee.org/document/11236281">Public Speaking Q&A Practice with LLM-Generated Personas in Virtual Reality</a></li>
              <li>[SIGGRAPH Asia '24] <a href="https://dl.acm.org/doi/10.1145/3681756.3697877">Designing LLM Response Layouts for XR Workspaces in Vehicles</a></li>
              <li>[CHI '23] <a href="https://dl.acm.org/doi/10.1145/3544549.3585872">Tingle Just for You: A Preliminary Study of AI-based Customized ASMR Content Generation</a></li>              
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Topic 3 -->
  <div class="col-12 mb-4">
    <div class="card h-100 border-0 shadow-sm topic-card">
      <div class="row g-0 align-items-center">
        <div class="col-md-5 p-3">
             <img src="{{ '/assets/img/topic3_new.png' | relative_url }}" class="img-fluid rounded" alt="Multimodal Sensing" style="width: 100%; height: auto;">
        </div>
        <div class="col-md-7">
          <div class="card-body">
            <h5 class="card-title">Multimodal Sensing Interfaces</h5>
            <p class="card-text">We explore innovative input modalities to enable seamless and discreet communication in diverse social and digital contexts. Our work focuses on developing novel sensing techniques that interpret silent speech, non-verbal sounds, and subtle gestures to facilitate natural interaction in both virtual and physical spaces.</p>
            <p class="card-text small text-muted mb-1">Selected publications:</p>
            <ul class="small text-muted mb-0" style="padding-left: 1.2rem;">
              <li>[UIST '25] <a href="https://dl.acm.org/doi/10.1145/3746058.3758359">Silent Yet Expressive: Toward Seamless VR Communication through Emotion-aware Silent Speech Interfaces</a></li>
              <li>[CHI '25] <a href="https://dl.acm.org/doi/10.1145/3706599.3720209">Exploring Emotion Expression Through Silent Speech Interface in Public VR/MR</a></li>
              <li>[EAIT '25] <a href="https://link.springer.com/article/10.1007/s10639-024-12697-w">Enhancing Learner Experience with Instructor Cues in Video Lectures: A Comprehensive Exploration and Design Discovery toward A Novel Gaze Visualization</a>
              </li>
              <li>[IJHCI '24] <a href="https://doi.org/10.1080/10447318.2024.2348837">EchoTap: Non-verbal Sound Interaction with Knock and Tap Gestures</a></li>
              <li>[ICMI '21] <a href="https://dl.acm.org/doi/10.1145/3461615.3485428">Knock & Tap: Classification and Localization of Knock and Tap Gestures using Deep Sound Transfer Learning</a></li>
              
            </ul>            
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<hr>

