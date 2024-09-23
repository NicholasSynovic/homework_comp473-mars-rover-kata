# 7. IO sends only R, L, M commands

## Status

| Status   | Time                         |
| -------- | ---------------------------- |
| Accepted | 2024-09-23T15:42:19.3066792Z |

## Context

Rover's can only understand R, L, and M commands for right, left, and move
respectfully.

## Decision

The IO class will accept an arbitrary input from the user, however, only R, L,
and M commands will be handled.

## Consequences

User input will have to be formatted to capitals and irrelevant charachters and
numbers will be dropped from the input.
