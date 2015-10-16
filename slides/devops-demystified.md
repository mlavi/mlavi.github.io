# Demystifying DevOps

## Overview

A brief history of the DevOps movement and community with a cross section view
 of many methods and practices that are breaking down the barriers to achieve
 agility and continuous delivery.

For a term that is not even six years old, DevOps remains a mysterious pursuit
 for many software engineering organizations.

DevOps seems intangible: you can't buy it, there is no certification, and frankly,
 there is no universal definition, yet everyone wants it or already "does" it,
 but still has trouble identifying it.

We will cover the following topics so that you can understand and chart your own
 journey to DevOps.

---
## Agenda

 - A Definition and Cultural Rendering of DevOps
 - A Brief History of DevOps
 - DevOps Impact on Organizations
 - The Journey to DevOps via:
     - Cloud Agility
     - Infrastructure as Code
     - Test, Build, Deploy Pattern
     - Pets versus Cattle versus Bacteria
     - Infrastructure Models and Orchestration
 - Epilogue: BusinessOps

---
# Mark Lavi

$ cat ~/.signature

Technology Evangelist, Calm.io || [mark@calm.io](mailto:mark@calm.io)
<br />A Sequoia Capital funded company: [team@calm.io](mailto:team@calm.io)
<br />mobile:+1-650-400-2100 || Twitter [@calm_mark](http://twitter.com/calm_mark) || GitHub [@mlavi](http://github.com/mlavi/)

$ cat ~/.profile || curl [http://mlavi.github.io/about/](http://mlavi.github.io/about/)

Previously:

- DevOps Lead at [Pertino](http://pertino.com) (Cloud VPN provider)
- Operations at [Kaazing](http://kaazing.com) (HTML5 WebSocket pioneer)
- Webmaster at Netscape.com, cnnfn.com, Silicon Graphics
    - Technology Evangelist for LDAP and JavaScript

*Infrastructure as Code* blog = [http://mlavi.github.io](http://mlavi.github.io)

---
# DevOps

---
# What is DevOps?

A culturally rendered term, but Mark's time tested definition follows:

<h1 align="center">DevOps is the <em>process</em> of removing all friction
<br />between the developer and customer value.</h1>

DevOps has many implications: values, people, tools, and practices.

- Illustration: [DevOps Automation Diagram](http://mlavi.github.io/post/devops-automation/)
- Rumination: [I Dream of DevOps, but What is DevOps?](https://calm.io/2015/09/23/i-dream-of-devops-but-what-is-devops/)

---
# Beware of DevOps Hype and Abuse!

<h1 align="center">DevOps is the <em>process</em> of removing all friction
<br />between the developer and customer value.</h1>

Ask yourself: *Does this [thing] meet our definition of DevOps?*

---
# A Brief History of DevOps

- 2008: "Agile Infrastructure" non-discussion at Agile Conference
    - Patrick Debois finds Andrew Clay Shafer, they create:
        - [Agile System Administration](https://groups.google.com/forum/#!forum/agile-system-administration) Google Group: virtual community
- 2009:
    - May: [10+ Deploys Per Day: Dev & Ops Cooperation at Flickr](http://www.slideshare.net/jallspaw/10-deploys-per-day-dev-and-ops-cooperation-at-flickr)
 by John Allspaw and Paul Hammond at Velocity Conference
    - October: [DevOpsDays Belgium](http://devopsdays.org): physical community begins
- 2013: [The Phoenix Project](https://en.wikipedia.org/wiki/The_Phoenix_Project:_A_Novel_About_IT,_DevOps,_and_Helping_Your_Business_Win) book by Gene Kim, Kevin Behr, George Spafford
- Today: a mysterious movement, buzzword, a dynamic community!
    - Industry studies showing DevOps enables business agility
    - "Rediscovery" of lean processes, [Agile Manifesto](http://www.agilemanifesto.org/), etc.

Reference: [The History Of DevOps](http://itrevolution.com/the-history-of-devops/) by Damon Edwards

---
# How to Journey to DevOps?

- We are all DevOps: ongoing impact to engineering organizations
- Break down silos that impede holistic solutions and change
    - Dev + Ops; not developers vs. QA vs. operations
    - Fail fast, fix fast
- Relentless iteration and automation to achieve goals:
    - *Continuous Delivery* = multiple production deploys per day,
      <br/>tied to continuous integration and integration stack testing
    - Continuous Feedback = closed loop operations
        - DevOps is a bi-directional process for customers: internal and external
        - What is the health of our application, APIs, key performance metrics?
    - Developers evolve into service engineers

---
# Cloud Agility

- All services, platforms, & tools are evolving
    - RESTful APIs are everywhere
    - Opportunity to codify and automate everything:
        - on private, public or hybrid cloud architectures
- Domain expertise democratized, repeatable, and auditable
- Ephemeral everything = agility

---
# Infrastructure as Code 

Software engineering practices applied to infrastructure:

- Version everything: even the database
- *Configuration Management*
    - Automate all the things!
- Ephemeral stacks and environments
    - Test all the things!
    - Challenge: full stack orchestration
- *Immutable Infrastructure* on the rise
    - Dynamic versus static configuration, feature flags
    - Bespoke, hand-crafted, snowflake servers == dark magick == friction
    - Automation friction == technical debt == a bug

---
# The Future of *Infrastructure as Code* 

- My dream: behavior and test driven operations
    - I am searching for others to discuss this topic!

---

# Test, Build, Deploy Pattern

Between your laptop and production:

 - the differences should be minimized
 - troubleshooting should be no different.

Therefore, your development laptop = a full system stack/environment:

- Test on your laptop
    - Develop to satisfy your testable code
- Build on your laptop
- Deploy on your laptop
    - Make code configurable with tools
    - Repeat for integration, metrics, logs, etc.
    - Commit to repository -> continuous integration & delivery

Reference: [BTD Pattern Blog Entry](http://mlavi.github.io/post/devops-btd-pattern/)

---
# Infrastructure Models
# Infrastructure Orchestration

- Complex orchestation of the entire distributed system/stack/environment
    - Load balance everything
    - Clustered everything
- Automate runbooks: operations as code
- Blue-Green vs. canary vs. rolling deployments and upgrades
    - Test and measure your operations
- Agile Ops: ChatOps = democratized operations

---
# Pets versus Cattle

##Immutable Infrastructure:

- Cloud agility enables ephemeral fleets
    - *Cattle* = numbered, can fail and reprovision anytime
    - *Pet* = uptime of years, named, backup maintenence
- Build time artifacts (think Jenkins+Configuration Management)
- Ideal for non-persistant tiers:
    - Simplify deployment: ship logs, metrics, etc. off the "box"
    - Roll 'em in and out of the load balancer, measure twice!

---
# Pets versus Cattle versus Bacteria

##Microservices:

- Refactor the monolith into public API modules (REST), which enables
  independent delivery, monitoring, and testing (per team).

##Containers can represent:

- Agile, lightweight, faster VMs:
    - an ideal approach for *continuous delivery* of *immutable infrastructure* artifacts
    - *Bacteria* = Short lived on the order of seconds: build, run, test, destroy
- Early days: Docker as a tool versus Docker tool set as a platform
    - [PERL motto](http://en.wikipedia.org/wiki/There%27s_more_than_one_way_to_do_it):
  "There is more than one way to do it."
- Production challenges remain: deployment, monitoring, metrics, logs, networking, persistence

---
# Epilogue: BusinessOps

- DevOps escapes the engineering domain
- Apply DevOps to business customers, systems, and processes
- Business agility: everything is ripe for automation!

---
# Thank You, Questions?

<h1 align="center">DevOps is the <em>process</em> of removing all friction
<br />between the developer and customer value.</h1>

$ cat ~/.signature

Technology Evangelist, Calm.io || [mark@calm.io](mailto:mark@calm.io)
<br />A Sequoia Capital funded company: [team@calm.io](mailto:team@calm.io)
<br />mobile:+1-650-400-2100 || Twitter [@calm_mark](http://twitter.com/calm_mark) || GitHub [@mlavi](http://github.com/mlavi/)

##Your Next Steps

- Find your local DevOps community and join us!
- Sildes on my *Infrastructure as Code* blog = [http://mlavi.github.io/post/devops_demystified/](http://mlavi.github.io/post/devops_demystified/)
