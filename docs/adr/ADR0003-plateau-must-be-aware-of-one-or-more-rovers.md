# 3. Plateau must be aware of one or more Rovers

## Status

| Status   | Time                         |
| -------- | ---------------------------- |
| Accepted | 2024-09-23T15:40:40.4373128Z |

## Context

Multiple Rover's can be on a single Plateau. Thus, the Plateau class must be
aware of all of the positions of the Rovers.

## Decision

Each Rover will inform the Plateau of its current X and Y coordinates. The
Plateau will be responsible for keeping track of the empty spaces as well as
informing the Rovers in case they attempt to move to a non-empty space.

## Consequences

Rovers will need to know their X and Y coordinates. Additionally, in the event
that a Rover attempts to move to a non-empty space, the Plateau will inform the
Rover and not execute the movement.
