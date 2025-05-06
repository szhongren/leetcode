# repo of leetcode solutions in Python.

problem descriptions in the source files

some questions have been started but not completed

1. secrets encryption
   - ASM vs KMS
   - interface (java annotation + middleware)
   - tests: check for proper usage of annotations
   - 2 parts: how to encrypt and how to rotate keys due to time
   - backwards compatibility with multiple nodes and multiple versions
   - outcome/impact was not great
2. integrations \*\*\*
   - schema
     - specialize or generalize? first question
     - generalized idea of a server, and UI vs API server (investigated tableau, power BI, looker)
     - abstract parent entity so we could build other types of integrations
     - client interface for actually doing the integration specific stuff
   - async workflow, lot of queues behind endpoints, and workers that call sync endpoints
     - importantly, most of this was generalized. integration specific details (auth, indexing, building entities) were all in the integration specific client that implemented the interface
   - impact
     - other integrations were able to be built quickly, 4 weeks to build the framework, <1 week to build DBT/Power BI integration
     - repurposed the same code for integrating with an acquisition
     - unlocked a new customer base and set of users, before it was more data teams, now includes business/less technical users
3. lineage \*\*\*
   - schema
     - key idea, nodes should be abstract enough to point to anything
     - nodes are a seperate layer above the actual entities
     - performance (need to get metadata for actual entities nodes pointed to), so cached metadata in the node itself (unlikely to change)
     - graph DB vs SQL DB, came down to cost and time to implement
     - tradeoff: fast MVP, with vague idea to move to graph DB later
   - can add custom nodes (for testing and potentially other things we didn't support yet)
   - impact
     - easy move to column level lineage after acquisition of DAG
     - increased customer base
     - allowed us to seperate indexing and lineage gathering, we could scale independently and easy to just plug in a lineage provider
   - choices I regret
     - graph traversal performance
4. security incident
   - response aimed for speed and customer trust
   - notified customers and worked with them to rotate secrets
   - 48 hours
   - plan to mitigate
   - long term fix was focused on correctness and backwards compatibility so we could roll back if we needed to

4 things:

- data catalog
- lineage
- anomaly detection
- metric definition, model definition

- data analysts want to share and get out of extension
- analytics eng managers
- heads of data

vanta principles:

- Put our customers first
  - security incident:
  - summary: we had a security incident, I detected the incident and led the response
  - details: security incident, context, I detected, I notified CTO and CISO, and what we did was 1. mitigate, 2. get affected customers, 3. work on communication, 4. work on long term fix
  - notified and worked with customers to rotate secrets within 48 hours
- Bias for action
  - Amazon: app needed data, we were supposed to get data from other team, but never did, so we ended up hacking togother an excel ingest to get the data after a month of delays
  - app worked, it was hacky and required manual action, but it did what customers wanted
  - eventually, that was just our source of truth
- Win as one team
  - Learned React at Amazon, and built the foundation of our app and a custom component that we could just use and continue building on
- Decide with frameworks
  - decision of how to implement lineage, less efficiency for more flexibility
- Lead with resilience
  - CCHH incident
  - summary: 5 days before claimn engine launch (hard HARD deadline because it's new year and tied to insurance timelines)
  - we had a piece of data that we needed to get from the insurance companies, but we didn't have it, and claims would not be processed without it, it was just a miss on our end
  - looked into the claims that we were getting over the past few years, used python to analyze the files, and realized that we could map it from another piece of data that we had
  - hacked together solution in 2 days, product launched
- Do what it says on the tin
  - got extra options grant
