# BGM Cryptography Specification

**Project:** Black Gold Messenger  
**Specification:** BGM Cryptography / E2EE  
**Version:** 0.1  
**Status:** Draft

---

## 1. Purpose

BGM Cryptography defines the cryptographic foundation for secure end-to-end communication between authorized BGM devices.

The design MUST provide:

- End-to-end encryption
- Message authentication
- Device authentication
- Forward secrecy
- Protection against message tampering
- Replay protection
- Multi-device support
- Server-independent security

---

## 2. Cryptographic Principles

BGM cryptography MUST follow these principles:

1. Private keys MUST remain under device control.
2. Private keys MUST NOT be transmitted through the network.
3. Encryption MUST occur before messages leave the sender device.
4. Decryption MUST occur only on an authorized recipient device.
5. Relays and servers MUST NOT require access to plaintext messages.
6. Cryptographic algorithms MUST use established, audited standards.
7. Random values MUST come from a cryptographically secure random source.
8. Cryptographic protocol versions MUST be explicitly identified.
9. BGM MUST NOT invent custom cryptographic algorithms.
10. Cryptographic operations MUST use well-established cryptographic libraries.

---

## 3. Identity Keys

Each BGM Identity has cryptographic identity material.

The identity layer MUST support:

BGM Identity
|
+-- Identity Public Key
|
+-- Authorized Devices
    |
    +-- Device A
    |   +-- Device Public Key
    |   +-- Device Private Key
    |
    +-- Device B
    |   +-- Device Public Key
    |   +-- Device Private Key
    |
    +-- Device C
        +-- Device Public Key
        +-- Device Private Key

The identity private key MUST remain protected and MUST NOT be transmitted as normal network data.

Each authorized device MUST have its own cryptographic key material.

---

## 4. Device Authentication

BGM devices MUST be cryptographically authenticated before participating in secure communication.

Device authentication MUST establish:

- Device identity
- Associated BGM Identity
- Device public key
- Authorization status
- Key validity
- Device revocation status

A device MUST NOT be trusted solely because it presents a valid BGM Identity ID.

Proof of authorization MUST be cryptographic.

---

## 5. Key Agreement

BGM MUST use an established authenticated key-agreement mechanism.

The initial implementation will use X25519.

X25519 MUST be used for establishing shared secret material between authorized devices.

Private X25519 keys MUST remain on their respective devices.

The raw X25519 shared secret MUST NOT be used directly as an encryption key.

A standardized key derivation function MUST be used before encryption keys are created.

---

## 6. Key Derivation

BGM MUST use a standardized key derivation function for deriving encryption keys from shared secret material.

The implementation will use HKDF.

The key derivation process MUST provide domain separation and protocol context.

Derived keys SHOULD be separated by purpose, such as:

- Message encryption
- Authentication
- Session state
- Future protocol extensions

Raw shared secrets MUST NOT be reused directly as message-encryption keys.

---

## 7. Authenticated Encryption

BGM encrypted payloads MUST provide confidentiality and integrity.

The initial authenticated-encryption construction will use ChaCha20-Poly1305.

Each encryption operation MUST use a unique nonce for the relevant key.

Authenticated encryption MUST protect against unauthorized modification of ciphertext.

If authentication fails, the message MUST NOT be accepted as valid plaintext.

---

## 8. Associated Data

BGM MUST support authenticated associated data.

Associated data MAY contain protocol metadata that does not need confidentiality but MUST be protected against unauthorized modification.

Examples include:

- Protocol version
- Message ID
- Sender Identity ID
- Sender Device ID
- Recipient Identity ID
- Message type
- Session identifier

The exact associated-data format MUST be defined by the BGM Message Protocol.

---

## 9. Digital Signatures

BGM MUST support digital signatures for identity and device authentication.

The initial signature algorithm will use Ed25519.

Ed25519 signatures MAY be used for:

- Device authorization
- Identity authentication
- Signed protocol metadata
- Key lifecycle operations
- Future trust-management operations

Signatures MUST be verified before signed data is trusted.

---

## 10. Forward Secrecy

BGM secure sessions MUST support forward secrecy.

Compromise of a current session key MUST NOT automatically expose previously protected messages.

The final session protocol MUST therefore use appropriate ephemeral key material and session-key rotation.

Forward secrecy MUST be implemented at the protocol/session layer rather than assumed from X25519 alone.

---

## 11. Replay Protection

BGM MUST protect against replayed messages.

Replay protection MUST NOT depend solely on timestamps.

The final protocol MUST define mechanisms such as:

- Unique message identifiers
- Session state
- Counters or sequence numbers
- Replay windows where appropriate
- Duplicate-message detection

A previously accepted message MUST NOT be accepted repeatedly as a new message.

---

## 12. Message Authentication

Every protected BGM message MUST provide cryptographic integrity protection.

The receiving device MUST verify authentication before exposing plaintext to the application layer.

Tampered messages MUST be rejected.

Cryptographic verification failures MUST NOT reveal sensitive cryptographic information.

---

## 13. Multi-Device Security

A single BGM Identity MAY have multiple authorized devices.

Each device MUST maintain independent device cryptographic material.

Adding a device MUST require authorization.

Removing or revoking a device MUST prevent that device from establishing new authorized sessions.

The protocol MUST define how existing sessions are invalidated after revocation.

---

## 14. Key Lifecycle

BGM MUST define a complete cryptographic key lifecycle.

The lifecycle MUST cover:

- Key generation
- Key registration
- Key storage
- Key use
- Key rotation
- Key replacement
- Key revocation
- Device removal
- Recovery procedures

Keys MUST NOT be reused for unrelated cryptographic purposes unless explicitly permitted by the protocol.

---

## 15. Secure Key Storage

Private cryptographic keys MUST be stored using the strongest secure storage available on the device.

Where supported, BGM SHOULD use platform security facilities such as:

- Android Keystore
- Hardware-backed key protection
- Linux secure storage mechanisms
- OS-level access controls

Private keys MUST NOT be stored in plaintext application files when a secure platform facility is available.

---

## 16. Session Security

BGM secure communication MUST use explicit cryptographic sessions.

A session MUST define:

- Participants
- Device identities
- Session identifier
- Key material
- Key derivation context
- Message sequence state
- Replay state
- Session creation
- Session rotation
- Session termination

The session protocol MUST be explicitly specified before production implementation.

---

## 17. Threat Model

BGM cryptographic design MUST consider at minimum:

- Network attackers
- Malicious relays
- Compromised servers
- Message interception
- Message modification
- Message replay
- Unauthorized devices
- Stolen device scenarios
- Key compromise
- Device revocation
- Metadata exposure

The cryptographic layer MUST NOT assume that the network or relay infrastructure is trusted.

---

## 18. Server Independence

BGM cryptographic security MUST NOT depend on a central server being trusted.

Relays or servers MAY transport encrypted data.

They MUST NOT require access to plaintext or private cryptographic keys.

A compromised relay MUST NOT be able to decrypt properly protected message content.

---

## 19. Protocol Versioning

Every cryptographic protocol operation MUST identify its protocol version.

Cryptographic protocol changes MUST be versioned.

Older protocol versions MUST NOT silently interpret newer cryptographic formats.

Future cryptographic algorithms MAY be introduced through explicit protocol version upgrades.

---

## 20. Cryptographic Agility

BGM MUST avoid permanent dependence on a single cryptographic construction.

The protocol SHOULD allow future migration to alternative standardized algorithms if required by:

- Security research
- Cryptographic weaknesses
- Platform availability
- Performance requirements
- Future post-quantum migration

Algorithm identifiers MUST therefore be represented explicitly in protocol metadata where appropriate.

---

## 21. Security Boundaries

The cryptographic layer MUST clearly separate:

Application
    |
    v
BGM Message Protocol
    |
    v
BGM Session / Key Management
    |
    v
BGM Cryptography
    |
    +-- X25519
    +-- HKDF
    +-- Ed25519
    +-- ChaCha20-Poly1305

Each layer MUST have clearly defined responsibilities.

---

## 22. Production Security Requirement

The current cryptographic implementation is a foundation and MUST NOT be considered production-ready until:

- Session protocol is fully specified
- Key derivation is implemented
- Forward secrecy is implemented
- Replay protection is implemented
- Device authentication is implemented
- Key lifecycle is implemented
- Secure key storage is implemented
- Negative security tests are implemented
- Tampering tests are implemented
- Multi-device security is tested
- Threat model is reviewed
- Protocol interoperability is tested
- Cryptographic implementation receives appropriate security review

BGM MUST NOT claim complete secure messaging solely because individual cryptographic primitives pass functional tests.

---

## 23. Current Cryptographic Stack

The planned BGM cryptographic foundation is:

Identity Authentication
        |
        v
     Ed25519
        |
        v
Authenticated Key Agreement
        |
        v
      X25519
        |
        v
       HKDF
        |
        v
Session / Message Keys
        |
        v
ChaCha20-Poly1305
        |
        v
Encrypted BGM Payload

This stack is a protocol foundation.

The complete secure messaging protocol will be defined and implemented in subsequent cryptographic steps.

---

**End of Specification**
