# BGM World Specification

## Purpose

BGM World provides a lightweight global hierarchy for discovering and organizing communities.

## Hierarchy

World
└── Continent
    └── Country
        └── Community

## World

The World represents the global BGM community directory.

## Continent

A Continent groups countries by geographic region.

## Country

A Country is a category that can contain multiple communities.

A country is not itself a single community.

## Community

A Community is an independent discussion space associated with a country and continent.

A community may contain:

- community_id
- name
- continent
- country
- description
- banner reference
- rules
- members

Community governance:
- No owner, admin, or moderator role.
- A join request is approved by one existing member.
- A member may leave voluntarily at any time.
- Removal requires requests from 10 unique existing members.
- The 10th unique removal request automatically removes the target member.

## Membership

Supported membership states:

NONE
REQUESTED
INVITED
APPROVED
MEMBER

Basic flows:

NONE -> REQUESTED -> APPROVED -> MEMBER

INVITED -> MEMBER

## Roles

Supported roles:

OWNER
ADMIN
MODERATOR
MEMBER

## Design Principles

- Lightweight
- Modular
- No central BGM server dependency
- Compatible with P2P architecture
- Suitable for low-RAM Android devices
- No heavy external framework required
- World data must remain independent from local peer discovery
- Community messaging will use existing BGM message infrastructure
