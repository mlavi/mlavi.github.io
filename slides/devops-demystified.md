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
 - The Journey to DevOps
     - Agile Infrastructure in the Cloud
     - Infrastructure as Code
     - Pets versus Cattle versus Bacteria
     - Test, Build, Deploy Pattern
     - Infrastructure Orchestration and Models
 - Epilogue: BusinessOps
     - We are all DevOps: your call to action!
---
# Mark Lavi

$ cat ~/.signature

DevOps and Automation Architect, Nutanix || [mark.lavi@nutanix.com](mailto:mark.lavi@nutanix.com)
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
## What is DevOps?

A culturally rendered term, but Mark's time tested definition follows:

<h1 align="center">DevOps is the <em>process</em> of removing all friction
<br />between the developer and customer value.</h1>

DevOps has many implications (values, tools, and practices) and it is
dynamically bound to the capabilities of the people who practice it,
therefore it will vary by organization.

- Illustration: [DevOps Automation Diagram](http://mlavi.github.io/post/devops-automation/)
- Rumination: [I Dream of DevOps, but What is DevOps?](https://calm.io/2015/09/23/i-dream-of-devops-but-what-is-devops/)

---
## Beware of DevOps Hype and Abuse!

<h1 align="center">DevOps is the <em>process</em> of removing all friction
<br />between the developer and customer value.</h1>

Ask yourself: *Does this [thing] meet our definition of DevOps?*

- Rumination: [Why is DevOps So Hard?](https://calm.io/2015/10/20/why-is-devops-so-hard/)

---
## A Brief History of DevOps

- 2008: "Agile Infrastructure" non-discussion at Agile Conference
    - Patrick Debois finds Andrew Clay Shafer, they create:
        - [Agile System Administration](https://groups.google.com/forum/#!forum/agile-system-administration) Google Group: virtual community
- 2009:
    - May: "10+ Deploys Per Day: Dev & Ops Cooperation at Flickr" [Video](https://www.youtube.com/watch?v=LdOe18KhtT4) [Slides](http://www.slideshare.net/jallspaw/10-deploys-per-day-dev-and-ops-cooperation-at-flickr)
 by John Allspaw and Paul Hammond at Velocity Conference
    - October: [DevOpsDays Belgium](http://devopsdays.org): physical community begins

---
## A Brief History of DevOps (continued)

- 2013: [The Phoenix Project](https://en.wikipedia.org/wiki/The_Phoenix_Project:_A_Novel_About_IT,_DevOps,_and_Helping_Your_Business_Win)
  book by Gene Kim, Kevin Behr, George Spafford
- Today: a mysterious movement, buzzword, and a dynamic community!
    - Industry studies showing DevOps enables business agility, lower MTTF
    - "Rediscovery" of lean processes, [Agile Manifesto](http://www.agilemanifesto.org/), etc.

References:

- [The History Of DevOps](http://itrevolution.com/the-history-of-devops/) by Damon Edwards
- [DevOps: A History](https://www.youtube.com/watch?v=IIkbn2V5A40) by Nell Shamrell-Harrington
---
# How to Journey to DevOps?

- We are all DevOps: ongoing impact to engineering organizations
- Break down silos that impede holistic solutions and change
    - Dev + Ops; not developers vs. QA vs. operations
    - Fail fast, fix fast

---
# How to Journey to DevOps? (continued)

- Relentless iteration and automation to achieve goals:
    - *Continuous Delivery* = multiple production deploys per day,
      <br/>tied to continuous integration and integration stack testing
    - Continuous Feedback = closed loop operations
        - DevOps is a bi-directional process for customers: internal and external
        - What is the health of our application, APIs, key performance metrics?
    - Developers evolve into service engineers

---
# The Journey to DevOps: Overview
 - Agile Infrastructure in the Cloud
 - Infrastructure as Code
 - Pets versus Cattle versus Bacteria
 - Test, Build, Deploy Pattern
 - Infrastructure Orchestration and Models 

---
## Agile Infrastructure in the Cloud

- All services, platforms, & tools are evolving
    - RESTful APIs are everywhere
    - Opportunity to codify and automate everything
    - ...on private, public or hybrid cloud architectures
- Domain expertise democratized, repeatable, and auditable
- Ephemeral everything = agility

---
## Infrastructure as Code 

*Infrastructure as Code* = software engineering practices applied to infrastructure.

- Version everything: even the database
- *Configuration Management*
    - Deploy all the things!
- Ephemeral stacks and environments
    - Test all the things!
    - Challenge: full stack orchestration

---
## Infrastructure as Code (continued)

- *Immutable Infrastructure* on the rise (cattle)
    - Dynamic versus static configuration, feature flags
    - Bespoke, hand-crafted, snowflake servers = dark magick = friction
    - Automation friction = technical debt = a bug
- Application expertise democratized, repeatable, and auditable

---
## The Future of *Infrastructure as Code*

- Combining software engineering with operations should lead to my dream...
- *Operations as Code* via behavior and test driven operations.
    - I am searching for others to discuss this topic!

---
## Pets versus Cattle

## Immutable Infrastructure

- Cloud agility enables ephemeral fleets
    - *Pet* = uptime of years, named, backup maintenence
    - *Cattle* = numbered, can fail and reprovision anytime
- Build time infrastructure artifacts = build system + configuration management
- Ideal for non-persistant tiers:
    - Simplify deployment: ship logs, metrics, etc. off the "box"
    - Roll 'em in and out of the load balancer, measure twice!

Reference: [Discussion on attribution of Pets v. Cattle](https://news.ycombinator.com/item?id=7311704)

---
## Pets vs. Cattle: Sidebar

## Microservices

- When monolithic, long-lived infrastructure decomposes, so goes the application...
- Refactor and decompose the monolith into public API modules (REST),
  which enables independent, continuous:
    - delivery = build and deploy
    - testing and monitoring
    - (per component, team, feature, etc.)
- API version management and feature lightness topics

---
## Pets vs. Cattle vs. Bacteria (continued)

## Containers

- Agile, lightweight, smaller, faster VMs:
    - ideal approach for *continuous delivery* of *immutable infrastructure* artifacts, especially microservices
    - minimal difference between laptop and production
    - *Bacteria*<sup>1</sup> = lifecycle on the order of seconds: build, run, test, destroy
- Early days: Docker as a tool versus Docker tool set as a platform
    - PERL motto = [There is more than one way to do it](http://en.wikipedia.org/wiki/There%27s_more_than_one_way_to_do_it).
- Production challenges remain: orchestration, health, networking, persistence, dynamic configuration

<sup>1</sup> Bacteria is the term I learned from [Tori Wieldt](https://blog.newrelic.com/author/toriwieldt/), New Relic Developer Advocate,
I think it is better than the term insect.

---
## Test, Build, Deploy Pattern

Between development and production:

 - the differences should be minimized
 - troubleshooting should be no different.

Therefore, development environments *SHOULD EVOLVE* from fully mocked
 systems to fully integrated application environments, leading to:

---
## Test, Build, Deploy Pattern (continued)

- __Test__ on your laptop
    - Develop to satisfy your testable code
- __Build__ on your laptop
- __Deploy__ on your laptop
    - Make code configurable with tools
    - Repeat for integration, metrics, logs, etc.
    - Commit to repository -> continuous integration & delivery

Reference: [BTD Pattern Blog Entry](http://mlavi.github.io/post/devops-btd-pattern/)

---
## Infrastructure Orchestration

- Orchestration of the entire distributed system/stack/environment
    - Application management lifecycle: all dependencies and operations
- Continuous Deployment + Upgrades:
    - Blue-Green (Red-Black): parallel population, atomic cutover
    - Rolling vs. canary: incremental cutover
    - Test and measure your operations
         - Close the loop to Continuous Delivery

---
## Infrastructure Models

- Local versus Global Redundancy
    - Load balance everything
    - Clustered everything
- Automate runbooks = *operations as code*
    - ChatOps = democratized operations are agile ops

---
# Epilogue: BusinessOps

- DevOps escapes the engineering domain
- Apply DevOps to business customers, systems, and processes
- Business agility: everything is ripe for automation!
    - Compliance and Security

---
# Thank You, Questions?

<h1 align="center">DevOps is the <em>process</em> of removing all friction
<br />between the developer and customer value.</h1>

$ cat ~/.signature

DevOps and Automation Architect, Nutanix || [mark.lavi@nutanix.com](mailto:mark.lavi@nutanix.com)
<br />mobile:+1-650-400-2100 || Twitter [@calm_mark](http://twitter.com/calm_mark) || GitHub [@mlavi](http://github.com/mlavi/)

##Your Next Steps

- Find your local DevOps community and join us!
- Evangelize: sildes on my *Infrastructure as Code* blog =
  [http://mlavi.github.io/post/devops_demystified/](http://mlavi.github.io/post/devops_demystified/)
