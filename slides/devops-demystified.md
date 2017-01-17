# Demystifying DevOps

## Overview

A brief history of the DevOps movement and community with a cross section view
 of methods and practices that break down the barriers to
 business agility and continuous delivery of applications.

For a term less than eight years old,
 DevOps remains a mysterious pursuit for many software engineering organizations.

DevOps seems intangible: you can't buy it, there is no certification, and no
 universal definition, yet everyone who wants it or does it has trouble identifying it.

We will cover these topics so that
 you can understand and chart your own journey to DevOps.

---
## Agenda

- A Definition and Cultural Rendering of DevOps
    - A Brief History of DevOps
    - DevOps Success, Challenges, and the Journey
- The Technical Journey to DevOps
    - Agile Infrastructure and Infrastructure as Code
        - Microservices
        - Pets versus Cattle versus Bacteria
        - Test, Build, Deploy Pattern
    - Infrastructure Orchestration and Models
- Epilogue: BusinessOps
    - We are all DevOps: your call to action!

---
# Mark Lavi

Currently:

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

A culturally rendered term, but Mark's time tested definition<sup>1</sup> follows:

<h1 align="center">DevOps is the <em>process</em> of removing all friction
<br />between the developer and customer value.</h1>

DevOps has many implications (values, tools, and practices) and it is
dynamically bound to the capabilities of the people who practice it,
therefore it can vary person by person on the same team.

It is a bi-directional process and concerns all internal and external customers.
e.g.: DevOps for yourself on your laptop.

- Illustration: [DevOps Automation Diagram](http://mlavi.github.io/post/devops-automation/)
- Blog: [I Dream of DevOps, but What is DevOps?](https://calm.io/2015/09/23/i-dream-of-devops-but-what-is-devops/)

<sup>1</sup>[Portmanteau](https://en.wiktionary.org/wiki/portmanteau#Etymology_2): two or more terms combined; a hybrid or mash-up

---
## Beware of DevOps Hype and Abuse!

<h1 align="center">DevOps is the <em>process</em> of removing all friction
<br />between the developer and customer value.</h1>

Ask yourself: *Does [this thing] meet our definition of DevOps?*

Use your definition as a lens to evaluate any use of the term!

- Blog: [Why is DevOps So Hard?](https://calm.io/2015/10/20/why-is-devops-so-hard/)

---
## A Brief History of DevOps<sup>2</sup>

2009:

- February: [Agile System Administration](https://groups.google.com/forum/#!forum/agile-system-administration) Google Group = virtual community begins
- May: Velocity conference in San Jose, CA:
    - "Agile Infrastructure" [Slides](http://www.slideshare.net/littleidea/agile-infrastructure-velocity-09)
    by Andrew Clay Shafer
    - "10+ Deploys Per Day: Dev & Ops Cooperation at Flickr" [Video](https://www.youtube.com/watch?v=LdOe18KhtT4) [Slides](http://www.slideshare.net/jallspaw/10-deploys-per-day-dev-and-ops-cooperation-at-flickr)
    by John Allspaw and Paul Hammond
- August: Agile 2009 conference in Chicago
    - [Patrick Debois](https://groups.google.com/forum/#!topic/agile-system-administration/HKCTSee2u4w) rejected talks leads him to find Andrew Clay Shafer.
    <br />Discussion ensues and the term DevOps is born!
- October: [DevOpsDays Belgium](https://groups.google.com/forum/#!topic/agile-system-administration/hp7WBg4uCJI) = physical community begins

<sup>2</sup>
[The History Of DevOps](http://itrevolution.com/the-history-of-devops/) by Damon Edwards,
<br />&nbsp;&nbsp;&nbsp;[DevOps: A History](https://www.youtube.com/watch?v=IIkbn2V5A40) by Nell Shamrell-Harrington

---
## A Brief History of DevOps (continued)

- 2013: [The Phoenix Project](https://en.wikipedia.org/wiki/The_Phoenix_Project:_A_Novel_About_IT,_DevOps,_and_Helping_Your_Business_Win)
  book by Gene Kim, Kevin Behr, George Spafford
    - A parable that illustrates the business impact of DevOps on a traditional manufacturer
- 2014: Annnual [State of DevOps Report](https://devops-research.com/research.html) begins
    - "...high-performing IT organizations are twice as likely to exceed their profitability, market share and productivity goals,
       and that high performers achieved higher levels of both throughput and stability."

---
## A Brief History of DevOps (continued)

- 2016: [Measuring DevOps ROI](https://devops.com/iterative-indicators-measuring-devops-roi/)
    - 200X deploy applications more frequently than slow performers
    - 2,555X faster lead times
    - 24X faster recovery times
    - 3X lower change failure rates
    - 4600: survey participants
- Today: a growing mysterious world-wide movement, buzzword, and dynamic community
    - "Rediscovery" of lean processes, [Agile Manifesto](http://www.agilemanifesto.org/), etc.
    - Software discipline applied to refactoring infrastructure and operations
    - Application architectures refactor around operations
    - Manufacturing theory applied to technical work
      
---
## DevOps Success and Challenges

### Success
Technology + Culture transformation for business agility<sup>3</sup>

### Challenges

- Fragmentation: ecosystem involves multiple tools and platforms, fragile integrations
- People: DevOps superstars bridge gaps, but hiring is difficult, expensive, and unscalable

<sup>3</sup> Blog: [Why is DevOps so Hard?](https://calm.io/2015/10/20/why-is-devops-so-hard/)
<br />&nbsp;&nbsp;&nbsp;Manufacturing Analog: [Toyota Production System](https://en.wikipedia.org/wiki/Toyota_Production_System)

---
## The Journey to DevOps

**We are all DevOps:** continual evolution for organizations

- Cultural change to reduce silos between Developer + Test + Operations
    - Dev + Ops; not developers vs. test/QA vs. operations
    - e.g.: ship a new feature by the end of the quarter to satisfy PR and marketing campaigns
- Iteration and automation yielding:
    - Distributed Work: domain expertise democratized, repeatable, and auditable
        - Continuous integration, continuous delivery, continuous deployment
    - Agility: everything is ephemeral; no single point of failure
        - Fail fast, fix fast = antifragile attitude, minimize risk, increase flow

---
## The Journey to DevOps (continued)

- Closed loop feedback for health and value measurements<sup>4</sup>
  <br />= monitors + logs + metrics for KPIs: Key Performance Indicators
    - Systems yeild domain KPIs which should roll up to business KPMs
    - Continuous Feedback = closed loop operations
        - What is the health of our application, APIs, key performance metrics?
        - Are we increasing the velocity and value in our pipelines?
- All become developers and evolve into service engineers

<sup>4</sup>[Proverb](https://athinkingperson.com/2012/12/02/who-said-what-gets-measured-gets-managed/):
"What is measured improves."

---
# Technical Journey to DevOps: Overview

- Agile Infrastructure
- Infrastructure as Code
    - Immutable Infrastructure
    - Microservices
    - Pets versus Cattle versus Bacteria
- Test, Build, Deploy Pattern
- Infrastructure Orchestration and Models 

---
## Agile Infrastructure

- All services, platforms, and tools are evolving
    - RESTful APIs are everywhere
    - Opportunity to codify and automate everything
    - ...on private, public or hybrid cloud architectures and bare-metal
- Domain expertise democratized, repeatable, and auditable
- Ephemeral everything = agility

---
## Infrastructure as Code 

*Infrastructure as Code* = software engineering practices applied to infrastructure

- Version everything: even the database<sup>5</sup>
- *Configuration Management*<sup>6</sup>
    - Deploy all the things!
    - Build + configure at run-time
- Ephemeral stacks and environments
    - Test all the things!
    - Challenge: full stack orchestration

<sup>5</sup> Blog: [Database Change Management](http://mlavi.github.io/post/database_change_management/)
<br /><sup>6</sup> [Software Configuration Management Systems](https://en.wikipedia.org/wiki/Continuous_configuration_automation) such as Puppet, Chef, Salt, Ansible, Juju, CFengine, etc.

---
## Infrastructure as Code (continued)

- *Immutable Infrastructure* on the rise (cattle)
    - Dynamic versus static configuration, feature flags
    - Bespoke, hand-crafted, snowflake servers = dark magick = friction
    - Automation friction = technical debt = a bug
- Application expertise democratized, repeatable, and auditable
- *Operations as Code* via behavior and test driven operations
    - I am searching for others to discuss this topic!

---
## Immutable Infrastructure

- Think of a system that has only:
    - a read-only filesystem
    - environment variables for dynamic, runtime configuration
- Infrastructure artifacts = build system + configuration management at build time
    - Infrastructure is built and placed in a repository for distribution
- Ideal for non-persistent application tiers:
    - Simplify deployment: ship logs, metrics, etc. off the "box"
    - Roll 'em in and out of the load balancer, measure twice!
    - Industry is addressing persistence, but cloud native apps are also a solution
- Closes the risk and gap between development and production

---
## Microservices

When monolithic, long-lived infrastructure decomposes, so withers the application architecture.

Refactoring and decomposing the application monolithic codebase into modules,
each with a public API (REST), enables independent, continuous:

- delivery = build and deploy
- testing and monitoring

per component, team, feature, etc.

Reference: [Amazon REST API manifesto](https://apievangelist.com/2012/01/12/the-secret-to-amazons-success-internal-apis/)

---
## Pets versus Cattle<sup>7</sup>

- Cloud agility enables ephemeral fleets
    - *Pet* = uptime of years, named, backup maintenence
    - *Cattle* = numbered, can fail and reprovision anytime
    - SGI example: 12 years uptime on IRIX! Yesterday's success = today's failure

This is a lens to evaluate infrastructure and ops; evolve to fleet management + app first design

<sup>7</sup> [Discussion on attribution of Pets versus Cattle](https://news.ycombinator.com/item?id=7311704)

---
## Pets vs. Cattle vs. Bacteria (continued)

## Containers

- Agile, lightweight, smaller, faster VMs:
    - ideal approach for *continuous delivery* of *immutable infrastructure* artifacts, especially microservices
    - minimal difference between laptop and production, millisecond activation
    - *Bacteria*<sup>8</sup> = lifecycle on the order of seconds: build, run, test, destroy
- Early days: Docker as a tool versus Docker as a platform
    - PERL motto = [There is more than one way to do it](http://en.wikipedia.org/wiki/There%27s_more_than_one_way_to_do_it).
- Production challenges remain: orchestration, health, networking, persistence, dynamic configuration
  -- many issues solved by adopting a container PaaS with limited flexibility

<sup>8</sup> Bacteria is the term I learned from [Tori Wieldt](https://blog.newrelic.com/author/toriwieldt/), New Relic Developer Advocate,
seems better than "insect" which also is in use.

---
## Test, Build, Deploy Pattern

Between development and production:

 - the differences should be minimized<sup>9</sup>
 - troubleshooting output and tools should be no different.

Therefore, development environments *SHOULD EVOLVE* from fully mocked
 systems to fully integrated application environments, leading to:

<sup>9</sup> See **Immutable Infrastructure**

---
## Test, Build, Deploy Pattern (continued)

- Create a minimum viable product test and mock your code
- Begin TDD: red, green, refactor

i.e.:

- __Test__ on your laptop
    - Develop tests to satisfy your testable code
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
    - Rolling vs. canary: incremental cutover with testing
    - Test and measure your operations
         - Close the loop to Continuous Delivery
- New disciplines and opportunities:
    - API version management
    - Dynamic feature roll out: Feature flags/lightness, aka "Death to Staging"
    - RuggedDevOps and SecDevOps, NetDevOps

---
## Infrastructure Models

- Local versus Global Redundancy
    - Load balance everything in a local context
    - Distributed, clustered workload schedulers
    - Global load balancing of clusters
- Automate runbooks and change controls = *operations as code*
    - ChatOps = democratized operations are agile ops

---
# Epilogue: BusinessOps

- DevOps escapes the technology domain
- Apply DevOps to business customers, systems, and processes
- Business agility: everything is ripe for automation!
    - Compliance<sup>10</sup> and Security

<sup>10</sup> [Compliance at Velocity](http://pages.chef.io/rs/255-VFB-268/images/compliance-at-velocity2015.pdf)

---
# Thank You, Questions?

<h1 align="center">DevOps is the <em>process</em> of removing all friction
<br />between the developer and customer value.</h1>

$ cat ~/.signature

DevOps and Automation Architect, Nutanix || [mark.lavi@nutanix.com](mailto:mark.lavi@nutanix.com)
<br />mobile:+1-650-400-2100 || Twitter [@calm_mark](http://twitter.com/calm_mark) || GitHub [@mlavi](http://github.com/mlavi/)

##We are All DevOps: Your Next Steps

- **Find:** your local DevOps community and join us!
    - [DevOpsDays.org](http://www.devopsdays.org), [MeetUp](https://www.meetup.com/find/devops/), and [devopsconferences.com](http://devopsconferences.com/?past)
- **Evangelize:** sildes on my *Infrastructure as Code* blog =
  [http://mlavi.github.io/post/devops_demystified/](http://mlavi.github.io/post/devops_demystified/)
