# Mark Lavi

$ cat .signature

Technology Evangelist, Calm.io || [mark@calm.io](mailto:mark@calm.io)
<br />A Sequoia Capital funded company: [team@calm.io](mailto:team@calm.io)
<br />mobile:+1-650-400-2100 || Twitter [@calm_mark](http://twitter.com/calm_mark) || GitHub [@mlavi](http://github.com/mlavi/)

$ cat .profile || curl [http://mlavi.github.io/about/](http://mlavi.github.io/about/)

Previously:

- DevOps Lead at [Pertino](http://pertino.com) (Cloud VPN provider)
- Operations at [Kaazing](http://kaazing.com) (HTML5 WebSocket pioneer)
- Webmaster at Netscape.com, cnnfn.com, Silicon Graphics
    - Technology Evangelist for LDAP and JavaScript

Infrastructure as Code blog = [http://mlavi.github.io](http://mlavi.github.io)

---
# DevOps

---
# What is DevOps?

- A culturally rendered term, but Mark's time tested definition follows:
- #DevOps is the *process* of reducing friction between a developer's mind and delivering that value to the customer.#
- DevOps has many implications: values, people, tools, and practices.

Illustration: [DevOps Automation Diagram](http://mlavi.github.io/post/devops-automation/)

---
# How to journey to DevOps?

- Break down silos that impede holistic solutions and change.
    - Dev+Ops, not developers vs. QA vs. operations
    - Fail fast, fix fast
- Relentless iteration and automation to achieve goals:
    - *Continuous Delivery:* multiple production deploys/day
    - Continuous Feedback = close loop Ops
        - DevOps is a bi-directional process for customers: internal and external
        - What is the health of our application, APIs, key performance metrics?
    - Developers evolve into service engineers

---
# Infrastructure as Code 

Software engineering practices applied to infrastructure:

- Version everything: even the database
- *Configuration Management*
    - Automate all the things!
- Ephemeral stacks and environments
    - Test all the things!
    - Challenge: full stack orchestration
- *Immutable Infrastructure*
    - Pets versus Cattle 
    - Bespoke, hand-crafted, snowflake servers == dark magick == friction
    - Automation friction == technical debt == a bug

---
# Infrastructure as Code 

- My dream: behavior and test driven operations
    - I am searching for others to discuss this topic!

---
# [Calm](http://calm.io) = DevOps Automation Platform

- Control your hybrid clouds and containers:
    - AWS EC2, PXE, KVM, VMware vCenter, OpenStack, Docker, XenServer
- Overlay and integrate your systems:
    - *Configuration Management:* Chef, Puppet, Salt
    - Jenkins, git, Nagios, etc.: anything with an API or (power)shell access
- Architectural blueprints define resources, orchestration, and operations:
    - RBAC, approvals, notifications, and financial budget controls.
    - Push button, ephemeral stacks
    - Continuous delivery for cattle or pets
    - Close loop operations
- A picture is worth a thousand words, let me know if you'd like a T-shirt or sticker!

---
# Container Thought Experiments

Containers represent:

* An ideal approach for *continuous delivery* of *immutable infrastructure* artifacts
* Production challenges remain: deployment, monitoring, metrics, logs, networking, persistence
* Early days: Docker as a tool versus Docker tool set as a platform
* [PERL motto](http://en.wikipedia.org/wiki/There%27s_more_than_one_way_to_do_it):
  "There is more than one way to do it."

## How do we take advantage of containers properly?
---
# "Heavy Containers"

        $ grep -e FROM -e RUN Dockerfile
        FROM ubuntu:14.04.2
        RUN apt-get update && apt-get install -y apache2 php5

## Criticisms:

- Full operating system (OS)
- Configuration management by shell
- No difference from a Virtual Machine

## Proposed Solution:

- Refactor into composable container layers
- Leverage minimalist OS
- Reuse *configuration management*

---
# Full Stack Components 
* application:
    * code
    * code libraries and frameworks
    * static application configuration data
* run time facilities:
    * language run time binaries
    * language run time configuration
    * language run time dependencies
* server facility:
    * server binaries
    * server configuration
    * server run time configuration
    * server start up customization
    * server plug-ins
    * server plug-in dependencies
---
# Container Refactoring

Each container built independently:

* docker build -t server/facility
    * FROM minimalist/OS
    * RUN puppet-agent apply
* docker build -t operations/facilities
    * FROM minimalist/OS
    * RUN chef-solo -c ~/solo.rb -j ~/node.json
* packer build -var 'image-tag=application/microserviceX' build.json
    * build.json:
{
  "builders": [
    { "type": "docker",
      "image": "{{image-tag}}",
      "commit": true
    }
  ],
  "provisioners": [
    { "type": "ansible-local" }
  ],
  "post-processors": [
    { "type": "docker-tag" }
  ]
}

---
# Compose Layers

* FROM server/facility
* FROM server/runtime
* FROM operations/facilities
* FROM developer/tools
* FROM application/microserviceX

---
# Container Refactor Benefits
* Each container layer can be maintained by a different team
* Each built on a different cadence and cacheable
* Composed together into a deployable artifact
* Enables *continuous delivery* of *immutable infrastructure* artifacts
    * Shift from configuration management at deploy-time (run time)
      to build time
* Reuse your *Configuration Management* for other cases

---
# Container Deployment

Job Schedulers, Tools, and Services:

* Cloud hosting provider tools: AWS EC2
* [Apache Mesos](http://mesos.apache.org/)
* [Google Kubernetes](http://kubernetes.io/)
* [Tectonic](https://tectonic.com/) = CoreOS + Kubernetes
* [Docker Swarm](https://github.com/docker/swarm)
* [Terraform](http://terraform.io)
* [Calm](http://calm.io) (beta)

---
# Container Challenges

* Dynamic updates to load balancer, DNS, monitoring,
and service discovery and configuration management systems
* Architectures which are not immutable, e.g:
    * Code or API versions which cannot coexist, preventing rolling blue-green deployments and rollbacks.

---
# Thank You, Questions?

* [mark@calm.io](mailto:mark@calm.io)
    * Full Blog Entry = [http://mlavi.github.io/post/container-infrastructure-strategy/](http://mlavi.github.io/post/container-infrastructure-strategy/)
* Resources for this talk:
    * James Russell, DevOps engineer at Sony Computer Entertainment America, DevNet Team [CoreOS Meetup Presentation](https://www.youtube.com/watch?v=M9hBsRUeRdg)
    * [Getting Weird with Containers](https://www.youtube.com/watch?v=gMpldbcMHuI)
      a.k.a. "Exploring Strategies for Minimal Containerization" by Brian Harrington,
      Principal Architect at CoreOS
    * Kevin Clarke's Code4Lib 2015 presentation on [Packer](http://www.kevinclarke.info/slides/c4l15/)
