# Protected Source Manifest

## Purpose

This manifest records protected source custody without publishing protected implementation content.

The public repository remains a bounded mission-control proof surface.

The protected reentry kernel is not included in this repository.

## Protected Artifact

```text
artifact_name: reentry_verita_kernel_v1.zip
artifact_role: protected private reentry-envelope governance reference kernel
public_status: NOT INCLUDED
repository_status: HASH-REFERENCED ONLY
```

## Current Protected Source Hash

```text
sha256: a113bb1cb9cfeb31ac03ee1158e316b68718a4cfb4420536f73cab045e77ad4e
```

## Prior Approval Blueprint Hash Reference

The prior approval blueprint referenced an earlier source-bundle hash for `reentry_verita_kernel_v1.zip`.

That prior hash remains part of the approval history, but the current working protected ZIP hash is the value above.

## Public/Private Boundary

Public repository may reference:

```text
protected artifact name
protected artifact hash
role of protected artifact
status: not included
safe integration posture
```

Public repository must not include:

```text
source code from protected kernel
thermal-envelope mechanics
attitude-change mechanics
vehicle/reentry parameters
trajectory or guidance logic
fabrication or materials logic
production control substrate
```

## Integration Posture

```text
Private reentry kernel informs the public stage-admission proof behavior.
The public repo exposes only safe surrogate outcomes, receipts, replay posture, and no-advance invariant proof.
```

## Controlled External Line

```text
The Reentry VERITA Kernel is protected private source material.
This repository provides a public mission-control evaluation surface only.
It does not publish or license the protected kernel.
```
