# 4. Rovers must be aware of the x-y coordinates

## Status

| Status   | Time                         |
| -------- | ---------------------------- |
| Accepted | 2024-09-23T15:40:59.3848095Z |

## Context

Each Rover needs to know its X and Y coordinates on the Plateau.

## Decision

The Rover class will keep track of and update its own X and Y coordinates.

## Consequences

The Rover will have to be able to communicate with the Plateau when it wants to
move, and hear back from the Plateau if the move was successful or not.
