# BGM Startup Flow

Version: 0.1.0

## 1. Startup Sequence

BGM launch sequence:

1. Start application
2. Show BGM splash
3. Initialize lightweight UI resources
4. Check available BGM identity
5. Continue to Home when identity is available
6. Show Identity Setup when identity is not available

## 2. Existing Core

Identity management belongs to the existing BGM core.

The UI must consume the existing identity API.

The UI must not duplicate identity generation,
cryptography, or identity storage logic.

## 3. Splash Behavior

Splash is temporary.

After initialization:
- transition to Home when identity exists
- transition to Identity Setup when identity does not exist

## 4. Failure Behavior

If initialization fails:
- show a simple readable error state
- provide a retry action
- do not crash the UI

## 5. Low-RAM Rules

Startup must avoid:
- unnecessary background services
- heavy animations
- large asset loading
- unnecessary network initialization
- loading all feature modules simultaneously

Feature modules should initialize only when required.

## 6. Future Extension

Additional startup checks may be added later,
provided they do not duplicate core responsibilities
or significantly increase startup cost.
