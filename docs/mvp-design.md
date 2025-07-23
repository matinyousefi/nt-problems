Title: mvp design doc 
Author: Matin Yousefi
Overview: This project aims to store math olympiad problems in the subject of number theory and offer a problem-based approache to learning olympiad number theory. 
Background: I have had the idea of writing a number theory book in my mind for so many years. The first year I thought NT as a full corse was in Corona years. I gave my weekly practices to students as chapters of a book. But the problems were too hard and we didn't get past chapter 5 i think - I had a tendency to use very hard problems for teaching. Before that I also gave a compressed course on Olympiad number theory which resulted in several handouts needless to say still too heavy and not proper for teaching. Once I started a project (Project 51) with another NT instructor and we reviewed problems from AoPS and exchanged .tex files in chat, that was left unfinished too. Another time we started a Group with several NT instuctors in Telegram and uploaded problems with photos and refrences as hashtags. Another time I tired to bring up a whole website to design problem sets with the aim of learning and teaching olympiad in a problem based manner. All of theses efforts failed. Keeping a project big and comullative is actually very harder than it looks. Contributers come and go and allocate time respective to the time they allocated to teaching the topic and most of them do not teach very long-term in Iran. Many non-profit chanels started to created content freely in Telegram. Non of which lasated more two or three years. So we need some way to for non-profit collaberation and Cummulative work upgrading the works outhers did before us. Maybe the solution is as easy as a git repository with some featers for quality check and translation. 
Requirements: every-one can help develop the project even with small amounts of times, students must be able to directly use the content, the project should be able to continued even after the author has ditanted away from the project. To honor or beloved native languge, we prefer to have automations that provide Farsi translation of the problems and contentsm we would like to design a project that could contain wast types of content creation (problem set for practice, handouts for learning, subject-based problem solbing approaches and thechniques)
Proposed Solution: 
Dependencies: aops and relation with the site 
Testing & Validation: materials that are thought are better 

# MVP Design Document: Olympiad Number Theory Problem Repository  

**Author**: Matin Yousefi  
**Last Updated**: [Today's Date]  

## Overview  
This project aims to create an open, collaborative repository of Olympiad-level number theory problems, structured to facilitate problem-based learning. The system will:  
- Organize problems by topic, difficulty, and technique  
- Support multilingual content (primarily English and Farsi)  
- Enable incremental contributions from educators and students  
- Preserve knowledge beyond individual contributors' involvement  

## Background & Motivation  
Teaching Olympiad number theory effectively requires curated problem sets that balance pedagogical value with appropriate difficulty. Past attempts to create such resources faced recurring challenges:  

1. **Sustainability Issues**  
   - *2019-2020*: Authored chapter-based course materials during COVID, but progression stalled due to excessive problem difficulty  
   - *Project 51*: Collaborative .tex file exchange with another instructor was abandoned  
   - *Telegram Groups*: Hashtag-based problem sharing among instructors lacked structure  

2. **Systemic Challenges**  
   - Contributor turnover (typical teaching tenure in Iran: 1-3 years)  
   - Over-reliance on transient platforms (Telegram channels averaging 2-year lifespans)  
   - Lack of cumulative progress across initiatives  

This project addresses these through:  
- Git-based version control for content preservation  
- Modular content design allowing granular contributions  
- Automated translation workflows for Farsi/English content  

## Requirements  

### Core Objectives  
- **Accessible Contribution Model**  
  - Support micro-contributions (single problems, solution sketches, translations)  
  - Clear contribution guidelines for non-technical users  

- **Immediate Student Utility**  
  - Self-contained problem sets with difficulty indicators  
  - Progressive learning paths (foundational → advanced techniques)  

- **Project Longevity**  
  - Decentralized maintenance model  
  - Automated quality checks (problem tagging, solution verification)  

### Content Scope  
| Content Type          | Description                          | Priority |
|-----------------------|--------------------------------------|----------|
| Practice Problem Sets | Curated sequences with solutions     | P0       |
| Technique Primers     | Example-driven method explanations   | P1       |
| Topic Roadmaps        | Learning progression recommendations | P2       |
